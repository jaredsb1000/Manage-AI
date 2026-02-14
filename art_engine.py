import os
import requests
import random

class HyperRenderer:
    """
    FREE VERSION: Uses Pollinations.ai to generate images.
    No API Key required. Unlimited usage.
    """
    
    def __init__(self):
        # No API Key needed for this version
        pass
        
    def enhance_prompt(self, subject, rarity):
        """Injects professional keywords based on rarity."""
        
        if rarity == "ULTRA_RARE":
            style = "Golden Aura, Divine Light, Ethereal, Intricate Jewelry, 8k, masterpiece"
        elif rarity == "EPIC":
            style = "Cyberpunk Neon Glow, Heavy Metal, Chrome, Futuristic, 4k, detailed"
        else:
            style = "Vibrant Colors, Pop Art Style, high quality, detailed"
            
        return f"{style} digital art of {subject}. No text."

    def generate_masterpiece(self, subject, filename, rarity):
        """Generates the image using the free Pollinations API and returns the local file path."""
        print(f"-> [RENDER] Initializing Free Renderer for: {subject}")
        
        prompt = self.enhance_prompt(subject, rarity)
        
        # Prepare the URL for Pollinations.ai
        # We use a random seed to ensure we don't get the exact same image twice
        seed = random.randint(1, 999999999)
        
        # URL encode the prompt (replace spaces with %20)
        safe_prompt = prompt.replace(" ", "%20")
        
        # Construct the API URL
        # Using the 'flux' or 'turbo' model gives better results
        api_url = f"https://pollinations.ai/p/{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"
        
        try:
            print(f"-> [RENDER] Downloading from Free API...")
            response = requests.get(api_url, timeout=30)
            
            if response.status_code == 200:
                image_data = response.content
                
                # Ensure directory exists
                os.makedirs("images", exist_ok=True)
                
                # Save file
                filepath = f"images/{filename}"
                with open(filepath, "wb") as f:
                    f.write(image_data)
                    
                print(f"-> [SUCCESS] Free Art saved: {filepath}")
                return filepath
            else:
                print(f"-> [ERROR] API returned status {response.status_code}")
                return None

        except Exception as e:
            print(f"-> [ERROR] Rendering failed: {e}")
            return None
