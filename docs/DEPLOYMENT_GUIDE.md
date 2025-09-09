# GitHub部署書籍管理系統 - 詳細步驟指南

## 部署架構說明

由於GitHub Pages只支援靜態網站，而我們的Flask API需要伺服器運行，所以我們將採用以下架構：

1. **後端API**：部署到免費的雲端平台（Render/Railway）
2. **前端頁面**：部署到GitHub Pages
3. **程式碼管理**：全部存放在GitHub repository

## 第一步：準備GitHub Repository

### 1.1 建立GitHub帳號
如果您還沒有GitHub帳號：
1. 前往 https://github.com
2. 點擊「Sign up」註冊新帳號
3. 驗證電子郵件地址

### 1.2 建立新的Repository
1. 登入GitHub後，點擊右上角的「+」號
2. 選擇「New repository」
3. 填寫repository資訊：
   - **Repository name**: `my-book-collection`
   - **Description**: `個人書籍收藏管理系統`
   - **Public/Private**: 選擇Public（GitHub Pages需要）
   - **Initialize with README**: 勾選
4. 點擊「Create repository」

## 第二步：上傳程式碼到GitHub

### 2.1 初始化Git Repository
```bash
cd my-book-collection
git init
git add .
git commit -m "Initial commit: Book collection management system"
```

### 2.2 連接到GitHub
```bash
git branch -M main
git remote add origin https://github.com/your-username/my-book-collection.git
git push -u origin main
```

## 第三步：部署後端API到Render

### 3.1 註冊Render帳號
1. 前往 https://render.com
2. 使用GitHub帳號登入
3. 授權Render存取您的GitHub repositories

### 3.2 建立Web Service
1. 點擊「New +」→「Web Service」
2. 連接您的GitHub repository
3. 選擇 `my-book-collection` repository
4. 設定以下參數：
   - **Name**: `my-book-api`
   - **Environment**: `Python 3`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: 選擇Free方案

### 3.3 設定環境變數
在Render的Environment Variables中新增：
- `SECRET_KEY`: 設定一個安全的密鑰（例如：`your-super-secret-key-here`）
- `PYTHON_VERSION`: `3.11.0`

### 3.4 部署並取得API URL
部署完成後，Render會提供一個URL，例如：
`https://my-book-api.onrender.com`

## 第四步：更新前端API設定

### 4.1 修改JavaScript檔案
編輯 `frontend/script.js`，更新API_BASE_URL：

```javascript
// 將這行：
const API_BASE_URL = 'http://localhost:5000/api';

// 改為：
const API_BASE_URL = 'https://your-actual-api-url.onrender.com/api';
```

### 4.2 提交變更
```bash
git add frontend/script.js
git commit -m "Update API URL for production"
git push origin main
```

## 第五步：部署前端到GitHub Pages

### 5.1 啟用GitHub Pages
1. 在GitHub repository中，點擊「Settings」
2. 滾動到「Pages」部分
3. 在「Source」中選擇「Deploy from a branch」
4. 選擇「main」分支和「/frontend」資料夾
5. 點擊「Save」

### 5.2 等待部署完成
GitHub Pages會自動部署，通常需要幾分鐘時間。

### 5.3 取得網站URL
部署完成後，GitHub會提供一個URL，例如：
`https://your-username.github.io/my-book-collection/`

## 第六步：測試完整系統

### 6.1 測試API
訪問 `https://your-api-url.onrender.com/health` 確認API正常運行

### 6.2 測試前端
1. 訪問您的GitHub Pages URL
2. 嘗試新增書籍
3. 測試搜尋功能
4. 測試刪除功能

## 第七步：自訂網域（可選）

### 7.1 購買網域
如果您想使用自己的網域，可以從以下服務商購買：
- Namecheap
- GoDaddy
- Cloudflare

### 7.2 設定GitHub Pages自訂網域
1. 在repository的「Settings」→「Pages」中
2. 在「Custom domain」輸入您的網域
3. 勾選「Enforce HTTPS」

### 7.3 設定DNS記錄
在您的網域DNS設定中新增CNAME記錄：
```
CNAME  www  your-username.github.io
```

## 維護與更新

### 更新程式碼
```bash
# 修改程式碼後
git add .
git commit -m "Update: description of changes"
git push origin main
```

### 監控服務狀態
- **Render Dashboard**：監控API服務狀態
- **GitHub Actions**：查看部署狀態
- **Browser DevTools**：檢查前端錯誤

### 備份策略
1. **程式碼備份**：GitHub自動備份
2. **資料備份**：定期匯出書籍資料
3. **設定備份**：記錄環境變數和設定

## 故障排除

### 常見問題

#### 1. API無法連接
**症狀**：前端顯示「無法載入書籍資料」
**解決方案**：
- 檢查Render服務狀態
- 確認API URL正確
- 檢查CORS設定

#### 2. GitHub Pages無法訪問
**症狀**：404錯誤或頁面無法載入
**解決方案**：
- 確認repository為public
- 檢查Pages設定
- 確認檔案路徑正確

#### 3. 新增書籍失敗
**症狀**：點擊新增按鈕無反應
**解決方案**：
- 檢查瀏覽器控制台錯誤
- 確認API端點正常
- 檢查網路連線

#### 4. 圖片無法顯示
**症狀**：書籍封面顯示為預設圖片
**解決方案**：
- 確認圖片URL有效
- 檢查圖片支援HTTPS
- 使用可靠的圖片託管服務

### 效能優化

#### 1. API回應速度
- 使用資料庫索引
- 實作快取機制
- 優化查詢語句

#### 2. 前端載入速度
- 壓縮CSS和JavaScript
- 使用CDN載入字體
- 優化圖片大小

#### 3. 使用者體驗
- 新增載入動畫
- 實作錯誤重試機制
- 提供離線支援

## 進階功能

### 1. 自動化部署
使用GitHub Actions實現自動化部署：

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to Render
      # 自動觸發Render重新部署
```

### 2. 資料庫升級
從SQLite升級到PostgreSQL：

```python
# 在Render中設定PostgreSQL
DATABASE_URL = os.environ.get('DATABASE_URL')
```

### 3. 使用者認證
新增登入功能：
- 實作JWT認證
- 新增使用者管理
- 保護API端點

## 成本分析

### 免費方案限制
- **Render Free**: 
  - 750小時/月運行時間
  - 閒置後自動休眠
  - 512MB RAM限制

- **GitHub Pages**:
  - 1GB儲存空間
  - 100GB頻寬/月
  - 10次建置/小時

### 付費升級選項
- **Render Starter**: $7/月
  - 24/7運行
  - 更多資源
  - 自訂網域

- **GitHub Pro**: $4/月
  - 私有repository
  - 進階功能

## 安全性考量

### 1. API安全
- 使用HTTPS
- 實作速率限制
- 驗證輸入資料

### 2. 資料保護
- 定期備份
- 加密敏感資料
- 存取控制

### 3. 前端安全
- 防止XSS攻擊
- 驗證使用者輸入
- 安全的API呼叫

## 總結

透過這個部署指南，您可以：
1. 完全免費地部署書籍管理系統
2. 獲得專業的雲端服務
3. 享受自動化的部署流程
4. 擁有可擴展的架構

這個解決方案適合個人使用，也可以作為學習雲端部署的實踐專案。隨著需求增長，可以輕鬆升級到付費方案獲得更多資源和功能。

