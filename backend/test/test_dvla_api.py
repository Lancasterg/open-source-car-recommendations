from source.external_api.dvla_history.dvla_history_api import DvlaApi
import os

api = DvlaApi()
api.make_request("mui7181")
