import requests
from bs4 import BeautifulSoup
from collections import Counter
import json

def count_words(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    words = text.split()
    word_counts = Counter(words)
    word_counts_dict = dict(word_counts)
    
    json_output = json.dumps(word_counts_dict)
    return json_output
