import firebase_admin
from firebase_admin import credentials
import json
import logging
import config

try:
    cred = credentials.Certificate(config.DB_CONFIG)
    json_file = open(config.DB_CONFIG)
    json_data = json.load(json_file)
    firebase_admin.initialize_app(
        cred, {"databaseURL": json_data["databaseURL"], "storageBucket": json_data["storageBucket"]}
    )
except Exception as e:
    logging.critical("{}:{}".format("firebase_handler", e))
