import sqlite3
from flask_restful import Resource, reqparse
from flask import request
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "Please enter username")
    parser.add_argument(
            'password',
            type = str,
            required = True,
            help = "Please enter password"
    )

    def post(self):
        # check if user already exists
        data = UserRegister.parser.parse_args()
        print(data)
        user = UserModel.findByUsername(data['username'])
        if user:
            return {"Error": "User already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save()
        return user.json(), 201
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()
        # insertQuery = "INSERT INTO users values (NULL,?,?)"
        # cursor.execute(insertQuery, (data['username'], data['password'],))
        # conn.commit()
        # conn.close()
        # return {"Message": "User registered successfully"}, 201
