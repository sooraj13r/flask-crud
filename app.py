from flask import Flask
from flask import request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item,ItemList

app =Flask(__name__)
app.secret_key ='jose'
api = Api(app)

app.config['JWT_AUH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate,identity) # /auth

# # config JWT to expire within half an hour
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port = 5000, debug =True)