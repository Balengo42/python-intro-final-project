import requests
import argparse
import matplotlib.pyplot as plt 
from collections import Counter


API_URL = "https://openlibrary.org/search.json" 

def fetch_data(author):
    """Fetch data from the API. Returns the raw JSON response, or an empty list on failure."""
    try:
        params = {
            "author": author,
            "fields": "title,author_name,first_publish_year,language,edition_count,key,subject"
        }
        response = requests.get(API_URL, params=params)
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
            "author": record.get("author_name", "Unknown")[0:],
            "year": record.get("first_publish_year", "Unknown"),
            "language": record.get ("language", "Unknown"),
            "edition": record.get("edition_count", "Unknown"),
            "key": record.get("key", "Unknown"),
            "subject": record.get("subject", []),
            })
    return result 

def subject_by_year(records, start_year, number_of_years =5):
    """ Find the most common subject for each year within a 5 year range from year selected"""
    subjects_by_year = {}

    for year in range(start_year, start_year + number_of_years):
        subjects_by_year[year] = Counter()
        
    for book in records:
        year= book["year"]

        if not isinstance(year,int):
            continue

        if start_year <= year <= start_year + number_of_years:
            subjects = book["subject"]

        if isinstance(subjects,list):
            for subject in subjects:
                subjects_by_year[year][subject] += 1

    top_subject_by_year = {}

    for year, subject_counts in subjects_by_year.items():
        if subject_counts:
            top_subject, count = subject_counts.most_common(1)[0]

            top_subject_by_year[year] = {
                "subject": top_subject,
                "count": count
            }

    return top_subject_by_year
    
def subject_plot(subject_data, start_year):
    """Creating a bar plot to show the most common subject for each year"""
    if not subject_data:
        print



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

    data = fetch_data(author)
    if not data:
        return

    records = process_data(data)
    
    while True:
        year = input("Enter a year to filter by (e.g, 1993):").strip()
        if year.isdigit():
         break
        print("Please enter a valid year using numbers only.")

    results= [r for r in records if str(r["year"]) == year]
    if not results:
        print(f"No books found by {author} published in {year}.")
        return

    while True:
        query = input("Do you want to know the edition(s) of the book(s) too? (yes/no):").strip().lower()
        if query == "yes":
            display_results(results, show_edition= query == "yes")
            break
        elif query == "no":
            display_results(results, show_edition=False)
            break
        else:
            print("Please enter yes or no.")


    subject_data = subject_by_year(records)
    if not subject_data:
        print("No subject data available.")
        return


    

if __name__ == "__main__":
    main() 
