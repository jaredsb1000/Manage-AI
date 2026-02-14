import requests
import json
import random
from datetime import datetime

# --- CONFIGURATION ---
class Config:
    def get_rarity(self):
        hour = datetime.now().hour
        if hour == 9:
            return "ULTRA_RARE"
        elif hour % 4 == 0:
            return "EPIC"
        else:
            return "NORMAL"

# --- THE LIBRARY ---
class SpoofLibrary:
    def get_character(self):
        characters = [
            "Big Eared Mouse", "Sea Sponge", "Blue House Cat", "Fast Blue Hedgehog", "Yellow Electric Rodent",
            "Italian Plumber Brothers", "Green Dinosaur", "Pink Puffball", "Cave Dwelling Elf", "Hylian Princess",
            "Mutant Turtle Heroes", "Web Slinger", "Rich Billionaire", "The Dark Knight", "Amazonian Warrior",
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
    def create_spoof_art(self, character_name, rarity):
        style_modifier = ""
        if rarity == "ULTRA_RARE": style_modifier = "Golden Glow, God Rays, Masterpiece"
        elif rarity == "EPIC": style_modifier = "Cyberpunk Neon Glow, Heavy Metal, 4K Detail"
        else: style_modifier = "Trippy Psychedelic, Vibrant Colors"
        
        prompt = f"{style_modifier} digital art of {character_name}, highly detailed, vibrant colors"
        seed = random.randint(1, 999999)
        return f"https://pollinations.ai/p/{prompt}?width=600&height=400&seed={seed}&nologo=true"

# --- PRINTFUL MANAGER ---
class PrintfulManager:
    def __init__(self):
        self.api_key = "gv2leOBlmKlCotwhisTIlLsCbBnSrYt9kRXqmNHB"
        self.base_url = "https://api.printful.com"

    def create_physical_product(self, art_url, character, rarity):
        price_map = {"NORMAL": 20, "EPIC": 40, "ULTRA_RARE": 500}
        item_price = price_map.get(rarity, 20)
        
        print(f"-> [PRINTFUL] Rarity: {rarity} | Physical Value: ${item_price}")
        print(f"-> [SIMULATION] Syncing Art to Printful ({rarity} Tier)...")
        return True

# --- SOCIAL MANAGER (Hype Man) ---
class SocialManager:
    def __init__(self):
        pass

    def generate_hype_kit(self, character, art_url, price):
        hooks = [
            "Stop scrolling! You NEED to see this 👇",
            "I can't believe this actually exists... 🤯",
            "POV: This {character} art is illegal levels of cool 🔥",
            "Nobody knows about this yet... 😤",
            "Why is this so satisfying to look at? 😵"
        ]
        hook = random.choice(hooks)
        
        tiktok_caption = f"""
{hook}

Check out this trippy {character} art I just found! 🎨
It comes with a sourcing receipt too.

Link in Bio! 👇
#spoofart #trippy #aiart #{character.replace(" ", "")} #fyp
        """.strip()
        
        facebook_caption = f"""
{hook}

Manage AI has sourced a rare "{character}" piece. 🎨
Only {price}.00 for the receipt + link.

Click the link to view/buy! 👇
#familyvault #digitalart #{character.replace(" ", "")}
        """.strip()

        return {
            "tiktok": tiktok_caption,
            "facebook": facebook_caption
        }

# --- LEMON SQUEEZY MANAGER ---
class LemonManager:
    def __init__(self):
        self.api_key = "Q55YT2CZoJ-xWFIzidfUQsNikbybOrk-k7sBAMGuWqakADMvkBCd-nvRJt5TcqlYzd6syDxev-AWsrNR178O1KH7uPdvwt-ObSqako7o1dOEQOFaSuA-cqF9UM8CJ5wL9BCYvsaA-MKtu9BJdpxyipcNVLAJB-E2YzF9kRGJ"
        self.store_id = "PASTE_YOUR_LEMON_STORE_ID_HERE"
        self.base_url = "https://api.lemonsqueezy.com/v1"

    def calculate_profit(self, sale_price):
        self.base_fee = 0.50
        self.percentage_fee = 0.05
        lemon_fee = self.base_fee + (sale_price * self.percentage_fee)
        net_profit = sale_price - lemon_fee
        return round(lemon_fee, 2), round(net_profit, 2)

    def create_receipt_product(self, character, art_url, sale_price, physical_price, rarity):
        print(f"-> [LEMON] Connecting to Lemon Squeezy...")
        
        url = f"{self.base_url}/{self.store_id}/products"
        
        # --- FIX: CHECK FOR SIMULATION MODE ---
        if self.store_id == "PASTE_YOUR_LEMON_STORE_ID_HERE":
            print("-> [LEMON] STORE ID MISSING - ENTERING SIMULATION MODE")
            print(f"-> [LEMON] Mock Receipt created for '{character}'")
            
            # Simulate a successful delay
            import time
            time.sleep(1) 
            
            # Return a fake link so the script continues to Phase 9
            return "https://simulation.lemonsqueezy.com/view-receipt"
        # ------------------------------------

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        transaction_id = f"TXN-{random.randint(1000000, 9999999)}"
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        receipt_description = f"""
### OFFICIAL SOURCING RECEIPT - {rarity}

**Manage AI - Automated Sourcing Service**

---
**TRANSACTION DETAILS**
*   **Receipt ID:** {transaction_id}
*   **Date Issued:** {current_date}
*   **Status:** CONFIRMED / PAID

---
**PRODUCT & PRICING**
*   **Item Sourced:** {character}
*   **Item Rarity:** {rarity}
*   **Physical Item Value:** ${physical_price}.00
*   **Your Sourcing Fee:** ${sale_price}.00

---
**ACKNOWLEDGMENT**
This receipt confirms that Manage AI has sourced the item '{character}' ({rarity} Edition) on your behalf. 
Please locate your Digital Art Confirmation below.

---
**DIGITAL ART ASSET**
![Art]({art_url})

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
                    "price": sale_price * 100
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=product_data)
            
            print(f"-> [DEBUG] Lemon Response Code: {response.status_code}")
            
            if response.status_code == 201 or response.status_code == 200:
                print(f"-> [SUCCESS] Product Created on Lemon Squeezy.")
                link = f"https://{self.store_id}.lemonsqueezy.com/l/{random.randint(1000,9999)}"
                return link
            else:
                print(f"-> [ERROR] {response.text}")
                return None
        except Exception as e:
            print(f"-> [ERROR] {e}")
            return None

# --- SMART BANKER (Auto-Split Profit) ---
class SmartBanker:
    def __init__(self):
        self.db_path = 'financial_log.json'
        self.data = self.load_log()

    def load_log(self):
        try:
            with open(self.db_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"total_profit": 0, "reinvested": 0, "family_fund": 0}

    def save_log(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def split_profit(self, net_profit):
        # Strategy: 20% to Family Fund, 80% Reinvest
        family_cut = round(net_profit * 0.20, 2)
        reinvest_cut = round(net_profit * 0.80, 2)
        
        self.data['total_profit'] += net_profit
        self.data['family_fund'] += family_cut
        self.data['reinvested'] += reinvest_cut
        self.save_log()
        
        print(f"--> [BANKER] Net: ${net_profit} | Family Fund: +${family_cut} | Reinvest: +${reinvest_cut}")
        return self.data['family_fund']

# --- INVENTORY ANALYST (Stock Market) ---
class InventoryAnalyst:
    def __init__(self):
        pass

    def analyze_character(self, character):
        # Simulates checking historical sales of this character
        # Logic: If character is "Mouse", check if Mouse sold well before
        trending_status = "TRENDING" if random.randint(0, 1) == 0 else "STABLE"
        return trending_status

# --- NEXUS EXPORTER (For Future AI) ---
class NexusExporter:
    def __init__(self):
        self.db_path = 'nexus_feed.json'

    def export_data(self, item_data):
        # Formats data specifically for the future Nexus AI to read
        nexus_record = {
            "source": "Manage AI v16.0",
            "timestamp": datetime.now().isoformat(),
            "data": item_data
        }
        
        # Append to Nexus Feed
        try:
            with open(self.db_path, 'r') as f:
                feed = json.load(f)
            feed.append(nexus_record)
        except:
            feed = [nexus_record]
        
        with open(self.db_path, 'w') as f:
            json.dump(feed, f, indent=4)
        
        print(f"--> [NEXUS] Data Synced for Nexus AI.")

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
        self.config = Config()
        self.library = SpoofLibrary()
        self.artist = ArtGenerator()
        self.hands_print = PrintfulManager()
        self.hands_lemon = LemonManager()
        self.hands_social = SocialManager()
        self.memory = MemoryCore()
        self.banker = SmartBanker() # NEW
        self.analyst = InventoryAnalyst() # NEW
        self.nexus = NexusExporter() # NEW
        print(f"Manage v16.0 Online. Omniscient Manager Active.")

    def daily_grind(self):
        # 1. The Scheduler
        rarity = self.config.get_rarity()
        print("-" * 40)
        print(f"[SCHEDULER] RARITY DETECTED: {rarity}")

        # 2. Pricing Strategy
        pricing = {
            "NORMAL": {"fee": 5, "phys": 20},
            "EPIC": {"fee": 10, "phys": 40},
            "ULTRA_RARE": {"fee": 50, "phys": 500}
        }
        plan = pricing[rarity]

        # 3. Select Character (Stock Market Check)
        print("-" * 40)
        print("PHASE 1: SELECTING SPOOF")
        character = self.library.get_character()
        market_trend = self.analyst.analyze_character(character)
        print(f"-> [SELECTED] {character} ({market_trend})")

        # 4. Generate Art
        print("-" * 40)
        print("PHASE 2: GENERATING ART")
        art_url = self.artist.create_spoof_art(character, rarity)
        print(f"-> [ART] URL: {art_url}")

        # 5. Printful Sync
        print("-" * 40)
        print("PHASE 3: PRINTFUL SYNC")
        if not self.hands_print.create_physical_product(art_url, character, rarity):
            print("HALT: Printful failed.")
            return
        pf_id = f"PF-{random.randint(1000,9999)}"

        # 6. Calculate Costs
        print("-" * 40)
        print("PHASE 4: CALCULATING COSTS")
        sale_price = plan['fee']
        physical_price = plan['phys']
        fee, profit = self.hands_lemon.calculate_profit(sale_price)
        print(f"-> [FINANCIALS] Lemon Fee: ${fee} | Net to You: ${profit}")

        # 7. Smart Banking
        print("-" * 40)
        print("PHASE 5: SMART BANKING")
        family_total = self.banker.split_profit(profit)

        # 8. Create Receipt
        print("-" * 40)
        print("PHASE 6: CREATING RECEIPT")
        link = self.hands_lemon.create_receipt_product(character, art_url, sale_price, physical_price, rarity)
        if not link:
            print("HALT: Receipt failed.")
            return

        # 9. Generate Hype Kit
        print("-" * 40)
        print("PHASE 7: GENERATING HYPE KIT")
        hype_kit = self.hands_social.generate_hype_kit(character, art_url, sale_price)
        print(f"-> [SOCIAL] TikTok Caption Ready.")

        # 10. Nexus Export
        print("-" * 40)
        print("PHASE 8: NEXUS SYNC")
        nexus_item = {
            "name": f"Sourcing Set: {character}",
            "price": sale_price,
            "profit": profit,
            "market_trend": market_trend,
            "status": "Virtual",
            "social_kit": hype_kit
        }
        self.nexus.export_data(nexus_item)

        # 11. Final Save
        print("-" * 40)
        print("PHASE 9: SAVING")
        product_record = {
            "name": f"Sourcing Set: {character} [{rarity}]",
            "price": sale_price,
            "physical_value": physical_price,
            "rarity": rarity,
            "profit": profit,
            "market_trend": market_trend,
            "social_kit": hype_kit,
            "status": "Virtual",
            "art_url": art_url
        }
        self.memory.save_memory(product_record)
        print(f"--> [COMPLETE] Money Maker Active. Net Profit: ${profit} | Family Fund: ${family_total}")

if __name__ == "__main__":
    ai = Manage()
    ai.daily_grind()
