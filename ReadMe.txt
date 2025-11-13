# Product Price Tracker
A beginner-friendly Python project that scrapes product titles and prices <br> from a demo e-commerce site and saves results to CSV. Includes a simple Streamlit UI.

## How to run
1. Create virtual environment and activate  
2. Install packages  
pip install -r requirements.txt

3. Run scraper:  
python scraper/price_scraper.py

4. (Optional) Start UI:  
streamlit run app.py

## Files
- `scraper/price_scraper.py` — main scraper  
- `products_all.csv` — example output  
- `app.py` — Streamlit UI  

## Example
![Top 10 Cheapest Products](top10_cheapest.png)

## License
MIT License
