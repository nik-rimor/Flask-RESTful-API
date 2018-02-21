from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp
from src.resources.user import UserModel

# users = [
#     User(1, "bob", "asdf"),
#     User(2, "spyros", "asdf")
# ]
#
# # this is a set comprehension that returns a set with username mapping for our users
# username_mapping = {u.username: u for u in users }
#
# # this is a set comprehension that returns a set with userid mapping for our users
# userid_mapping = { u.id: u for u in users}


class EntityLogin(Resource):
    def post(self):
        request_data = request.get_json()
        username = request_data['username']
        password = request_data['password']
        user = UserModel.find_by_username(username)
        if user and safe_str_cmp(user.password, password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        else:
            return {"message": "Invalid Login data"}



# def authenticate(username, password):
#     user = username_mapping.get(username, None)
#     if user and safe_str_cmp(user.password, password) :
#         return user
#
# def identity(payload):
#     user_id =payload['identity']
#     return User.find_by_id()
