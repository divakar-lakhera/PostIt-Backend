import logging

logging.info("Init Database")
import app.db.keys
from firebase_admin import db, storage
import app.db.firebase_handler
import time


try:
    database_reference = db.reference("/")
    post_reference = database_reference.child("posts")
    user_reference = database_reference.child("users")
    rate_limiter_reference = database_reference.child("rlm")
    storage_bucket = storage.bucket()
except Exception as e:
    logging.critical("{}".format(e))
logging.info("Init Database Complete")


def write_for_post(post_id, user_id, resource_url, is_private, expiration_time):
    database_entry = {
        post_id: {
            "user_id": user_id,
            "res_url": resource_url,
            "exp_time": expiration_time,
            "is_private": is_private,
            "p_time": int(time.time_ns()),
        }
    }
    try:
        post_reference.set(database_entry)
    except Exception as e:
        logging.critical("{}".format(e))


def write_for_user(user_id, email_id, pwd_hash):
    database_entry = {
        user_id: {
            "user_id": user_id,
            "email_id": email_id,
            "pwd_hash": pwd_hash,
            "p_time": int(time.time_ns()),
        }
    }
    try:
        user_reference.set(database_entry)
    except Exception as e:
        logging.critical("{}".format(e))


def upload_post(user_id, post_id, content):
    try:
        file_blob = storage_bucket.blob("{}".format(post_id))
        file_blob.upload_from_string(content)
    except Exception as e:
        logging.critical("{}".format(e))


def delete_post(user_id, post_id):
    try:
        file_blob = storage_bucket.blob("{}".format(post_id))
        file_blob.delete()
    except Exception as e:
        logging.critical("{}".format(e))


def rl_get_prev(userid):
    pass
