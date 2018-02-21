from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from src.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument("store_id",
                        type=int,
                        required=True,
                        help="Every item needs a store id."
                        )

    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json(), 200

        return {"message": "No item with name {} found!.".format(name)}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            # return a message with Bad Request code 400
            return {"message": "An item with name {} already exists".format(name)}, 400

        # use the get_json() method to retrieve the json data from the page
        #request_data = request.get_json()
        # instead we use the request parser here
        data = Item.parser.parse_args()
        item = ItemModel(name= name, price= data["price"], store_id= data["store_id"]) # or ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500


        return item.json(), 201  # code for created ok

    @jwt_required
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item is None:
            return {"message": "No item with name {} found!.".format(name)}, 404
        else:
            try:
                item.delete_from_db()
            except:
                return {"message": "An error occurred deleting the item."}, 500


        return {"message": "Item Deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        try:
            if item is None:
                item = ItemModel(name, data["price"], data["store_id"])
            else:
                item.price = data["price"]
                item.store_id = data["store_id"]

            item.save_to_db()
        except:
            return {"message": "An error occurred inserting/updating the item."}, 500


        return item.json()


class ItemList(Resource):
    def get(self):
        try:
            # python way
            return {"items": [item.json() for item in ItemModel.query.all()]}, 200
            # alternative map and lambda way
            # return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}

        except:
            return {"message": "An error occurred retrieving the item list."}, 500



