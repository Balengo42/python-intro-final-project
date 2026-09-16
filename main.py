import textwrap
import requests
import argparse
import matplotlib.pyplot as plt 
from collections import Counter

API_URL = "https://openlibrary.org/search.json" 
Known_subjects= ["Romance", "Fiction","Literature", "Fantasy", "Action", "Adventure", "Comedy", "Historical", 
"Historical Fiction","Science Fiction", "Thriller", "Mystery", "Horror", "Biography","Autobiography", "History",
"Self-help", "Poetry", "Children's Literature", "Young Adult", "Literary Fiction", "Non-fiction", "Graphic Novel", "Short Story",
"Drama", "Satire", "Crime", "Dystopian", "Memoir", "Classic", "Paranormal", "Western", "War",
"Political Fiction", "Science", "Philosophy", "Religion", "Spirituality", "Travel", "Art", "Music", "Food and Drink"]

Known_subjects_lower = {g.lower() for g in Known_subjects}

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


def filter_subjects(subjects):
    """Filter subjects to only known subjects."""
    if not isinstance(subjects, list):
        return ["Unknown"]

    filtered_subjects = [subject for subject in subjects if isinstance(subject, str) and subject.lower() in Known_subjects_lower]
    
    return filtered_subjects if filtered_subjects else ["Unknown"]


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
            "subject": filter_subjects(record.get("subject", []))
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

        if start_year <= year < start_year + number_of_years:
            subjects = book["subject"]
            if isinstance(subjects,list):
                for subject in subjects:
                    if subject == "Unknown":
                        continue
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

def prepare_plot_data(subject_data, start_year, number_of_years=5):
    """Prepare data for plotting."""
    years = list(range(start_year, start_year + number_of_years))
    plot_years = []
    top_counts = []
    top_subjects = []

    for year in years:
        if year in subject_data:
            plot_years.append(year)
            top_counts.append(subject_data[year]["count"])
            top_subjects.append(subject_data[year]["subject"])

    return{ "years": plot_years, "counts": top_counts, "subjects": top_subjects,}


def build_subject_plot(plot_data, start_year, author, number_of_years=5):
    """Build a bar plot to show the most common subject for each year."""
    if not plot_data["years"]:
        return None
    end_year = start_year + number_of_years - 1
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(plot_data["years"], plot_data["counts"])

    ax.set_xlabel("Publication Year")
    ax.set_ylabel("Number of Books")
    ax.set_title(f"Most Common Subject by Year for {author} ({start_year}-{end_year})")
    ax.set_xticks(plot_data["years"])

    ax.set_ylim(0, max(plot_data["counts"]) * 1.25)
    for bar, subject, count in zip(bars, plot_data["subjects"], plot_data["counts"]):
        label = "\n".join(textwrap.wrap(subject, width=14))
        ax.text(bar.get_x() + bar.get_width() / 2, count, label, ha='center', va='bottom', rotation=0, fontsize=10)

    fig.text(0.5, 0.01, "Each bar label is the genre of the most common subject in that year for this author", ha='center', fontsize=8)
    fig.tight_layout(rect=[0, 0.04, 1, 1])

    return fig 


def subject_plot(subject_data, start_year, author, number_of_years=5):
    """Prepare data and build the subject plot."""
    plot_data = prepare_plot_data(subject_data, start_year, number_of_years)
    if not plot_data["years"]:
        print("No subject data available.")
        return None
    fig = build_subject_plot(plot_data, start_year, author, number_of_years)
    end_year = start_year + number_of_years - 1
    filename = f"top_subject_by_year_{start_year}_{end_year}.png"

    fig.savefig(filename)
    print(f"Plot saved as {filename}.")
    plt.show()

    return filename


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
        print(f"Subject: {', '.join(record['subject'])}")
        print(f"Year: {record['year']}")
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


    subject_data = subject_by_year(

        records,
        int(year),
        number_of_years =5
    )
    subject_plot(subject_data, int(year), author)

    

if __name__ == "__main__":
    main() 
