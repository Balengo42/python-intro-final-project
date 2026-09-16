# Book Search by Author & Year
This program lets a user search through the Open Library for books by an author, filtered down to a specific publication year. Receiving the title, subject, langauge, link, and optional edition count. It also makes a chart showing the most published genre per year by that author in a 5 year range starting at the year entered.
## API

This project uses the https://openlibrary.org/search.json API.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-intro-final-project.git
   cd python-intro-final-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   # .venv\Scripts\activate       # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```

## CLI Interactions
The user walks through three prompts in said order:
1.Enter an author
Searches the Open Library matching that author name
2.Enter a year to filter by:
Filters those results down to a book published in that year given, and also uses it as the start of the 5 year range used for chart.
3.Do you want to know the edition(s) of the book(s) too? (yes/no)
Gives the user an option if to include the edition count in the printed result

After all these prompts, the program prints: matching book's title, author, subject(s), year, language, and a link to its Open Library page

Then it displays a bar chart of the most common genre per year for that author within a 5 year range from given year.

## Extension Track
In this project I choose Option A - Visual Analysis. In this trackI used matplotlib to build a bar chart that answers, which genre did the searched author publish most often, within a 5 year range beginning from the year entered. Each bar represents a year, and its height shows the book count for that year. 

## Visualization
The visualization is a bar chart that with the entered author and year, we get to know which genre/subject was publsihed most often in the 5 year window starting from the year entered. 
Each bar represents one year and its height shows how many books by that author published in that year, were of that genre named at top. Giving you an idea of what genre the author mostly publishes. Also a bar chart best fits this information since it gives an exact count and the bars themselves show the years easily. 

# Video Explanation
