import csv


class ItemRepository:

    def __init__(self):
        self.items = []
        self.load_items()

    def load_items(self):
        with open('sample_grocery.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.items.append(row)

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def delete_item(self, sku):
        for index, item in enumerate(self.items):
            if item['sku'] == sku:
                del self.items[index]
                break
