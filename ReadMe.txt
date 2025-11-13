Add User-Agent header and polite delays.

Respect robots.txt and website terms — for demo sites it’s fine; for real sites read rules.

Add exception handling (try/except) around network calls.

Log activity to file (use logging.FileHandler).

Use config file (JSON or YAML) for base URL, max pages, delay.

For long-term tracking, store scraped data in SQLite or Postgres instead of CSV.