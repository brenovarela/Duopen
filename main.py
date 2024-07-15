import os
import sys
import django
import fire
from src.pluggy import Pluggy
from src.config import PLUGGY_CLIENT_ID, PLUGGY_CLIENT_SECRET


# Configurar o ambiente Django
sys.path.append(os.path.join(os.path.dirname(__file__), 'website'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.website.settings')
django.setup()

from example.models import Item

def insert_item(item_id):
    pluggy = Pluggy(PLUGGY_CLIENT_ID, PLUGGY_CLIENT_SECRET)
    
    try:
        item_data = pluggy.get_item(item_id)
        print(item_data)
        pluggy.send_data_to_endpoint(item_data)
        item, created = Item.objects.get_or_create(item_id=item_id)
        item.item_data = item_data
        item.save()
        print(f'Successfully added/updated item: {item_id}')
    except Exception as e:
        print(f'Failed to add/update item: {item_id}. Error: {e}')

if __name__ == '__main__':
    fire.Fire({
        'insert_item': insert_item
    })
