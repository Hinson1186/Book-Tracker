#!/usr/bin/env python3
"""
書籍管理API - 範例資料匯入腳本

這個腳本會新增一些範例書籍資料到您的API中，
方便您快速體驗API的功能。
"""

import requests
import json

# API基本URL
BASE_URL = "http://localhost:5001/api"

# 範例書籍資料
sample_books = [
    {
        "title": "Python程式設計：從入門到實務",
        "author": "張志成",
        "cover_image_url": "https://via.placeholder.com/300x400/4CAF50/white?text=Python"
    },
    {
        "title": "JavaScript權威指南",
        "author": "David Flanagan",
        "cover_image_url": "https://via.placeholder.com/300x400/FF9800/white?text=JavaScript"
    },
    {
        "title": "深入淺出資料結構與演算法",
        "author": "李明華",
        "cover_image_url": "https://via.placeholder.com/300x400/2196F3/white?text=Algorithm"
    },
    {
        "title": "網頁設計與前端開發",
        "author": "陳美玲",
        "cover_image_url": "https://via.placeholder.com/300x400/E91E63/white?text=Web+Design"
    },
    {
        "title": "資料庫系統概論",
        "author": "王大明",
        "cover_image_url": "https://via.placeholder.com/300x400/9C27B0/white?text=Database"
    },
    {
        "title": "機器學習實戰",
        "author": "林小芳",
        "cover_image_url": "https://via.placeholder.com/300x400/607D8B/white?text=ML"
    },
    {
        "title": "軟體工程：理論與實務",
        "author": "黃志明",
        "cover_image_url": "https://via.placeholder.com/300x400/795548/white?text=Software"
    },
    {
        "title": "網路安全與資訊保護",
        "author": "劉建國",
        "cover_image_url": "https://via.placeholder.com/300x400/F44336/white?text=Security"
    }
]

def add_sample_books():
    """新增範例書籍資料"""
    print("=== 書籍管理API - 範例資料匯入 ===\n")
    
    success_count = 0
    error_count = 0
    
    for i, book in enumerate(sample_books, 1):
        print(f"{i}. 正在新增：{book['title']}")
        
        try:
            response = requests.post(f"{BASE_URL}/books", json=book)
            
            if response.status_code == 201:
                result = response.json()
                print(f"   ✓ 成功新增 (ID: {result['id']})")
                success_count += 1
            else:
                print(f"   ✗ 新增失敗 - 狀態碼: {response.status_code}")
                print(f"     錯誤訊息: {response.text}")
                error_count += 1
                
        except requests.exceptions.ConnectionError:
            print("   ✗ 連線失敗 - 請確認API伺服器是否正在運行")
            error_count += 1
            break
        except Exception as e:
            print(f"   ✗ 發生錯誤: {e}")
            error_count += 1
    
    print(f"\n=== 匯入完成 ===")
    print(f"成功新增: {success_count} 本書")
    print(f"失敗: {error_count} 本書")
    
    if success_count > 0:
        print(f"\n您現在可以訪問 http://localhost:5001/api/books 查看所有書籍")

def show_all_books():
    """顯示所有書籍"""
    try:
        response = requests.get(f"{BASE_URL}/books")
        if response.status_code == 200:
            books = response.json()
            print(f"\n=== 目前資料庫中的書籍 ({len(books)} 本) ===")
            for book in books:
                print(f"ID: {book['id']} | {book['title']} - {book['author']}")
        else:
            print(f"取得書籍清單失敗 - 狀態碼: {response.status_code}")
    except Exception as e:
        print(f"取得書籍清單時發生錯誤: {e}")

if __name__ == "__main__":
    # 先顯示目前的書籍
    show_all_books()
    
    # 詢問是否要新增範例資料
    print("\n是否要新增範例書籍資料？")
    print("注意：這會新增 8 本範例書籍到您的資料庫中")
    
    choice = input("請輸入 'y' 確認新增，或按 Enter 取消: ").lower().strip()
    
    if choice == 'y':
        add_sample_books()
        show_all_books()
    else:
        print("已取消新增範例資料")

