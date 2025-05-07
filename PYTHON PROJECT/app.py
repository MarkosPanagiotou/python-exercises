from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Σύνδεση με τη βάση
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="product_db"
)

cursor = db.cursor(dictionary=True)

# GET /products
@app.route('/products', methods=['GET'])
def get_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return jsonify(products)

# GET /products/<id>
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
    product = cursor.fetchone()
    return jsonify(product if product else {"error": "Product not found"}), 200 if product else 404

# POST /products
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                   (data['name'], data['price'], data['stock']))
    db.commit()
    return jsonify({"message": "Product added"}), 201

# POST /products/bulk
@app.route('/products/bulk', methods=['POST'])
def add_products_bulk():
    products = request.json
    values = [(p['name'], p['price'], p['stock']) for p in products]
    cursor.executemany("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", values)
    db.commit()
    return jsonify({"message": f"{len(products)} products added"}), 201

# PUT /products/<id>
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    cursor.execute("UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s",
                   (data['name'], data['price'], data['stock'], id))
    db.commit()
    return jsonify({"message": "Product updated"})

# PUT /products/<id>/stock
@app.route('/products/<int:id>/stock', methods=['PUT'])
def update_stock(id):
    data = request.json
    cursor.execute("UPDATE products SET stock=%s WHERE id=%s", (data['stock'], id))
    db.commit()
    return jsonify({"message": "Stock updated"})

# DELETE /products/<id>
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "Product deleted"})

# DELETE /products/all
@app.route('/products/all', methods=['DELETE'])
def delete_all_products():
    cursor.execute("DELETE FROM products")
    db.commit()
    return jsonify({"message": "All products deleted"})

if __name__ == '__main__':
    app.run(debug=True)

    
