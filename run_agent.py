import asyncio
import os
import json
import httpx
import base64
from playwright.async_api import async_playwright

COOKIE_FILE = "cookies.json"
# ⚠️ UPDATE THIS to the exact dashboard URL you want the agent to monitor
DASHBOARD_URL = "https://learner.saveetha.in" 
OLLAMA_URL = "http://localhost:11434/api/generate"

def image_to_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode('utf-8')

async def ask_qwen_vision(prompt, image_path):
    print("🧠 Querying Qwen-2.5-VL Vision Model inside cloud context...")
    image_base64 = image_to_base64(image_path)
    
    payload = {
        "model": "qwen2.5-vl:3b",
        "prompt": prompt,
        "images": [image_base64],
        "stream": False
    }
    
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            response = await client.post(OLLAMA_URL, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "")
            return f"❌ Ollama Error Code: {response.status_code}"
        except Exception as e:
            return f"❌ Failed connecting to Ollama: {str(e)}"

async def run_ai_automation():
    if not os.path.exists(COOKIE_FILE):
        print(f"❌ Error: {COOKIE_FILE} missing from runner filesystem.")
        return

    print("🚀 Booting sandbox-compliant cloud browser...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
        )
        
        print("🔑 Pre-authenticating session via state mapping...")
        
        # Load custom cookie array structure cleanly
        with open(COOKIE_FILE, 'r') as f:
            cookies = json.load(f)
        
        context = await browser.new_context()
        await context.add_cookies(cookies)
        page = await context.new_page()
        
        print(f"🌐 Loading endpoint: {DASHBOARD_URL}")
        await page.goto(DASHBOARD_URL, timeout=60000, wait_until="networkidle")
        
        # Take layout proof snapshot
        screenshot_path = "page_view.png"
        await page.screenshot(path=screenshot_path)
        print("📸 Stored layout frame visualization matrix.")
        
        ai_prompt = (
            "Analyze this webpage screenshot carefully. Ensure the user is fully logged in. "
            "Locate and extract the primary stats, summary grids, update cards, or logs "
            "visible on this layout context. Summarize everything found into clean Markdown format."
        )
        
        ai_analysis = await ask_qwen_vision(ai_prompt, screenshot_path)
        
        print("\n🤖 === MODEL SYNTHESIS METRIC ===")
        print(ai_analysis)
        print("===================================\n")
        
        # Write outputs to a text file artifact
        with open("dashboard_report.txt", "w") as f:
            f.write(ai_analysis)
            
        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_ai_automation())
