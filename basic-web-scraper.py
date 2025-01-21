
# 6. Basic Web Scraper (Requires 'requests' and 'BeautifulSoup')
def scrape_titles(url):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [tag.text for tag in soup.find_all('h2')]
    print("\nPage Titles:")
    for title in titles:
        print(title)

url = input("Enter a URL to scrape (e.g., https://example.com): ")
scrape_titles(url)