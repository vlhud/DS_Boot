#!/usr/bin/env python3

import sys
import httpx
from bs4 import BeautifulSoup
import re
import cProfile
import pstats

def fetch_financial_data(ticker: str, field: str):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    response = httpx.get(url, headers=headers, follow_redirects=True)
    if response.status_code != 200:
        raise Exception(f"URL does not exist or is inaccessible: {url}")

    soup = BeautifulSoup(response.text, "html.parser")
    field_row = soup.find_all('div', {'class': re.compile('row lv-0')})

    if not field_row:
        raise Exception(f"Row not found on the page.")

    for row in field_row:
        label = row.find('div', {'class': re.compile('rowTitle')})
        if label and label.text.strip() == field:
            values = row.find_all('div', {'class': re.compile('column yf-')})
            values_txt = [value.text.strip() for value in values]
            return values_txt

def main():
    if len(sys.argv) != 3:
        print("Usage: ./financial.py <TICKER> <FIELD>")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        result = fetch_financial_data(ticker, field)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    
    main()
    
    profiler.disable()
    
    profiler.dump_stats('profile_stats.prof')
    
    p = pstats.Stats('profile_stats.prof')
    p.sort_stats('cumulative') 
    p.print_stats(5)