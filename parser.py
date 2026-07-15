import requests
from bs4 import BeautifulSoup

def fetch_habr_headlines():
    url = "https://habr.com/ru/all/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('a', class_='tm-title__link')
        
        print(f"--- Найдено {len(articles)} свежих заголовков ---\n")
        
        for index, article in enumerate(articles, 1):
            headline = article.text.strip()
            print(f"{index}. {headline}")
            
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")

if name == "main":
    fetch_habr_headlines()
