from flask import jsonify
from flask_restful import Resource

from source.external_api.dvla_history.dvla_history_api import DvlaApi
from source.server.database.models.db_mot_history import DatabaseController, CarModel


class MotApi(Resource):
    ENDPOINT = "/v1/motHistory/<string:registration>"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dvla_history_api = DvlaApi()
        self.db_controller = DatabaseController()

    def _clean_registration(self, registration: str):
        return ''.join(char for char in registration if char.isalnum()).upper()

    def get(self, registration: str):
        registration = self._clean_registration(registration)
        car_query_result = CarModel.query.get(registration)

        # If registration doesn't exist or is out of date
        if car_query_result is None:
            dvla_response = self.dvla_history_api.make_request(registration)[0]
            self.db_controller.create_models(dvla_response)
            response = dvla_response
        else:
            response = self.db_controller.serialize_all(registration, car_query_result)
        return jsonify(response)

    def put(self, registration: str):
        pass
