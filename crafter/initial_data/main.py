import os
import django
from lxml import etree

os.environ['DJANGO_SETTINGS_MODULE'] = 'crafter.settings'
django.setup()
from items.models import Item, ItemParam
from recipes.models import Recipe, RecipeProduction, RecipeIngredient


def add_items_from_file(file_path):
    xml_file = etree.ElementTree(file=file_path)
    xml_tag_list = xml_file.getroot()
    for xml_tag_item in xml_tag_list:
        for key in xml_tag_item.attrib:
            if key == 'id':
                atr_id = xml_tag_item.attrib[key]
            elif key == 'name':
                atr_name = xml_tag_item.attrib[key]
            elif key == 'type':
                atr_type = xml_tag_item.attrib[key]
            else:
                print('Item atribut : %s in tag : %s not parsed.' % (key, xml_tag_item.tag))

        new_item = Item(
                id=atr_id,
                name=atr_name,
                type=atr_type
        )

        new_item.save()

        for i in xml_tag_item:
            if i.tag == 'set':
                new_param = ItemParam(
                    item=new_item,
                    name=i.attrib['name'],
                    value=i.attrib['val']
                )

                new_param.save()

            elif i.tag == 'for':
                pass
            elif i.tag == 'cond':
                pass
            else:
                print('Item: %s with id: %s have non parsed tag: %s' % (xml_tag_item.get('name'), xml_tag_item.get('id'),i.tag))


def add_items(items_path):
    files = os.listdir(items_path)
    files.sort()
    for file in files:
        item_file_path = os.path.join(items_path, file)
        add_items_from_file(item_file_path)


def add_recipes(file_path):
    xml_file = etree.ElementTree(file=file_path)
    xml_tag_list = xml_file.getroot()
    for xml_tag_item in xml_tag_list:
        for key in xml_tag_item.attrib:
            if key == 'id':
                atr_id = xml_tag_item.attrib[key]
            elif key == 'name':
                atr_name = xml_tag_item.attrib[key]
            else:
                print('Recipe atribut : %s in tag : %s not parsed.' % (key, xml_tag_item.tag))

        new_recipe = Recipe(
            id=atr_id,
            name=atr_name
        )

        for i in xml_tag_item:
            if i.tag == 'recipe':
                new_recipe.item = Item.objects.get(pk=i.attrib['id'])
                new_recipe.level = i.attrib['level']
                new_recipe.type = i.attrib['type']
            elif i.tag == 'mpCost':
                new_recipe.mpCost = i.text
            elif i.tag == 'successRate':
                new_recipe.successRate = i.text
            elif i.tag == 'production':
                pass
            elif i.tag == 'ingredient':
                pass
            else:
                print('Recipe tag: %s not parsed.' % i.tag)

        new_recipe.save()

        for i in xml_tag_item:
            if i.tag == 'production':
                new_production = RecipeProduction(
                    recipe=new_recipe,
                    item=Item.objects.get(pk=i.attrib['id']),
                    count=i.attrib['count']
                )
                new_production.save()
            elif i.tag == 'ingredient':
                new_ingredient = RecipeIngredient(
                    recipe=new_recipe,
                    item=Item.objects.get(pk=i.attrib['id']),
                    count=i.attrib['count']
                )
                new_ingredient.save()


def main():
    # items
    Item.objects.all().delete()
    ItemParam.objects.all().delete()
    add_items('./data/items')
    print('Items added: %i with %i params' % (Item.objects.count(), ItemParam.objects.count()))

    # recipes
    Recipe.objects.all().delete()
    RecipeProduction.objects.all().delete()
    RecipeIngredient.objects.all().delete()
    add_recipes('./data/recipes.xml')
    print('Recipes added: %i, with %i productions and %i ingridients' % (
        Recipe.objects.count(),
        RecipeProduction.objects.count(),
        RecipeIngredient.objects.count()))

if __name__ == '__main__':
    main()
