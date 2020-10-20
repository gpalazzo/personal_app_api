from flask_restful import Resource
import pandas as pd
from flask import request


class PersonalBalance(Resource):

    def __init__(self):
        self.json_from_post = request.get_json()

    def post(self):
        return self.json_from_post, 201
