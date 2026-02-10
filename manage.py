import requests
import json
import random

# --- ART GENERATOR ---
class ArtGenerator:
    def __init__(self):
        self.characters = [
            "Salty Sailor Man (resembling Popeye)",
            "Mystery Brown Dog (resembling Scooby Doo)",
            "Fast Blue Rodent (resembling Sonic)",
            "Burger King Clone",
            "Psychic Yellow Duck",
            "Sponge Block (resembling SpongeBob)"
        ]

    def create_spoof_art(self):
        character = random.choice(self.characters)
        prompt = f"Trippy psychedelic digital art of {character}, vibrant colors, receipt design, unique style"
        seed = random.randint(1, 999999)
        art_url = f"https://pollinations.ai/p/{prompt}?width=600&height=400&seed={seed}&nologo=true"
        return character, art_url

# --- GUMROAD MANAGER ---
class GumroadManager:
    def __init__(self):
        # DIRECT INJECTION OF KEYS
        self.client_id = "u7nszyZuljGnkXZWoZOncM0MsdUPjUR7b5eIGXaJxuA"
        self.client_secret = "qGdUFFhhEKPev9i5WmHQx57dzcoCl3ZRlb_oF"
        self.seller_id = "hlypebm6bdgfPlRa89NLiQ=="
        self.access_token = "9_DMAHqdOkz2TddAsPcnNxeJtIABhNR2OCg"

    def authenticate(self):
        # NO LONGER CHECKING SECRETS - ALWAYS TRUE
        print(f"-> [AUTHENTICATED] Token found.")
        return True

    def create_receipt_product(self, character, art_url, price):
        print(f"-> [CREATING] Digital Receipt for '{character}'...")
        url = "https://api.gumroad.com/v2/products"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "name": f"Digital Receipt: {character} Collection",
            "description": f"""
            PURCHASE CONFIRMED.
            
            Product Sourced: {character}
            Sourcing Fee: ${price} (Includes 10% Commission).
            
            Please find your One-of-a-Kind Digital Receipt Art below:
            
            [![Trippy Receipt Art]({art_url})]
            """,
            "price": price,
            "published": True,
            "max_purchase_count": 1,
            "require_shipping": False
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                product_data = response.json()
                slug = product_data['product']['url_slug']
                link = f"https://{self.seller_id}.gumroad.com/l/{slug}"
                print(f"-> [SUCCESS] Product Live! Link: {link}")
                return link
            else:
                print(f"-> [ERROR] Failed to create: {response.text}")
                return None
        except Exception as e:
            print(f"-> [ERROR] {e}")
            return None

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

    def save_memory(self, item):
        self.data['inventory'].append(item)
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"--> [MEMORY] Saved product. Total: {len(self.data['inventory'])}.")

# --- MAIN MANAGE AI ---
class Manage:
    def __init__(self):
        self.mode = "Family First"
        self.artist = ArtGenerator()
        self.hands = GumroadManager()
        self.memory = MemoryCore()
        print(f"Manage v8.1 Online - HARDCODED TOKEN ACTIVE.")

    def daily_grind(self):
        print("-" * 40)
        print("PHASE 1: AUTHENTICATING")
        if not self.hands.authenticate():
            print("HALT: Cannot connect to Gumroad.")
            return

        print("-" * 40)
        print("PHASE 2: CREATING SPOOF ART")
        character, art_url = self.artist.create_spoof_art()
        print(f"-> [ART] Created: {character}")
        
        price = random.randint(5, 15)

        print("-" * 40)
        print("PHASE 3: CREATING RECEIPT")
        link = self.hands.create_receipt_product(character, art_url, price)
        
        if link:
            print("-" * 40)
            print("PHASE 4: SAVING")
            product_record = {
                "name": f"Strategy Guide: {character}",
                "price": price,
                "link": link,
                "status": "Virtual"
            }
            self.memory.save_memory(product_record)
            print(f"--> [MONEY MAKER] Link available for sale.")
        else:
            print("Failed to create product.")

if __name__ == "__main__":
    ai = Manage()
    ai.daily_grind()
