from flask import Flask
from flask_restful import Api
from book_service import Test

main = Flask(__name__)
api = Api(main)
api.add_resource(Test,
                 '/test'
                )               

if __name__ == "__main__":
    app.run(port = 5001, debug =True)
