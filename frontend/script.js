// API設定 - 請在部署後替換為實際的API URL
const API_BASE_URL = 'http://localhost:5000/api'; // 本地測試用
// const API_BASE_URL = 'https://your-api-domain.onrender.com/api'; // 部署後使用

// DOM元素
const bookGrid = document.getElementById('bookGrid');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const addBookBtn = document.getElementById('addBookBtn');
const addBookModal = document.getElementById('addBookModal');
const addBookForm = document.getElementById('addBookForm');
const searchInput = document.getElementById('searchInput');
const bookCount = document.getElementById('bookCount');
const confirmModal = document.getElementById('confirmModal');
const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');

// 全域變數
let allBooks = [];
let filteredBooks = [];
let bookToDelete = null;

// 初始化
document.addEventListener('DOMContentLoaded', function() {
    loadBooks();
    setupEventListeners();
});

// 設定事件監聽器
function setupEventListeners() {
    addBookBtn.addEventListener('click', openModal);
    addBookForm.addEventListener('submit', handleAddBook);
    searchInput.addEventListener('input', handleSearch);
    confirmDeleteBtn.addEventListener('click', confirmDelete);
    
    // 模態框關閉事件
    document.querySelector('.close').addEventListener('click', closeModal);
    
    // 點擊模態框外部關閉
    window.addEventListener('click', function(event) {
        if (event.target === addBookModal) {
            closeModal();
        }
        if (event.target === confirmModal) {
            closeConfirmModal();
        }
    });
    
    // ESC鍵關閉模態框
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closeModal();
            closeConfirmModal();
        }
    });
}

// 載入所有書籍
async function loadBooks() {
    try {
        showLoading(true);
        hideError();
        
        const response = await fetch(`${API_BASE_URL}/books`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        allBooks = await response.json();
        filteredBooks = [...allBooks];
        displayBooks(filteredBooks);
        updateBookCount();
        
    } catch (error) {
        console.error('載入書籍失敗:', error);
        showError('無法載入書籍資料。請檢查網路連線或API伺服器狀態。');
        allBooks = [];
        filteredBooks = [];
        displayBooks([]);
        updateBookCount();
    } finally {
        showLoading(false);
    }
}

// 顯示書籍
function displayBooks(books) {
    if (books.length === 0) {
        bookGrid.innerHTML = `
            <div class="empty-state">
                <h3>📚 還沒有任何書籍</h3>
                <p>點擊「新增書籍」按鈕來新增您的第一本書！</p>
                <button class="btn btn-primary" onclick="openModal()">
                    <span class="btn-icon">+</span>
                    開始新增書籍
                </button>
            </div>
        `;
        return;
    }

    bookGrid.innerHTML = books.map(book => `
        <div class="book-card" data-book-id="${book.id}">
            <img src="${book.cover_image_url || 'https://via.placeholder.com/300x240/f5f7fa/7f8c8d?text=📚'}" 
                 alt="${escapeHtml(book.title)}" 
                 class="book-cover"
                 onerror="this.src='https://via.placeholder.com/300x240/f5f7fa/7f8c8d?text=📚'">
            <div class="book-info">
                <div class="book-title">${escapeHtml(book.title)}</div>
                <div class="book-author">👤 ${escapeHtml(book.author)}</div>
                <div class="book-actions">
                    <button class="btn btn-danger btn-small" onclick="showDeleteConfirm(${book.id}, '${escapeHtml(book.title)}', '${escapeHtml(book.author)}')">
                        <span class="btn-icon">🗑️</span>
                        刪除
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

// 更新書籍數量顯示
function updateBookCount() {
    const total = allBooks.length;
    const filtered = filteredBooks.length;
    
    if (total === 0) {
        bookCount.textContent = '尚無書籍';
    } else if (filtered === total) {
        bookCount.textContent = `共 ${total} 本書`;
    } else {
        bookCount.textContent = `顯示 ${filtered} / ${total} 本書`;
    }
}

// 搜尋功能
function handleSearch(event) {
    const searchTerm = event.target.value.toLowerCase().trim();
    
    if (searchTerm === '') {
        filteredBooks = [...allBooks];
    } else {
        filteredBooks = allBooks.filter(book => 
            book.title.toLowerCase().includes(searchTerm) ||
            book.author.toLowerCase().includes(searchTerm)
        );
    }
    
    displayBooks(filteredBooks);
    updateBookCount();
}

// 開啟新增書籍模態框
function openModal() {
    addBookModal.style.display = 'block';
    document.getElementById('bookTitle').focus();
    document.body.style.overflow = 'hidden'; // 防止背景滾動
}

// 關閉新增書籍模態框
function closeModal() {
    addBookModal.style.display = 'none';
    addBookForm.reset();
    document.body.style.overflow = 'auto';
}

// 顯示刪除確認對話框
function showDeleteConfirm(bookId, title, author) {
    bookToDelete = bookId;
    document.getElementById('deleteBookTitle').textContent = title;
    document.getElementById('deleteBookAuthor').textContent = `作者：${author}`;
    confirmModal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

// 關閉刪除確認對話框
function closeConfirmModal() {
    confirmModal.style.display = 'none';
    bookToDelete = null;
    document.body.style.overflow = 'auto';
}

// 處理新增書籍
async function handleAddBook(event) {
    event.preventDefault();
    
    const title = document.getElementById('bookTitle').value.trim();
    const author = document.getElementById('bookAuthor').value.trim();
    const coverUrl = document.getElementById('bookCover').value.trim();
    
    if (!title || !author) {
        showError('書名和作者為必填欄位');
        return;
    }
    
    // 禁用提交按鈕防止重複提交
    const submitBtn = event.target.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="btn-icon">⏳</span>新增中...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/books`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: title,
                author: author,
                cover_image_url: coverUrl || ''
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
        }
        
        const newBook = await response.json();
        allBooks.push(newBook);
        
        // 重新應用搜尋篩選
        const searchTerm = searchInput.value.toLowerCase().trim();
        if (searchTerm === '') {
            filteredBooks = [...allBooks];
        } else {
            filteredBooks = allBooks.filter(book => 
                book.title.toLowerCase().includes(searchTerm) ||
                book.author.toLowerCase().includes(searchTerm)
            );
        }
        
        displayBooks(filteredBooks);
        updateBookCount();
        closeModal();
        showSuccess(`成功新增書籍「${title}」！`);
        
    } catch (error) {
        console.error('新增書籍失敗:', error);
        showError(`新增書籍失敗：${error.message}`);
    } finally {
        // 恢復提交按鈕
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
    }
}

// 確認刪除書籍
async function confirmDelete() {
    if (!bookToDelete) return;
    
    const deleteBtn = confirmDeleteBtn;
    const originalText = deleteBtn.innerHTML;
    deleteBtn.disabled = true;
    deleteBtn.innerHTML = '<span class="btn-icon">⏳</span>刪除中...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/books/${bookToDelete}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        // 從陣列中移除書籍
        const bookTitle = allBooks.find(book => book.id === bookToDelete)?.title || '書籍';
        allBooks = allBooks.filter(book => book.id !== bookToDelete);
        filteredBooks = filteredBooks.filter(book => book.id !== bookToDelete);
        
        displayBooks(filteredBooks);
        updateBookCount();
        closeConfirmModal();
        showSuccess(`成功刪除書籍「${bookTitle}」！`);
        
    } catch (error) {
        console.error('刪除書籍失敗:', error);
        showError(`刪除書籍失敗：${error.message}`);
    } finally {
        deleteBtn.disabled = false;
        deleteBtn.innerHTML = originalText;
    }
}

// 顯示載入狀態
function showLoading(show) {
    loadingSpinner.style.display = show ? 'flex' : 'none';
}

// 顯示錯誤訊息
function showError(message) {
    const errorText = errorMessage.querySelector('.error-text');
    if (errorText) {
        errorText.textContent = message;
    } else {
        errorMessage.innerHTML = `<span class="error-icon">⚠️</span><span class="error-text">${message}</span>`;
    }
    errorMessage.style.display = 'flex';
    
    // 5秒後自動隱藏
    setTimeout(() => {
        hideError();
    }, 5000);
}

// 隱藏錯誤訊息
function hideError() {
    errorMessage.style.display = 'none';
}

// 顯示成功訊息
function showSuccess(message) {
    // 移除現有的成功訊息
    const existingSuccess = document.querySelector('.success');
    if (existingSuccess) {
        existingSuccess.remove();
    }
    
    // 建立新的成功訊息元素
    const successDiv = document.createElement('div');
    successDiv.className = 'success';
    successDiv.innerHTML = `<span>✅</span><span>${message}</span>`;
    
    // 插入到容器頂部
    const container = document.querySelector('.container');
    container.insertBefore(successDiv, container.firstChild);
    
    // 3秒後自動移除
    setTimeout(() => {
        successDiv.remove();
    }, 3000);
}

// HTML轉義函數
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}

// 檢查API連線狀態
async function checkApiHealth() {
    try {
        const response = await fetch(`${API_BASE_URL.replace('/api', '')}/health`);
        if (response.ok) {
            console.log('API連線正常');
            return true;
        }
    } catch (error) {
        console.warn('API連線檢查失敗:', error);
    }
    return false;
}

// 頁面載入時檢查API狀態
window.addEventListener('load', function() {
    checkApiHealth().then(isHealthy => {
        if (!isHealthy) {
            console.warn('API可能未啟動，請檢查後端服務');
        }
    });
});

