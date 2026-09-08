import requests
import argparse

API_URL = "https://openlibrary.org/search.json"  # Replace with your chosen API endpoint


def fetch_data(author):
    """Fetch data from the API. Returns the raw JSON response, or an empty list on failure."""
    try:
        response = requests.get(API_URL, params= {"author":author})
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
            "key": record.get("key", "Unknown")
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
        print(f"Link to book: https://openlibrary.org{record['key']}/")
        if show_edition:
            print(f"Edition: {record['edition']}")
        print("-" * 40)


def main():
    parser = argparse.ArgumentParser(description= "Search library data by author.")
    parser.add_argument("--author", help = "Author to search for")

    args = parser.parse_args()

    if args.author:
        author = str(args.author)
    else:
        author = input("Enter an author:").strip()

    while not author:
        print("Please enter an author")
        author = input("Enter an author:").strip()

    while True:
        year = input("Enter a year to filter by (e.g, 1993):").strip()
        if year.isdigit():
         break
        print("Please enter a valid year using numbers only.")

    data = fetch_data(author)
    if not data:
        return

    records = process_data(data)
    results= [r for r in records if str(r["year"]) == year]
    query = input("Do you want to know the edition(s) of the book(s) too? (yes/no):").strip().lower()
    display_results(results, show_edition= query == "yes")

if __name__ == "__main__":
    main()
