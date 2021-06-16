# -*- coding: utf-8 -*-
# !/usr/bin/python3

# Python standard dependencies
import os

# Python external dependencies
from flask import Flask, send_file, abort, request
from flask_cors import CORS
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource

from utils.Database import Database

from config import config_by_name

FLASK_LEVEL = os.environ.get("FLASK_LEVEL", "dev")

database = Database()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[FLASK_LEVEL])
    CORS(app, supports_credentials=True)
    database.initDatabase(app)
    return app