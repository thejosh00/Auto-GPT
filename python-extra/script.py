import requests
from bs4 import BeautifulSoup

def get_html_title(url):
    try:
        # Send a GET request to the URL and fetch the content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response contains an HTTP error status code
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and return the HTML title
        return soup.title.string if soup.title else None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None

# Example usage
url = "https://www.example.com/"
html_title = get_html_title(url)
print("http://www.google.com")

