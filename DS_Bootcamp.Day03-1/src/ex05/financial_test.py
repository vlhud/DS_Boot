#!/usr/bin/env python3

import sys
import time
import requests
from bs4 import BeautifulSoup
import re
import pytest

def fetch_financial_data(ticker: str, field: str):
    time.sleep(5)

    url = f"https://finance.yahoo.com/quote/{ticker}/financials"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"URL does not exist or is inaccessible: {url}")

    soup = BeautifulSoup(response.content, "html.parser")

    field_row = soup.find_all('div', {'class': re.compile('row lv-0')})
    if not field_row:
        raise Exception(f"Row not found on the page.")

    for row in field_row:
        label = row.find('div', {'class': re.compile('rowTitle')})
        if label and label.text.strip() == field:
            values = row.find_all('div', {'class': re.compile('column yf-')})
            if not values:
                raise Exception(f"No values found for field: {field}")
            return (field, tuple(value.text.strip() for value in values))

def test_total_revenue():
    result = fetch_financial_data("MSFT", "Total Revenue")
    assert result is not None
    assert len(result) == 2
    values = result
    assert len(values) > 0
    assert any(',' in value for value in values)

def test_return_type():
    result = fetch_financial_data("MSFT", "Total Revenue")
    assert isinstance(result, tuple)

def test_invalid_ticker():
    with pytest.raises(Exception):
        fetch_financial_data("INVALIDTICKER123", "Total Revenue")

if __name__ == "__main__":
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
