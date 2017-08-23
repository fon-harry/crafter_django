import os
import json
from collections import OrderedDict
from lxml import etree

items = []


def increment(counter=[0]):
    counter[0] += 1
    return counter[0]


def parse_item_file(file_path):
    xml = etree.ElementTree(file=file_path)
    root = xml.getroot()
    for child in root:
        item_id = child.get('id')
        item_type = child.get('type')
        item_name = child.get('name')

        fields = OrderedDict([
            ('item_id', item_id),
            ('item_type', item_type),
            ('item_name', item_name),
        ])

        item = OrderedDict([
            ('model', 'items.item'),
            ('pk', increment()),
            ('fields', fields)
        ])

        items.append(item)


def get_items(items_path):
    files = os.listdir(items_path)
    files.sort()
    for file in files:
        item_file_path = os.path.join(items_path, file)
        parse_item_file(item_file_path)


def get_recipes(file_path):
    xml = etree.ElementTree(file=file_path)
    root = xml.getroot()
    for child in root:
        item_id = child.get('id')
        recipe_name = child.get('name')

        print(item_id, recipe_name)

        for stats in child:
            print(stats.values())


def main():
    # items
    get_items('./data_/items')

    with open('items.json', 'w') as f:
        json.dump(items, f, indent=4)

    # recipes
    # get_recipes('./data_/recipes.xml')


if __name__ == '__main__':
    main()
