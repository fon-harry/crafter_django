import os
import django
from lxml import etree

os.environ['DJANGO_SETTINGS_MODULE'] = 'crafter.settings'
django.setup()
from items.models import Item


def add_items_from_file(file_path):
    xml = etree.ElementTree(file=file_path)
    root = xml.getroot()
    for child in root:

        new_item = Item(
                id=child.get('id'),
                name=child.get('name'),
                type=child.get('type')
        )

        new_item.save()


def add_items(items_path):
    files = os.listdir(items_path)
    files.sort()
    for file in files:
        item_file_path = os.path.join(items_path, file)
        add_items_from_file(item_file_path)


def add_recipes(file_path):
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
    Item.objects.all().delete()
    add_items('./data/items')
    print('Items added: %i' % Item.objects.count())

    # recipes
    # add_recipes('./data/recipes.xml')


if __name__ == '__main__':
    main()
