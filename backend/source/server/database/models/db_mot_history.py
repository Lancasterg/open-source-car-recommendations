from datetime import datetime

import humps
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from typing import Dict

db = SQLAlchemy()

class CarModel(db.Model):
    """
    Database model to store data on cars
    """
    registration = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    first_used_date = db.Column(db.String, nullable=False)
    fuel_type = db.Column(db.String, nullable=False)
    primary_colour = db.Column(db.String, nullable=False)


class MotTestsModel(db.Model):
    """
    Database model to store data on MOT tests
    """
    mot_test_number = db.Column(db.String, primary_key=True, nullable=False)
    registration = db.Column(db.String, nullable=False)
    completed_date = db.Column(db.String, nullable=False)
    test_result = db.Column(db.String, nullable=False)
    expiry_date = db.Column(db.String, nullable=True)
    odometer_value = db.Column(db.String, nullable=False)
    odometer_unit = db.Column(db.String, nullable=False)


class RfrCommentsModel(db.Model):
    """
    Database model to store data on MOT comments
    """
    dummy_primary_key = db.Column(db.String, primary_key=True, nullable=False)
    mot_test_number = db.Column(db.String, nullable=False, unique=False)
    text = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=True)


def init_database(app: Flask):
    """
    Initialise the database
    :param app: The Flask application
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()


class DatabaseController:
    """
    Class to interact with the database.

    Also includes methods for serialising
    """

    def serialise(self, model: db.Model) -> Dict:
        """
        Convert db.Model to Dict
        :return: Conversion of db.Model as a Dict object
        """
        return {c: getattr(model, c) for c in inspect(model).attrs.keys()}

    def serialize_all(self, registration: str, car_query_result):
        """
        Serialise all data regarding MOT's to Json
        :param registration: Registration of the car
        :param car_query_result: Result of the initial query to the CarsModel
        :return:
        """
        # Serialise the response for the CarModel
        response = self.serialise(car_query_result)
        mot_response_model = MotTestsModel.query.filter_by(registration=registration).all()

        # Build up list of Json serialised MotTestsModel
        mot_response_list = []
        for mot_attributes in mot_response_model:
            mot_response_json = self.serialise(mot_attributes)
            rfr_comments_model = RfrCommentsModel.query.filter_by(
                mot_test_number=mot_response_json["mot_test_number"]).all()

            # Build up list of Json serialised RfrCommentsModel
            rfr_comments_json = []
            for rfr_comment in rfr_comments_model:
                serialized_rfr = self.serialise(rfr_comment)

                # Remove unwanted keys
                serialized_rfr.pop("dummy_primary_key")
                serialized_rfr.pop("mot_test_number")
                rfr_comments_json.append(serialized_rfr)

            mot_response_json["rfr_comments"] = rfr_comments_json
            mot_response_list.append(mot_response_json)

        response["mot_history"] = mot_response_list

        # Convert keys from snake_case to camelCase
        response = humps.camelize(response)
        return response

    def create_models(self, api_response):
        self.create_new_car_model(api_response)
        self.create_new_mot_tests_model(api_response)
        self.create_new_rfr_comments_model(api_response)

    def create_new_car_model(self, api_response):
        car_model = CarModel(registration=api_response["registration"].upper(),
                             make=api_response["make"].lower(),
                             model=api_response["model"].lower(),
                             first_used_date=api_response["firstUsedDate"],
                             fuel_type=api_response["fuelType"].lower(),
                             primary_colour=api_response["primaryColour"].lower())
        db.session.add(car_model)
        db.session.commit()

    def create_new_mot_tests_model(self, api_response):
        mot_tests = api_response["motTests"]
        for mot_test in mot_tests:
            mot_tests_model = MotTestsModel(registration=api_response["registration"].upper(),
                                            completed_date=mot_test["completedDate"],
                                            test_result=mot_test["testResult"],
                                            expiry_date=mot_test.get("expiryDate"),
                                            odometer_value=mot_test["odometerValue"],
                                            odometer_unit=mot_test["odometerUnit"],
                                            mot_test_number=mot_test["motTestNumber"])
            db.session.add(mot_tests_model)
        db.session.commit()

    def create_new_rfr_comments_model(self, api_response):
        mot_tests = api_response["motTests"]
        for mot_test in mot_tests:
            mot_test_number = mot_test["motTestNumber"]
            for text_comments in mot_test["rfrAndComments"]:
                rfr_comments_model = RfrCommentsModel(dummy_primary_key=f"{datetime.now().microsecond}",
                                                      mot_test_number=mot_test_number,
                                                      text=text_comments["text"],
                                                      type=text_comments["type"])
                db.session.add(rfr_comments_model)
        db.session.commit()
