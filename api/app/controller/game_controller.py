import os

from flask_restplus import Namespace, Resource

from service.game_service import GameService

api = Namespace('Game', description='Game-related operations')

@api.route('/')
class GameGet(Resource):
    def get(self):
        response = GameService.get()
        return response.getResponse()

@api.route('/<string:game_name>/')
class GameLaunch(Resource):
    def get(self, game_name):
        return GameService.getGame(game_name)

@api.route('/<string:game_name>/<string:filename>')
class GameGetFile(Resource):
    def get(self, game_name, filename):
        return GameService.getFileGame(game_name, filename)