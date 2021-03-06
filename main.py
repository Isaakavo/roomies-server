from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from res.api_models import Users, Tasks, Login
from models.models import db
import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/roomies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True  

migrate = Migrate(app, db)

db.init_app(app)


api.add_resource(Users, '/api/users', '/api/users/<username>/tasks') 
api.add_resource(Tasks, '/api/tasks')
api.add_resource(Login, '/api/login')

with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run(debug = True)