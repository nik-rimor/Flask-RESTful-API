from flask_restful import Resource, reqparse
from src.models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="This field cannot be left blank."
                        )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "User with this name is already registered"}, 400

        try:
            user = UserModel(**data)
            user.save_to_db()

        except:
            return {"message": "An error occurred registering the user."}, 500


        return {"message": "User created successfully."}, 201

