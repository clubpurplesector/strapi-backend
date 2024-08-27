import feedparser
from bs4 import BeautifulSoup
import difflib
import requests

# URLs of the RSS feeds
feed_urls = [
    "https://www.formula1.com/content/fom-website/en/latest/all.xml",
    # "http://feeds.bbci.co.uk/sport/formula1/rss.xml",
    # "https://www.espn.com/espn/rss/f1/news",
    # "https://www.autosport.com/rss/feed/f1",
    # "https://www.skysports.com/rss/12040"
]

def fetch_and_parse_feed(url):
    """Fetch and parse the RSS feed."""
    feed = feedparser.parse(url)
    return feed['entries']

def get_clean_text(html_text):
    """Extract text from HTML."""
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text()

def get_dominant_image(link):
    """Extract the image with the highest width and height from the article."""
    try:
        response = requests.get(link)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize variables to track the largest image
        max_area = 0
        dominant_image_url = None

        # Iterate over all img tags in the article
        for img_tag in soup.find_all('img'):
            width = img_tag.get('width')
            height = img_tag.get('height')

            # Some sites might use style attributes or may not define width/height
            if not width or not height:
                continue

            try:
                width = int(width)
                height = int(height)
                area = width * height

                # Check if this image has the largest area
                if area > max_area:
                    max_area = area
                    dominant_image_url = img_tag['src']
            except ValueError:
                continue  # Skip if width or height is not an integer

        return dominant_image_url
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the image from {link}: {e}")
        return None

def are_similar(title1, title2, threshold=0.7):
    """Check if two titles are similar."""
    ratio = difflib.SequenceMatcher(None, title1, title2).ratio()
    return ratio >= threshold

def combine_and_deduplicate_news():
    """Fetch feeds, deduplicate and combine similar news."""
    all_entries = []

    # Fetch and parse all feeds
    for url in feed_urls:
        entries = fetch_and_parse_feed(url)
        all_entries.extend(entries)

    combined_news = []

    # Deduplicate news based on title similarity
    for entry in all_entries:
        title = entry.get('title', '')
        summary = get_clean_text(entry.get('summary', ''))
        link = entry.get('link', '')
        image_url = get_dominant_image(link)

        is_duplicate = False

        for news in combined_news:
            if are_similar(title, news['title']):
                is_duplicate = True
                break

        if not is_duplicate:
            combined_news.append({
                'title': title,
                'summary': summary,
                'link': link,
                'image_url': image_url
            })

    # Display the combined news
    for news in combined_news:
        print(f"Title: {news['title']}\nLink: {news['link']}\nSummary: {news['summary']}")
        if news['image_url']:
            print(f"Image: {news['image_url']}")
        print('-' * 80)

def update_feed():
    """Update the feed every 24 hours."""
    combine_and_deduplicate_news()

# Run the scheduler
if __name__ == "__main__":
    print("Fetching and combining news articles...")
    update_feed()
