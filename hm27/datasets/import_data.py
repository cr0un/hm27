import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hm27.settings')

import django
django.setup()

from ads.models import Ad, Category

def load_data_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def import_data_to_database():
    ads_data = load_data_from_json('./hm27/datasets/ads.json')
    categories_data = load_data_from_json('./hm27/datasets/categories.json')

    for category_data in categories_data:
        category_id = category_data.pop("id")
        if not Category.objects.filter(id=category_id).exists():  # Проверьте, существует ли категория
            Category.objects.create(id=category_id, **category_data)

    for ad_data in ads_data:
        ad_id = ad_data["id"]
        if not Ad.objects.filter(id=ad_id).exists():  # Проверьте, существует ли объявление
            ad_data["price"] = float(ad_data["price"])
            ad_data["is_published"] = ad_data["is_published"] == "TRUE"
            category = Category.objects.first()  # Получаем первую категорию
            Ad.objects.create(category=category, **ad_data)  # Создаем объявление с категорией

import_data_to_database()


if __name__ == '__main__':
    import_data_to_database()
