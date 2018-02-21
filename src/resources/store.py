from flask_restful import Resource
from flask_jwt_extended import jwt_required
from src.models.store import StoreModel


class Store(Resource):

    @jwt_required
    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json(), 200

        return {"message": "No store with name {} found!.".format(name)}, 404


    @jwt_required
    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"message": "There is already a store with name {}".format(store.name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return store.json(), 201  # code for created ok

    @jwt_required
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store is None:
            return {"message": "No item with name {} found!.".format(name)}, 404

        if store.json():
            return {"message": "Store cannot be deleted since there are items in its catalog!"}, 400
        else:
            try:
                store.delete_from_db()
                return {"message": "Store successfully deleted!"}, 200
            except:
                return {"message": "An error occurred deleting the store."}, 500

    # no put method because we are not allowing editing of stores

class StoreList(Resource):
    def get(self):
        try:
            # python way
            return {"Stores": [store.json() for store in StoreModel.query.all()]}, 200
            # alternative map and lambda way
            # return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}

        except:
            return {"message": "An error occurred retrieving the Stores list."}, 500
