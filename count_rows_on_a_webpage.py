from bs4 import BeautifulSoup
import requests

url = "https://www.grcourt.org/wp-content/uploads/Reports/2022/Q1-2022-Civil-Report.html"

# Make a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table element
table = soup.find("table")

if table is not None:
    # Find all the table rows within the table
    rows = table.find_all("tr")

    # Count the number of rows
    row_count = len(rows)

    print("Number of rows in the table:", row_count)
else:
    print("Table element not found")
