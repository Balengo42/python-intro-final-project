import requests
import argparse

API_URL = "https://openlibrary.org/search.json?author=tolkien"  # Replace with your chosen API endpoint


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
    records = data.get("docs", [])
    result = []
    for record in records:
        result.append({
            "title": record.get("title", "Unknown"),
            "author": record.get("author_name", ["Unknown"])[0],
            "year": record.get("first_publish_year", "Unknown"),
            "language": record.get ("language", ["Unknown"]),
            "edition": record.get("edition_count", "Unknown"),
            })
        return result 


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
