from db_commands import start_database
from flask_app import app

if __name__ == "__main__":
    start_database()
    app.run()
