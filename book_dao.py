import pymysql
from flask import jsonify
from query_config import *
import logging


conn = pymysql.connect(
    host = 'localhost',
    database = 'book_store',
    user = 'root',
    password = '',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor 

)
class BookOperations():
    '''
    DAO Class to provide CRUD operations on the database.
    Args:
        null
    Returns:
        null
    Raises:
        null
    '''
    def find_by_id(self, book_id):
        '''
        DAO Class to provide CRUD operations on the database.
        Args:
            book_id : str
        Returns:
            Fetched data as dict
        Raises:
            Raise exception when fetching operation failed
        '''
        try:
            cursor = conn.cursor()
            cursor.execute(query_select_by_id,
                           (book_id,)
                        )
            result = cursor.fetchall()
            if result:
                return jsonify({'Books':result})
            else:
                return False
        except:
            logging.error("An error occured ! @BookOperations.find_by_id()")
            return {'message':'An error occured! Please try again'}

    def update_book(self,updated_item,book_id):
        '''
        Update function to update a book.
        Args:
            updated_item : dictionary
            book_id : str
        Returns:
            Updated data as dict
        Raises:
            Raise exception when updation operation failed
        '''
        try:
            cursor = conn.cursor()
            cursor.execute(query_update,(updated_item['title'],
                                         updated_item['price'],
                                         book_id)
                                        )
            conn.commit()
        except:
            logging.error("An error occured ! @BookOperations.update_book()")
            return {'message':'An error occured!'}
    
    def insert_book(self, new_item):
        '''
        DAO function to insert a new book.
        Args:
            new_item : dictionary
        Returns:
            Inserted data as dict
        Raises:
            Raise exception when updation operation failed
        '''
        try:
            cursor = conn.cursor()
            cursor.execute(query_insert,(new_item['title'],
                                         new_item['price'])
                                        )
            conn.commit()
        except:
            logging.error("An error occured ! @BookOperations.insert_book()")
            return {'message': 'An error occured!'}
    
    def delete_book(self,
                    book_id
                   ):
        '''
        DAO function to delete an existing book.
        Args:
            book_id : str
        Returns:
            Inserted data as dict
        Raises:
            Raise exception when deletion operation failed
        '''
        try:
            cursor = conn.cursor()
            cursor.execute(query_delete,
                           (book_id,)
                          )
            conn.commit()
        except:
            logging.error("An error occured ! @BookOperations.delete_book()")
            return {'message':'An error occured!'}


class BookData():

    '''
    DAO class to retrieve all data from database.
    Args:
        null
    Returns:
        It will etrieve all books as dict
    Raises:
        Raise error message if any error occured during selection
    '''
    def get_all_books(self):
        '''
        DAO function class to retrieve all books.
        Args:
            null
        Returns:
            It will etrieve all books as dict
        Raises:
            Raise error message if any error occured during selection
        '''
        try:
            cursor = conn.cursor()
            cursor.execute(query_select_all)
            result = cursor.fetchall() 
            return jsonify({'Books':result})
        except:
            logging.error("An error occured! @ Bookdata.get_all_books()")
            return {'message':'An error occured!'}

        