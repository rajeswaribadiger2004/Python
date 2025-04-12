import requests
from bs4 import BeautifulSoup

def get_quotes(page_number):
    """Fetch quotes from a specific page number on 'Quotes to Scrape'."""
    url = f"http://quotes.toscrape.com/page/{page_number}/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []

    # Extract quotes, authors, and tags
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes

def display_quotes(quotes):
    """Format and display the quotes in a user-friendly way."""
    if not quotes:
        print("No quotes found.")
        return

    for i, quote in enumerate(quotes, start=1):
        print(f"Quote {i}:")
        print(f"  \"{quote['text']}\"")
        print(f"  - {quote['author']}")
        print(f"  Tags: {', '.join(quote['tags']) if quote['tags'] else 'None'}")
        print("-" * 50)

def main():
    print("Welcome to the Quote Scraper!")

    while True:
        # Ask the user for the page number to scrape
        page_number = input("Enter the page number to scrape (or 'quit' to exit): ")
        
        if page_number.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break
        
        # Validate page number
        if not page_number.isdigit():
            print("Please enter a valid number.")
            continue
        
        page_number = int(page_number)
        quotes = get_quotes(page_number)
        
        if quotes:
            display_quotes(quotes)
        else:
            print(f"Could not retrieve quotes from page {page_number}.")

if __name__ == "__main__":
    main()

#OUTPUT
'''
Welcome to the Quote Scraper!
Enter the page number to scrape (or 'quit' to exit): 6
Quote 1:
  "“There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves, it is not my nature.”"
  - Jane Austen
  Tags: friendship, love
--------------------------------------------------
Quote 2:
  "“Do one thing every day that scares you.”"
  - Eleanor Roosevelt
  Tags: attributed, fear, inspiration
--------------------------------------------------
Quote 3:
  "“I am good, but not an angel. I do sin, but I am not the devil. I am just a small girl in a big world trying to find someone to love.”"
  - Marilyn Monroe
  Tags: attributed-no-source
--------------------------------------------------
Quote 4:
  "“If I were not a physicist, I would probably be a musician. I often think in music. I live my daydreams in music. I see my life in terms of music.”"
  - Albert Einstein
  Tags: music
--------------------------------------------------
Quote 5:
  "“If you only read the books that everyone else is reading, you can only think what everyone else is thinking.”"
  - Haruki Murakami
  Tags: books, thought
--------------------------------------------------
Quote 6:
  "“The difference between genius and stupidity is: genius has its limits.”"
  - Alexandre Dumas fils
  Tags: misattributed-to-einstein
--------------------------------------------------
Quote 7:
  "“He's like a drug for you, Bella.”"
  - Stephenie Meyer
  Tags: drug, romance, simile
--------------------------------------------------
Quote 8:
  "“There is no friend as loyal as a book.”"
  - Ernest Hemingway
  Tags: books, friends, novelist-quotes
--------------------------------------------------
Quote 9:
  "“When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.”"
  - Helen Keller
  Tags: inspirational
--------------------------------------------------
Quote 10:
  "“Life isn't about finding yourself. Life is about creating yourself.”"
  - George Bernard Shaw
  Tags: inspirational, life, yourself,life
----------------------------------------'''
