import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import JWTManager

from src.security import EntityLogin
from src.resources.user import UserRegister
from src.resources.item import Item, ItemList
from src.resources.store import Store, StoreList

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
# To allow flask propagating exception even if debug is set to false on app
app.config['PROPAGATE_EXCEPTIONS'] = True
# Set up SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE1_URI')
# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = os.getenv('APP_SECRET_KEY')

api = Api(app)

jwt = JWTManager(app)


api.add_resource(EntityLogin, "/login")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)