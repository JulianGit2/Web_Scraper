# Scrape Website and check if article is available

import requests
import MailResult
import time
from datetime import datetime
from bs4 import BeautifulSoup

# URL with unavailable product
URL = "Your URL"

headers = {"google my user agent"}


while True:

    page = requests.get(URL, headers=headers)
    soup = str(BeautifulSoup(page.content, "html.parser"))
    available = "OutOfStock" not in soup

    if available:
        MailResult.send_mail()
        print("Found it!")
        break
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, ": Not found")

    time.sleep(60)


