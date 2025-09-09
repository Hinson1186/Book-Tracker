# 書籍管理API系統使用指南

## 概述

這是一個基於Flask開發的書籍管理API系統，提供完整的書籍資料管理功能，包括新增、查詢、更新和刪除書籍資料。每本書籍包含書名、作者和封面圖片URL等基本資訊。

## 系統特色

- **RESTful API設計**：遵循REST架構原則，提供直觀的API端點
- **完整的CRUD操作**：支援創建、讀取、更新、刪除書籍資料
- **跨域支援**：內建CORS支援，方便前端應用程式整合
- **資料驗證**：提供完整的輸入資料驗證和錯誤處理
- **SQLite資料庫**：使用輕量級SQLite資料庫，無需額外設定
- **開發友善**：包含完整的測試腳本和詳細的使用說明

## 系統需求

- Python 3.11 或更高版本
- Flask 3.1.1
- Flask-SQLAlchemy
- Flask-CORS

## 安裝與設定

### 1. 環境準備

確保您的系統已安裝Python 3.11或更高版本：

```bash
python3 --version
```

### 2. 啟動虛擬環境

```bash
cd book-api
source venv/bin/activate
```

### 3. 安裝相依套件

所有必要的套件已經安裝在虛擬環境中，包括：
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- requests (用於測試)

### 4. 啟動API伺服器

```bash
python run_server.py
```

伺服器將在 `http://localhost:5001` 啟動，您會看到以下訊息：

```
啟動書籍API伺服器...
API端點:
  GET    /api/books       - 取得所有書籍
  POST   /api/books       - 新增書籍
  GET    /api/books/<id>  - 取得單一書籍
  PUT    /api/books/<id>  - 更新書籍
  DELETE /api/books/<id>  - 刪除書籍

 * Running on http://127.0.0.1:5001
```

## API端點說明

### 基本URL

所有API端點的基本URL為：`http://localhost:5001/api`

### 書籍資料格式

每本書籍包含以下欄位：

| 欄位名稱 | 資料類型 | 必填 | 說明 |
|---------|---------|------|------|
| id | 整數 | 自動生成 | 書籍唯一識別碼 |
| title | 字串 | 是 | 書名 |
| author | 字串 | 是 | 作者姓名 |
| cover_image_url | 字串 | 否 | 封面圖片URL |

### 1. 取得所有書籍

**端點：** `GET /api/books`

**說明：** 取得資料庫中所有書籍的清單

**請求範例：**
```bash
curl -X GET http://localhost:5001/api/books
```

**回應範例：**
```json
[
  {
    "id": 1,
    "title": "Python程式設計",
    "author": "張三",
    "cover_image_url": "https://example.com/python-book.jpg"
  },
  {
    "id": 2,
    "title": "JavaScript權威指南",
    "author": "李四",
    "cover_image_url": "https://example.com/js-book.jpg"
  }
]
```

### 2. 新增書籍

**端點：** `POST /api/books`

**說明：** 新增一本書籍到資料庫

**請求標頭：**
```
Content-Type: application/json
```

**請求主體：**
```json
{
  "title": "書名",
  "author": "作者姓名",
  "cover_image_url": "封面圖片URL（可選）"
}
```

**請求範例：**
```bash
curl -X POST http://localhost:5001/api/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python程式設計",
    "author": "張三",
    "cover_image_url": "https://example.com/python-book.jpg"
  }'
```

**成功回應（201 Created）：**
```json
{
  "id": 1,
  "title": "Python程式設計",
  "author": "張三",
  "cover_image_url": "https://example.com/python-book.jpg"
}
```

**錯誤回應（400 Bad Request）：**
```json
{
  "error": "書名和作者為必填欄位"
}
```

### 3. 取得單一書籍

**端點：** `GET /api/books/<id>`

**說明：** 根據書籍ID取得特定書籍的詳細資訊

**請求範例：**
```bash
curl -X GET http://localhost:5001/api/books/1
```

**成功回應（200 OK）：**
```json
{
  "id": 1,
  "title": "Python程式設計",
  "author": "張三",
  "cover_image_url": "https://example.com/python-book.jpg"
}
```

**錯誤回應（404 Not Found）：**
```json
{
  "message": "The requested URL was not found on the server."
}
```

### 4. 更新書籍

**端點：** `PUT /api/books/<id>`

**說明：** 更新指定ID的書籍資訊

**請求標頭：**
```
Content-Type: application/json
```

**請求主體：**
```json
{
  "title": "新書名（可選）",
  "author": "新作者（可選）",
  "cover_image_url": "新封面URL（可選）"
}
```

**請求範例：**
```bash
curl -X PUT http://localhost:5001/api/books/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python進階程式設計",
    "cover_image_url": "https://example.com/python-advanced.jpg"
  }'
```

**成功回應（200 OK）：**
```json
{
  "id": 1,
  "title": "Python進階程式設計",
  "author": "張三",
  "cover_image_url": "https://example.com/python-advanced.jpg"
}
```

### 5. 刪除書籍

**端點：** `DELETE /api/books/<id>`

**說明：** 從資料庫中刪除指定ID的書籍

**請求範例：**
```bash
curl -X DELETE http://localhost:5001/api/books/1
```

**成功回應（204 No Content）：**
無回應內容，僅回傳狀態碼204

**錯誤回應（404 Not Found）：**
```json
{
  "message": "The requested URL was not found on the server."
}
```

## 錯誤處理

API使用標準的HTTP狀態碼來表示請求結果：

| 狀態碼 | 說明 |
|--------|------|
| 200 | 請求成功 |
| 201 | 資源創建成功 |
| 204 | 請求成功，無回應內容 |
| 400 | 請求格式錯誤或缺少必要欄位 |
| 404 | 請求的資源不存在 |
| 500 | 伺服器內部錯誤 |

## 測試API

系統提供了完整的測試腳本 `test_api_5001.py`，您可以執行以下命令來測試所有API功能：

```bash
python test_api_5001.py
```

測試腳本會依序執行以下測試：
1. 取得所有書籍（空清單）
2. 新增第一本書籍
3. 新增第二本書籍
4. 取得所有書籍（包含兩本書）
5. 取得單一書籍
6. 更新書籍資訊
7. 刪除書籍
8. 確認刪除後的書籍清單
9. 嘗試取得已刪除的書籍（404錯誤）
10. 測試錯誤處理（缺少必要欄位）

## 資料準備指南

### 書籍資料格式

為了方便您準備書籍資料，建議使用以下JSON格式：

```json
{
  "title": "書名",
  "author": "作者姓名",
  "cover_image_url": "封面圖片URL"
}
```

### 封面圖片處理

1. **使用現有圖片URL**：如果您已有書籍封面圖片的網路連結，可直接使用該URL
2. **上傳到圖片託管服務**：建議使用以下免費圖片託管服務：
   - Imgur
   - Cloudinary
   - GitHub（透過repository存放圖片）
3. **本地圖片處理**：如果您有本地圖片，需要先上傳到網路空間才能使用

### 批量資料匯入

如果您有大量書籍資料需要匯入，可以撰寫簡單的Python腳本：

```python
import requests
import json

# 書籍資料清單
books = [
    {
        "title": "第一本書",
        "author": "作者一",
        "cover_image_url": "https://example.com/book1.jpg"
    },
    {
        "title": "第二本書",
        "author": "作者二",
        "cover_image_url": "https://example.com/book2.jpg"
    }
    # 可以繼續新增更多書籍...
]

# 批量新增書籍
for book in books:
    response = requests.post(
        "http://localhost:5001/api/books",
        json=book
    )
    if response.status_code == 201:
        print(f"成功新增：{book['title']}")
    else:
        print(f"新增失敗：{book['title']} - {response.text}")
```

## 部署指南

### 本地開發環境

在開發階段，使用內建的Flask開發伺服器即可：

```bash
python run_server.py
```

### 生產環境部署

對於生產環境，建議使用專業的WSGI伺服器，例如Gunicorn：

1. 安裝Gunicorn：
```bash
pip install gunicorn
```

2. 啟動生產伺服器：
```bash
gunicorn -w 4 -b 0.0.0.0:5001 run_server:app
```

### 雲端部署

您可以將此API部署到各種雲端平台：

- **Heroku**：適合小型專案，提供免費方案
- **Railway**：現代化的部署平台
- **DigitalOcean App Platform**：簡單易用的PaaS服務
- **AWS Elastic Beanstalk**：Amazon的應用程式部署服務

## 前端整合範例

### JavaScript Fetch API

```javascript
// 取得所有書籍
async function getAllBooks() {
    const response = await fetch('http://localhost:5001/api/books');
    const books = await response.json();
    return books;
}

// 新增書籍
async function addBook(bookData) {
    const response = await fetch('http://localhost:5001/api/books', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bookData)
    });
    return await response.json();
}

// 更新書籍
async function updateBook(bookId, bookData) {
    const response = await fetch(`http://localhost:5001/api/books/${bookId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bookData)
    });
    return await response.json();
}

// 刪除書籍
async function deleteBook(bookId) {
    const response = await fetch(`http://localhost:5001/api/books/${bookId}`, {
        method: 'DELETE'
    });
    return response.status === 204;
}
```

### React範例

```jsx
import React, { useState, useEffect } from 'react';

function BookList() {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        fetchBooks();
    }, []);

    const fetchBooks = async () => {
        try {
            const response = await fetch('http://localhost:5001/api/books');
            const booksData = await response.json();
            setBooks(booksData);
        } catch (error) {
            console.error('取得書籍清單失敗:', error);
        }
    };

    const addBook = async (bookData) => {
        try {
            const response = await fetch('http://localhost:5001/api/books', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(bookData)
            });
            if (response.ok) {
                fetchBooks(); // 重新載入書籍清單
            }
        } catch (error) {
            console.error('新增書籍失敗:', error);
        }
    };

    return (
        <div>
            <h1>我的書籍清單</h1>
            {books.map(book => (
                <div key={book.id}>
                    <h3>{book.title}</h3>
                    <p>作者：{book.author}</p>
                    {book.cover_image_url && (
                        <img src={book.cover_image_url} alt={book.title} />
                    )}
                </div>
            ))}
        </div>
    );
}

export default BookList;
```

## 常見問題

### Q: 如何修改API的預設端口？

A: 編輯 `run_server.py` 檔案，修改最後一行的端口號碼：
```python
app.run(host='0.0.0.0', port=您的端口號, debug=True)
```

### Q: 資料庫檔案存放在哪裡？

A: SQLite資料庫檔案位於 `src/database/app.db`，包含所有書籍資料。

### Q: 如何備份書籍資料？

A: 您可以複製 `src/database/app.db` 檔案作為備份，或使用API匯出所有書籍資料。

### Q: 可以同時執行多個API實例嗎？

A: 可以，但需要使用不同的端口號碼，並確保每個實例使用獨立的資料庫檔案。

### Q: 如何重設資料庫？

A: 刪除 `src/database/app.db` 檔案，重新啟動API伺服器即會自動建立新的空資料庫。

## 技術支援

如果您在使用過程中遇到任何問題，請檢查：

1. Python版本是否為3.11或更高
2. 虛擬環境是否正確啟動
3. 所有相依套件是否正確安裝
4. 端口5001是否被其他程式佔用
5. 防火牆設定是否允許該端口的連線

## 授權資訊

本專案採用MIT授權條款，您可以自由使用、修改和分發此程式碼。

---

**作者：** Manus AI  
**版本：** 1.0.0  
**最後更新：** 2025年9月6日

