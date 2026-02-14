from art_engine import HyperRenderer
import requests
import json
import random
import os
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

# --- CHARACTER FORGE (Generates Stats & Skills) ---
class CharacterForge:
    def generate_data(self, rarity):
        multiplier = 1
        if rarity == "EPIC": multiplier = 1.5
        if rarity == "ULTRA_RARE": multiplier = 2.0

        stats = {
            "str": min(100, int(random.randint(40, 70) * multiplier)),
            "int": min(100, int(random.randint(40, 70) * multiplier)),
            "dex": min(100, int(random.randint(40, 70) * multiplier))
        }

        skill_pool = [
            "Firewall", "Data Mining", "Stealth", "Hacking", 
            "Combat", "Diplomacy", "Engineering", "Sorcery",
            "Speed", "Strength", "Agility", "Telepathy"
        ]
        
        num_skills = 3 if rarity == "NORMAL" else (4 if rarity == "EPIC" else 5)
        skills = random.sample(skill_pool, num_skills)
        
        return stats, skills

# --- PRINTFUL MANAGER ---
class PrintfulManager:
    def __init__(self):
        self.api_key = os.getenv("PRINTFUL_API_KEY")
        self.base_url = "https://api.printful.com"

    def create_physical_product(self, art_url, character, rarity):
        # NOTE: In a full integration, we would map 'rarity' to a specific Printful Variant ID here.
        # For now, we simulate the sync.
        print(f"-> [PRINTFUL] Syncing {character} to Printful...")
        return True

# --- SOCIAL MANAGER ---
class SocialManager:
    def generate_hype_kit(self, character, art_url, price):
        hooks = [
            "Stop scrolling! You NEED to see this 👇",
            "I can't believe this actually exists... 🤯",
            "POV: This {character} art is illegal levels of cool 🔥",
            "Nobody knows about this yet... 😤",
            "Why is this so satisfying to look at? 😵"
        ]
        hook = random.choice(hooks)
        tiktok_caption = f"{hook}\n\nCheck out this {character} art! 🎨\nLink in Bio! 👇"
        return {"tiktok": tiktok_caption, "facebook": tiktok_caption}

# --- LEMON SQUEEZY MANAGER ---
class LemonManager:
    def __init__(self):
        self.api_key = os.getenv("LEMON_API_KEY")
        self.store_id = os.getenv("LEMON_STORE_ID")
        self.base_url = "https://api.lemonsqueezy.com/v1"

    def calculate_profit(self, sale_price):
        self.base_fee = 0.50
        self.percentage_fee = 0.05
        lemon_fee = self.base_fee + (sale_price * self.percentage_fee)
        net_profit = sale_price - lemon_fee
        return round(lemon_fee, 2), round(net_profit, 2)

    def create_receipt_product(self, character, art_url, sale_price, physical_price, rarity, stats, skills):
        print(f"-> [LEMON] Connecting to Lemon Squeezy...")
        
        if not self.store_id or self.store_id == "PASTE_YOUR_LEMON_STORE_ID_HERE":
            print("-> [LEMON] STORE ID MISSING - ENTERING SIMULATION MODE")
            return "https://simulation.lemonsqueezy.com/view-receipt"
        
        return "https://simulation.lemonsqueezy.com/view-receipt"

# --- SMART BANKER ---
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
        family_cut = round(net_profit * 0.20, 2)
        reinvest_cut = round(net_profit * 0.80, 2)
        self.data['total_profit'] += net_profit
        self.data['family_fund'] += family_cut
        self.data['reinvested'] += reinvest_cut
        self.save_log()
        print(f"--> [BANKER] Net: ${net_profit} | Family Fund: +${family_cut} | Reinvest: +${reinvest_cut}")
        return self.data['family_fund']

# --- INVENTORY ANALYST ---
class InventoryAnalyst:
    def analyze_character(self, character):
        return "TRENDING" if random.randint(0, 1) == 0 else "STABLE"

# --- NEXUS EXPORTER ---
class NexusExporter:
    def __init__(self):
        self.db_path = 'nexus_feed.json'
    def export_data(self, item_data):
        try:
            with open(self.db_path, 'r') as f: feed = json.load(f)
            feed.append(item_data)
        except: feed = [item_data]
        with open(self.db_path, 'w') as f: json.dump(feed, f, indent=4)
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
            return {"business_status": "Active", "inventory": []}

    def save_memory(self, item):
        self.data['inventory'].append(item)
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"--> [MEMORY] Saved product. Total: {len(self.data['inventory'])}.")

# --- MAIN MANAGE AI ---
class Manage:
    def __init__(self):
        self.config = Config()
        self.library = SpoofLibrary()
        self.renderer = HyperRenderer()
        self.forge = CharacterForge()
        self.hands_print = PrintfulManager()
        self.hands_lemon = LemonManager()
        self.hands_social = SocialManager()
        self.memory = MemoryCore()
        self.banker = SmartBanker()
        self.analyst = InventoryAnalyst()
        self.nexus = NexusExporter()
        print(f"Manage v18.0 (Physical Asset Edition) Online.")

    def daily_grind(self):
        # 1. Scheduler
        rarity = self.config.get_rarity()
        print("-" * 40)
        print(f"[SCHEDULER] RARITY DETECTED: {rarity}")

        # 2. PRODUCT CONFIGURATION (New Logic)
        # Defines what physical item is created, its price, and its edition tier.
        product_config = {
            "ULTRA_RARE": {
                "fee": 100, 
                "phys": 60, 
                "type": "Premium Stretched Canvas", 
                "edition": "1 of 1 (Unique)",
                "desc": "Museum-quality canvas on a wooden frame."
            },
            "EPIC": {
                "fee": 50, 
                "phys": 35, 
                "type": "Unisex Heavy Blend Hoodie", 
                "edition": "1 of 100,000 (Limited)",
                "desc": "Comfortable, classic fit hoodie."
            },
            "NORMAL": {
                "fee": 25, 
                "phys": 15, 
                "type": "Ceramic Coffee Mug", 
                "edition": "1 of 1,000,000 (Open)",
                "desc": "Durable ceramic mug in glossy finish."
            }
        }
        
        plan = product_config[rarity]
        
        # Extract variables for use later
        physical_product_name = plan["type"]
        edition_tier = plan["edition"]
        product_description = plan["desc"]
        sale_price = plan['fee']
        physical_price = plan['phys']

        # 3. Select Character
        print("-" * 40)
        print("PHASE 1: SELECTING SPOOF")
        character = self.library.get_character()
        market_trend = self.analyst.analyze_character(character)
        print(f"-> [SELECTED] {character} ({market_trend})")

        # 4. Generate Art & Stats
        print("-" * 40)
        print("PHASE 2: GENERATING MASTERPIECE & DATA")
        
        seed = random.randint(100000, 999999)
        filename = f"{seed}.jpg"
        
        # Call the HyperRenderer
        art_path = self.renderer.generate_masterpiece(character, filename, rarity)
        
        # Generate Stats & Skills
        stats, skills = self.forge.generate_data(rarity)
        
        print(f"-> [DATA] Stats: {stats} | Skills: {skills}")

        # 5. Printful Sync
        print("-" * 40)
        print("PHASE 3: PRINTFUL SYNC")
        self.hands_print.create_physical_product(art_path, character, rarity)

        # 6. Calculate Costs
        print("-" * 40)
        print("PHASE 4: CALCULATING COSTS")
        fee, profit = self.hands_lemon.calculate_profit(sale_price)
        print(f"-> [FINANCIALS] Lemon Fee: ${fee} | Net to You: ${profit}")

        # 7. Smart Banking
        print("-" * 40)
        print("PHASE 5: SMART BANKING")
        family_total = self.banker.split_profit(profit)

        # 8. Create Receipt
        print("-" * 40)
        print("PHASE 6: CREATING RECEIPT")
        link = self.hands_lemon.create_receipt_product(character, art_path, sale_price, physical_price, rarity, stats, skills)

        # 9. Generate Hype Kit
        print("-" * 40)
        print("PHASE 7: GENERATING HYPE KIT")
        hype_kit = self.hands_social.generate_hype_kit(character, art_path, sale_price)

        # 10. Nexus Export
        print("-" * 40)
        print("PHASE 8: NEXUS SYNC")
        self.nexus.export_data({"name": character, "price": sale_price})

        # 11. Final Save (Includes Physical Product Data)
        print("-" * 40)
        print("PHASE 9: SAVING")
        product_record = {
            "name": character,
            "rarity": rarity,
            "price": sale_price,
            "profit": profit,
            "market_trend": market_trend,
            "art_url": art_path,
            "stats": stats,
            "skills": skills,
            
            # NEW: Physical Product Mapping
            "product_type": physical_product_name,   # e.g., "Unisex Hoodie"
            "edition": edition_tier,                 # e.g., "1 of 100,000"
            "product_desc": product_description       # e.g., "Comfortable, classic fit..."
        }
        self.memory.save_memory(product_record)
        print(f"--> [COMPLETE] Net Profit: ${profit} | Family Fund: ${family_total}")

if __name__ == "__main__":
    ai = Manage()
    ai.daily_grind()
