import os

from flask import Blueprint
from flask_restplus import Api

from controller.game_controller import api as game_ns

blueprint = Blueprint("api", __name__)
api = Api(
    blueprint,
    title=os.environ.get('FLASK_SERVER_NAME', ''),
    description=os.environ.get('FLASK_SERVER_DESCRIPTION', '')
)

# Routes

api.add_namespace(game_ns, path='/api/game')