import csv
import os
from copy import deepcopy

import undetected_chromedriver as uc
import requests
from scrapy import Selector
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from zenrows import ZenRowsClient
import json
driver = uc.Chrome()
url = "https://www.apartments.com/los-angeles-ca/?bb=6phuy5jiwN556r5n2F"

client = ZenRowsClient("") #TODO Add your key
with open("apartments.csv", "r") as file:
    input_records = list(csv.DictReader(file))
all_records = []
fresh = []

proxy = "http://{}:js_render=true@proxy.zenrows.com:8001" #TODO Add your key
proxies = {"http": proxy, "https": proxy}
response = requests.get(url, proxies=proxies, verify=False)
response = Selector(text=response.text)
for record in input_records:
    url = record['link']
    response = requests.get(url, proxies=proxies, verify=False)
    response = Selector(text=response.text)
    item = dict()
    try:
        item['name'] = response.css("#propertyName::text").get("").strip()
    except ValueError:
        pass
    street = "".join(response.css(".delivery-address *::text").extract())
    city_state = " ".join([i.strip() for i in response.css(".stateZipContainer *::text").extract() if i.strip()])
    item['address'] = f"{street} {city_state}"
    item['phone_number'] = response.css(".phoneNumber::text").get('')
    raw = response.css(".rentInfoDetail::text").extract()
    if raw:
        item['rental_price'] = raw[0]
        item['bedroom'] = raw[1]
        item['bathrooms'] = raw[2]
        if len(raw) > 3:
            item['sq_ft'] = raw[3]
        else:
            item['sq_ft'] = ''
    else:
        item['rental_price'] = ''
        item['bedroom'] = ''
        item['bathrooms'] = ''
        item['sq_ft'] = ''
    item['images'] = "".join(response.css(".aspectRatioImage img::attr(src)").extract())
    item['pmc'] = response.css(".pmcLogo::attr(src)").get("").split("/")[-1].replace(".jpg", '')
    item['amenities'] = ", ".join(response.css(".specInfo span::text").extract())
    item['move_in_special'] = response.css(".moveInSpecialsContainer p::text").get("")
    for i in response.css(".pricingGridItem"):
        item['model_name'] = i.css(".modelName::text").get('')
        item['rental'] = i.css(".rentLabel::text").get("").strip()
        raw = [iter.strip() for iter in i.css(".detailsTextWrapper *::text").extract() if iter.strip().replace(',', '')]
        if raw:
            item['model_bedroom'] = raw[0]
            item['model_bathroom'] = raw[1]
            if len(raw)> 2:
                item['model_sq_ft'] = raw[2]
            else:
                item['model_sq_ft'] = ''
            if len(raw) > 3:
                item['model_deposit'] = raw[3]
            else:
                item['model_deposit'] = ''
        else:
            item['model_bathroom'] = ''
            item['model_bedroom'] = ''
            item['model_sq_ft'] = ''
            item['model_deposit'] = ''
        item['model_image'] = i.css(".floorPlanButtonImage::attr(data-background-image)").get("")
        for unit_price in i.css(".grid-container.js-unitExtension"):
            item['unit'] = unit_price.css(".unitColumn span[title]::text").get("")
            item['unit_price'] = unit_price.css(".pricingColumn span[data-rentalkey]::text").get("").strip()
            item['unit_price_sq_ft'] = " ".join(unit_price.css(".sqftColumn span::text").extract())
            item['unit_price_availability'] = "".join([test.strip() for test in unit_price.css(".availableColumn .dateAvailable::text").extract() if test.strip()])
            item['link'] = unit_price.css(".availableColumn .profile::attr(data-apply-now-url)").get("")
            new_item = deepcopy(item)
            all_records.append(new_item)
            print(item)

file_name = f'data_1.csv'
file_exists = os.path.isfile(file_name)

with open(file_name, 'a', newline='', encoding="UTF-8") as csvfile:
    fieldnames = list(all_records[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()
    for entry in all_records:
        writer.writerow(entry)