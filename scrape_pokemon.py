from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    pokemon = {}

    url = "https://www.pokemon.com/us/pokedex"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    pokemon["name"] = soup.find("a", class_="result-name").get_text()
    pokemon["weaknesses"] = soup.find("span", class_="result-weaknesses).get_text()
    pokemon["abilities"] = soup.find("span", class_="result-abilities").get_text()

    return pokemon
