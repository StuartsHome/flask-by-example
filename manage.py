import os
from flask_migrate import Migrate, MigrateCommand#, Manager
from flask_script import Manager

from app import app, db             # Importing variables from app

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)
#migrate = Migrate()
#db.init_app(app)
#migrate.init_app(app, db)

"""
def create_app():
    db.init_app(app)
    migrate.init_app(app, db)
    return app
"""
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()