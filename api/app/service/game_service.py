import os
from io import StringIO

from flask import send_file, abort, Response
from minio import Minio

from utils.ApiResponse import ApiResponse


MINIO_HOST = os.environ.get("MINIO_HOST")
MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")

client = Minio(
    MINIO_HOST,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

class GameService():
    @staticmethod
    def is_valid_game(game_name):
        try:
            client.get_object("javascript-games", game_name + "index.html")
        except Exception:
            return False
        return True
    
    @staticmethod
    def get():
        response = ApiResponse()

        objs = client.list_objects(
            "javascript-games"
        )
        games = []
        
        for obj in objs:
            if obj.is_dir:
                games.append({
                    "name": obj.object_name[:-1],
                    "valid": GameService.is_valid_game(obj.object_name)
                })

        response.setDetails(games)
        return response
    
    @staticmethod
    def getGame(name):
        filepath = "/tmp/javascript-games/" + name + "/index.html"
        try:
            client.fget_object("javascript-games", name + "/index.html", filepath)
        except Exception as e:
            print(e)
            abort(404)

        with open(filepath, "rb") as fp:
            content = fp.read()
        os.unlink(filepath)
        return Response(content, mimetype="text/html")
    
    @staticmethod
    def getFileGame(game, filename):
        filepath = "/tmp/javascript-games/" + game + "/" + filename
        try:
            client.fget_object("javascript-games", game + "/" + filename, filepath)
        except Exception as e:
            print(e)
            abort(404)

        with open(filepath, "rb") as fp:
            content = fp.read()
        os.unlink(filepath)
        return Response(content)