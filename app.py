from flask import Flask
from flask_restful import Api
from item import ItemList

app =Flask(__name__)
api = Api(app)

api.add_resource(ItemList,'/items')

if __name__ == "__main__":
    app.run(port = 5000, debug =True)
