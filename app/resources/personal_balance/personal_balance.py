from flask_restful import Resource
from flask import request
from utils.clients.db_client import DBClient


class PersonalBalance(Resource):

    def __init__(self):
        self.json_from_post = request.get_json()
        self.post_output = self._get_data()

    def post(self):
        return self.post_output, 201

    def _get_data(self):
        db = DBClient(db_name="financial")
        df = db.execute_sql_statement(sql_file_name="get_personal_balance",
                                      api_post_json=self.json_from_post)
        return df.to_json()
