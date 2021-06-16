from flask_sqlalchemy import SQLAlchemy

from utils.logger import Logger

class Database():
    def __init__(self) -> None:
        self.database = SQLAlchemy()

    def getDatabase(self):
        return self.database
    
    def initDatabase(self, app):
        self.database.init_app(app)

    def save_changes(self, data = False):
        try:
            if data is not False:
                self.database.session.add(data)
            self.database.session.commit()
            return True
        except Exception as e:
            print(e)
            return False