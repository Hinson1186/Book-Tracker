# 📚 我的書籍收藏管理系統

一個完整的書籍管理系統，包含Flask API後端和現代化的前端介面，支援書籍的新增、查詢、更新和刪除功能。

## 🌟 系統特色

- **完整的RESTful API**：基於Flask開發的後端API
- **現代化前端介面**：響應式設計，支援桌面和行動裝置
- **雲端部署**：支援GitHub Pages + Render免費部署
- **資料管理**：支援書名、作者、封面圖片管理
- **搜尋功能**：即時搜尋書名和作者
- **美觀介面**：現代化UI設計，使用者體驗佳

## 🏗️ 系統架構

```
my-book-collection/
├── backend/                 # Flask API後端
│   ├── src/
│   │   ├── models/         # 資料模型
│   │   ├── routes/         # API路由
│   │   └── database/       # 資料庫檔案
│   ├── app.py              # 主應用程式
│   ├── requirements.txt    # Python相依套件
│   └── Procfile           # 部署設定
├── frontend/               # 前端頁面
│   ├── index.html         # 主頁面
│   ├── style.css          # 樣式檔案
│   └── script.js          # JavaScript邏輯
├── docs/                  # 文件
└── README.md             # 專案說明
```

## 🚀 快速開始

### 本地開發

1. **啟動後端API**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

2. **開啟前端頁面**
```bash
# 使用瀏覽器開啟 frontend/index.html
# 或使用本地伺服器
cd frontend
python -m http.server 8080
```

3. **訪問應用程式**
- 前端：http://localhost:8080
- API：http://localhost:5000

### 雲端部署

詳細部署步驟請參考：[GitHub部署指南](docs/DEPLOYMENT_GUIDE.md)

## 📖 API文件

### 基本端點

| 方法 | 端點 | 功能 | 說明 |
|------|------|------|------|
| GET | `/health` | 健康檢查 | 檢查API狀態 |
| GET | `/api/books` | 取得所有書籍 | 返回書籍清單 |
| POST | `/api/books` | 新增書籍 | 新增一本書 |
| GET | `/api/books/<id>` | 取得單一書籍 | 根據ID取得書籍 |
| PUT | `/api/books/<id>` | 更新書籍 | 更新書籍資訊 |
| DELETE | `/api/books/<id>` | 刪除書籍 | 刪除指定書籍 |

### 資料格式

```json
{
  "id": 1,
  "title": "書名",
  "author": "作者姓名",
  "cover_image_url": "封面圖片URL"
}
```

## 🎨 前端功能

- **書籍展示**：卡片式佈局展示所有書籍
- **搜尋功能**：即時搜尋書名和作者
- **新增書籍**：模態框表單新增書籍
- **刪除書籍**：確認對話框刪除書籍
- **響應式設計**：支援各種螢幕尺寸
- **美觀介面**：現代化設計風格

## 🛠️ 技術棧

### 後端
- **Flask**：Python Web框架
- **SQLAlchemy**：ORM資料庫操作
- **Flask-CORS**：跨域請求支援
- **SQLite**：輕量級資料庫

### 前端
- **HTML5**：語義化標記
- **CSS3**：現代化樣式和動畫
- **JavaScript ES6+**：前端邏輯
- **Fetch API**：HTTP請求

### 部署
- **GitHub Pages**：前端靜態網站託管
- **Render**：後端API託管
- **GitHub Actions**：自動化部署（可選）

## 📱 螢幕截圖

### 桌面版
![桌面版介面](screenshots/desktop.png)

### 行動版
![行動版介面](screenshots/mobile.png)

## 🔧 開發指南

### 環境需求
- Python 3.11+
- 現代瀏覽器（Chrome, Firefox, Safari, Edge）

### 安裝步驟
1. Clone repository
2. 安裝後端相依套件
3. 啟動API伺服器
4. 開啟前端頁面

### 開發建議
- 使用虛擬環境管理Python套件
- 遵循RESTful API設計原則
- 保持前後端分離架構
- 定期備份資料庫

## 🚀 部署到雲端

### 後端部署（Render）
1. 推送程式碼到GitHub
2. 連接Render服務
3. 設定環境變數
4. 自動部署

### 前端部署（GitHub Pages）
1. 啟用GitHub Pages
2. 選擇frontend資料夾
3. 更新API URL
4. 自動發布

## 🤝 貢獻指南

歡迎提交Issue和Pull Request！

1. Fork專案
2. 建立功能分支
3. 提交變更
4. 發起Pull Request

## 📄 授權

MIT License - 詳見 [LICENSE](LICENSE) 檔案

## 📞 聯絡資訊

如有問題或建議，請透過以下方式聯絡：
- 建立GitHub Issue
- 發送電子郵件

---

**製作者：** Manus AI  
**版本：** 1.0.0  
**最後更新：** 2025年9月6日

