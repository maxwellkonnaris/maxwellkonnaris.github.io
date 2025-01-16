import requests
from bs4 import BeautifulSoup
import json

def fetch_metadata(url):
    """
    Fetch metadata from the given URL. Extracts title, description, and image from meta tags,
    with fallback to page content if description is unavailable.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title from og:title or <title> tag
        title = soup.find('meta', property='og:title') or soup.find('title')

        # Extract description from og:description, meta[name="description"], or fallback to first <p> tag
        description = (
            soup.find('meta', property='og:description') or
            soup.find('meta', attrs={'name': 'description'})
        )
        if not description:
            first_paragraph = soup.find('p')
            description = first_paragraph.text.strip() if first_paragraph else "No Description Found"

        # Extract image from og:image
        image = soup.find('meta', property='og:image')

        # Return extracted metadata
        return {
            "title": title['content'] if title and title.has_attr('content') else title.string if title else "No Title Found",
            "description": description['content'] if description and hasattr(description, 'content') else description,
            "image": image['content'] if image else "No Image Found",
            "url": url
        }
    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e), "url": url}

def save_news_metadata(urls, output_file="news.json"):
    """
    Fetch metadata for a list of URLs and save it as a JSON file.
    """
    news = []
    for url in urls:
        metadata = fetch_metadata(url)
        news.append(metadata)
        print(f"Fetched metadata for {url}")

    # Save metadata to a JSON file
    with open(output_file, "w") as file:
        json.dump(news, file, indent=4)
    print(f"News metadata saved to {output_file}")

if __name__ == "__main__":
    # List of URLs to fetch metadata from
    urls = [
        "https://www.huck.psu.edu/news/penn-state-researchers-announce-new-comprehensive-omics-database"
        # Add more URLs as needed
    ]
    save_news_metadata(urls)
