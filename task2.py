import requests
from bs4 import BeautifulSoup


# 2. Напишите программу, которая на основе данных таблиц создает список цитат из фильмов, выпущенных после 1995 года:
# https://ru.wikipedia.org/wiki/100_%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85_%D1%86%D0%B8%D1%82%D0%B0%D1%82_%D0%B8%D0%B7_%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%B7%D0%B0_100_%D0%BB%D0%B5%D1%82_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_AFI
def main():
    url = "https://ru.wikipedia.org/wiki/100_известных_цитат_из_американских_фильмов_за_100_лет_по_версии_AFI"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    quotes = []
    for row in soup.find("table", class_="wikitable").findAll("tr")[1:]:
        row_values = row.findAll("td")
        date = int(row_values[6].text)
        if date > 1995:
            quote = row_values[1].text[: len(row_values[1].text) - 1]
            quotes.append(quote)

    print(quotes)


if __name__ == "__main__":
    main()
