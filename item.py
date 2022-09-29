import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import jsonify

class Item(Resource):
    parser= reqparse.RequestParser() # initialize new object
    parser.add_argument('price',
            type=float,
            required = True,
            help= "This filed cannot be left blank"
        )
    # @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': "Item not found"}, 404
    
    @classmethod
    def find_by_name(cls, name):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()  
        connection.close()

        if row:
            return {'item':{'name': row[0], 'price':row[1]}} 
    def post(self, name):
        item = self.find_by_name(name)
        if item:
            return {'message':'Item already exists'}
        
        data =Item.parser.parse_args()
        # data = request.get_json()
        item ={'name':name, 'price':data['price']}
        try:
            self.insert(item)
        except:
            return {'message': 'An error occured during the inserion'}, 500 #internal server error
        return item,201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('INSERT INTO items VALUES(?,?)', (item['name'],item['price']))
        connection.commit()
        connection.close()

    def delete(self, name):
        item = self.find_by_name(name)
        if item is None:
            return {'message':'Item does not exists'},400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'DELETE FROM items WHERE name = ?'
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {'message': 'Items deleted'}

    def put(self, name):

        data = Item.parser.parse_args()
        item =self.find_by_name(name)
        updated_item = {'name':name, 'price': data['price']}
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {'message': 'An error occued during the insertion'},500
        else:
            try:
                self.update(updated_item)
            except:
                return {'message': 'An error occued during the updation'},500
        return updated_item
    def update(cls,item):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'UPDATE items SET price = ? WHERE name =?'
        cursor.execute(query,(item['price'],item['name']))
        connection.commit()
        connection.close()

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