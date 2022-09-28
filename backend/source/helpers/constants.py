from dataclasses import dataclass

"""
    File to contain all constants.
    Author George Lancaster - lancaster0180@gmail.com
"""


@dataclass
class Urls:
    """
    Dataclass for the API's we will be using
    """

    # Up-to-date with vehicle specifications
    URL_DVLA_CURRENT_PROD = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    URL_DVLA_CURRENT_DEV = "https://uat.driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

    # Historical MOT history
    URL_DVLA_HISTORICAL = "https://beta.check-mot.service.gov.uk/trade/vehicles/mot-tests?registration="


@dataclass
class Environments:
    """
    Which environment are we running in
    """
    DEV = "dev"
    PROD = "prod"
    LOCAL = "local"


@dataclass
class FilesAndDirectories:
    """
    Dataclass for various files and directories
    """

    # Files
    FILE_CURRENT_DVLA_API_KEY = "dvla-current-api-key.txt"
    FILE_HISTORY_DVLA_API_KEY = "dvla-history-api-key.txt"

    # Directories
    DIR_DVLA_CURRENT = "dvla_current"
    DIR_DVLA_HISTORY = "dvla_history"
    DIR_RESOURCES = "resources"
    DIR_SOURCE = "source"
    DIR_API_KEYS = "api-keys"


@dataclass
class EnvironmentVariables:
    """
    Dataclass for environment variables
    """
    ENV_MOT_HISTORY_API_KEY = "ENV_MOT_HISTORY_API_KEY"
