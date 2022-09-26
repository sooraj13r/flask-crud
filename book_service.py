
from flask_restful import Resource,reqparse
from flask import jsonify
from book_dao import BookData,BookOperations
import logging


class BookService(Resource):
    '''
    Service class used to select, insert, update and delete a book.
    Args:
        null
    Returns:
        null
    Raises:
        null
    '''
    parser= reqparse.RequestParser() # initialize new object
    parser.add_argument('price',
                        type=float,
                        required = True,
                        help= "This filed cannot be left blank"
                        )

    parser.add_argument('title',
                        type=str,
                        required = True,
                        help= "This filed cannot be left blank"
                       )

    def __init__(self) -> None:
        self.book_object = BookOperations()

    def get(self, book_id):
        '''
        Service function to select a book
        Args:
            book_id : str
        Returns:
            Returns dict of fetched data
        Raises:
            null
        '''
        logging.info("GET  method initiated")
        is_book_exist = self.book_object.find_by_id(book_id)
        if is_book_exist:
            result = is_book_exist
            logging.info("Item returned!")
        else:
            result = {'message': "Item not found"}
            logging.warning("Item not found!")
        return result
      
    def put(self, book_id):
        '''
        Service function to update a book
        Args:
            book_id : str
        Returns:
            It will return the updated data as dict
        Raises:
            Raise error message if any error occured during updation
        '''
        logging.info("PUT method initiated")
        data = BookService.parser.parse_args()
        is_book_exist =self.book_object.find_by_id(book_id)
        updated_item = {
                        'title':data['title'], 
                        'price': data['price']
                      }
        result = updated_item
        if is_book_exist:
            
            try:
                self.book_object.update_book(updated_item,
                                             book_id
                                            )  
            except:
                logging.error("An error occured during insertion @ BookService.put()")
                result ={'message': 'An error occued during the updation'}
        else:
            try:
                self.book_object.insert_book(updated_item)
            except:
                logging.error("An error occured during updation @ BookService.put()")
                result = {'message': 'An error occued during the insertion'}
        logging.info("Item updated!")
        return result

    def post(self, book_id):
        '''
        Service function to insert a new book
        Args:
            book_id : str
        Returns:
            It will return the inserted data as dict
        Raises:
            Raise error message if any error occured during insertion
        '''
        logging.info("POST method initiated!")
        is_book_exist =self.book_object.find_by_id(book_id)
        if is_book_exist:
            logging.warning("Item already exists @BookStore.post()")
            result = {'message':'Item already exists'}
        data = BookService.parser.parse_args()
        new_book = {
                    'title':data['title'], 
                    'price': data['price']
                   }
        result = new_book
        try:
            self.book_object.insert_book(new_book)
        except:
            logging.error("An error occured during insertion @ BookService.post()")
            result = {'message': 'An error occured during the inserion'}
        logging.info("Item inserted!")
        return result  

    def delete(self, book_id):
        '''
        Service function to delete a book
        Args:
            book_id : str
        Returns:
            It will return the inserted data as dict
        Raises:
            Raise error message if any error occured during deletion
        '''
        logging.info("DELETE method initiated!")
        is_book_exist =self.book_object.find_by_id(book_id)
        if is_book_exist:
            try:
                self.book_object.delete_book(book_id)
            except:
                logging.error("An error occured during deletion @ BookService.delete()")
                result = {'message': 'An error occured during deletion'}
        else:
            logging.warning("Item does not exists! @ BookService.delete()")
            result = {'message':'Item does not exists'}
        logging.info("Item deleted!")
        result = {'message': 'Items deleted! Book id no : {}'.format(book_id)}
        return result     

class Book(Resource):
    '''
        Service class to retrieve all books
        Args:
            null
        Returns:
            It will retrieve all books as dict
        Raises:
            Raise error message if any error occured during selection
        '''
    def get(self):
        '''
        Service function to retrieve all books
        Args:
            null
        Returns:
            It will etrieve all books as dict
        Raises:
            Raise error message if any error occured during selection
        '''
        logging.info("GET method initiated!")
        try:
            book_obj = BookData()
            res_book = book_obj.get_all_books()
            logging.info("Items returned!") 
        except:
            logging.error("An error occured @ Books.get()")
            res_book = {'message': 'An error occured!'}
        finally:
            return res_book 

class Test(Resource):
    def get(self):
        return {'message': 'Hello Wolrd!'}
    
