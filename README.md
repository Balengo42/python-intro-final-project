# Book Search by Author & Year

What this program does is the user can fetch a book based on the author they put and year. Also, they are asked if they want to know the editions of the books. 
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

The user is prompted by asking them a name of an author, and then a year. Which is followed up by if they want to know the edition of the books that may appear.

## CLI Interactions
The CLI, allows it to filter by author name and year that its published. It goes as it follows, "Enter an author:", then "Enter a year to filter by" and lastly it asks "Do you want to know the edition(s) of the book(s) too? (yes/no)." Then it gives the details to the book(s) and a link to go into the actual webpage for the book.

## Visualization
Based on the users author and year input, it gives a 5 year range including the one inputed, and shows a 5 year range of the most common subject/genre published in those years by that author. This gives the user a view into what subjects/genres were the most published by that during that 5 year range. So this will answer or give more info to the user of about that author 

# Video
