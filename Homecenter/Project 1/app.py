from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# modelagem
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json

    if "name" in data and "price" in data:

        product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", "")
        )

        db.session.add(product)
        db.session.commit()

        return jsonify({"message": "Product added successfully!"})

    return jsonify({"error": "Name and price are required"}), 500

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)

    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully!"})
    return jsonify({"error": "Product not found"}), 404

# Definição de uma rota raiz (página inicial)
@app.route('/')
def hello_word():
    return 'Hello, word!'

if __name__ == "__main__":
    app.run(debug=True)
