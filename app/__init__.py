from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # CORS(app, origins="*", supports_credentials=False)
    # CORS(app, resources={r"/api/*": {"origins": "*"}})
    # CORS(app)
    CORS(app, resources={r"/api/*": {"origins": ["http://127.0.0.1:5000", "http://127.0.0.1:2000"]}})
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.Model.metadata.reflect(db.engine)
    from .api import configure_api
    configure_api(app)
    return app

app = create_app()

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
