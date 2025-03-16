import json
from flask import Flask, Response, render_template
from flask_cors import CORS
from datetime import datetime, timezone
import feedparser

app = Flask(__name__, template_folder='templates')
CORS(app)

# Load RSS feed URLs from config.json
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

config = load_config()
rss_feeds = config.get("rss_feeds", [])

# Fetch news
def fetch_news():
    news_items = []
    for url in rss_feeds:
        feed = feedparser.parse(url)
        if 'entries' in feed:
            for entry in feed.entries[:5]:  # Fetch latest 5 articles per source
                news_items.append({
                    "title": entry.title,
                    "link": entry.link,
                    "source": feed.feed.title if 'title' in feed.feed else "Unknown"
                })
    return news_items

# Serve RSS feed
@app.route('/rss')
def rss_feed():
    news = fetch_news()
    rss_feed = f'''<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
        <channel>
            <title>World Wide News</title>
            <link>https://worldwidenewsrss.onrender.com</link>
            <description>Real-time global news from various sources</description>
            <lastBuildDate>{datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}</lastBuildDate>
    '''
    for item in news:
        rss_feed += f'''
            <item>
                <title>{item["title"]}</title>
                <link>{item["link"]}</link>
                <source>{item["source"]}</source>
                <pubDate>{datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}</pubDate>
            </item>
        '''
    
    rss_feed += '''
        </channel>
    </rss>'''
    
    return Response(rss_feed, mimetype='application/xml')

# Serve Webpage
@app.route('/')
def home():
    news = fetch_news()
    return render_template('index.html', news=news)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5050)
