import requests
import json
import random
import os

# --- DATABASE MODULE ---
class MemoryCore:
    def __init__(self):
        self.db_path = 'database.json'
        self.data = self.load_database()

    def load_database(self):
        try:
            with open(self.db_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "business_status": "Active",
                "wallet": {"total_profit": 0, "reinvested": 0, "family_fund": 0},
                "inventory": [],
                "logs": []
            }

    def save_memory(self, items):
        # Saves MULTIPLE items at once
        for item in items:
            self.data['inventory'].append(item)
        
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=4)
        
        print(f"--> [MEMORY] Saved {len(items)} new items. Total: {len(self.data['inventory'])}")

# --- PLATFORM MANAGER ---
class PlatformManager:
    def __init__(self):
        self.identity = "Jaredsb1000-Family-Protector"

        def list_product(self, item):
        print(f"--> [UPLOADING] '{item['title']}' to Shopify...")

# --- TREND HUNTER (LIVE CONNECTION) ---
class TrendHunter:
    def scan_market(self):
        print("Connecting to Live Product Feed (DummyJSON)...")
        
        try:
            # Fetches 5 real products from the internet
            response = requests.get('https://dummyjson.com/products?limit=5')
            if response.status_code == 200:
                data = response.json()
                products = data['products']
                
                formatted_products = []
                for p in products:
                    formatted_products.append({
                        "name": p['title'],
                        "price": p['price'],
                        "status": "Volume",
                        "description": p['description']
                    })
                return formatted_products
            else:
                print("Connection Failed. Using backup.")
                return []
        except Exception as e:
            print(f"Error: {e}")
            return []

# --- MAIN MANAGE AI ---
class Manage:
    def __init__(self):
        self.mode = "Family First"
        self.memory = MemoryCore()
        self.hands = PlatformManager()
        self.eyes = TrendHunter()
        print(f"Manage v5.0 Online. Connected to Live Web.")

    def daily_grind(self):
        print("-" * 40)
        print("PHASE 1: HUNTING (LIVE)")
        items = self.eyes.scan_market()
        
        if not items:
            print("No items found.")
            return

        print(f"Found {len(items)} items. Processing...")
        
        print("-" * 40)
        print("PHASE 2: UPLOADING")
        for item in items:
            self.hands.list_product(item)
        
        print("-" * 40)
        print("PHASE 3: SAVING")
        self.memory.save_memory(items)
        
        print("-" * 40)
        print(f"STATUS: Complete. Inventory Updated.")

if __name__ == "__main__":
    ai = Manage()
    ai.daily_grind()
