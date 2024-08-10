import requests
from bs4 import BeautifulSoup

# URL of the mutual fund holdings page
url = 'https://www.valueresearchonline.com/funds/holdings/12345'  # Replace with actual URL

# Send a GET request to fetch the page content
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table or section containing the holdings
holdings_table = soup.find('table', class_='fund-holdings-table')  # Adjust class name as necessary

# Extract data from the table
holdings = []
if holdings_table:
    for row in holdings_table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        stock_name = cells[0].text.strip()  # Adjust index if necessary
        allocation = cells[1].text.strip()  # Adjust index if necessary
        holdings.append({'stock_name': stock_name, 'allocation': allocation})

# Output the scraped data
for holding in holdings:
    print(f"Stock: {holding['stock_name']}, Allocation: {holding['allocation']}")