import os
import sys

# 設定路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from flask import Flask, jsonify
from flask_cors import CORS
from src.models.user import db
from src.routes.book import book_bp

def create_app():
    app = Flask(__name__)
    
    # 設定密鑰
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # 啟用CORS - 允許所有來源
    CORS(app, origins=['*'])
    
    # 資料庫設定
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # 處理PostgreSQL URL格式
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # 本地開發使用SQLite
        db_path = os.path.join(current_dir, 'src', 'database', 'app.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 初始化資料庫
    db.init_app(app)
    
    # 註冊藍圖
    app.register_blueprint(book_bp, url_prefix='/api')
    
    # 建立資料表
    with app.app_context():
        db.create_all()
    
    # 健康檢查端點
    @app.route('/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'message': '書籍管理API運行正常',
            'endpoints': [
                'GET /api/books - 取得所有書籍',
                'POST /api/books - 新增書籍',
                'GET /api/books/<id> - 取得單一書籍',
                'PUT /api/books/<id> - 更新書籍',
                'DELETE /api/books/<id> - 刪除書籍'
            ]
        })
    
    # 根路徑
    @app.route('/')
    def index():
        return jsonify({
            'message': '歡迎使用書籍管理API',
            'version': '1.0.0',
            'documentation': '/health'
        })
    
    return app

# 建立應用程式實例
app = create_app()

if __name__ == '__main__':
    # 本地開發
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)

