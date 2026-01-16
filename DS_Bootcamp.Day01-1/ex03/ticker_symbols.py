import sys

def data():
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    if len(sys.argv) != 2:
        return

    tiker=sys.argv[1]
    if tiker in STOCKS:
        company_name=next(key for key, value in COMPANIES.items() if value==tiker)
        print(company_name, STOCKS[tiker])
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    data()