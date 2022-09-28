from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from source.server.database.models.db_mot_history import init_database
from source.server.endpoints.v1 import MotApi

app = Flask(__name__)
api = Api(app)
CORS(app)
init_database(app)

api.add_resource(MotApi, MotApi.ENDPOINT)

if __name__ == '__main__':
    app.run(debug=True)
