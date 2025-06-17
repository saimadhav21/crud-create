import os
from flask import Flask
from dotenv import load_dotenv

api_port = os.getenv("API_PORT")

load_dotenv()

def creat_app():
    app = Flask(__name__)
    
    return app

app = creat_app()

if __name__ == "__main__":
    app.run(debug=True, port=api_port)
