from flask import Flask, Response
from flask_cors import CORS
from datetime import datetime, timezone
import feedparser

app = Flask(__name__)
CORS(app)

# List of RSS feed URLs
rss_feeds = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best",
    "http://rss.cnn.com/rss/edition_world.rss",
    "https://www.france24.com/en/rss",
    "https://www.dw.com/en/rss",
    "https://www.cgtn.com/rss",
    "https://www.rt.com/rss/news/",
    "https://www.voanews.com/rss",
    "https://www.africanews.com/rss"
]

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
    rss_data = generate_rss()  # Replace with your RSS generation function
    response = Response(rss_data, mimetype='application/xml')
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    return response

if __name__ == '__main__':
    app.run(port=5050, debug=True)
