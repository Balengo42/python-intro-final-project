import requests

API_URL = "https://your-api-url-here.com"  # Replace with your chosen API endpoint


def fetch_data():
    """Fetch data from the API. Returns the raw JSON response, or an empty list on failure."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: could not fetch data. {e}")
        return []


def process_data(data):
    """Extract and transform the fields you need. Returns a list of dictionaries."""
    pass


def display_results(results):
    """Print results to the terminal in a readable format."""
    pass


def main():
    data = fetch_data()
    if not data:
        return

    records = process_data(data)
    display_results(records)


if __name__ == "__main__":
    main()
