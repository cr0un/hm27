import csv
import json

def csv_to_json(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    return data

ads_csv_file = 'ads.csv'
categories_csv_file = 'categories.csv'

ads_data = csv_to_json(ads_csv_file)
categories_data = csv_to_json(categories_csv_file)

with open('ads.json', 'w', encoding='utf-8') as json_file:
    json.dump(ads_data, json_file, indent=4, ensure_ascii=False)

with open('categories.json', 'w', encoding='utf-8') as json_file:
    json.dump(categories_data, json_file, indent=4, ensure_ascii=False)
