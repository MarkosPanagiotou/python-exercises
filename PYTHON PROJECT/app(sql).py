from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Markos'
app.config['MYSQL_PASSWORD'] = 'Markos'
app.config['MYSQL_DB'] = 'products_db'

mysql = MySQL(app)


@app.route('/products', methods=['GET'])
def get_products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    cur.close()

    products = [{'id': row[0], 'name': row[1], 'price': row[2], 'stock': row[3]} for row in data]
    return jsonify(products)


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id = %s", (id,))
    data = cur.fetchone()
    cur.close()

    if data:
        product = {'id': data[0], 'name': data[1], 'price': data[2], 'stock': data[3]}
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()
    name = new_product['name']
    price = new_product['price']
    stock = new_product['stock']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Product added successfully'}), 201


@app.route('/products/bulk', methods=['POST'])
def add_products_bulk():
    products = request.get_json()

    cur = mysql.connection.cursor()
    for product in products:
        cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                    (product['name'], product['price'], product['stock']))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Products added successfully'}), 201


@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    update_data = request.get_json()
    name = update_data['name']
    price = update_data['price']
    stock = update_data['stock']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s",
                (name, price, stock, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Product updated successfully'})


@app.route('/products/<int:id>/stock', methods=['PUT'])
def update_product_stock(id):
    update_data = request.get_json()
    stock = update_data['stock']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE products SET stock=%s WHERE id=%s", (stock, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Product stock updated successfully'})


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Product deleted successfully'})


@app.route('/products/all', methods=['DELETE'])
def delete_all_products():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products")
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'All products deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
