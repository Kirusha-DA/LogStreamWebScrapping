import requests
from bs4 import BeautifulSoup


# 1. Напишите программу для получения названий последних статей из блога:
# https://www.oreilly.com/radar/
def main():
    url = "https://www.oreilly.com/radar/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    titles = [title.text for title in soup.find_all("h2", class_="post-title")]
    print(titles)


if __name__ == "__main__":
    main()
