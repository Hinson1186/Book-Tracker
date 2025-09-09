# 書籍管理API - 快速開始指南

## 5分鐘快速上手

### 1. 啟動API伺服器

```bash
cd book-api
source venv/bin/activate
python run_server.py
```

看到以下訊息表示啟動成功：
```
啟動書籍API伺服器...
 * Running on http://127.0.0.1:5001
```

### 2. 測試API功能

開啟新的終端視窗，執行測試：
```bash
cd book-api
source venv/bin/activate
python test_api_5001.py
```

### 3. 新增您的第一本書

使用curl命令新增書籍：
```bash
curl -X POST http://localhost:5001/api/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "您的書名",
    "author": "作者姓名",
    "cover_image_url": "封面圖片URL"
  }'
```

### 4. 查看所有書籍

```bash
curl -X GET http://localhost:5001/api/books
```

## 常用API端點

| 功能 | 方法 | URL | 說明 |
|------|------|-----|------|
| 取得所有書籍 | GET | `/api/books` | 返回書籍清單 |
| 新增書籍 | POST | `/api/books` | 新增一本書 |
| 取得單一書籍 | GET | `/api/books/{id}` | 根據ID取得書籍 |
| 更新書籍 | PUT | `/api/books/{id}` | 更新書籍資訊 |
| 刪除書籍 | DELETE | `/api/books/{id}` | 刪除書籍 |

## 下一步

- 閱讀完整的 [README.md](README.md) 了解詳細功能
- 查看 [DEPLOYMENT.md](DEPLOYMENT.md) 學習部署方式
- 開始準備您的書籍資料並使用API管理

