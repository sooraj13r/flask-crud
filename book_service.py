
from flask_restful import Resource
from flask import jsonify
from conn import BookData

class Test(Resource):
    def get(self):
        #obj = BookData()
        #res = obj.get_all_books()
        return {'message': 'Blaa'}
    
