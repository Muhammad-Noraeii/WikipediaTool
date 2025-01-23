

# WikipediaTool Documentation

## Overview

**WikipediaTool** is a Python-based command-line interface (CLI) tool for interacting with Wikipedia. It enables users to search for articles, view summaries, fetch related links, display full articles, and export results as PDF files. Designed for speed, simplicity, and flexibility, this tool is perfect for developers, researchers, and anyone who needs quick access to Wikipedia data.

---

## Features

### 1. Search Articles
- Enter a search query, and the tool fetches a list of matching Wikipedia articles.
- Results are displayed in a neat table with the title and a snippet for context.

### 2. Get Article Summary
- Retrieve a concise and clear summary of any Wikipedia article.
- Summaries are displayed in the terminal with an option to save them as a PDF.

### 3. Get Article Links
- View all related links for a specific article.
- Perfect for exploring connected topics.

### 4. View Full Article
- Fetch and display the entire content of an article.
- Useful for detailed reading directly in the terminal.

### 5. Save as PDF
- Save search results, summaries, or full articles as PDF files.
- PDFs are formatted neatly and stored in the current working directory.

### 6. Multilingual Support
- Search and fetch articles in multiple Wikipedia-supported languages.
- Default language is English, but users can switch to languages like French, German, and more.

---

## Installation

Follow these steps to install and set up **WikipediaTool**:

### Prerequisites
- **Python 3.6+**
- A terminal or command prompt

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Muhammad-Noraeii/WikipediaTool.git
   cd WikipediaTool
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool**:
   ```bash
   python wikipedia_tool.py
   ```

---

## Usage

### Running the Tool
After running the tool, you’ll see the following interactive menu:

```
1. Search Articles
2. Get Article Summary
3. Get Article Links
4. View Full Article
5. Change Language
6. Exit
```

### Menu Options

1. **Search Articles**:
   - Enter a search query to get a list of articles.
   - Example:
     ```
     Enter search query: Python
     ```
     Output:
     ```
     Search Results
     ------------------------------------------------------
     # | Title                     | Snippet
     ------------------------------------------------------
     1 | Python (programming)      | Python is a high-level programming language.
     2 | Python (genus)            | Python is a genus of snakes found in Africa.
     ```

2. **Get Article Summary**:
   - Enter the title of an article to retrieve a summary.
   - Example:
     ```
     Enter article title: Python (programming)
     ```
     Output:
     ```
     Title: Python (programming)
     Summary: Python is an interpreted high-level general-purpose programming language...
     ```

3. **Get Article Links**:
   - Enter the title of an article to see a list of related links.
   - Example:
     ```
     Enter article title: Python (programming)
     ```
     Output:
     ```
     Links for Python (programming):
     1. Guido van Rossum
     2. Programming paradigm
     3. Object-oriented programming
     ```

4. **View Full Article**:
   - Enter the title of an article to display the full content.
   - Example:
     ```
     Enter article title: Python (programming)
     ```
     Output:
     ```
     Title: Python (programming)
     Full Article:
     Python is an interpreted high-level general-purpose programming language...
     ```

5. **Change Language**:
   - Switch the language of Wikipedia articles.
   - Example:
     ```
     Enter new language code (e.g., en, fr, de): fr
     ```
     The tool will now fetch articles from French Wikipedia.

6. **Save as PDF**:
   - After fetching results, summaries, or full articles, the tool prompts you to save the content as a PDF.
   - Example:
     ```
     Would you like to save this summary as a PDF? (y/n): y
     ```
     Output:
     ```
     Saved as PDF: Python_summary.pdf
     ```

---

## Example Workflow

1. **Search for Articles**:
   - Search for the term "Python".
   - Select an article to view its summary or links.

2. **View and Save Summary**:
   - Fetch the summary of "Python (programming)".
   - Save it as `Python_summary.pdf`.

3. **Switch Language**:
   - Change the language to French (`fr`).
   - Search for "Python" again and fetch results in French.

4. **Explore Links**:
   - Get related links for a chosen article to explore more topics.

---


## Screenshots

### Screenshot 1: Main Menu
![Screenshot 2](https://mojox.org/uploads/wpt.menu.PNG)

### Screenshot 2: Viewing Article Summary
   ![Screenshot 2](https://mojox.org/uploads/wp.summery.PNG)
   

---

## Dependencies

The following Python libraries are required to run the tool:

- `requests`: For making API requests to Wikipedia.
- `rich`: For beautiful and colorful terminal output.
- `reportlab`: For generating PDF files.

Install them via:

```bash
pip install -r requirements.txt
```

---

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

