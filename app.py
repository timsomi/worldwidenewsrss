import json
from flask import Flask, Response
from flask_cors import CORS
from datetime import datetime, timezone
import feedparser
import os

app = Flask(__name__)
CORS(app)

# Load RSS feed URLs from config.json
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

config = load_config()
rss_feeds = config.get("rss_feeds", [])

# Function to fetch news
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

# Function to generate RSS XML
def generate_rss():
    news = fetch_news()
    rss_feed = f'''<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
        <channel>
            <title>Aggregated World News</title>
            <link>https://yourwebsite.com/news</link>
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
    
    return rss_feed

@app.route('/rss')
def rss_feed():
    rss_data = generate_rss()
    response = Response(rss_data, mimetype='application/xml')
    response.headers['Access-Control-Allow-Origin'] = '*'  
    return response


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))  # Use Render's assigned PORT
    app.run(host="0.0.0.0", port=port)
