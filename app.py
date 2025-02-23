from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# 📌 Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"id": book.id, "title": book.title, "author": book.author, "year": book.year} for book in books])

# 📌 Get book by title
@app.route('/books/title/<string:title>', methods=['GET'])
def get_book_by_title(title):
    book = Book.query.filter_by(title=title).first()
    if book:
        return jsonify({"id": book.id, "title": book.title, "author": book.author, "year": book.year})
    return jsonify({"error": "Book not found"}), 404

# 📌 Get book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({"id": book.id, "title": book.title, "author": book.author, "year": book.year})
    return jsonify({"error": "Book not found"}), 404

# 📌 Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data["title"], author=data["author"], year=data["year"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully!", "book": {"id": new_book.id, "title": new_book.title, "author": new_book.author, "year": new_book.year}})

# 📌 Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        data = request.json
        book.title = data.get("title", book.title)
        book.author = data.get("author", book.author)
        book.year = data.get("year", book.year)
        db.session.commit()
        return jsonify({"message": "Book updated successfully!", "book": {"id": book.id, "title": book.title, "author": book.author, "year": book.year}})
    return jsonify({"error": "Book not found"}), 404

# 📌 Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully!"})
    return jsonify({"error": "Book not found"}), 404

# 📌 Run Flask App
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return "Welcome to the Flask CRUD API!"

# 📌 Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"id": book.id, "title": book.title, "author": book.author, "year": book.year} for book in books])

# 📌 Get book by title
@app.route('/books/title/<string:title>', methods=['GET'])
def get_book_by_title(title):
    book = Book.query.filter_by(title=title).first()
    if book:
        return jsonify({"id": book.id, "title": book.title, "author": book.author, "year": book.year})
    return jsonify({"error": "Book not found"}), 404

# 📌 Get book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify({"id": book.id, "title": book.title, "author": book.author, "year": book.year})
    return jsonify({"error": "Book not found"}), 404

# 📌 Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data["title"], author=data["author"], year=data["year"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully!", "book": {"id": new_book.id, "title": new_book.title, "author": new_book.author, "year": new_book.year}})

# 📌 Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        data = request.json
        book.title = data.get("title", book.title)
        book.author = data.get("author", book.author)
        book.year = data.get("year", book.year)
        db.session.commit()
        return jsonify({"message": "Book updated successfully!", "book": {"id": book.id, "title": book.title, "author": book.author, "year": book.year}})
    return jsonify({"error": "Book not found"}), 404

# 📌 Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully!"})
    return jsonify({"error": "Book not found"}), 404

# 📌 Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
