from flask import request
from flask_restful import Resource, abort
from models.models import UserModel, AssignedTaskModel ,db
from schemas.schemas import UserSchema, TasksSchema
import datetime

user_schema = UserSchema()
task_schema = TasksSchema()

class Users(Resource):
  def get(self):
    data = request.get_json()
    username_req = user_schema.load(data)
    user = UserModel.query.filter_by(username=username_req['username']).first()
    if not user:
      print('aborting')
      abort(404, message='No user with that username')
    resp = user_schema.dump(user)
    return resp, 200

  def post(self):
    data = request.get_json()
    args = user_schema.load(data)
    user = UserModel.query.filter_by(username=args['username']).first()
    if not user:
      print('in user not')  
      user = UserModel(username = args['username'], password = args['password'], created=datetime.datetime.now())
      db.session.add(user)
      db.session.commit()
      resp = user_schema.dump(user)
      return  resp, 201
    resp = user_schema.dump(user)
    return resp, 201


class Tasks(Resource):
  def get(self):
    data = request.get_json()
    args = task_schema.load(data)
    user = UserModel.query.filter_by(username=args['username']).first()
    resp = task_schema.dump(user.tasks, many= True)
    return resp

  def post(self):
    data = request.get_json()
    args = task_schema.load(data)
    user = UserModel.query.filter_by(username=args['username']).first()
    if not user:
      abort(404, message='No user found')
    task = AssignedTaskModel(user_id=user.id ,task=args['task'], description=args['description'], created=datetime.datetime.now(), ended=datetime.datetime.now())
    user.tasks.append(task)
    db.session.add(user)
    db.session.commit()
    resp = user_schema.dump(user)
    return resp, 201