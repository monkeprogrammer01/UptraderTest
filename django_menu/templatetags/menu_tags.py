from django import template
from django.urls import reverse, NoReverseMatch
from django_menu.models import Menu, MenuItem

register = template.Library()

def build_menu_tree(menu_items):
    children_map = {item.id: [] for item in menu_items}
    tree = []

    for item in menu_items:
        if item.parent_id and item.parent_id in children_map:
            children_map[item.parent_id].append(item)
        else:
            tree.append(item)

    return tree, children_map


@register.inclusion_tag('django_menu/django_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    print(request)
    if not request:
        return {'menu_tree': [], 'children_map': {}, 'current_path': ''}

    current_path = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': [], 'children_map': {}, 'current_path': current_path}

    menu_items = menu.items.select_related('parent').all()

    tree, children_map = build_menu_tree(menu_items)

    return {
        'menu_tree': tree,
        'children_map': children_map,
        'current_path': current_path
    }
