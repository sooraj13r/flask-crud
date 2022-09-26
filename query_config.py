
query_select_all= "SELECT * FROM book ORDER BY id DESC"
query_select_by_id = "SELECT * FROM book WHERE id = %s"
query_update = 'UPDATE book SET book_title = %s, book_price = %s WHERE id =%s'
query_insert = 'INSERT INTO book (book_title, book_price) VALUES(%s,%s)'
query_delete = 'DELETE FROM book WHERE id = %s'