import sqlite3
from flask_restful import Resource
from flask import jsonify

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items'
        cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name':row[0],'price':row[1],'price':row[2]})
        result = cursor.fetchall() 
        return jsonify({'Books':result})
