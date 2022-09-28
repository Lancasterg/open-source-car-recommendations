from pathlib import Path
from os.path import join
from source.helpers.constants import FilesAndDirectories as fad


def get_root_dir():
    """
    Get the root dir (/path/to/your/project/car-recommendations)
    """
    return Path(str(__file__)).parent.parent.parent.absolute()


def get_dvla_api_key(env: str) -> str:
    """
    Get the API key for the DVLA API
    :param env: One of (dev, prod)
    :return: Either the dev or prod key for the API
    """
    if env not in ("dev", "prod", "local"):
        raise ValueError(f"Invalid argument for env: {env}\n Must be one of: ('dev', 'prod'")
    with open(join(get_root_dir(), fad.DIR_RESOURCES, fad.DIR_API_KEYS, f"{env}-{fad.FILE_CURRENT_DVLA_API_KEY}"), "r") as open_file:
        return open_file.read()

#
# def get_dvla_history_key():
#     with open(join(get_root_dir(), ioc.DIR_DVLA, ioc.DIR_API_KEY, f"{ioc.DIR_API_KEY}.txt"), "r") as open_file:
#         return open_file.read()

