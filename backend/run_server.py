#!/usr/bin/env python3
import os
import sys

# 設定路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.book import Book
from src.routes.user import user_bp
from src.routes.book import book_bp

app = Flask(__name__, static_folder=os.path.join(current_dir, 'src/static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# 啟用 CORS 以允許跨域請求
CORS(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(book_bp, url_prefix='/api')

# 資料庫設定
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(current_dir, 'src/database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

if __name__ == '__main__':
    print("啟動書籍API伺服器...")
    print("API端點:")
    print("  GET    /api/books       - 取得所有書籍")
    print("  POST   /api/books       - 新增書籍")
    print("  GET    /api/books/<id>  - 取得單一書籍")
    print("  PUT    /api/books/<id>  - 更新書籍")
    print("  DELETE /api/books/<id>  - 刪除書籍")
    print()
    app.run(host='0.0.0.0', port=5001, debug=True)

