import asyncio
import os
import sys
import httpx
import base64
import time
from playwright.async_api import async_playwright

COOKIE_FILE = "cookies.json"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:3b"

if len(sys.argv) < 2:
    print("❌ Error: Missing destination URL target input argument parameter.")
    sys.exit(1)
TARGET_URL = sys.argv[1]

def image_to_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode('utf-8')

async def ask_qwen(prompt, image_path=None):
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    if image_path:
        payload["images"] = [image_to_base64(image_path)]
        
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            response = await client.post(OLLAMA_URL, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "").strip()
        except Exception as e:
            return f"Error connecting to AI server core: {e}"
    return "I do not know."

async def fallback_web_search(query):
    print(f"🔍 AI is uncertain. Searching the live internet for: {query}")
    url = f"https://duckduckgo.com{httpx.utils.quote(query)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            res = await client.get(url, headers=headers)
            if res.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(res.text, 'html.parser')
                snippets = [span.text for span in soup.find_all('span', class_='zcm__result__snippet')][:3]
                if not snippets:
                    snippets = [a.text for a in soup.find_all('a', class_='result__snippet')][:3]
                return "\n".join(snippets) if snippets else "No direct live search results surfaced."
        except Exception as e:
            return f"Search execution stalled: {e}"
    return "Search failed."

# 📜 SENSORY RECONNAISSANCE ROUTINE: Scrolls every inch to read full layout frames dynamically
async def trigger_full_page_sensory_scan(page, tab_id="context"):
    print(f"📜 [{tab_id}] Scanning environmental ecosystem. Scrolling full height up and down...")
    await page.evaluate("""async () => {
        await new Promise((resolve) => {
            let totalHeight = 0;
            let distance = 150;
            let timer = setInterval(() => {
                let scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;
                if(totalHeight >= scrollHeight){
                    clearInterval(timer);
                    // Snap back to top seamlessly
                    window.scrollTo(0, 0);
                    resolve();
                }
            }, 80);
        });
    }""")
    await asyncio.sleep(2)

async def process_monitoring_loop():
    print(f"🚀 Initializing continuous adaptive monitor for target URL: {TARGET_URL}")
    start_time = time.time()
    six_hours_in_seconds = 6 * 60 * 60

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
        )
        
        context = await browser.new_context(
            storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None,
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()
        
        # Abort images for rendering efficiency speed limits
        await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

        try:
            print(f"🌐 Landed on Course Core Endpoint Node: {TARGET_URL}")
            await page.goto(TARGET_URL, timeout=60000, wait_until="load")
            await asyncio.sleep(5)
            
            # --- ENVIRONMENTAL SCAN 1: Understand the course surface layer page ---
            await trigger_full_page_sensory_scan(page, "Course Surface")
            
            # --- STEP 1: LOCATE AND CLICK CHAT TAB WITH NOTIFICATION BADGE ---
            print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
            chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
            await chat_tab.wait_for(timeout=15000)
            await chat_tab.click()
            print("✅ Chat Tab container activated smoothly.")
            await asyncio.sleep(6) # Let the chat window canvas sync completely

            # MONITOR THE CHAT LOOP CONTINUOUSLY
            while (time.time() - start_time) < six_hours_in_seconds:
                print(f"\n🔄 Monitoring chat stream for changes... (Time: {((time.time() - start_time)/3600):.2f}/6.00 hours)")
                
                # --- ENVIRONMENTAL SCAN 2: Scroll chat layout box entirely to render lazy components ---
                await trigger_full_page_sensory_scan(page, "Chat Canvas")
                
                # Take complete full-page snapshot of the chat view
                snap_path = "full_chat_landscape.png"
                await page.screenshot(path=snap_path, full_page=True)
                print("📸 Captured master full-height landscape snapshot matrix.")

                # Let Qwen process its entire environment to decide actions adaptively
                meta_prompt = (
                    "Look at this full-height screenshot of the class chat portal. "
                    "Analyze the conversation streams adaptively. Look closely for any reflection question, "
                    "prompt box, or message thread started by 'Scholar' or 'AI Teaching Assistant'. "
                    "If a question is present, extract the exact question text. If none is found, output: 'NO_ACTIVE_PROMPT'."
                )
                question_asked = await ask_qwen(meta_prompt, snap_path)
                print(f"📡 AI Environment Analysis: {question_asked}")

                if "NO_ACTIVE_PROMPT" not in question_asked and len(question_asked) > 5:
                    print(f"❓ Question Detected: '{question_asked}'")
                    
                    check_prompt = f"Answer this question precisely: '{question_asked}'. If you hesitate or do not know the answer with 100% certainty, reply with exactly: 'HE_HESITATES_SEARCH_LIVE_INTERNET'."
                    ai_response = await ask_qwen(check_prompt, snap_path)

                    if "HE_HESITATES_SEARCH_LIVE_INTERNET" in ai_response or "I do not know" in ai_response:
                        search_results = await fallback_web_search(question_asked)
                        refine_prompt = f"The question is: '{question_asked}'. Internet research references:\n{search_results}\nCompile a highly accurate answer."
                        ai_response = await ask_qwen(refine_prompt)

                    print(f"🤖 Formulated Response: {ai_response}")

                if os.path.exists(snap_path):
                    os.remove(snap_path)
                    
                # Delay for 60 seconds before cycling the scan over again
                await asyncio.sleep(60)

        except Exception as e:
            print(f"❌ Main Execution Loop interrupted: {e}")
        finally:
            await context.close()
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run_ai_automation())
