# models.py

from flask import jsonify
from db import get_db_connection

def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

def get_product_by_id(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return jsonify(product) if product else ('Product not found', 404)

def add_product(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                   (data['name'], data['price'], data['stock']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added'}), 201

def bulk_add(data_list):
    conn = get_db_connection()
    cursor = conn.cursor()
    for data in data_list:
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                       (data['name'], data['price'], data['stock']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Bulk insert completed'}), 201

def update_product(product_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s",
                   (data['name'], data['price'], data['stock'], product_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product updated'})

def update_stock(product_id, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock = %s WHERE id = %s", (stock, product_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Stock updated'})

def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product deleted'})

def delete_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products")
    conn.commit()
    conn.close()
    return jsonify({'message': 'All products deleted'})
