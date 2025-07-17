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

def store(extracted):
    with open("data.txt",'a') as file:
        file.write(extracted + "\n")

def read():
    with open("data.txt",'r') as file:
        return file.read()



if __name__ == "__main__":
    source = scrape(URL)
    extracted =extract(source)
    print(extracted)
    content = read()
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            mail(extracted)
