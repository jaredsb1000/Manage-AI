# art_engine.py
import os
import requests
from openai import OpenAI

class HyperRenderer:
    """
    The Manage AI - HyperRenderer Engine.
    Integrates top-tier AI models (DALL-E 3) to generate 
    commercial-grade, high-fidelity art assets.
    """
    
    def __init__(self):
        # Initialize the client with your API Key from GitHub Secrets
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def enhance_prompt(self, subject, style="cinematic"):
        enhancement_keywords = {
            "cinematic": "8k resolution, photorealistic, cinematic lighting, volumetric fog, octane render, unreal engine 5, highly detailed texture, masterpiece, sharp focus",
            "cyberpunk": "neon lights, cybernetic implants, high tech, low life, chromatic aberration, futuristic city, rain slicked streets, 4k",
            "fantasy": "ethereal, magical, intricate details, oil painting style, dynamic lighting, ray tracing, epic composition"
        }
        
        keywords = enhancement_keywords.get(style, enhancement_keywords["cinematic"])
        enhanced = f"A breathtaking, high-definition capture of {subject}. {keywords}. No text, no watermarks, no blurry edges."
        return enhanced

    def generate_masterpiece(self, subject, filename, style="cinematic"):
        print(f"-> [RENDER] Initializing HyperRenderer for: {subject}")
        final_prompt = self.enhance_prompt(subject, style)
        
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=final_prompt,
                size="1024x1024",
                quality="hd",
                n=1,
                response_format="b64_json"
            )
            
            image_data = response.data[0].b64_json
            os.makedirs("images", exist_ok=True)
            filepath = f"images/{filename}"
            
            with open(filepath, "wb") as f:
                f.write(image_data)
                
            print(f"-> [SUCCESS] Masterpiece saved: {filepath}")
            return filepath

        except Exception as e:
            print(f"-> [ERROR] Rendering failed: {e}")
            return None
