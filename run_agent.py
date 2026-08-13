# import asyncio
# import os
# import json
# import httpx
# import base64
# from playwright.async_api import async_playwright

# COOKIE_FILE = "cookies.json"
# # ⚠️ UPDATE THIS to your real dashboard URL
# DASHBOARD_URL = "https://learner.saveetha.in" 
# OLLAMA_URL = "http://localhost:11434/api/generate"

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen_vision(prompt, image_path):
#     print("🧠 Querying Qwen-2.5-VL Vision Model inside cloud context...")
#     image_base64 = image_to_base64(image_path)
    
#     payload = {
#         "model": "qwen2.5vl:3b",
#         "prompt": prompt,
#         "images": [image_base64],
#         "stream": False
#     }
    
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "")
#             return f"❌ Ollama Error Code: {response.status_code}"
#         except Exception as e:
#             return f"❌ Failed connecting to Ollama: {str(e)}"

# async def run_ai_automation():
#     if not os.path.exists(COOKIE_FILE):
#         print(f"❌ Error: {COOKIE_FILE} missing from runner filesystem.")
#         return

#     print("🚀 Booting sandbox-compliant cloud browser...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
        
#         print("🔑 Pre-authenticating session via native storage state mapping...")
        
#         # FIXED LINE: We pass the cookie file directly into the context creator.
#         # Playwright will automatically handle if it's structured as an array or state object.
#         try:
#             context = await browser.new_context(storage_state=COOKIE_FILE)
#         except Exception as e:
#             print(f"⚠️ Warning: Direct storage_state failed ({e}). Trying backup loader...")
#             # Fallback block if your JSON is structured as a strict array
#             with open(COOKIE_FILE, 'r') as f:
#                 cookies_data = json.load(f)
#             context = await browser.new_context()
#             if isinstance(cookies_data, list):
#                 await context.add_cookies(cookies_data)
#             elif isinstance(cookies_data, dict) and "cookies" in cookies_data:
#                 await context.add_cookies(cookies_data["cookies"])
#             else:
#                 raise ValueError("cookies.json format is unrecognized.")

#         page = await context.new_page()
        
#         print(f"🌐 Loading endpoint: {DASHBOARD_URL}")
#         await page.goto(DASHBOARD_URL, timeout=60000, wait_until="networkidle")
        
#         # Take layout proof snapshot
#         screenshot_path = "page_view.png"
#         await page.screenshot(path=screenshot_path)
#         print("📸 Stored layout frame visualization matrix.")
        
#         ai_prompt = (
#             "Analyze this webpage screenshot carefully. Ensure the user is fully logged in. "
#             "Locate the rewards points in the page which is at the top of the website between two gift box icons, also tell what are the timings of the class and the class names to be attended. "
#             "visible on this layout context. Summarize everything found into clean Markdown format."
#         )
        
#         ai_analysis = await ask_qwen_vision(ai_prompt, screenshot_path)
        
#         print("\n🤖 === MODEL SYNTHESIS METRIC ===")
#         print(ai_analysis)
#         print("===================================\n")
        
#         # Write outputs to a text file artifact
#         with open("dashboard_report.txt", "w") as f:
#             f.write(ai_analysis)
            
#         await context.close()
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())



# import asyncio
# import os
# import json
# import httpx
# import base64
# from playwright.async_api import async_playwright

# COOKIE_FILE = "cookies.json"
# # ✅ FIXED: Points directly to the actual student learner portal, not the main landing site
# DASHBOARD_URL = "https://learner.saveetha.in" 
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen_vision(prompt, image_path):
#     print("🧠 Querying Qwen-2.5-VL Vision Model inside cloud context...")
#     image_base64 = image_to_base64(image_path)
    
#     payload = {
#         "model": MODEL_NAME,
#         "prompt": prompt,
#         "images": [image_base64],
#         "stream": False
#     }
    
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "")
#             return f"❌ Ollama Error Code: {response.status_code}"
#         except Exception as e:
#             return f"❌ Failed connecting to Ollama: {str(e)}"

# async def run_ai_automation():
#     if not os.path.exists(COOKIE_FILE):
#         print(f"❌ Error: {COOKIE_FILE} missing from runner filesystem.")
#         return

#     print("🚀 Booting sandbox-compliant cloud browser...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
        
#         print("🔑 Pre-authenticating session via native storage state mapping...")
#         context = await browser.new_context(storage_state=COOKIE_FILE)
#         page = await context.new_page()
        
#         print(f"🌐 Loading endpoint: {DASHBOARD_URL}")
#         # ✅ FIXED: Swapped 'networkidle' to 'load' to prevent the page from timing out on tracking assets
#         await page.goto(DASHBOARD_URL, timeout=60000, wait_until="load")
        
#         # Optional helper: Give elements an extra 2 seconds to settle visually
#         await asyncio.sleep(2)
        
#         screenshot_path = "page_view.png"
#         await page.screenshot(path=screenshot_path)
#         print("📸 Stored layout frame visualization matrix.")

        
        # ai_prompt = (
        #     "Analyze this webpage screenshot carefully. Ensure the user is fully logged in. "
        #     "Locate the rewards points in the page which is at the top of the website between two gift box icons, also tell what are the timings of the class and the class names to be attended. "
        #     "visible on this layout context. Summarize everything found into clean Markdown format."
        # )

#         ai_analysis = await ask_qwen_vision(ai_prompt, screenshot_path)
        
#         print("\n🤖 === MODEL SYNTHESIS METRIC ===")
#         print(ai_analysis)
#         print("===================================\n")
        
#         with open("dashboard_report.txt", "w") as f:
#             f.write(ai_analysis)
            
#         await context.close()
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())




import asyncio
import os
import json
import httpx
import base64
from playwright.async_api import async_playwright

COOKIE_FILE = "cookies.json"
DASHBOARD_URL = "https://learner.saveetha.in" 
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:3b"

def image_to_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode('utf-8')

async def ask_qwen_vision(prompt, image_path):
    # ✅ FIX 1: Add an aggressive wait loop to ensure the model is 100% ready in memory
    print("⏳ Verifying Ollama system service layer status...")
    async with httpx.AsyncClient(timeout=10.0) as check_client:
        for attempt in range(1, 20):
            try:
                # Check if the server is awake and the model exists
                response = await check_client.get("http://localhost:11434/api/tags")
                if response.status_code == 200 and MODEL_NAME in response.text:
                    print("✅ Ollama and Qwen Vision model are fully loaded and operational!")
                    break
            except Exception:
                pass
            print(f"⏳ Waiting for model compilation layer (Attempt {attempt}/20)...")
            await asyncio.sleep(5)

    print("🧠 Querying Qwen-2.5-VL Vision Model inside cloud context...")
    image_base64 = image_to_base64(image_path)
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image_base64],
        "stream": False
    }
    
    # ✅ FIX 2: Increased timeout to 300 seconds (5 minutes) because vision models take time to process images on free cloud cores
    async with httpx.AsyncClient(timeout=300.0) as client:
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
        
        print("🔑 Pre-authenticating session via native storage state mapping...")
        context = await browser.new_context(storage_state=COOKIE_FILE)
        page = await context.new_page()
        
        print(f"🌐 Loading endpoint: {DASHBOARD_URL}")
        # ✅ FIX 3: Give the authenticated Saveetha dashboard ample time to settle down
        await page.goto(DASHBOARD_URL, timeout=90000, wait_until="load")
        
        print("⏳ Holding session thread for post-login token settling...")
        await asyncio.sleep(10) # 10-second defensive sleep for secure DOM elements to render
        
        screenshot_path = "page_view.png"
        await page.screenshot(path=screenshot_path)
        print("📸 Stored layout frame visualization matrix.")


        ai_prompt = (
            "Analyze this webpage screenshot carefully. Ensure the user is fully logged in. "
            "Locate the rewards points in the page which is at the top of the website between two gift box icons, also tell what are the timings of the class and the class names to be attended. "
            "visible on this layout context. Summarize everything found into clean Markdown format."
        )

        ai_analysis = await ask_qwen_vision(ai_prompt, screenshot_path)
        
        print("\n🤖 === MODEL SYNTHESIS METRIC ===")
        print(ai_analysis)
        print("===================================\n")
        
        with open("dashboard_report.txt", "w") as f:
            f.write(ai_analysis)
            
        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_ai_automation())
