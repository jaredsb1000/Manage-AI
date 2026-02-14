import os
from openai import OpenAI

class HyperRenderer:
    """
    The Manage AI - HyperRenderer Engine.
    Integrates DALL-E 3 (HD) for commercial-grade art.
    """
    
    def __init__(self):
        # Looks for the 'OPENAI_API_KEY' in GitHub Secrets
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def enhance_prompt(self, subject, rarity):
        """Injects professional keywords based on rarity."""
        
        # Base keywords for quality
        base_quality = "8k resolution, photorealistic, cinematic lighting, volumetric fog, octane render, unreal engine 5, highly detailed texture, masterpiece, sharp focus, no text, no watermarks"
        
        # Style modifiers
        if rarity == "ULTRA_RARE":
            style = "Golden Aura, Divine Light, Ethereal, Intricate Jewelry"
        elif rarity == "EPIC":
            style = "Cyberpunk Neon Glow, Heavy Metal, Chrome, Futuristic"
        else:
            style = "Trippy Psychedelic, Vibrant Colors, Pop Art Style"
            
        return f"A breathtaking, high-definition capture of {subject}. {style}. {base_quality}."

    def generate_masterpiece(self, subject, filename, rarity):
        """Generates the image and returns the local file path."""
        print(f"-> [RENDER] Initializing HyperRenderer for: {subject}")
        
        prompt = self.enhance_prompt(subject, rarity)
        
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="hd", # CRITICAL: Uses HD mode
                n=1,
                response_format="b64_json"
            )
            
            image_data = response.data[0].b64_json
            
            # Ensure directory exists
            os.makedirs("images", exist_ok=True)
            
            # Save file
            filepath = f"images/{filename}"
            with open(filepath, "wb") as f:
                f.write(image_data)
                
            print(f"-> [SUCCESS] Masterpiece saved: {filepath}")
            return filepath

        except Exception as e:
            print(f"-> [ERROR] Rendering failed: {e}")
            # Fallback placeholder if API fails
            return "https://placehold.co/600x400/161b22/58a6ff?text=Render+Failed"
