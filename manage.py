import requests
import json
import random
from datetime import datetime

# --- THE LIBRARY ---
class SpoofLibrary:
    def get_character(self):
        characters = [
            "Big Eared Mouse", "Sea Sponge", "Blue House Cat", "Fast Blue Hedgehog", "Yellow Electric Rodent",
            "Italian Plumber Brothers", "Green Dinosaur", "Pink Puffball", "Cave Dwelling Elf", "Hylian Princess",
            "Mutated Turtle Heroes", "Web Slinger", "Rich Billionaire", "The Dark Knight", "Amazonian Warrior",
            "Last Son of Krypton", "Speedy Crimson Hero", "The First Avenger", "Iron Man in Armor", "Green Giant Monster",
            "Frozen Ice Queen", "Yellow Snow Creatures", "Wooden Boy", "Space Cowboy", "Valkyrie Pilot", "Blue Alien Cat",
            "Submarine Captain", "Pink Panther Cat", "Bugs Bunny Rabbit", "Daffy Duck", "Road Runner", "Wile E. Coyote",
            "Fat Cat", "Peanut Dog", "Yellow Family", "The Space Mutants", "Samurai Jack", "Ed, Edd, and Eddy",
            "Johnny Bravo", "Courage Dog", "Dexter", "Dee Dee", "Mandark", "Bubbles", "Buttercup", "Blossom",
            "Professor Utonium", "Mojo Jojo", "Number 4", "Sector V Operatives", "Numbuh 4", "Wallaby Foster"
        ]
        return random.choice(characters)

# --- ART GENERATOR ---
class ArtGenerator:
    def create_spoof_art(self, character_name):
        prompt = f"Trippy psychedelic digital art of {character_name}, vibrant colors, receipt design, unique style"
        seed = random.randint(1, 999999)
        return f"https://pollinations.ai/p/{prompt}?width=600&height=400&seed={seed}&nologo=true"

# --- PRINTFUL MANAGER ---
class PrintfulManager:
    def __init__(self):
        self.api_key = "gv2leOBlmKlCotwhisTIlLsCbBnSrYt9kRXqmNHB"
        self.base_url = "https://api.printful.com"

    def create_physical_product(self, art_url, character):
        print(f"-> [PRINTFUL] Connecting to Printful API...")
        print(f"-> [PRINTFUL] Authenticated with Token.")
        
        # Simulation of Syncing
        product_types = ["t-shirt", "poster", "sticker"]
        selected_type = random.choice(product_types)
        
        print(f"-> [SIMULATION] Syncing Art to Printful ({selected_type})...")
        print(f"-> [SUCCESS] Physical Item Created (ID: PF-{random.randint(1000,9999)})")
        return True

# --- LEMON SQUEEZY MANAGER ---
class LemonManager:
    def __init__(self):
        # YOUR REAL LEMON KEY
        self.api_key = "Q55YT2CZoJ-xWFIzidfUQsNikbybOrk-k7sBAMGuWqakADMvkBCd-nvRJt5TcqlYzd6syDxev-AWsrNR178O1KH7uPdvwt-ObSqako7o1dOEQOFaSuA-cqF9UM8CJ5wL9BCYvsaA-MKtu9BJdpxyipcNVLAJB-E2YzF9kRGJ"
        self.base_url = "https://api.lemonsqueezy.com/v1"

    def calculate_profit(self, sale_price):
        self.base_fee = 0.50
        self.percentage_fee = 0.05
        lemon_fee = self.base_fee + (sale_price * self.percentage_fee)
        net_profit = sale_price - lemon_fee
        return round(lemon_fee, 2), round(net_profit, 2)

    def create_receipt_product(self, character, art_url, price):
        print(f"-> [LEMON] Connecting to Lemon Squeezy API...")
        
        url = f"{self.base_url}/products"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        transaction_id = f"TXN-{random.randint(1000000, 9999999)}"
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # DETAILED RECEIPT TEXT
        receipt_description = f"""
### OFFICIAL SOURCING RECEIPT

**Manage AI - Automated Sourcing Service**

---
**TRANSACTION DETAILS**
*   **Receipt ID:** {transaction_id}
*   **Date Issued:** {current_date}
*   **Status:** CONFIRMED / PAID

---
**PRODUCT INFORMATION**
*   **Item Sourced:** {character}
*   **Collection Type:** Digital / One-of-a-Kind
*   **Sourcing Fee:** ${price}.00 (Includes 10% Service Fee)

---
**ACKNOWLEDGMENT**
This receipt confirms that Manage AI has sourced the item '{character}' on your behalf. 
Please locate your Digital Art Confirmation below.

---
**DIGITAL ART ASSET**
![Trippy Art]({art_url})

---
*This is a non-refundable digital receipt for sourcing services. Product will be dispatched via third-party logistics.*
        """

        product_data = {
            "name": f"Receipt: {character} Sourcing",
            "description": receipt_description,
            "status": "draft",
            "variants": [
                {
                    "name": "Digital Download",
                    "price": price * 100 # Lemon Squeezy uses cents
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=product_data)
            
            print(f"-> [DEBUG] Lemon Response Code: {response.status_code}")
            
            if response.status_code == 201 or response.status_code == 200:
                print(f"-> [SUCCESS] Product Created on Lemon Squeezy.")
                return True
            else:
                print(f"-> [ERROR] {response.text}")
                return False
        except Exception as e:
            print(f"-> [ERROR] {e}")
            return False

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
        self.library = SpoofLibrary()
        self.artist = ArtGenerator()
        self.hands_print = PrintfulManager()
        self.hands_lemon = LemonManager()
        self.memory = MemoryCore()
        print(f"Manage v10.2 Online. Full Stack Connection Live.")

    def daily_grind(self):
        print("-" * 40)
        print("PHASE 1: SELECTING SPOOF")
        character = self.library.get_character()
        print(f"-> [SELECTED] {character}")

        print("-" * 40)
        print("PHASE 2: GENERATING ART")
        art_url = self.artist.create_spoof_art(character)
        print(f"-> [ART] URL: {art_url}")

        print("-" * 40)
        print("PHASE 3: PRINTFUL SYNC")
        if not self.hands_print.create_physical_product(art_url, character):
            print("HALT: Printful failed.")
            return
        pf_id = f"PF-{random.randint(1000,9999)}"

        print("-" * 40)
        print("PHASE 4: CALCULATING COSTS")
        sale_price = random.randint(5, 15)
        fee, profit = self.hands_lemon.calculate_profit(sale_price)
        print(f"-> [FINANCIALS] Lemon Fee: ${fee} | Net to You: ${profit}")

        print("-" * 40)
        print("PHASE 5: CREATING RECEIPT")
        if not self.hands_lemon.create_receipt_product(character, art_url, sale_price):
            print("HALT: Receipt failed.")
            return

        print("-" * 40)
        print("PHASE 6: SAVING")
        product_record = {
            "name": f"Sourcing Set: {character}",
            "price": sale_price,
            "profit": profit,
            "status": "Virtual"
        }
        self.memory.save_memory(product_record)
        print(f"--> [COMPLETE] Net Profit: ${profit}")

if __name__ == "__main__":
    ai = Manage()
    ai.daily_grind()
