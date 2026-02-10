import requests
import json
import os
import random

# --- ART GENERATOR (The Spoof Engine) ---
class ArtGenerator:
    def __init__(self):
        # List of "Spoof" characters to avoid Copyright
        self.characters = [
            "Salty Sailor Man (resembling Popeye)",
            "Mystery Brown Dog (resembling Scooby Doo)",
            "Fast Blue Rodent (resembling Sonic)",
            "Burger King Clone",
            "Psychic Yellow Duck",
            "Sponge Block (resembling SpongeBob)"
        ]

    def create_spoof_art(self):
        # Picks a character and generates a unique image URL
        character = random.choice(self.characters)
        
        # Prompt for the AI Art Generator (Pollinations)
        # Includes "Trippy", "Psychedelic", and "Cartoon" keywords
        prompt = f"Trippy psychedelic digital art of {character}, vibrant colors, receipt design, unique style"
        
        # Generates a random URL (Free service)
        seed = random.randint(1, 999999)
        art_url = f"https://pollinations.ai/p/{prompt}?width=600&height=400&seed={seed}&nologo=true"
        
        return character, art_url

# --- GUMROAD MANAGER ---
class GumroadManager:
    def __init__(self):
        self.client_id = os.getenv("GUMROAD_CLIENT_ID")
        self.client_secret = os.getenv("GUMROAD_CLIENT_SECRET")
        self.seller_id = os.getenv("GUMROAD_SELLER_ID")
        self.access_token = os.getenv("GUMROAD_ACCESS_TOKEN")

    def authenticate(self):
        if self.access_token:
            print(f"-> [AUTHENTICATED] Access Token found.")
            return True
        else:
            print("-> [ERROR] Missing GUMROAD_ACCESS_TOKEN.")
            return False

    def create_receipt_product(self, character, art_url, price):
        if not self.access_token:
            return None

        print(f"-> [CREATING] Receipt for '{character}'...")
        url = "https://api.gumroad.com/v2/products"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # The Product IS the Receipt with embedded Art
        data = {
            "name": f"Digital Receipt: {character} Collection",
            "description": f"""
            OFFICIAL DIGITAL RECEIPT
            
            Thank you for supporting the Family Vault.
            
            Item Collected: {character} Edition
            Collection Value: ${price}
            
            Please find your One-of-a-Kind Spoof Cartoon Art below:
            
            ![Receipt Art]({art_url})
            
            ---
            This receipt confirms your status as a collector.
            """,
            "price": price,
            "published": True,
            "max_purchase_count": 1, # One of a kind
            "require_shipping": False
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                product_data = response.json()
                slug = product_data['product']['url_slug']
                link = f"https://{self.seller_id}.gumroad.com/l/{slug}"
                print(f"-> [SUCCESS] Receipt Live! Link: {link}")
                return link
            else:
                print(f"-> [ERROR] Failed to create: {response.text}")
                return None
        except Exception as e:
            print(f"-> [ERROR] {e}")
            return None

# --- MAIN MANAGE AI ---
class Manage:
    def __init__(self):
        self.mode = "Family First"
        self.artist = ArtGenerator()
        self.hands = GumroadManager()
        print(f"Manage v8.0 Online. The Spoof Artist (Phase 1).")

    def daily_grind(self):
        print("-" * 40)
        print("PHASE 1: AUTHENTICATING")
        if not self.hands.authenticate():
            print("HALT: Cannot connect to Gumroad.")
            return

        print("-" * 40)
        print("PHASE 2: CREATING SPOOF ART")
        # Generates a new character and art
        character, art_url = self.artist.create_spoof_art()
        print(f"-> [ART] Created: {character}")
        
        # Random Price for Collection ($5 - $15)
        price = random.randint(5, 15)

        print("-" * 40)
        print("PHASE 3: LISTING RECEIPT")
        link = self.hands.create_receipt_product(character, art_url, price)
        
        if link:
            print("-" * 40)
            print(f"--> [MONEY MAKER] Digital Receipt ready for ${price}.")
            print(f"--> [LINK] {link}")
            print("   (Pure Profit - No Shipping Needed)")

if __name__ == "__main__":
    ai = Manage()
    ai.daily_grind()
