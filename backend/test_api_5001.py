#!/usr/bin/env python3
"""
書籍API測試腳本
"""
import requests
import json

BASE_URL = "http://localhost:5001/api"

def test_api():
    print("=== 書籍API測試 ===\n")
    
    # 測試1: 取得所有書籍 (應該是空的)
    print("1. 測試取得所有書籍:")
    response = requests.get(f"{BASE_URL}/books")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()
    
    # 測試2: 新增書籍
    print("2. 測試新增書籍:")
    book_data = {
        "title": "Python程式設計",
        "author": "張三",
        "cover_image_url": "https://example.com/python-book.jpg"
    }
    response = requests.post(f"{BASE_URL}/books", json=book_data)
    print(f"狀態碼: {response.status_code}")
    book1 = response.json()
    print(f"回應: {book1}")
    book1_id = book1.get('id')
    print()
    
    # 測試3: 新增第二本書
    print("3. 測試新增第二本書:")
    book_data2 = {
        "title": "JavaScript權威指南",
        "author": "李四",
        "cover_image_url": "https://example.com/js-book.jpg"
    }
    response = requests.post(f"{BASE_URL}/books", json=book_data2)
    print(f"狀態碼: {response.status_code}")
    book2 = response.json()
    print(f"回應: {book2}")
    book2_id = book2.get('id')
    print()
    
    # 測試4: 取得所有書籍 (現在應該有兩本)
    print("4. 測試取得所有書籍 (現在應該有兩本):")
    response = requests.get(f"{BASE_URL}/books")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()
    
    # 測試5: 取得單一書籍
    print("5. 測試取得單一書籍:")
    response = requests.get(f"{BASE_URL}/books/{book1_id}")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()
    
    # 測試6: 更新書籍
    print("6. 測試更新書籍:")
    update_data = {
        "title": "Python進階程式設計",
        "author": "張三",
        "cover_image_url": "https://example.com/python-advanced.jpg"
    }
    response = requests.put(f"{BASE_URL}/books/{book1_id}", json=update_data)
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()
    
    # 測試7: 刪除書籍
    print("7. 測試刪除書籍:")
    response = requests.delete(f"{BASE_URL}/books/{book2_id}")
    print(f"狀態碼: {response.status_code}")
    print(f"回應內容長度: {len(response.content)}")
    print()
    
    # 測試8: 確認刪除後的書籍列表
    print("8. 確認刪除後的書籍列表:")
    response = requests.get(f"{BASE_URL}/books")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()
    
    # 測試9: 嘗試取得已刪除的書籍 (應該回傳404)
    print("9. 嘗試取得已刪除的書籍 (應該回傳404):")
    response = requests.get(f"{BASE_URL}/books/{book2_id}")
    print(f"狀態碼: {response.status_code}")
    print()
    
    # 測試10: 測試錯誤處理 - 缺少必要欄位
    print("10. 測試錯誤處理 - 缺少必要欄位:")
    invalid_data = {"title": "只有書名"}
    response = requests.post(f"{BASE_URL}/books", json=invalid_data)
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    print()
    
    print("=== 測試完成 ===")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("錯誤: 無法連接到API伺服器")
        print("請確保Flask應用程式正在運行 (python src/main.py)")
    except Exception as e:
        print(f"測試過程中發生錯誤: {e}")

