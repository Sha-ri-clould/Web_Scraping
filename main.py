import requests
import selectorlib
from emailing import mail
from selectorlib import Extractor

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(URL):
    response = requests.get(URL)
    source = response.text
    return source

def extract(source):
    extractor= selectorlib.Extractor.from_yaml_file("extract.yaml")
    extracted = extractor.extract(source)["tours"]
    return extracted


if __name__ == "__main__":
    source = scrape(URL)
    extracted =extract(source)
    print(extracted)



