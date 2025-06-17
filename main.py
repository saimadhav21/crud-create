import os
from flask import Flask
from dotenv import load_dotenv
from routes.user_routes import user_bp

api_port = os.getenv("API_PORT")

load_dotenv()

def creat_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp)

    return app

app = creat_app()

if __name__ == "__main__":
    app.run(debug=True, port=api_port)
