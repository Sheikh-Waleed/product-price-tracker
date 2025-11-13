# scraper/price_scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

BASE_URL = "https://books.toscrape.com/"

def parse_price(price_text):
    # Example price_text: "£51.77"
    cleaned = price_text.replace('£', '').strip()
    try:
        return float(cleaned)
    except ValueError:
        return None

def scrape_page(page_url):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; PriceScraper/1.0)'}
    logging.info(f"Fetching: {page_url}")
    resp = requests.get(page_url, headers=headers, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    products = []

    for product in soup.select('article.product_pod'):
        title_tag = product.select_one('h3 > a')
        price_tag = product.select_one('p.price_color')
        link = urljoin(page_url, title_tag['href']) if title_tag else None
        title = title_tag['title'] if title_tag else None
        price = price_tag.get_text(strip=True) if price_tag else None

        products.append({
            'title': title,
            'price': price,
            'link': link
        })

    return products


def get_next_page(soup, current_url):
    next_li = soup.select_one('li.next > a')
    if next_li:
        return urljoin(current_url, next_li['href'])
    return None

def scrape_all(start_url, max_pages=5, delay=1.0):
    url = start_url
    all_products = []
    page_count = 0
    while url and page_count < max_pages:
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; PriceScraper/1.0)'}
        logging.info(f"Fetching: {url}")
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        all_products.extend(scrape_page(url))
        page_count += 1
        next_url = get_next_page(soup, url)
        url = next_url
        time.sleep(delay)  # polite delay
    return all_products

def main():
    start_url = urljoin(BASE_URL, "catalogue/category/books_1/index.html")
    products = scrape_all(start_url, max_pages=3, delay=1.2)
    df = pd.DataFrame(products)
    # drop duplicates (if any)
    df.drop_duplicates(subset='link', inplace=True)
    # save cleaned CSV
    df.to_csv('products_all.csv', index=False)
    print("Saved products_all.csv with", len(df), "rows")

if __name__ == "__main__":
    main()