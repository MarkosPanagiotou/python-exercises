import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='markos',       
        password='markos2003',   
        database='products_db'
    )
    
    return connection
