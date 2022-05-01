from re import A
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data_extraction import get_title, get_description, get_image, get_price

def export_csv(titles, descriptions, images, prices):
    df = pd.DataFrame(list(zip(titles, descriptions, images, prices)),
                columns = ["title", "description", "image", "price"])
    df.to_csv("dior.csv", sep= ";")


URL = "https://www.dior.com/fr_fr/parfum/nouveautes"

print("Getting HTML data from Dior website")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
html = driver.page_source

print("Parsing the HTML")
parser = BeautifulSoup(html, "html.parser")
items = parser.find_all("a", {"class": "product-wrapper"})

titles = []
descriptions = []
images = []
prices = []

print("Extract titles, descriptions, images and prices data from Dior website")
for item in items:
    title = get_title(item)
    description = get_description(item)
    image = get_image(item)
    price = get_price(item)
    titles.append(title)
    descriptions.append(description)
    images.append(image)
    prices.append(price)

export_csv(titles, descriptions, images, prices)
print("The Dior data has been exported into CSV file")






