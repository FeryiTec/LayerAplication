import json
from repository.item_repository import ItemRepository
item_repository = ItemRepository()

class ItemController:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def get_items(self):
        items = self.item_repository.get_items()
        return json.dumps(items)

    def add_item(self):
        item = json.loads(request.data)
        self.item_repository.add_item(item)
        return 'Item added successfully'

    def delete_item(self, sku):
        self.item_repository.delete_item(sku)
        return 'Item deleted successfully'
