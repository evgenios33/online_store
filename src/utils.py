import json
import os

from .categories import Category
from .products import Product


def read_data_from_json(file_path: str) -> dict:
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="UTF-8") as file:
        json_data = json.load(file)

    return json_data


def create_objects_from_json(json_data):
    categories = []
    for item in json_data:
        products = []
        for product in item["products"]:
            products.append(Product(**product))
        item["products"] = products
        categories.append(Category(**item))

    return categories
