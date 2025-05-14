from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

load_dotenv()

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))


def scrape_website_tool(url: str):
    """Scrape single website."""
    scrape_result = app.scrape_url(url=url,
                                   params={"formats": ["markdown"]},
                                   )
    markdown_text = scrape_result.get("markdown")
    return markdown_text


def crawl_website():
    pass


def extract_website():
    pass
