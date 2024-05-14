from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@localhost:3306/blog_db"
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

