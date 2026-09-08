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


def display_results(results, show_edition = False):
    """Print results to the terminal in a readable format."""
    if not results:
        print("No results found.")
        return

    print(f"\n{len(results)} results found:")
    print("-" * 40)
    for record in results:
        print(f"Title: {record['title']}")
        print(f"Author: {record['author']}")
        print(f"year: {record['year']}")
        print(f"Language: {record['language']}")
        if show_edition:
            print(f"Edition: {record['edition']}")
        print("-" * 40)


def main():
    parser = argparse.ArgumentParser(description= "Query library data by year.")
    parser.add_argument("year", help = "Year to filter by (e.g., 1993)")
    args = parser.parse_args()
    if not args.year.isdigit():
        print("Please enter a valid year.")
        return


    data = fetch_data()
    if not data:
        return
    
    records = process_data(data)
    results= [r for r in records if str(r["year"]) == args.year]


    query = input("Do you want to know the edition(s) of the book(s) too? (yes/no):").strip().lower()
    display_results(results, show_edition= query == "yes")


if __name__ == "__main__":
    main()
