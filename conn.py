import pymysql
from flask import jsonify


# conn = pymysql.connect(
#     host = 'localhost',
#     database = 'book_store',
#     user = 'root',
#     password = '',
#     charset = 'utf8mb4',
#     cursorclass = pymysql.cursors.DictCursor 

# )
conn = pymysql.connect(
    host = '46.17.172.154',
    database = 'u310898995_book_store',
    user = 'u310898995_bookuser',
    password = 'Book@1234',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor 

)


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
            query_select_all = "SELECT * FROM book"
            cursor.execute(query_select_all)
            result = cursor.fetchall() 
            return jsonify({'Books':result})
        except:
            
            return {'message':'An error occured!'}

        
