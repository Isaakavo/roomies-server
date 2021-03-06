from jose import jwt, JWTError
from datetime import datetime, timedelta
from flask import make_response, jsonify
from schemas.schemas import TokenDataSchema

#Secret Key
#Algorith
#Expiration time

SECRET_KEY = 'a0553cb8e8d497fd1fea5fb5798dbf9e8468cdd45dd166170bc8327ad82c637c'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

token_data_schema = TokenDataSchema()

def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
  return encoded_jwt

# To verify the token we pass all the string containing the Bearer key and the JWT
# once it is decoded it must contain the user id and expiration time
# The libraty check if the token has expired, if it has, an error is thrown
def get_current_user(token: str):
  try:
    jwtData = token.split()[1]
    payload = jwt.decode(jwtData, SECRET_KEY, algorithms= [ALGORITHM])
    token_data = token_data_schema.dump(payload)
  except JWTError as e:
    print(e)
    resp = make_response({'error':str(e)}, 401,{'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'})
    return resp
  return token_data

