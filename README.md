# [Book Search by Author & Year]ls

What this program does is the user can fetch a book based on the author they put and year. Also, are asked if they want to know the editions of the books. 
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

Describe each interaction your CLI supports. For example:

- **Filter by region** — enter a region name to see all matching records
- **Look up by name** — enter a name to see details for one specific record
The CLI, allows it to filter by author name and year that its published. 