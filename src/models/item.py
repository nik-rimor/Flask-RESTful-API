from src.db import db

class ItemModel(db.Model):
    __tablename__ = "tblItems"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('tblStores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "price": self.price,
            "store_id": self.store_id,
            "store": self.store.name
        }
    @classmethod
    def find_by_id(cls, id):
        return ItemModel.query.filter_by(id=int(id)).first()

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

