import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from time import sleep
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
console = Console()

def animated_intro():
    """
    Displays an animated welcome message.
    """
    console.print("[bold green]Loading Wikipedia CLI Tool...[/bold green]", style="bold green")
    sleep(1)
    console.print("[bold cyan]Welcome to the Wikipedia CLI Tool![/bold cyan]\n", style="bold cyan")
    sleep(0.5)

def get_wikipedia_data(lang, action, params, retries=3, timeout=10):
    """
    Sends a request to the Wikipedia API with the given language, action, and parameters.
    Includes retry logic for network errors.
    """
    base_url = f"https://{lang}.wikipedia.org/w/api.php"
    params['format'] = 'json'
    params['action'] = action

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(base_url, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.Timeout:
            console.print(f":warning: [yellow]Attempt {attempt}/{retries} timed out.[/yellow]")
        except requests.ConnectionError:
            console.print(f":warning: [yellow]Attempt {attempt}/{retries} failed due to connection error.[/yellow]")
        except requests.RequestException as e:
            console.print(f":warning: [yellow]Attempt {attempt}/{retries} failed: {e}[/yellow]")
    console.print(":x: [bold red]Error: Unable to fetch data after multiple attempts.[/bold red]")
    return None

def display_table(title, columns, rows):
    """
    Displays data in a table format.
    Includes styled borders and colors.
    """
    table = Table(title=title, title_style="bold magenta", border_style="bright_green")
    for col in columns:
        table.add_column(col, justify="left", style="cyan", header_style="bold yellow")
    for row in rows:
        table.add_row(*row)
    console.print(table)

def save_to_pdf(title, content, filename):
    """
    Saves the provided content to a PDF file.
    """
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter  # PDF page size

        # Title of the article
        c.setFont("Helvetica-Bold", 16)
        c.drawString(30, height - 40, f"{title}")

        # Font for the content
        c.setFont("Helvetica", 12)

        # Writing the content in the PDF
        text_object = c.beginText(30, height - 60)
        text_object.setFont("Helvetica", 12)
        text_object.setTextOrigin(30, height - 60)
        text_object.textLines(content)

        c.drawText(text_object)
        c.save()

        pdf_size = os.path.getsize(filename) / 1024  # Convert to KB
        console.print(f"[bold green]Saved as PDF:[/bold green] {filename} (Size: {pdf_size:.2f} KB)")
    except Exception as e:
        logging.error(f"Error saving PDF: {e}")
        console.print(":x: [bold red]Failed to save PDF.[/bold red]")

def search_articles(lang, query):
    """
    Searches for articles matching the query and displays the results in a styled table.
    """
    console.print(f"\n[bold yellow]Searching for articles matching:[/bold yellow] '{query}' in '{lang}' Wikipedia...\n")
    params = {'list': 'search', 'srsearch': query}
    data = get_wikipedia_data(lang, 'query', params)
    if data and 'query' in data and data['query']['search']:
        rows = [[str(i), result['title'], result['snippet']] for i, result in enumerate(data['query']['search'], 1)]
        display_table("Search Results", ["#", "Title", "Snippet"], rows)

        # Ask if user wants to save to PDF
        save_choice = input("\nWould you like to save these results as a PDF? (y/n): ").strip().lower()
        if save_choice == 'y':
            search_results_text = "\n".join([f"{i}. {result['title']} - {result['snippet']}" for i, result in enumerate(data['query']['search'], 1)])
            save_to_pdf("Search Results", search_results_text, "search_results.pdf")
        return data['query']['search']
    console.print(":x: [bold red]No results found![/bold red]")
    return []

def get_article_summary(lang, title):
    """
    Fetches the summary of a specific article and displays it in a styled panel.
    Also gives an option to save the summary as PDF.
    """
    console.print(f"\n[bold yellow]Fetching summary for:[/bold yellow] '{title}'\n")
    params = {'prop': 'extracts', 'exintro': True, 'explaintext': True, 'titles': title}
    data = get_wikipedia_data(lang, 'query', params)
    if data and 'query' in data:
        pages = data['query']['pages']
        for page in pages.values():
            if 'extract' in page:
                summary = page['extract']
                console.print(
                    Panel(
                        summary,
                        title=page['title'],
                        title_align="center",
                        style="green",
                        border_style="bright_cyan",
                    )
                )

                # Ask if user wants to save to PDF
                save_choice = input("\nWould you like to save this summary as a PDF? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_to_pdf(page['title'], summary, f"{page['title']}_summary.pdf")
                return
    console.print(":x: [bold red]Summary not available for this article![/bold red]")

def get_article_links(lang, title):
    """
    Fetches links related to a specific article and displays them in a styled table.
    """
    console.print(f"\n[bold yellow]Fetching links for:[/bold yellow] '{title}'\n")
    params = {'prop': 'links', 'titles': title, 'pllimit': 'max'}
    data = get_wikipedia_data(lang, 'query', params)
    if data and 'query' in data:
        pages = data['query']['pages']
        for page in pages.values():
            if 'links' in page:
                rows = [[str(i), link['title']] for i, link in enumerate(page['links'], 1)]
                display_table(f"Links in {title}", ["#", "Link Title"], rows)

                # Ask if user wants to save to PDF
                save_choice = input("\nWould you like to save these links as a PDF? (y/n): ").strip().lower()
                if save_choice == 'y':
                    links_text = "\n".join([f"{i}. {link['title']}" for i, link in enumerate(page['links'], 1)])
                    save_to_pdf(f"Links in {title}", links_text, f"{title}_links.pdf")
                return
    console.print(":x: [bold red]No links available for this article![/bold red]")

def get_full_article(lang, title):
    """
    Fetches and displays the full article from Wikipedia.
    """
    console.print(f"\n[bold yellow]Fetching full article for:[/bold yellow] '{title}'\n")
    params = {'prop': 'extracts', 'explaintext': True, 'titles': title}
    data = get_wikipedia_data(lang, 'query', params)
    if data and 'query' in data:
        pages = data['query']['pages']
        for page in pages.values():
            if 'extract' in page:
                full_article = page['extract']
                console.print(Panel(full_article, title=page['title'], title_align="center", style="green", border_style="bright_cyan"))

                # Ask if user wants to save to PDF
                save_choice = input("\nWould you like to save this full article as a PDF? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_to_pdf(page['title'], full_article, f"{page['title']}_full_article.pdf")
                return
    console.print(":x: [bold red]Full article not available![/bold red]")

def get_random_article(lang="en"):
    """
    Fetches a random article from Wikipedia.
    """
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": 1
    }
    
    data = get_wikipedia_data(lang, "query", params)
    if data and 'query' in data and 'random' in data['query']:
        random_article = data['query']['random'][0]
        title = random_article['title']
        console.print(f"\n[bold yellow]Random Article:[/bold yellow] {title}")
        get_article_summary(lang, title)
        return title
    else:
        console.print(":x: [bold red]Unable to fetch random article.[/bold red]")

def main():
    """
    Main function to handle the Wikipedia CLI tool logic.
    """
    animated_intro()
    lang = input("Enter language code (default: 'en'): ") or 'en'

    while True:
        menu = Panel(
            Text(
                "\n1. Search Articles\n2. Get Article Summary\n3. Get Article Links\n4. View Full Article\n5. Change Language\n6. Random Article\n7. Exit",
                justify="center",
            ),
            title="Main Menu",
            title_align="center",
            border_style="bright_blue",
        )
        console.print(menu)
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            query = input("\nEnter search query: ").strip()
            if query:
                search_articles(lang, query)
            else:
                console.print(":x: [bold red]Search query cannot be empty![/bold red]")

        elif choice == '2':
            title = input("\nEnter article title: ").strip()
            if title:
                get_article_summary(lang, title)
            else:
                console.print(":x: [bold red]Article title cannot be empty![/bold red]")

        elif choice == '3':
            title = input("\nEnter article title: ").strip()
            if title:
                get_article_links(lang, title)
            else:
                console.print(":x: [bold red]Article title cannot be empty![/bold red]")

        elif choice == '4':
            title = input("\nEnter article title: ").strip()
            if title:
                get_full_article(lang, title)
            else:
                console.print(":x: [bold red]Article title cannot be empty![/bold red]")

        elif choice == '5':
            lang = input("\nEnter new language code (e.g., 'en', 'fr', 'de'): ").strip()
            if lang:
                console.print(f":white_check_mark: [bold green]Language changed to:[/bold green] '{lang}'")
            else:
                console.print(":x: [bold red]Language code cannot be empty![/bold red]")

        elif choice == '6':
            get_random_article(lang)  # Calling the random article function

        elif choice == '7':
            console.print("\n[bold green]Goodbye![/bold green]")
            break

        else:
            console.print(":x: [bold red]Invalid choice! Please try again.[/bold red]")

if __name__ == "__main__":
    main()
