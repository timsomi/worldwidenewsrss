# WorldWideNewsRSS

## Description
WorldWideNewsRSS is an automated news aggregator that fetches and publishes news from multiple RSS feeds. This project is designed to provide up-to-date news coverage by pulling articles from various sources and displaying them in a centralized platform.

## Features
- Fetches news from multiple RSS feeds
- Auto-publishes news content as an RSS feed
- Supports filtering and categorization of news
- Lightweight and efficient automation
- Can be integrated with websites and blogs
- Provides an API endpoint for RSS consumption

## Installation
### Prerequisites
- Git
- Python 3+
- Required Python libraries (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/timsomi/worldwidenewsrss.git
   cd worldwidenewsrss
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure RSS feed sources in `config.json`.
4. Run the application:
   ```sh
   python app.py
   ```

## Usage
- Modify the `config.json` file to add or remove RSS sources.
- Run `app.py` to start the Flask server.
- Access the aggregated RSS feed via:
  ```
  http://localhost:5050/rss
  ```
- Automate the script using a cron job for scheduled updates.

## API Endpoint
The application provides an API endpoint to fetch the latest aggregated RSS feed:
- `GET /rss` - Returns the aggregated news feed in RSS XML format.

## Contributing
Pull requests are welcome! Please open an issue to discuss major changes.

## License
This project is licensed under the MIT License.

## Contact
For inquiries, reach out via [GitHub Issues](https://github.com/timsomi/worldwidenewsrss/issues).
