
# WikipediaTool: Command-Line Wikipedia Search & Interaction

Welcome to **WikipediaTool** — your personal command-line interface for browsing Wikipedia! Whether you’re looking for articles, summaries, or links related to a topic, this tool offers a seamless and interactive experience. It's fast, reliable, and fully customizable to support different languages.

## Features
- **Search Articles**: Find articles based on search queries with a real-time display of results.
- **Get Article Summary**: Fetch a concise summary of any article in a matter of seconds.
- **View Article Links**: Get a list of related articles and external links for further exploration.
- **View Full Article**: Access the full content of any article, no fluff, just the facts.
- **Random Article**: Discover something new by getting a random Wikipedia article at the click of a button.
- **Multilingual Support**: Switch between multiple languages for a global Wikipedia browsing experience.

## Why Use WikipediaTool?
- **Fast & Interactive**: No more endless clicks—just type and get your results instantly in a beautifully formatted table.
- **PDF Export**: Save your search results, article summaries, or full articles as PDF files with a single click.
- **Command-Line Power**: For users who prefer the speed and simplicity of terminal-based tools over web browsing.
- **Easy Setup**: Install with a single command and start exploring Wikipedia at your fingertips.

## Requirements

Ensure you have the following installed before running the tool:

- **requests** — For making API requests to Wikipedia.
- **reportlab** — For generating PDF files of the article content.
- **rich** — For displaying beautiful, styled tables and panels in the terminal.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Muhammad-Noraeii/WikipediaTool.git
   cd WikipediaTool
   ```

2. **Install dependencies**:
   
   If you haven’t yet, create a virtual environment and activate it, then run:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Once the installation is complete, run the tool using:

```bash
python wikipedia_tool.py
```

You will be presented with an interactive menu in the terminal, offering options like:

- **Search for Articles**: Enter a keyword to get a list of relevant articles.
- **Get Article Summary**: Choose an article to get a brief overview.
- **Get Article Links**: See links to related articles for further exploration.
- **View Full Article**: Get the entire article content directly in your terminal.
- **Change Language**: Switch between Wikipedia’s supported languages.
- **Exit**: Quit the program.

### Example

```bash
1. Search Articles
2. Get Article Summary
3. Get Article Links
4. View Full Article
5. Change Language
6. Exit
Enter your choice: 1
Enter search query: Python
```

### Exporting to PDF

After viewing search results, summaries, or full articles, you’ll be prompted with the option to save the output as a **PDF**. This feature allows you to preserve valuable information and refer to it later.



Here are a few screenshots of the tool in action:

- **Search Results**: Displays articles and snippets in a colorful table.
- **Article Summary**: Showcases the article’s summary in a neat panel.
- **Article Links**: Lists related links for further exploration.

### Contributing

We welcome contributions to make this tool even better! Here’s how you can get involved:

1. Fork the repository.
2. Create a branch for your feature.
3. Implement the feature or fix the bug.
4. Submit a pull request with a detailed explanation of the changes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)  for more details.

