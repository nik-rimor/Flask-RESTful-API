from src.db import db

class StoreModel(db.Model):
    __tablename__ = "tblStores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # knows it is a many to one relationship , so this is a list
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            "name": self.name,
            "items": [item.json() for item in self.items.all()]
        }

    def check_empty(self):
        return next((item.json() for item in self.items.all()), None)

    @classmethod
    def find_by_name(cls, name):
        return StoreModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

