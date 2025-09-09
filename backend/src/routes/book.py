from flask import Blueprint, jsonify, request
from src.models.user import db
from src.models.book import Book

book_bp = Blueprint('book', __name__)

@book_bp.route('/books', methods=['GET'])
def get_books():
    """取得所有書籍"""
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@book_bp.route('/books', methods=['POST'])
def create_book():
    """新增書籍"""
    data = request.json
    
    # 驗證必要欄位
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': '書名和作者為必填欄位'}), 400
    
    book = Book(
        title=data['title'],
        author=data['author'],
        cover_image_url=data.get('cover_image_url', '')
    )
    
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

@book_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """取得單一書籍"""
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

@book_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """更新書籍"""
    book = Book.query.get_or_404(book_id)
    data = request.json
    
    if not data:
        return jsonify({'error': '請提供要更新的資料'}), 400
    
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.cover_image_url = data.get('cover_image_url', book.cover_image_url)
    
    db.session.commit()
    return jsonify(book.to_dict())

@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """刪除書籍"""
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

