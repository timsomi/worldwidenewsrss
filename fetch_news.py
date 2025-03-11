import feedparser

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

# Function to fetch and parse news
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

# Run function to check output
news = fetch_news()
for item in news[:10]:  # Print first 10 articles for testing
    print(f"{item['source']}: {item['title']} ({item['link']})\n")
