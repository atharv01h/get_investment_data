import requests

# Replace YOUR_API_KEY with your actual API key from Alpha Vantage
API_KEY = 'YOUR_API_KEY'

def get_investment_suggestion(stock_symbol):
    """
    Retrieves the latest investment suggestion for the given stock symbol using Alpha Vantage API.
    Returns the investment suggestion as a string.
    """
    # Make the API call to get the latest quote for the stock symbol
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Extract the investment suggestion from the response
    suggestion = data.get('AnalystTargetPrice', 'N/A')

    # Return the investment suggestion
    return f'Investment suggestion for {stock_symbol}: {suggestion}'


print(get_investment_suggestion('AAPL'))


#BY ATHARV HATWAR
