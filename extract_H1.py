import requests
from bs4 import BeautifulSoup
from read_files import read_files
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/101.0.4951.54 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': 'https://google.com',
    'DNT': '1',
    'Accept-Language': 'en-GB,en;q=0.5'
    }

def extract_h1_tag(url):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        h1_tag = soup.find('h1')
        return h1_tag.text if h1_tag else "No H1 tag found"
    except Exception as e:
        return str(e)

urls = read_files("urls.txt")

for url in urls:
    print(extract_h1_tag(url.strip()))
    time.sleep(5)