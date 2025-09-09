# 📖 書籍管理API文件

## 概述

書籍管理API是一個RESTful Web服務，提供完整的書籍資料管理功能。API基於Flask框架開發，支援書籍的新增、查詢、更新和刪除操作。

## 基本資訊

- **API版本**: 1.0.0
- **基礎URL**: `https://your-api-domain.onrender.com`
- **資料格式**: JSON
- **字符編碼**: UTF-8
- **HTTP方法**: GET, POST, PUT, DELETE

## 認證

目前版本不需要認證，所有端點都是公開的。未來版本可能會加入API金鑰或JWT認證。

## 資料模型

### 書籍物件 (Book Object)

```json
{
  "id": 1,
  "title": "Python程式設計",
  "author": "張三",
  "cover_image_url": "https://example.com/cover.jpg"
}
```

#### 欄位說明

| 欄位 | 類型 | 必填 | 說明 |
|------|------|------|------|
| `id` | integer | 是 | 書籍唯一識別碼（自動生成） |
| `title` | string | 是 | 書籍標題 |
| `author` | string | 是 | 作者姓名 |
| `cover_image_url` | string | 否 | 封面圖片URL |

## API端點

### 1. 健康檢查

檢查API服務狀態。

```
GET /health
```

#### 回應

```json
{
  "status": "healthy",
  "message": "書籍管理API運行正常",
  "endpoints": [
    "GET /api/books - 取得所有書籍",
    "POST /api/books - 新增書籍",
    "GET /api/books/<id> - 取得單一書籍",
    "PUT /api/books/<id> - 更新書籍",
    "DELETE /api/books/<id> - 刪除書籍"
  ]
}
```

### 2. 取得所有書籍

取得所有書籍的清單。

```
GET /api/books
```

#### 回應

**成功 (200 OK)**

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
    "title": "JavaScript完全攻略",
    "author": "李四",
    "cover_image_url": "https://example.com/js-book.jpg"
  }
]
```

**空清單 (200 OK)**

```json
[]
```

### 3. 新增書籍

新增一本新書籍到收藏中。

```
POST /api/books
```

#### 請求標頭

```
Content-Type: application/json
```

#### 請求主體

```json
{
  "title": "新書標題",
  "author": "作者姓名",
  "cover_image_url": "https://example.com/cover.jpg"
}
```

#### 回應

**成功 (201 Created)**

```json
{
  "id": 3,
  "title": "新書標題",
  "author": "作者姓名",
  "cover_image_url": "https://example.com/cover.jpg"
}
```

**錯誤 (400 Bad Request)**

```json
{
  "error": "書名和作者為必填欄位"
}
```

### 4. 取得單一書籍

根據ID取得特定書籍的詳細資訊。

```
GET /api/books/{id}
```

#### 路徑參數

| 參數 | 類型 | 說明 |
|------|------|------|
| `id` | integer | 書籍ID |

#### 回應

**成功 (200 OK)**

```json
{
  "id": 1,
  "title": "Python程式設計",
  "author": "張三",
  "cover_image_url": "https://example.com/python-book.jpg"
}
```

**未找到 (404 Not Found)**

```json
{
  "error": "書籍不存在"
}
```

### 5. 更新書籍

更新現有書籍的資訊。

```
PUT /api/books/{id}
```

#### 路徑參數

| 參數 | 類型 | 說明 |
|------|------|------|
| `id` | integer | 書籍ID |

#### 請求標頭

```
Content-Type: application/json
```

#### 請求主體

```json
{
  "title": "更新後的書名",
  "author": "更新後的作者",
  "cover_image_url": "https://example.com/new-cover.jpg"
}
```

#### 回應

**成功 (200 OK)**

```json
{
  "id": 1,
  "title": "更新後的書名",
  "author": "更新後的作者",
  "cover_image_url": "https://example.com/new-cover.jpg"
}
```

**未找到 (404 Not Found)**

```json
{
  "error": "書籍不存在"
}
```

**錯誤 (400 Bad Request)**

```json
{
  "error": "書名和作者為必填欄位"
}
```

### 6. 刪除書籍

從收藏中刪除指定的書籍。

```
DELETE /api/books/{id}
```

#### 路徑參數

| 參數 | 類型 | 說明 |
|------|------|------|
| `id` | integer | 書籍ID |

#### 回應

**成功 (200 OK)**

```json
{
  "message": "書籍刪除成功"
}
```

**未找到 (404 Not Found)**

```json
{
  "error": "書籍不存在"
}
```

## 錯誤處理

### HTTP狀態碼

| 狀態碼 | 說明 |
|--------|------|
| 200 | 請求成功 |
| 201 | 資源創建成功 |
| 400 | 請求錯誤（參數無效） |
| 404 | 資源不存在 |
| 500 | 伺服器內部錯誤 |

### 錯誤回應格式

所有錯誤回應都使用以下格式：

```json
{
  "error": "錯誤描述訊息"
}
```

## 使用範例

### cURL範例

#### 取得所有書籍

```bash
curl -X GET https://your-api-domain.onrender.com/api/books
```

#### 新增書籍

```bash
curl -X POST https://your-api-domain.onrender.com/api/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python程式設計",
    "author": "張三",
    "cover_image_url": "https://example.com/cover.jpg"
  }'
```

#### 更新書籍

```bash
curl -X PUT https://your-api-domain.onrender.com/api/books/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python進階程式設計",
    "author": "張三",
    "cover_image_url": "https://example.com/new-cover.jpg"
  }'
```

#### 刪除書籍

```bash
curl -X DELETE https://your-api-domain.onrender.com/api/books/1
```

### JavaScript範例

#### 使用Fetch API

```javascript
// 取得所有書籍
async function getAllBooks() {
  try {
    const response = await fetch('https://your-api-domain.onrender.com/api/books');
    const books = await response.json();
    console.log(books);
  } catch (error) {
    console.error('Error:', error);
  }
}

// 新增書籍
async function addBook(bookData) {
  try {
    const response = await fetch('https://your-api-domain.onrender.com/api/books', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(bookData)
    });
    const newBook = await response.json();
    console.log('Book added:', newBook);
  } catch (error) {
    console.error('Error:', error);
  }
}

// 刪除書籍
async function deleteBook(bookId) {
  try {
    const response = await fetch(`https://your-api-domain.onrender.com/api/books/${bookId}`, {
      method: 'DELETE'
    });
    const result = await response.json();
    console.log('Book deleted:', result);
  } catch (error) {
    console.error('Error:', error);
  }
}
```

### Python範例

#### 使用requests庫

```python
import requests
import json

API_BASE_URL = 'https://your-api-domain.onrender.com/api'

# 取得所有書籍
def get_all_books():
    response = requests.get(f'{API_BASE_URL}/books')
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

# 新增書籍
def add_book(title, author, cover_url=''):
    book_data = {
        'title': title,
        'author': author,
        'cover_image_url': cover_url
    }
    response = requests.post(
        f'{API_BASE_URL}/books',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(book_data)
    )
    if response.status_code == 201:
        return response.json()
    else:
        print(f'Error: {response.status_code} - {response.json()}')
        return None

# 刪除書籍
def delete_book(book_id):
    response = requests.delete(f'{API_BASE_URL}/books/{book_id}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

# 使用範例
if __name__ == '__main__':
    # 新增書籍
    new_book = add_book('Python程式設計', '張三', 'https://example.com/cover.jpg')
    print('Added book:', new_book)
    
    # 取得所有書籍
    books = get_all_books()
    print('All books:', books)
    
    # 刪除書籍（假設ID為1）
    if books and len(books) > 0:
        result = delete_book(books[0]['id'])
        print('Delete result:', result)
```

## 速率限制

目前版本沒有實施速率限制，但建議合理使用API：

- 避免在短時間內發送大量請求
- 實施適當的錯誤處理和重試機制
- 考慮快取常用的資料

## CORS支援

API支援跨域請求（CORS），允許從任何網域的前端應用程式存取。

支援的HTTP方法：
- GET
- POST
- PUT
- DELETE
- OPTIONS

## 資料驗證

### 新增書籍驗證規則

- `title`: 必填，字串類型，長度1-200字符
- `author`: 必填，字串類型，長度1-100字符
- `cover_image_url`: 選填，必須是有效的URL格式

### 更新書籍驗證規則

與新增書籍相同的驗證規則。

## 效能考量

### 回應時間

- 健康檢查：< 100ms
- 取得書籍清單：< 500ms
- 新增/更新/刪除書籍：< 1000ms

### 資料限制

- 最大書籍數量：建議不超過10,000本
- 書名最大長度：200字符
- 作者名最大長度：100字符
- 封面URL最大長度：500字符

## 版本更新

### v1.0.0 (目前版本)
- 基本的CRUD操作
- RESTful API設計
- JSON資料格式
- CORS支援

### 未來版本計劃
- API認證機制
- 分頁支援
- 搜尋和篩選功能
- 批量操作
- 資料匯出功能

## 故障排除

### 常見問題

**Q: API回應緩慢怎麼辦？**
A: 檢查網路連線，如果問題持續，可能是伺服器負載過高，請稍後再試。

**Q: 新增書籍時出現400錯誤？**
A: 檢查請求資料格式，確保title和author欄位已填寫且格式正確。

**Q: 圖片URL無法顯示？**
A: 確保URL是直接連結到圖片檔案，且圖片伺服器支援HTTPS。

**Q: CORS錯誤怎麼解決？**
A: API已啟用CORS支援，如果仍有問題，請檢查前端程式碼的請求設定。

### 聯絡支援

如果遇到技術問題或需要協助，請透過以下方式聯絡：

- GitHub Issues: 在專案repository中建立issue
- 電子郵件: 發送詳細的問題描述

---

**API文件版本**: 1.0.0  
**最後更新**: 2025年9月6日  
**維護者**: Manus AI

