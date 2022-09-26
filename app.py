from flask import Flask
from flask_restful import Api
from book_service import Book,BookService,Test
import logging
from log_config import config_log

config_log()
app = Flask(__name__)
api = Api(app)

api.add_resource(BookService,
                 '/books/<string:book_id>'
                )
api.add_resource(Book,
                 '/books'
                )
api.add_resource(Test,
                 '/test'
                )               

if __name__ == "__main__":
    app.run(port = 5000, debug =True)
    logging.info('Host sarted on port:{}'.format(5000))