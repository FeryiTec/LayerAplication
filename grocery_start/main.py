import flask
from controller.item_resource import ItemController
from repository.item_repository import ItemRepository

item_repository = ItemRepository()
app = flask.Flask(__name__)
item_controller = ItemController(item_repository)


@app.route('/item', methods=['GET'])
def get_items():
    return item_controller.get_items()


@app.route('/item', methods=['POST'])
def add_item():
    return item_controller.add_item()


@app.route('/item/<sku>', methods=['DELETE'])
def delete_item(sku):
    return item_controller.delete_item(sku)


if __name__ == '__main__':
    app.run(debug=True)
