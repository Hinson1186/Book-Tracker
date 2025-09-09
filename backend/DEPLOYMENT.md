# 書籍管理API部署指南

## 部署選項概覽

本書籍管理API系統支援多種部署方式，從本地開發到雲端生產環境都有相應的解決方案。以下是各種部署選項的詳細說明。

## 本地部署

### 開發環境部署

適用於開發和測試階段：

```bash
# 1. 進入專案目錄
cd book-api

# 2. 啟動虛擬環境
source venv/bin/activate

# 3. 啟動開發伺服器
python run_server.py
```

開發伺服器特色：
- 自動重載：程式碼變更時自動重啟
- 詳細錯誤訊息：便於除錯
- 僅適用於開發環境，不建議用於生產

### 生產環境本地部署

使用Gunicorn作為WSGI伺服器：

```bash
# 1. 安裝Gunicorn
pip install gunicorn

# 2. 更新requirements.txt
pip freeze > requirements.txt

# 3. 啟動生產伺服器
gunicorn -w 4 -b 0.0.0.0:5001 run_server:app
```

Gunicorn參數說明：
- `-w 4`：使用4個工作進程
- `-b 0.0.0.0:5001`：綁定到所有網路介面的5001端口
- `run_server:app`：指定應用程式模組和變數

## 雲端部署

### 使用Manus部署服務

最簡單的部署方式是使用Manus內建的部署功能：

```bash
# 確保所有相依套件都在requirements.txt中
pip freeze > requirements.txt

# 使用Manus部署後端服務
# 這將自動處理所有部署細節
```

部署後您將獲得：
- 永久的公開URL
- 自動SSL憑證
- 負載平衡
- 自動擴展

### Railway部署

Railway是一個現代化的雲端部署平台：

1. **準備部署檔案**

建立 `railway.json`：
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn -w 4 -b 0.0.0.0:$PORT run_server:app",
    "healthcheckPath": "/api/books",
    "healthcheckTimeout": 100
  }
}
```

建立 `Procfile`：
```
web: gunicorn -w 4 -b 0.0.0.0:$PORT run_server:app
```

2. **部署步驟**
```bash
# 安裝Railway CLI
npm install -g @railway/cli

# 登入Railway
railway login

# 初始化專案
railway init

# 部署
railway up
```

### Heroku部署

Heroku是知名的PaaS平台：

1. **準備Heroku檔案**

建立 `Procfile`：
```
web: gunicorn -w 4 -b 0.0.0.0:$PORT run_server:app
```

建立 `runtime.txt`：
```
python-3.11.0
```

2. **部署步驟**
```bash
# 安裝Heroku CLI
# 下載：https://devcenter.heroku.com/articles/heroku-cli

# 登入Heroku
heroku login

# 建立應用程式
heroku create your-book-api

# 設定環境變數
heroku config:set FLASK_ENV=production

# 部署
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### DigitalOcean App Platform

DigitalOcean提供簡單的應用程式部署服務：

1. **準備部署設定**

建立 `.do/app.yaml`：
```yaml
name: book-api
services:
- name: api
  source_dir: /
  github:
    repo: your-username/book-api
    branch: main
  run_command: gunicorn -w 4 -b 0.0.0.0:$PORT run_server:app
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  http_port: 5001
  routes:
  - path: /
```

2. **部署步驟**
- 登入DigitalOcean控制台
- 選擇App Platform
- 連接GitHub repository
- 選擇部署設定
- 點擊部署

### AWS Elastic Beanstalk

Amazon的應用程式部署服務：

1. **準備AWS檔案**

建立 `.ebextensions/python.config`：
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: run_server:app
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: /opt/python/current/app
```

2. **部署步驟**
```bash
# 安裝EB CLI
pip install awsebcli

# 初始化EB應用程式
eb init

# 建立環境並部署
eb create book-api-env
eb deploy
```

## 環境變數設定

### 必要環境變數

```bash
# Flask設定
FLASK_ENV=production
SECRET_KEY=your-secret-key-here

# 資料庫設定（如使用外部資料庫）
DATABASE_URL=sqlite:///app.db

# CORS設定
CORS_ORIGINS=*
```

### 設定方式

**本地環境：**
建立 `.env` 檔案：
```bash
FLASK_ENV=production
SECRET_KEY=your-very-secret-key
```

**雲端平台：**
大多數雲端平台都提供環境變數設定介面，或透過CLI設定：
```bash
# Heroku
heroku config:set SECRET_KEY=your-secret-key

# Railway
railway variables set SECRET_KEY=your-secret-key
```

## 資料庫考量

### SQLite（預設）

優點：
- 無需額外設定
- 適合小型應用程式
- 檔案型資料庫，易於備份

限制：
- 不支援高並發
- 不適合大型應用程式
- 雲端部署時資料可能遺失

### PostgreSQL（建議用於生產環境）

修改 `run_server.py` 以支援PostgreSQL：

```python
import os
from urllib.parse import urlparse

# 資料庫設定
database_url = os.environ.get('DATABASE_URL')
if database_url:
    # 解析DATABASE_URL
    url = urlparse(database_url)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # 預設使用SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(current_dir, 'src/database', 'app.db')}"
```

安裝PostgreSQL相依套件：
```bash
pip install psycopg2-binary
```

## 效能優化

### 快取設定

安裝Redis快取：
```bash
pip install redis flask-caching
```

在 `run_server.py` 中新增快取：
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/api/books')
@cache.cached(timeout=300)  # 快取5分鐘
def get_books():
    # 原有程式碼
```

### 資料庫連線池

```python
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,
    'pool_recycle': 120,
    'pool_pre_ping': True
}
```

### 壓縮回應

```python
from flask_compress import Compress

Compress(app)
```

## 監控與日誌

### 基本日誌設定

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/book-api.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
```

### 健康檢查端點

新增健康檢查功能：
```python
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()}
```

## 安全性設定

### HTTPS設定

生產環境必須使用HTTPS：

```python
from flask_talisman import Talisman

# 強制HTTPS
Talisman(app, force_https=True)
```

### API金鑰驗證

新增簡單的API金鑰驗證：
```python
from functools import wraps

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != os.environ.get('API_KEY'):
            return jsonify({'error': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/books', methods=['POST'])
@require_api_key
def create_book():
    # 原有程式碼
```

### 速率限制

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/books', methods=['POST'])
@limiter.limit("10 per minute")
def create_book():
    # 原有程式碼
```

## 備份策略

### 自動備份腳本

```python
import shutil
import datetime
import os

def backup_database():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    source = 'src/database/app.db'
    destination = f'backups/app_backup_{timestamp}.db'
    
    os.makedirs('backups', exist_ok=True)
    shutil.copy2(source, destination)
    print(f'備份完成：{destination}')

# 設定定期備份（可使用cron job）
```

### 雲端備份

使用雲端儲存服務：
```python
import boto3

def upload_to_s3(file_path, bucket_name, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        return True
    except Exception as e:
        print(f'上傳失敗：{e}')
        return False
```

## 故障排除

### 常見問題

1. **端口被佔用**
```bash
# 查找佔用端口的進程
lsof -i :5001

# 終止進程
kill -9 <PID>
```

2. **資料庫連線錯誤**
```bash
# 檢查資料庫檔案權限
ls -la src/database/

# 重建資料庫
rm src/database/app.db
python run_server.py
```

3. **記憶體不足**
```bash
# 檢查記憶體使用
free -h

# 重啟應用程式
sudo systemctl restart your-app
```

### 日誌分析

```bash
# 查看最新日誌
tail -f logs/book-api.log

# 搜尋錯誤
grep "ERROR" logs/book-api.log

# 分析存取模式
awk '{print $1}' access.log | sort | uniq -c | sort -nr
```

## 維護建議

### 定期維護任務

1. **每日**
   - 檢查應用程式狀態
   - 監控錯誤日誌
   - 檢查磁碟空間

2. **每週**
   - 備份資料庫
   - 更新相依套件
   - 檢查安全性更新

3. **每月**
   - 效能分析
   - 清理舊日誌
   - 檢查資源使用情況

### 更新流程

```bash
# 1. 備份現有資料
cp src/database/app.db backups/

# 2. 更新程式碼
git pull origin main

# 3. 更新相依套件
pip install -r requirements.txt

# 4. 重啟服務
sudo systemctl restart book-api
```

---

**注意：** 選擇部署方式時請考慮您的技術能力、預算和擴展需求。對於初學者，建議從Manus部署服務或Railway開始，這些平台提供簡單的部署流程和良好的文件支援。

