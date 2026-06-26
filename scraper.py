import requests
from bs4 import BeautifulSoup

def get_crop_prices(crop, state):
    url = "https://agmarknet.gov.in"  # Replace with the actual URL for crop prices
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    # Send a request to the website
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch data"}

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "lxml")

    # Extract crop price table
    crop_prices = []
    table = soup.find("table", {"class": "table-class"})  # Update with actual class name
    if table:
        rows = table.find_all("tr")[1:]  # Skip header row
        for row in rows:
            cols = row.find_all("td")
            crop_name = cols[0].text.strip()
            location = cols[1].text.strip()
            price = cols[2].text.strip()

            if crop.lower() in crop_name.lower() and state.lower() in location.lower():
                crop_prices.append({"crop": crop_name, "location": location, "price": price})

    return crop_prices if crop_prices else {"error": "No data found for the given crop and state"}

