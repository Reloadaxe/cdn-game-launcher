from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from routes import blueprint
from app import create_app, database

# Initialization

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, database.getDatabase(), "/migrations")
manager.add_command('db', MigrateCommand)

# Commands

@manager.command
def run():
    app.run(debug=True, port=5000, host="0.0.0.0")

if __name__ == "__main__":
    manager.run()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', "X-Requested-With, Access-Control-Allow-Headers, Content-Type, Authorization, Origin, Accept")
    return response