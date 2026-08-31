# import asyncio
# import os
# import sys
# import httpx
# import base64
# import time
# from playwright.async_api import async_playwright

# COOKIE_FILE = "cookies.json"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument parameter.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         payload["images"] = [image_to_base64(image_path)]
        
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error connecting to AI server core: {e}"
#     return "I do not know."

# async def fallback_web_search(query):
#     print(f"🔍 AI is uncertain. Searching the live internet for: {query}")
#     url = f"https://duckduckgo.com{httpx.utils.quote(query)}"
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
#     async with httpx.AsyncClient(timeout=15.0) as client:
#         try:
#             res = await client.get(url, headers=headers)
#             if res.status_code == 200:
#                 from bs4 import BeautifulSoup
#                 soup = BeautifulSoup(res.text, 'html.parser')
#                 snippets = [span.text for span in soup.find_all('span', class_='zcm__result__snippet')][:3]
#                 if not snippets:
#                     snippets = [a.text for a in soup.find_all('a', class_='result__snippet')][:3]
#                 return "\n".join(snippets) if snippets else "No direct live search results surfaced."
#         except Exception as e:
#             return f"Search execution stalled: {e}"
#     return "Search failed."

# # 📜 SENSORY RECONNAISSANCE ROUTINE: Scrolls every inch to read full layout frames dynamically
# async def trigger_full_page_sensory_scan(page, tab_id="context"):
#     print(f"📜 [{tab_id}] Scanning environmental ecosystem. Scrolling full height up and down...")
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     // Snap back to top seamlessly
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 80);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def process_monitoring_loop():
#     print(f"🚀 Initializing continuous adaptive monitor for target URL: {TARGET_URL}")
#     start_time = time.time()
#     six_hours_in_seconds = 6 * 60 * 60

#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
        
#         context = await browser.new_context(
#             storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None,
#             viewport={"width": 1280, "height": 800}
#         )
#         page = await context.new_page()
        
#         # Abort images for rendering efficiency speed limits
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Landed on Course Core Endpoint Node: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)
            
#             # --- ENVIRONMENTAL SCAN 1: Understand the course surface layer page ---
#             await trigger_full_page_sensory_scan(page, "Course Surface")
            
#             # --- STEP 1: LOCATE AND CLICK CHAT TAB WITH NOTIFICATION BADGE ---
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             print("✅ Chat Tab container activated smoothly.")
#             await asyncio.sleep(6) # Let the chat window canvas sync completely

#             # MONITOR THE CHAT LOOP CONTINUOUSLY
#             while (time.time() - start_time) < six_hours_in_seconds:
#                 print(f"\n🔄 Monitoring chat stream for changes... (Time: {((time.time() - start_time)/3600):.2f}/6.00 hours)")
                
#                 # --- ENVIRONMENTAL SCAN 2: Scroll chat layout box entirely to render lazy components ---
#                 await trigger_full_page_sensory_scan(page, "Chat Canvas")
                
#                 # Take complete full-page snapshot of the chat view
#                 snap_path = "full_chat_landscape.png"
#                 await page.screenshot(path=snap_path, full_page=True)
#                 print("📸 Captured master full-height landscape snapshot matrix.")

#                 # Let Qwen process its entire environment to decide actions adaptively
#                 meta_prompt = (
#                     "Look at this full-height screenshot of the class chat portal. "
#                     "Analyze the conversation streams adaptively. Look closely for any reflection question, "
#                     "prompt box, or message thread started by 'Scholar' or 'AI Teaching Assistant'. "
#                     "If a question is present, extract the exact question text. If none is found, output: 'NO_ACTIVE_PROMPT'."
#                 )
#                 question_asked = await ask_qwen(meta_prompt, snap_path)
#                 print(f"📡 AI Environment Analysis: {question_asked}")

#                 if "NO_ACTIVE_PROMPT" not in question_asked and len(question_asked) > 5:
#                     print(f"❓ Question Detected: '{question_asked}'")
                    
#                     check_prompt = f"Answer this question precisely: '{question_asked}'. If you hesitate or do not know the answer with 100% certainty, reply with exactly: 'HE_HESITATES_SEARCH_LIVE_INTERNET'."
#                     ai_response = await ask_qwen(check_prompt, snap_path)

#                     if "HE_HESITATES_SEARCH_LIVE_INTERNET" in ai_response or "I do not know" in ai_response:
#                         search_results = await fallback_web_search(question_asked)
#                         refine_prompt = f"The question is: '{question_asked}'. Internet research references:\n{search_results}\nCompile a highly accurate answer."
#                         ai_response = await ask_qwen(refine_prompt)

#                     print(f"🤖 Formulated Response: {ai_response}")

#                 if os.path.exists(snap_path):
#                     os.remove(snap_path)
                    
#                 # Delay for 60 seconds before cycling the scan over again
#                 await asyncio.sleep(60)

#         except Exception as e:
#             print(f"❌ Main Execution Loop interrupted: {e}")
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())









# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# COOKIE_FILE = "cookies.json"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# KNOWLEDGE_FILE = "ai_self_learning_data.json"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     """Loads long-term tracking files, ensuring standard dictionary schemas exist."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 Repository memory baseline safely committed to '{KNOWLEDGE_FILE}'")

# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 50);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         with open(image_path, "rb") as img:
#             payload["images"] = [base64.b64encode(img.read()).decode('utf-8')]
            
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error: {e}"
#     return "I do not know."

# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     six_hours_in_seconds = 6 * 60 * 60

#     print("🚀 Initializing adaptive concurrent task worker layer...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None)
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             # 🛠️ EXTRACTION PHASE: Pull Subject Name + Code string layout from the top text blocks
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
            
#             # Use regex to clean and find the code context (e.g., '19AI408')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}] | Profile -> '{subject_header}'")

#             # Initialize subject key section inside the json tracking structure if missing
#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []

#             # STEP 1: Click the Chat Tab
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)

#             # STEP 2: Click Discussion Topics
#             # Uses the red badge parent container container implicitly without relying on its numbers
#             discussion_topics_tab = page.locator("div:has-text('Discussion topics'), button:has-text('Discussion topics')").last
#             await discussion_topics_tab.click()
#             await asyncio.sleep(5)

#             # STEP 3: Scroll layout and scan elements from bottom up
#             await trigger_full_page_sensory_scan(page)
            
#             # Target all visible text links inside the Discussion rows panel area
#             topic_locators = page.locator("div.discussion-topics-list a, div:has([style*='background-color: rgb(220, 53, 69)']) a, .discussion-title")
#             count = await topic_locators.count()
            
#             target_topic_name = None
#             target_element = None

#             print(f"📋 Found {count} total rows in discussion area. Processing from bottom up...")
#             # LOOP FROM BOTTOM TO TOP: Iterating backwards to access the oldest items first
#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
                
#                 topic_title = lines[0] # Grabs header line name (e.g., 'M6_Recursion')
                
#                 # Check if this topic hasn't been completed yet for this specific subject code
#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break

#             if not target_topic_name:
#                 print(f"✨ All visible topics under subject [{subject_code}] have already been processed! Exiting.")
#                 await context.close()
#                 await browser.close()
#                 return

#             print(f"🎯 Found unvisited target row item at bottom of list: '{target_topic_name}'")
            
#             # --- STEP 4: INSTANT SELECTION LOCKING ---
#             # Append the name to our JSON list and save it IMMEDIATELY before clicking
#             # This locks the row name so overlapping workflows skip it
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             # Click on the chosen topic to enter its chat canvas window view
#             print(f"🖱️ Entering chat forum container: {target_topic_name}")
#             await target_element.click()
#             await asyncio.sleep(6)

#             # KEEP RUNNING FOR THE WHOLE 6 HOURS TO MONITOR UPDATES
#             while (time.time() - start_time) < six_hours_in_seconds:
#                 print(f"🔄 Monitoring conversation frame for updates... (Running for {((time.time() - start_time)/3600):.2f}/6.00 hours)")
#                 await trigger_full_page_sensory_scan(page)
                
#                 snap_path = "live_chat_view.png"
#                 await page.screenshot(path=snap_path, full_page=True)
                
#                 meta_prompt = (
#                     "Look at this screenshot of the class discussion chat panel. "
#                     "Analyze the conversation updates carefully. Look for message components from "
#                     "'Scholar' or 'AI Teaching Assistant' that ask a direct question or prompt. "
#                     "If found, extract the exact question text. If none exists, output: 'NO_ACTIVE_PROMPT'."
#                 )
#                 question_text = await ask_qwen(meta_prompt, snap_path)
                
#                 if "NO_ACTIVE_PROMPT" not in question_text and len(question_text) > 5:
#                     print(f"❓ Extracted Prompt Question: '{question_text}'")
#                     # Process and formulate your answers here...
                    
#                 if os.path.exists(snap_path):
#                     os.remove(snap_path)
                    
#                 await asyncio.sleep(60) # Watch checking interval refresh pace

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())







# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# COOKIE_FILE = "cookies.json"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# KNOWLEDGE_FILE = "ai_self_learning_data.json"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     """Loads the long-term repository tracking file safely."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 Repository memory baseline safely committed to '{KNOWLEDGE_FILE}'")

# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 50);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         with open(image_path, "rb") as img:
#             payload["images"] = [base64.b64encode(img.read()).decode('utf-8')]
            
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error: {e}"
#     return "I do not know."

# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     six_hours_in_seconds = 6 * 60 * 60

#     print("🚀 Initializing adaptive sequential task worker layer...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None)
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             # Extract Subject Name + Code string layout from the top text blocks
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
            
#             # Map out subject code context (e.g., '19AI408')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []

#             # STEP 1: Click the Chat Tab
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)

#             # STEP 2: Click Discussion Topics
#             discussion_topics_tab = page.locator("div:has-text('Discussion topics'), button:has-text('Discussion topics')").last
#             await discussion_topics_tab.click()
#             await asyncio.sleep(5)

#             # STEP 3: Scroll layout thoroughly to load every single available topic card into memory
#             print("📜 Scrolling down to the absolute bottom of discussion list...")
#             await trigger_full_page_sensory_scan(page)
            
#             # Locate all active discussion rows using your red background banner marker
#             topic_locators = page.locator("div.discussion-topics-list a, div:has([style*='background-color: rgb(220, 53, 69)']) a, .discussion-title")
#             count = await topic_locators.count()
            
#             target_topic_name = None
#             target_element = None

#             print(f"📋 Mapped {count} total rows in discussion area. Starting analysis strictly from the oldest items at the bottom...")
            
#             # 🔄 STRICT LINEAR BOTTOM-TO-TOP CHECK Loop
#             # This handles your rule precisely: it checks the bottom element first, moving up only if already visited.
#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
                
#                 topic_title = lines[0] # Safely extract title text
                
#                 # If this item has NOT been completed yet, lock onto it instantly
#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break
#                 else:
#                     print(f"⏭️ Skipping already completed row: '{topic_title}' (Checking next row up)")

#             if not target_topic_name:
#                 print(f"✨ Perfect! Every single task inside the [{subject_code}] discussion tree has been completely verified and solved.")
#                 await context.close()
#                 browser.close()
#                 return

#             print(f"🎯 Targeted oldest uncompleted task: '{target_topic_name}'")
            
#             # Save the title name to JSON memory IMMEDIATELY to prevent overlapping runs from duplicating work
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             # Click the selected topic card to launch into the inner live forum discussion channel 
#             print(f"🖱️ Entering chat forum container: {target_topic_name}")
#             await target_element.click()
#             await asyncio.sleep(6)

#             # MONITOR THE OPENED DISCUSSION CANVAS FOR THE WHOLE 6 HOURS
#             while (time.time() - start_time) < six_hours_in_seconds:
#                 print(f"🔄 Monitoring conversation frame for updates... (Running for {((time.time() - start_time)/3600):.2f}/6.00 hours)")
#                 await trigger_full_page_sensory_scan(page)
                
#                 snap_path = "live_chat_view.png"
#                 await page.screenshot(path=snap_path, full_page=True)
                
#                 meta_prompt = (
#                     "Look at this screenshot of the class discussion chat panel. "
#                     "Analyze the conversation updates carefully. Look for message components from "
#                     "'Scholar' or 'AI Teaching Assistant' that ask a direct question or prompt. "
#                     "If found, extract the exact question text. If none exists, output: 'NO_ACTIVE_PROMPT'."
#                 )
#                 question_text = await ask_qwen(meta_prompt, snap_path)
                
#                 if "NO_ACTIVE_PROMPT" not in question_text and len(question_text) > 5:
#                     print(f"❓ Extracted Prompt Question: '{question_text}'")
#                     # Processing logic for question answering goes here...
                    
#                 if os.path.exists(snap_path):
#                     os.remove(snap_path)
                    
#                 await asyncio.sleep(60)

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())





# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# COOKIE_FILE = "cookies.json"
# BASE_URL = "https://saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# KNOWLEDGE_FILE = "ai_self_learning_data.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     """Loads the long-term repository tracking memory file safely."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     """Saves updated task status parameters right into the repo files."""
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 Repository memory baseline safely committed to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         payload["images"] = [image_to_base64(image_path)]
            
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error: {e}"
#     return "I do not know."

# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_to_absolute_top_of_chat(page):
#     """Navigates to the absolute beginning of the conversation thread container."""
#     print("📜 Navigating up to find the person who first started this discussion...")
#     previous_height = 0
#     for attempt in range(25):
#         await page.evaluate("window.scrollTo(0, 0);")
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"]');
#             if(chatDiv) chatDiv.scrollTop = 0;
#         }""")
#         await asyncio.sleep(2)
#         current_height = await page.evaluate("document.body.scrollHeight")
#         if current_height == previous_height:
#             break
#         previous_height = current_height
#     print("✅ Arrived at the absolute initial message position frame.")

# async def send_chat_message(page, message_text):
#     """Locates the input interface, enters the text, and triggers submission."""
#     print(f"✍️ Submitting compiled string token into chat layout input...")
#     try:
#         chat_box = page.get_by_placeholder("Write a message...")
#         await chat_box.wait_for(timeout=10000)
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
        
#         send_btn = page.locator("button:has-text('Send')")
#         if await send_btn.count() == 0:
#             send_btn = page.locator("button").last
            
#         await send_btn.click()
#         print("🚀 Message pushed successfully to live portal thread!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission layer encountered a selector fault: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting parallel sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None)
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             # Extract Subject Name + Code string layout from page text blocks
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []

#             # STEP 1: Open the Chat Tab
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)

#             # STEP 2: Navigate into the Discussion Topics Area
#             discussion_topics_tab = page.locator("div:has-text('Discussion topics'), button:has-text('Discussion topics')").last
#             await discussion_topics_tab.click()
#             await asyncio.sleep(5)

#             # STEP 3: Scroll layout and scan elements strictly from bottom up
#             await trigger_full_page_sensory_scan(page)
            
#             topic_locators = page.locator("div.discussion-topics-list a, div:has([style*='background-color: rgb(220, 53, 69)']) a, .discussion-title")
#             count = await topic_locators.count()
            
#             target_topic_name = None
#             target_element = None

#             print(f"📋 Found {count} rows. Scanning from the bottom up to clear older tasks...")
#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines[0]
                
#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break
#                 else:
#                     print(f"⏭️ Skipping already completed row: '{topic_title}'")

#             if not target_topic_name:
#                 print(f"✨ All visible topics under subject [{subject_code}] have already been processed! Exiting.")
#                 await context.close()
#                 await browser.close()
#                 return

#             print(f"🎯 Targeted oldest uncompleted task: '{target_topic_name}'")
            
#             # Save the title name to JSON memory IMMEDIATELY to lock out concurrent workflows
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             # Click the selected topic card to launch into the discussion forum
#             await target_element.click()
#             await asyncio.sleep(6)

#             # Move browser viewport context up to the genesis of the thread
#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path, full_page=True)
            
#             ai_prompt = (
#                 "Look at the very first message at the top of this chat page layout that started this discussion topic. "
#                 "Read that message question carefully and compose an accurate, high-quality response to it. "
#                 "CRUCIAL RULE: Keep your compiled answer very brief, short, and to the point. No fluff."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
#             print(f"🤖 Compiled Brief Answer Layout Token: '{initial_answer}'")
            
#             if os.path.exists(snap_path):
#                 os.remove(snap_path)

#             # Submit your initial response directly to the active chat box
#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await trigger_full_page_sensory_scan(page)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     # Target Identity Verification Check Block
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
                        
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame, full_page=True)
                        
#                         followup_prompt = (
#                             f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. "
#                             f"Review this conversation screenshot, locate their specific message, and formulate a precise, brief follow-up response to what they asked."
#                         )
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
                        
#                         await send_chat_message(page, followup_answer)
                        
#                         if os.path.exists(reply_frame):
#                             os.remove(reply_frame)
#                         break
                
#                 # Check for updates every 2 minutes
#                 await asyncio.sleep(120)

#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())





# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# COOKIE_FILE = "cookies.json"
# BASE_URL = "https://saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# KNOWLEDGE_FILE = "ai_self_learning_data.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     """Loads the long-term repository tracking memory file safely."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     """Saves updated task status parameters right into the repo files."""
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 Repository memory baseline safely committed to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         payload["images"] = [image_to_base64(image_path)]
            
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error: {e}"
#     return "I do not know."

# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_to_absolute_top_of_chat(page):
#     """Navigates to the absolute beginning of the conversation thread container."""
#     print("AI scrolling up to find the first message that started the chat...")
#     previous_height = 0
#     for attempt in range(25):
#         await page.evaluate("window.scrollTo(0, 0);")
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"]');
#             if(chatDiv) chatDiv.scrollTop = 0;
#         }""")
#         await asyncio.sleep(2)
#         current_height = await page.evaluate("document.body.scrollHeight")
#         if current_height == previous_height:
#             break
#         previous_height = current_height
#     print("✅ Arrived at the absolute initial message position frame.")

# async def send_chat_message(page, message_text):
#     """Locates the input interface, enters the text, and triggers submission."""
#     print(f"✍️ Submitting compiled string token into chat layout input...")
#     try:
#         chat_box = page.get_by_placeholder("Write a message...")
#         await chat_box.wait_for(timeout=10000)
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
        
#         send_btn = page.locator("button:has-text('Send')")
#         if await send_btn.count() == 0:
#             send_btn = page.locator("button").last
            
#         await send_btn.click()
#         print("🚀 Message pushed successfully to live portal thread!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission layer encountered a selector fault: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None)
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             # Extract Subject Name + Code string layout from page text blocks
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []

#             # STEP 1: Open the Chat Tab
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)

#             # STEP 2: Navigate into the Discussion Topics Area (Using red badge as anchor)
#             print("🔍 STEP 2: Scanning for the 'Discussion topics' region using the red badge marker layout...")
#             discussion_topics_tab = page.locator("div:has-text('Discussion topics'), button:has-text('Discussion topics')").last
#             await discussion_topics_tab.click()
#             await asyncio.sleep(5)

#             # STEP 3: Scroll layout and scan elements strictly from bottom up using red tag landmarks
#             print("🔍 STEP 3: Scrolling list thoroughly to map topics via red background banner landmarks...")
#             await trigger_full_page_sensory_scan(page)
            
#             # Locate all active discussion links
#             topic_locators = page.locator("div.discussion-topics-list a, div:has([style*='background-color: rgb(220, 53, 69)']) a, .discussion-title")
#             count = await topic_locators.count()
            
#             target_topic_name = None
#             target_element = None

#             print(f"📋 Found {count} total rows. Evaluating from the bottom up to pick the oldest unfinished task...")
#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines[0]
                
#                 # Verify if this row title hasn't been completed yet for this subject code
#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break
#                 else:
#                     print(f"⏭️ Skipping already completed row: '{topic_title}'")

#             if not target_topic_name:
#                 print(f"✨ All visible topics under subject [{subject_code}] have already been processed! Exiting.")
#                 await context.close()
#                 await browser.close()
#                 return

#             print(f"🎯 Targeted oldest uncompleted task row: '{target_topic_name}'")
            
#             # Save the title name to JSON memory IMMEDIATELY to lock out concurrent workflows
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             # Click the selected topic card to launch into the discussion forum
#             await target_element.click()
#             await asyncio.sleep(6)

#             # Move browser viewport context up to the absolute genesis of the thread
#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path, full_page=True)
            
#             ai_prompt = (
#                 "Look at the very first message at the top of this chat page layout that started this discussion topic. "
#                 "Read that message question carefully and compose an accurate, high-quality response to it. "
#                 "CRUCIAL RULE: Keep your compiled answer very brief, short, and to the point. No fluff."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
#             print(f"🤖 Compiled Brief Answer Layout Token: '{initial_answer}'")
            
#             if os.path.exists(snap_path):
#                 os.remove(snap_path)

#             # Submit your brief initial response directly to the active chat box
#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await trigger_full_page_sensory_scan(page)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     # STRICT RULE VALIDATION: Only respond when "Scholar" explicitly addresses your specific name token
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
                        
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame, full_page=True)
                        
#                         followup_prompt = (
#                             f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. "
#                             f"Review this conversation screenshot, locate their specific message, and formulate a precise, brief follow-up response to what they asked."
#                         )
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
                        
#                         await send_chat_message(page, followup_answer)
                        
#                         if os.path.exists(reply_frame):
#                             os.remove(reply_frame)
#                         break
                
#                 # Check for updates every 2 minutes
#                 await asyncio.sleep(120)

#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())








# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# # ✅ FIXED: Updated to save data directly inside your required file name target
# KNOWLEDGE_FILE = "complete-interact.json"
# BASE_URL = "https://learner.saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# COOKIE_FILE = "cookies.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     """Loads the complete-interact.json file. Creates it dynamically if missing."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     print(f"🆕 '{KNOWLEDGE_FILE}' not found or empty. Building a clean tracking list structure...")
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     """Writes progress instantly to complete-interact.json."""
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 Repository memory baseline safely committed to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         payload["images"] = [image_to_base64(image_path)]
            
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error: {e}"
#     return "I do not know."

# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_to_absolute_top_of_chat(page):
#     """Navigates to the absolute beginning of the conversation thread container."""
#     print("AI scrolling up to find the first message that started the chat...")
#     previous_height = 0
#     for attempt in range(25):
#         await page.evaluate("window.scrollTo(0, 0);")
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"]');
#             if(chatDiv) chatDiv.scrollTop = 0;
#         }""")
#         await asyncio.sleep(2)
#         current_height = await page.evaluate("document.body.scrollHeight")
#         if current_height == previous_height:
#             break
#         previous_height = current_height
#     print("✅ Arrived at the absolute initial message position frame.")

# async def send_chat_message(page, message_text):
#     """Locates the input interface, enters the text, and triggers submission."""
#     print(f"✍ * Submitting compiled string token into chat layout input...")
#     try:
#         chat_box = page.get_by_placeholder("Write a message...")
#         await chat_box.wait_for(timeout=10000)
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
        
#         send_btn = page.locator("button:has-text('Send')")
#         if await send_btn.count() == 0:
#             send_btn = page.locator("button").last
            
#         await send_btn.click()
#         print("🚀 Message pushed successfully to live portal thread!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission layer encountered a selector fault: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None)
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             # Extract Subject Name + Code layout string context
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []

#             # STEP 1: Open Chat Tab
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)

#             # STEP 2: Open Discussion Topics
#             print("🔍 STEP 2: Scanning for the 'Discussion topics' region using the red badge marker layout...")
#             discussion_topics_tab = page.locator("div:has-text('Discussion topics'), button:has-text('Discussion topics'), [class*='Discussion']").last
#             await discussion_topics_tab.click()
#             await asyncio.sleep(5)

#             # STEP 3: Scroll layout thoroughly to map topics
#             print("🔍 STEP 3: Scrolling list thoroughly to map topics via red background banner landmarks...")
#             await trigger_full_page_sensory_scan(page)
            
#             # ✅ FIXED SELECTORS: Broadened target filters to grab chat list entries robustly
#             topic_locators = page.locator("//div[contains(@class, 'discussion')]//a | //a[contains(@href, 'topic')] | //div[contains(@style, 'rgb(220, 53, 69)')]//parent::div//a | .discussion-title")
#             count = await topic_locators.count()
            
#             target_topic_name = None
#             target_element = None

#             print(f"📋 Found {count} total rows. Evaluating from the bottom up to pick the oldest unfinished task...")
#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines[0] # Select header title string token explicitly
                
#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break
#                 else:
#                     print(f"⏭ * Skipping already completed row: '{topic_title}'")

#             if not target_topic_name:
#                 print(f"✨ All visible topics under subject [{subject_code}] have already been processed in complete-interact.json! Exiting.")
#                 await context.close()
#                 await browser.close()
#                 return

#             print(f"🎯 Targeted oldest uncompleted task row: '{target_topic_name}'")
            
#             # Save the title name to JSON memory IMMEDIATELY to lock out concurrent workflows
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             # Click the selected topic card to launch into the discussion forum
#             await target_element.click()
#             await asyncio.sleep(6)

#             # Move browser viewport context up to the absolute genesis of the thread
#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path, full_page=True)
            
#             ai_prompt = (
#                 "Look at the very first message at the top of this chat page layout that started this discussion topic. "
#                 "Read that message question carefully and compose an accurate, high-quality response to it. "
#                 "CRUCIAL RULE: Keep your compiled answer very brief, short, and to the point. No fluff."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
#             print(f"🤖 Compiled Brief Answer Layout Token: '{initial_answer}'")
            
#             if os.path.exists(snap_path):
#                 os.remove(snap_path)

#             # Submit initial response directly to the active chat box
#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await trigger_full_page_sensory_scan(page)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
                        
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame, full_page=True)
                        
#                         followup_prompt = (
#                             f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. "
#                             f"Review this conversation screenshot, locate their specific message, and formulate a precise, brief follow-up response to what they asked."
#                         )
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
                        
#                         await send_chat_message(page, followup_answer)
                        
#                         if os.path.exists(reply_frame):
#                             os.remove(reply_frame)
#                         break
                
#                 await asyncio.sleep(120)

#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())










# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# KNOWLEDGE_FILE = "complete-interact.json"
# BASE_URL = "https://learner.saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# COOKIE_FILE = "cookies.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     """Loads the tracking file safely. Creates it dynamically if missing."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     print(f"🆕 '{KNOWLEDGE_FILE}' not found or empty. Initializing empty tracking dictionary layout...")
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     """Writes progress tracking metrics instantly to complete-interact.json."""
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 Session verification state logs saved locally to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         payload["images"] = [image_to_base64(image_path)]
            
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error: {e}"
#     return "I do not know."

# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_to_absolute_top_of_chat(page):
#     print("AI scrolling up to find the first message that started the chat...")
#     previous_height = 0
#     for attempt in range(25):
#         await page.evaluate("window.scrollTo(0, 0);")
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"]');
#             if(chatDiv) chatDiv.scrollTop = 0;
#         }""")
#         await asyncio.sleep(2)
#         current_height = await page.evaluate("document.body.scrollHeight")
#         if current_height == previous_height:
#             break
#         previous_height = current_height
#     print("✅ Arrived at the absolute initial message position frame.")

# async def send_chat_message(page, message_text):
#     print(f"✍️ Submitting compiled string token into chat layout input...")
#     try:
#         chat_box = page.get_by_placeholder("Write a message...")
#         await chat_box.wait_for(timeout=10000)
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
        
#         send_btn = page.locator("button:has-text('Send')")
#         if await send_btn.count() == 0:
#             send_btn = page.locator("button").last
            
#         await send_btn.click()
#         print("🚀 Message pushed successfully to live portal thread!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission layer encountered a selector fault: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None)
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             # Extract Subject Name + Code layout string context
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []

#             # STEP 1: Open Chat Tab
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)

#             # STEP 2: Open Discussion Topics
#             print("🔍 STEP 2: Scanning for the 'Discussion topics' region using the red badge marker layout...")
#             discussion_topics_tab = page.locator("div:has-text('Discussion topics'), button:has-text('Discussion topics'), [class*='Discussion']").last
#             await discussion_topics_tab.click()
#             await asyncio.sleep(5)

#             # STEP 3: Scroll layout thoroughly to map topics
#             print("🔍 STEP 3: Scrolling list thoroughly to map topics via red background banner landmarks...")
#             await trigger_full_page_sensory_scan(page)
            
#             # ✅ FIXED CSS SELECTORS: Separated from raw XPath strings to prevent engine syntax compiler errors
#             topic_locators = page.locator("div.discussion-topics-list a, .discussion-title a, a[href*='topic'], div[style*='background-color'] a")
#             count = await topic_locators.count()
            
#             target_topic_name = None
#             target_element = None

#             print(f"📋 Found {count} total rows. Evaluating from the bottom up to pick the oldest unfinished task...")
#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines[0] # Select header title string token explicitly
                
#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break
#                 else:
#                     print(f"⏭️ Skipping already completed row: '{topic_title}'")

#             if not target_topic_name:
#                 print(f"✨ All visible topics under subject [{subject_code}] have already been processed in complete-interact.json! Exiting.")
#                 # Ensure an empty file write occurs as a confirmation marker layout if complete
#                 save_knowledge_base(knowledge)
#                 await context.close()
#                 await browser.close()
#                 return

#             print(f"🎯 Targeted oldest uncompleted task row: '{target_topic_name}'")
            
#             # Save the title name to JSON memory IMMEDIATELY to lock out concurrent workflows
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             # Click the selected topic card to launch into the discussion forum
#             await target_element.click()
#             await asyncio.sleep(6)

#             # Move browser viewport context up to the absolute genesis of the thread
#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path, full_page=True)
            
#             ai_prompt = (
#                 "Look at the very first message at the top of this chat page layout that started this discussion topic. "
#                 "Read that message question carefully and compose an accurate, high-quality response to it. "
#                 "CRUCIAL RULE: Keep your compiled answer very brief, short, and to the point. No fluff."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
#             print(f"🤖 Compiled Brief Answer Layout Token: '{initial_answer}'")
            
#             if os.path.exists(snap_path):
#                 os.remove(snap_path)

#             # Submit initial response directly to the active chat box
#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await trigger_full_page_sensory_scan(page)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
                        
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame, full_page=True)
                        
#                         followup_prompt = (
#                             f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. "
#                             f"Review this conversation screenshot, locate their specific message, and formulate a precise, brief follow-up response to what they asked."
#                         )
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
                        
#                         await send_chat_message(page, followup_answer)
                        
#                         if os.path.exists(reply_frame):
#                             os.remove(reply_frame)
#                         break
                
#                 await asyncio.sleep(120)

#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#             # Defensive step: Try to write the tracker history file out even on errors
#             try: save_knowledge_base(knowledge)
#             except: pass
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())










# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# KNOWLEDGE_FILE = "complete-interact.json"
# BASE_URL = "https://saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# COOKIE_FILE = "cookies.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     """Loads complete-interact.json from repository storage safely."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     """Writes progress tracking metrics instantly to complete-interact.json."""
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 File updated: Verification logs saved straight to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path:
#         payload["images"] = [image_to_base64(image_path)]
            
#     async with httpx.AsyncClient(timeout=120.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 return response.json().get("response", "").strip()
#         except Exception as e:
#             return f"Error: {e}"
#     return "I do not know."
# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_inner_discussion_panel(page):
#     print("📜 Scrolling inner sidebar panel mapping matrix...")
#     try:
#         feed_panel = page.locator("div[class*='conversation'], div[class*='list'], .chat-sidebar, nav").first
#         if await feed_panel.count() > 0:
#             box = await feed_panel.bounding_box()
#             if box:
#                 await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
#                 for _ in range(4):
#                     await page.mouse.wheel(0, 250)
#                     await asyncio.sleep(1)
#         else:
#             await page.evaluate("window.scrollBy(0, 300);")
#     except Exception as e:
#         print(f"⚠️ Sidebar scroll block note: {e}")
#     await asyncio.sleep(2)

# async def scroll_to_absolute_top_of_chat(page):
#     print("📜 Scrolling up inner conversation container history to locate the first message...")
#     previous_height = 0
#     for attempt in range(25):
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"], main, div[style*="overflow-y"]');
#             if(chatDiv) chatDiv.scrollTop = 0;
#             else window.scrollTo(0, 0);
#         }""")
#         await asyncio.sleep(1.5)
#         current_height = await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"], main');
#             return chatDiv ? chatDiv.scrollHeight : document.body.scrollHeight;
#         }""")
#         if current_height == previous_height:
#             break
#         previous_height = current_height
#     print("✅ Arrived at the absolute initial message position frame.")

# async def send_chat_message(page, message_text):
#     print(f"✍️ Initiating event monitoring input sequence for message...")
#     chat_box = page.get_by_placeholder("Write a message...")
    
#     input_ready = False
#     for attempt in range(1, 11):
#         print(f"📡 [Event Monitor] Verifying chat box input readiness (Try {attempt}/10)...")
#         if await chat_box.is_visible() and await chat_box.is_enabled():
#             input_ready = True
#             break
#         await asyncio.sleep(3)

#     if not input_ready:
#         print("❌ Event Monitor Alert: Input box failed to stabilize after 10 tries. Skipping submission step.")
#         return False

#     try:
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
        
#         send_btn = page.locator("button:has-text('Send')").or_(page.locator("button[type='submit']"))
#         if await send_btn.count() == 0:
#             send_btn = page.locator("button").last
            
#         await send_btn.click()
#         print("🚀 Response successfully sent directly to the chat board!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission layer encountered an unexpected exception: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
        
#         context = await browser.new_context(
#             storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None,
#             viewport={"width": 1920, "height": 1080}
#         )
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint string: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             await page.screenshot(path="step0_landing_page.png")
#             print("📸 Diagnostic Saved: 'step0_landing_page.png' captured.")

#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []
#             knowledge["last_run_timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

#             # STEP 1: Click Chat Tab
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)

#             await page.screenshot(path="step1_clicked_chat.png")
#             print("📸 Diagnostic Saved: 'step1_clicked_chat.png' captured.")

#             # STEP 2: Wait and click Discussion Topics
#             print("🔍 STEP 2: Sensing for the 'Discussion topics' region...")
#             discussion_topics_tab = page.locator("a:has-text('Discussion topics'), button:has-text('Discussion topics'), div:has-text('Discussion topics')").last
            
#             tab_located = False
#             for sensor_try in range(1, 11):
#                 print(f"📡 [Sidebar Sensor] Searching for 'Discussion topics' visibility (Try {sensor_try}/10)...")
#                 if await discussion_topics_tab.is_visible():
#                     tab_located = True
#                     break
#                 await asyncio.sleep(3)

#             if not tab_located:
#                 print("❌ Fatal: Sidebar failed to render 'Discussion topics' block. Saving crash frame.")
#                 await page.screenshot(path="step2_error_sidebar_missing.png")
#                 return

#             await discussion_topics_tab.click(force=True)
#             print("🎯 Successfully navigated into the Discussion Topics list canvas panel!")
#             await asyncio.sleep(6)

#             await page.screenshot(path="step2_clicked_discussion.png")
#             print("📸 Diagnostic Saved: 'step2_clicked_discussion.png' captured.")

#             print("⏳ Holding canvas context for nested item components to initialize...")
#             for load_try in range(5):
#                 list_rows = page.locator("a[href*='topic'], .discussion-list-item a, [class*='topic'] a")
#                 if await list_rows.count() > 0:
#                     print(f"✨ Detected {await list_rows.count()} raw data entries populated inside list container!")
#                     break
#                 await asyncio.sleep(3)

#             await scroll_inner_discussion_panel(page)
            
#             topic_locators = page.locator("a[href*='topic'], [class*='topic'] a, div[style*='background-color'] + div a")
#             count = await topic_locators.count()

#             target_topic_name = None
#             target_element = None

#             print(f"📋 Found {count} total rows. Evaluating from the bottom up to pick the oldest unfinished task...")
#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines[0]
                
#                 if any(x in topic_title for x in ["Discussion topics", "Class conversation", "Chat", "Home", "Dashboard"]):
#                     continue

#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break
#                 else:
#                     print(f"⏭️ Skipping already completed row: '{topic_title}'")

#             if not target_topic_name:
#                 print(f"✨ All visible topics under subject [{subject_code}] have already been processed in complete-interact.json! Exiting.")
#                 save_knowledge_base(knowledge)
#                 await context.close()
#                 await browser.close()
#                 return

#             print("="*60)
#             print(f"📢 WRITING TO FILE & LAUNCHING CHAT: [{target_topic_name}]")
#             print("="*60)

#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             print(f"🖱️ Entering chat forum container room for: {target_topic_name}")
#             await target_element.scroll_into_view_if_needed()
#             await target_element.click(force=True)
#             print("⏳ Awaiting room panel rendering and data stream synchronization...")
#             await asyncio.sleep(8) 

#             await page.screenshot(path="step3_entered_room.png")
#             print("📸 Diagnostic Saved: 'step3_entered_room.png' captured.")

#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path)
            
#             ai_prompt = (
#                 "Look at the very first message at the top of this chat page layout that started this discussion topic. "
#                 "Read that message question carefully and compose an accurate, high-quality response to it. "
#                 "CRUCIAL RULE: Keep your compiled answer very brief, short, and to the point. No fluff."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
#             print(f"🤖 Compiled Brief Answer Layout Token:\n'{initial_answer}'\n")
            
#             if os.path.exists(snap_path):
#                 os.remove(snap_path)

#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await page.evaluate("""() => {
#                     let chatDiv = document.querySelector('.chat-history, .message-list-container, main');
#                     if(chatDiv) chatDiv.scrollTop = chatDiv.scrollHeight;
#                 }""")
#                 await asyncio.sleep(2)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
                        
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame)
                        
#                         followup_prompt = (
#                             f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. "
#                             f"Review this conversation screenshot, locate their specific message, and formulate a precise, brief follow-up response to what they asked."
#                         )
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
                        
#                         await send_chat_message(page, followup_answer)
                        
#                         if os.path.exists(reply_frame):
#                             os.remove(reply_frame)
#                         break
                
#                 await asyncio.sleep(120)

#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#             try: save_knowledge_base(knowledge)
#             except: pass
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())
















# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# KNOWLEDGE_FILE = "complete-interact.json"
# BASE_URL = "https://saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# COOKIE_FILE = "cookies.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 File updated: Logs saved straight to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path and os.path.exists(image_path):
#         try:
#             payload["images"] = [image_to_base64(image_path)]
#         except Exception as e:
#             print(f"⚠️ Image conversion notice: {e}")
            
#     async with httpx.AsyncClient(timeout=300.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 res_text = response.json().get("response", "").strip()
#                 if res_text:
#                     return res_text
#         except Exception as e:
#             return f"SYSTEM_ERROR_SIGNAL: {str(e)}"
#     return "SYSTEM_ERROR_SIGNAL: Blank layout response"

# async def trigger_full_page_sensory_scan(page):
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_inner_discussion_panel(page):
#     try:
#         feed_panel = page.locator("div[class*='conversation'], div[class*='list'], .chat-sidebar, nav").first
#         if await feed_panel.count() > 0:
#             box = await feed_panel.bounding_box()
#             if box:
#                 await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
#                 for _ in range(4):
#                     await page.mouse.wheel(0, 250)
#                     await asyncio.sleep(1)
#         else:
#             await page.evaluate("window.scrollBy(0, 300);")
#     except Exception as e:
#         print(f"⚠️ Sidebar scroll notification: {e}")
#     await asyncio.sleep(2)
# # ✅ FIXED: Replaced standard timeouts with a strict 10-try event monitoring system to ensure the absolute first question registers
# async def scroll_to_absolute_top_of_chat(page):
#     print("📜 STEP 3: Initializing Event Monitor to navigate to the absolute top of the conversation...")
    
#     # Run the event tracking loops up to 10 distinct times
#     for attempt in range(1, 11):
#         # Scan how many message elements currently exist in the layout container
#         initial_msg_count = await page.locator(".message, .chat-item, p, span, div[class*='msg']").count()
#         print(f"📡 [Top Monitor] Scrolling upward (Try {attempt}/10)... Current elements visible: {initial_msg_count}")
        
#         # Drive the inner container view coordinate scrollbars straight to zero index
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"], main, div[style*="overflow-y"]');
#             if(chatDiv) chatDiv.scrollTop = 0;
#             else window.scrollTo(0, 0);
#         }""")
        
#         # Wait a dynamic 3-second buffer check to allow network database segments to sync onto the canvas
#         await asyncio.sleep(3)
        
#         # Scan the post-scroll element count to verify if new older data components loaded into position
#         updated_msg_count = await page.locator(".message, .chat-item, p, span, div[class*='msg']").count()
        
#         # EVENT STATUS MONITOR MATCH CHECK: If the element counts are equal, it confirms the absolute genesis is reached
#         if initial_msg_count == updated_msg_count and attempt > 2:
#             print(f"✅ Event Monitor Confirmed: Top of chat history reached. Total messages populated: {updated_msg_count}")
#             break
            
#     await asyncio.sleep(2)

# async def send_chat_message(page, message_text):
#     if not message_text or any(err in message_text for err in ["SYSTEM_ERROR_SIGNAL", "Error:", "I do not know", "fault", "offline"]):
#         print("🛑 SECURITY FILTER WARNING: Blocked faulty or empty text string payload to protect your profile dashboard!")
#         return False

#     print(f"✍️ Initiating event monitoring input sequence for message submission...")
#     chat_box = page.get_by_placeholder("Write a message...")
    
#     input_ready = False
#     for attempt in range(1, 11):
#         if await chat_box.is_visible() and await chat_box.is_enabled():
#             input_ready = True
#             break
#         await asyncio.sleep(3)

#     if not input_ready:
#         print("❌ Event Monitor Alert: Input container box missed stability windows.")
#         return False

#     try:
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
#         send_btn = page.locator("button:has-text('Send')").or_(page.locator("button[type='submit']"))
#         if await send_btn.count() == 0:
#             send_btn = page.locator("button").last
            
#         await send_btn.click()
#         print("🚀 Response successfully sent directly to the chat board!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission encountered a processing exception: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None, viewport={"width": 1920, "height": 1080})
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint string: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             await page.screenshot(path="step0_landing_page.png")
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []
#             knowledge["last_run_timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

#             # STEP 1: Click Chat Tab
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)
#             await page.screenshot(path="step1_clicked_chat.png")

#             # STEP 2: Open Discussion Topics
#             print("🔍 STEP 2: Sensing for the 'Discussion topics' region...")
#             discussion_topics_tab = page.locator("a:has-text('Discussion topics'), button:has-text('Discussion topics'), div:has-text('Discussion topics')").last
            
#             tab_located = False
#             for sensor_try in range(1, 11):
#                 if await discussion_topics_tab.is_visible():
#                     tab_located = True
#                     break
#                 await asyncio.sleep(3)

#             if not tab_located:
#                 print("❌ Fatal: Sidebar failed to render 'Discussion topics' block.")
#                 await page.screenshot(path="step2_error_sidebar_missing.png")
#                 return

#             await discussion_topics_tab.click(force=True)
#             await asyncio.sleep(6)
#             await page.screenshot(path="step2_clicked_discussion.png")

#             print("⏳ Holding canvas context for nested item components to initialize...")
#             for load_try in range(5):
#                 list_rows = page.locator("a[href*='topic'], .discussion-list-item a, [class*='topic'] a")
#                 if await list_rows.count() > 0: break
#                 await asyncio.sleep(3)

#             await scroll_inner_discussion_panel(page)
#             topic_locators = page.locator("a[href*='topic'], [class*='topic'] a, div[style*='background-color'] + div a")
#             count = await topic_locators.count()

#             target_topic_name = None
#             target_element = None

#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines
#                 if any(x in topic_title for x in ["Discussion topics", "Class conversation", "Chat", "Home", "Dashboard"]): continue

#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break

#             if not target_topic_name:
#                 print("✨ All threads processed.")
#                 save_knowledge_base(knowledge)
#                 return

#             print(f"📢 CLAIMED CHAT: [{target_topic_name}]")
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             await target_element.scroll_into_view_if_needed()
#             await target_element.click(force=True)
#             await asyncio.sleep(8) 
#             await page.screenshot(path="step3_entered_room.png")

#             # ✅ TRIGGER FIX: Run the high-precision event monitoring top loader
#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path)
#             print("📸 Visual snapshot saved: 'genesis_chat_message.png' contains the true initial question.")
            
#             ai_prompt = (
#                 "Look at the very first message at the top of this chat page layout that started this discussion topic. "
#                 "Read that message question carefully and compose an accurate, high-quality response to it. "
#                 "CRUCIAL RULE: Keep your compiled answer very brief, short, and to the point. No fluff."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
            
#             # Text Fallback parsing if image decoding breaks
#             if "SYSTEM_ERROR_SIGNAL" in initial_answer:
#                 print("⚠️ Vision channel timed out on CPU engine layer. Pulling raw markup string elements as fallback...")
#                 try:
#                     first_message_text = await page.locator(".message, .chat-item, p, span, div[class*='content']").first.inner_text()
#                     print(f"📄 Successfully pulled initial question text context: '{first_message_text[:120]}...'")
                    
#                     text_prompt = f"Read this student assignment question carefully: '{first_message_text}'. Compose a high-quality response to it. CRUCIAL RULE: Keep your answer very brief, short, and directly to the point."
#                     initial_answer = await ask_qwen(text_prompt)
#                 except Exception as text_err:
#                     print(f"❌ Fallback text scraper crashed: {text_err}")
            
#             print(f"🤖 Final Verified Answer Token:\n'{initial_answer}'\n")
#             if os.path.exists(snap_path): os.remove(snap_path)

#             # Fire response payload
#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await page.evaluate("""() => {
#                     let chatDiv = document.querySelector('.chat-history, .message-list-container, main');
#                     if(chatDiv) chatDiv.scrollTop = chatDiv.scrollHeight;
#                 }""")
#                 await asyncio.sleep(2)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame)
                        
#                         followup_prompt = f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. Review this conversation context and formulate a precise, brief follow-up response."
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
                        
#                         if "SYSTEM_ERROR_SIGNAL" in followup_answer:
#                             print("⚠️ Vision failed on follow-up. Using text fallback synthesis...")
#                             followup_answer = await ask_qwen(f"Scholar just asked you a question in a class forum thread. Respond to it briefly and professionally. Context: {msg}")
                            
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
#                         await send_chat_message(page, followup_answer)
#                         if os.path.exists(reply_frame): os.remove(reply_frame)
#                         break
                
#                 await asyncio.sleep(120)
#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#             try: save_knowledge_base(knowledge)
#             except: pass
#         finally:
#             await context.close()
#             browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())















# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# KNOWLEDGE_FILE = "complete-interact.json"
# BASE_URL = "https://saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# COOKIE_FILE = "cookies.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# # ✅ FIXED: Strict string extraction to pull ONLY the clean URL string from arguments
# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = str(sys.argv[1])

# def load_knowledge_base():
#     """Loads complete-interact.json from repository storage safely."""
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     """Writes progress tracking metrics instantly to complete-interact.json."""
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 File updated: Logs saved straight to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path and os.path.exists(image_path):
#         try:
#             payload["images"] = [image_to_base64(image_path)]
#         except Exception as e:
#             print(f"⚠️ Image conversion notice: {e}")
            
#     async with httpx.AsyncClient(timeout=300.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 res_text = response.json().get("response", "").strip()
#                 if res_text:
#                     return res_text
#         except Exception as e:
#             return f"SYSTEM_ERROR_SIGNAL: {str(e)}"
#     return "SYSTEM_ERROR_SIGNAL: Blank layout response"
# async def trigger_full_page_sensory_scan(page):
#     """Scrolls down smoothly to trigger lazy-loaded component blocks on heavy pages."""
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_inner_discussion_panel(page):
#     print("📜 Scrolling inner sidebar panel mapping matrix...")
#     try:
#         feed_panel = page.locator("div[class*='conversation'], div[class*='list'], .chat-sidebar, nav").first
#         if await feed_panel.count() > 0:
#             box = await feed_panel.bounding_box()
#             if box:
#                 await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
#                 for _ in range(4):
#                     await page.mouse.wheel(0, 250)
#                     await asyncio.sleep(1)
#         else:
#             await page.evaluate("window.scrollBy(0, 300);")
#     except Exception as e:
#         print(f"⚠️ Sidebar scroll block note: {e}")
#     await asyncio.sleep(2)

# async def scroll_to_absolute_top_of_chat(page):
#     print("CN STEP 3: Initializing Event Monitor to navigate to the absolute top of the conversation...")
#     for attempt in range(1, 11):
#         initial_msg_count = await page.locator(".message, .chat-item, p, span, div[class*='msg']").count()
#         print(f"📡 [Top Monitor] Scrolling upward (Try {attempt}/10)... Current elements visible: {initial_msg_count}")
        
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"], main, div[style*="overflow-y"]');
#             if(chatDiv) chatDiv.scrollTop = 0;
#             else window.scrollTo(0, 0);
#         }""")
#         await asyncio.sleep(3)
#         updated_msg_count = await page.locator(".message, .chat-item, p, span, div[class*='msg']").count()
        
#         if initial_msg_count == updated_msg_count and attempt > 2:
#             print(f"✅ Event Monitor Confirmed: Top of chat history reached. Total messages populated: {updated_msg_count}")
#             break
#     await asyncio.sleep(2)

# async def send_chat_message(page, message_text):
#     if not message_text or any(err in message_text for err in ["SYSTEM_ERROR_SIGNAL", "Error:", "I do not know", "fault", "offline"]):
#         print("🛑 SECURITY FILTER WARNING: Blocked faulty or empty text string payload to protect your profile dashboard!")
#         return False

#     print(f"✍️ Initiating event monitoring input sequence for message submission...")
#     chat_box = page.get_by_placeholder("Write a message...")
    
#     input_ready = False
#     for attempt in range(1, 11):
#         if await chat_box.is_visible() and await chat_box.is_enabled():
#             input_ready = True
#             break
#         await asyncio.sleep(3)

#     if not input_ready:
#         print("❌ Event Monitor Alert: Input container box missed stability windows.")
#         return False

#     try:
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
        
#         # ✅ FIXED: Exact primary chat button targeting to eliminate strict mode overlap crashes
#         send_btn = page.locator("button.btn-primary.faculty-chat-send").or_(page.locator("button:has-text('Send')")).first
#         await send_btn.click()
#         print("🚀 Response successfully sent directly to the chat board!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission encountered a processing exception: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None, viewport={"width": 1920, "height": 1080})
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint string: {TARGET_URL}")
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             await page.screenshot(path="step0_landing_page.png")
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []
#             knowledge["last_run_timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

#             # STEP 1: Open Chat Tab
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)
#             await page.screenshot(path="step1_clicked_chat.png")

#             # STEP 2: Open Discussion Topics
#             print("🔍 STEP 2: Sensing for the 'Discussion topics' region...")
#             discussion_topics_tab = page.locator("a:has-text('Discussion topics'), button:has-text('Discussion topics'), div:has-text('Discussion topics')").last
            
#             tab_located = False
#             for sensor_try in range(1, 11):
#                 if await discussion_topics_tab.is_visible():
#                     tab_located = True
#                     break
#                 await asyncio.sleep(3)

#             if not tab_located:
#                 print("❌ Fatal: Sidebar failed to render 'Discussion topics' block.")
#                 await page.screenshot(path="step2_error_sidebar_missing.png")
#                 return

#             await discussion_topics_tab.click(force=True)
#             await asyncio.sleep(6)
#             await page.screenshot(path="step2_clicked_discussion.png")

#             print("⏳ Holding canvas context for nested item components to initialize...")
#             for load_try in range(5):
#                 list_rows = page.locator("a[href*='topic'], .discussion-list-item a, [class*='topic'] a")
#                 if await list_rows.count() > 0: break
#                 await asyncio.sleep(3)

#             await scroll_inner_discussion_panel(page)
#             topic_locators = page.locator("a[href*='topic'], [class*='topic'] a, div[style*='background-color'] + div a")
#             count = await topic_locators.count()

#             target_topic_name = None
#             target_element = None

#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines
#                 if any(x in topic_title for x in ["Discussion topics", "Class conversation", "Chat", "Home", "Dashboard"]): continue

#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break

#             if not target_topic_name:
#                 print("✨ All threads processed.")
#                 save_knowledge_base(knowledge)
#                 return

#             print(f"📢 CLAIMED CHAT: [{target_topic_name}]")
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             await target_element.scroll_into_view_if_needed()
#             await target_element.click(force=True)
#             await asyncio.sleep(8) 
#             await page.screenshot(path="step3_entered_room.png")

#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path)
#             print("📸 Visual snapshot saved: 'genesis_chat_message.png' contains the true initial question.")
            
#             ai_prompt = (
#                 "Look at the very first message at the top of this chat page layout that started this discussion topic. "
#                 "Read that message question carefully and compose an accurate, high-quality response to it. "
#                 "CRUCIAL RULE: Keep your compiled answer very brief, short, and to the point. No fluff."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
            
#             if "SYSTEM_ERROR_SIGNAL" in initial_answer:
#                 print("⚠️ Vision channel failed. Pulling raw markup string elements as fallback...")
#                 try:
#                     first_message_text = await page.locator(".message, .chat-item, p, span, div[class*='content']").first.inner_text()
#                     print(f"📄 Successfully pulled initial question text context: '{first_message_text[:120]}...'")
#                     text_prompt = f"Read this student assignment question carefully: '{first_message_text}'. Compose a high-quality response to it. CRUCIAL RULE: Keep your answer very brief, short, and directly to the point."
#                     initial_answer = await ask_qwen(text_prompt)
#                 except Exception as text_err:
#                     print(f"❌ Fallback text scraper crashed: {text_err}")
            
#             print(f"🤖 Final Verified Answer Token:\n'{initial_answer}'\n")
#             if os.path.exists(snap_path): os.remove(snap_path)

#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await page.evaluate("""() => {
#                     let chatDiv = document.querySelector('.chat-history, .message-list-container, main');
#                     if(chatDiv) chatDiv.scrollTop = chatDiv.scrollHeight;
#                 }""")
#                 await asyncio.sleep(2)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame)
                        
#                         followup_prompt = f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. Review this conversation context and formulate a precise, brief follow-up response."
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
                        
#                         if "SYSTEM_ERROR_SIGNAL" in followup_answer:
#                             print("⚠️ Vision failed on follow-up. Using text fallback synthesis...")
#                             followup_answer = await ask_qwen(f"Scholar just asked you a question in a class forum thread. Respond to it briefly and professionally. Context: {msg}")
                            
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
#                         await send_chat_message(page, followup_answer)
#                         if os.path.exists(reply_frame): os.remove(reply_frame)
#                         break
                
#                 await asyncio.sleep(120)
#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#             try: save_knowledge_base(knowledge)
#             except: pass
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())










# import asyncio
# import os
# import sys
# import json
# import httpx
# import base64
# import time
# import re
# from playwright.async_api import async_playwright

# KNOWLEDGE_FILE = "complete-interact.json"
# BASE_URL = "https://learner.saveetha.in"
# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "qwen2.5vl:3b"
# COOKIE_FILE = "cookies.json"
# MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

# # ✅ FIXED: Extracts strictly the second command argument slot as a clean text string URL path
# if len(sys.argv) < 2:
#     print("❌ Error: Missing destination URL target input argument.")
#     sys.exit(1)
# TARGET_URL = sys.argv[1]

# def load_knowledge_base():
#     if os.path.exists(KNOWLEDGE_FILE):
#         try:
#             with open(KNOWLEDGE_FILE, 'r') as f:
#                 data = json.load(f)
#                 if "completed_topics" not in data:
#                     data["completed_topics"] = {}
#                 return data
#         except Exception:
#             pass
#     return {"completed_topics": {}}

# def save_knowledge_base(data):
#     with open(KNOWLEDGE_FILE, 'w') as f:
#         json.dump(data, f, indent=2)
#     print(f"💾 File updated: Logs saved straight to '{KNOWLEDGE_FILE}'")

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img:
#         return base64.b64encode(img.read()).decode('utf-8')

# async def ask_qwen(prompt, image_path=None):
#     payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
#     if image_path and os.path.exists(image_path):
#         try:
#             payload["images"] = [image_to_base64(image_path)]
#         except Exception as e:
#             print(f"⚠️ Image conversion notice: {e}")
            
#     async with httpx.AsyncClient(timeout=300.0) as client:
#         try:
#             response = await client.post(OLLAMA_URL, json=payload)
#             if response.status_code == 200:
#                 res_text = response.json().get("response", "").strip()
#                 if res_text:
#                     return res_text
#         except Exception as e:
#             return f"SYSTEM_ERROR_SIGNAL: {str(e)}"
#     return "SYSTEM_ERROR_SIGNAL: Blank layout response"
# async def trigger_full_page_sensory_scan(page):
#     await page.evaluate("""async () => {
#         await new Promise((resolve) => {
#             let totalHeight = 0;
#             let distance = 150;
#             let timer = setInterval(() => {
#                 let scrollHeight = document.body.scrollHeight;
#                 window.scrollBy(0, distance);
#                 totalHeight += distance;
#                 if(totalHeight >= scrollHeight){
#                     clearInterval(timer);
#                     window.scrollTo(0, 0);
#                     resolve();
#                 }
#             }, 40);
#         });
#     }""")
#     await asyncio.sleep(2)

# async def scroll_inner_discussion_panel(page):
#     try:
#         feed_panel = page.locator("div[class*='conversation'], div[class*='list'], .chat-sidebar, nav").first
#         if await feed_panel.count() > 0:
#             box = await feed_panel.bounding_box()
#             if box:
#                 await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
#                 for _ in range(4):
#                     await page.mouse.wheel(0, 250)
#                     await asyncio.sleep(1)
#         else:
#             await page.evaluate("window.scrollBy(0, 300);")
#     except Exception as e:
#         print(f"⚠️ Sidebar scroll notification: {e}")
#     await asyncio.sleep(2)

# async def scroll_to_absolute_top_of_chat(page):
#     print("CN STEP 3: Initializing Event Monitor hunting loop for the official Instructor's question thread...")
#     instructor_located = False
#     for attempt in range(1, 25):
#         instructor_badge = page.locator("span:has-text('Instructor'), div:has-text('Instructor'), [class*='instructor']").first
#         if await instructor_badge.is_visible():
#             print(f"🎯 [Event Monitor] Instructor beacon successfully spotted on target view frame (Try {attempt})!")
#             instructor_located = True
#             break
            
#         print(f"📡 [Top Monitor] Instructor badge not found yet. Scrolling upward... (Try {attempt}/25)")
#         await page.evaluate("""() => {
#             let chatDiv = document.querySelector('.chat-history, .message-list-container, [class*="chat"], main, div[style*="overflow-y"]');
#             if(chatDiv) chatDiv.scrollTop -= 400;
#             else window.scrollBy(0, -400);
#         }""")
#         await asyncio.sleep(2.5)

#     if not instructor_located:
#         print("⚠️ Warning: Could not locate 'Instructor' tag. Defaulting to fallback top position.")
#         await page.evaluate("window.scrollTo(0, 0);")
#     await asyncio.sleep(2)

# async def send_chat_message(page, message_text):
#     if not message_text or any(err in message_text for err in ["SYSTEM_ERROR_SIGNAL", "Error:", "I do not know", "fault", "offline"]):
#         print("🛑 SECURITY FILTER WARNING: Blocked faulty text string payload to protect your profile dashboard!")
#         return False

#     print(f"✍️ Initiating event monitoring input sequence for message submission...")
#     chat_box = page.get_by_placeholder("Write a message...")
    
#     input_ready = False
#     for attempt in range(1, 11):
#         if await chat_box.is_visible() and await chat_box.is_enabled():
#             input_ready = True
#             break
#         await asyncio.sleep(3)

#     if not input_ready:
#         print("❌ Event Monitor Alert: Input container box missed stability windows.")
#         return False

#     try:
#         await chat_box.fill(message_text)
#         await asyncio.sleep(1)
#         send_btn = page.locator("button.btn-primary.faculty-chat-send").or_(page.locator("button:has-text('Send')")).first
#         await send_btn.click()
#         print("🚀 Response successfully sent directly to the chat board!")
#         return True
#     except Exception as e:
#         print(f"❌ Submission encountered a processing exception: {e}")
#         return False
# async def run_ai_automation():
#     knowledge = load_knowledge_base()
#     start_time = time.time()
#     two_hours_in_seconds = 2 * 60 * 60

#     print("🚀 Booting sandbox-compliant cloud worker matrix...")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
#         )
#         context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None, viewport={"width": 1920, "height": 1080})
#         page = await context.new_page()
#         await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

#         try:
#             print(f"🌐 Accessing target endpoint string: {TARGET_URL}")
#             # ✅ FIXED: Now cleanly loads the targeted string variable without array syntax contamination
#             await page.goto(TARGET_URL, timeout=60000, wait_until="load")
#             await asyncio.sleep(5)

#             await page.screenshot(path="step0_landing_page.png")
#             subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
#             subject_header = subject_header.strip().replace('\n', ' ')
#             match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
#             subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
#             print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

#             if subject_code not in knowledge["completed_topics"]:
#                 knowledge["completed_topics"][subject_code] = []
#             knowledge["last_run_timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

#             # STEP 1: Click Chat Tab
#             print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
#             chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
#             await chat_tab.wait_for(timeout=15000)
#             await chat_tab.click()
#             await asyncio.sleep(5)
#             await page.screenshot(path="step1_clicked_chat.png")

#             # STEP 2: Open Discussion Topics
#             print("🔍 STEP 2: Sensing for the 'Discussion topics' region...")
#             discussion_topics_tab = page.locator("a:has-text('Discussion topics'), button:has-text('Discussion topics'), div:has-text('Discussion topics')").last
            
#             tab_located = False
#             for sensor_try in range(1, 11):
#                 if await discussion_topics_tab.is_visible():
#                     tab_located = True
#                     break
#                 await asyncio.sleep(3)

#             if not tab_located:
#                 print("❌ Fatal: Sidebar failed to render 'Discussion topics' block.")
#                 return

#             await discussion_topics_tab.click(force=True)
#             await asyncio.sleep(6)
#             await page.screenshot(path="step2_clicked_discussion.png")

#             print("⏳ Holding canvas context for nested item components to initialize...")
#             for load_try in range(5):
#                 list_rows = page.locator("a[href*='topic'], .discussion-list-item a, [class*='topic'] a")
#                 if await list_rows.count() > 0: break
#                 await asyncio.sleep(3)

#             await scroll_inner_discussion_panel(page)
#             topic_locators = page.locator("a[href*='topic'], [class*='topic'] a, div[style*='background-color'] + div a")
#             count = await topic_locators.count()

#             target_topic_name = None
#             target_element = None

#             for i in range(count - 1, -1, -1):
#                 raw_text = await topic_locators.nth(i).inner_text()
#                 lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
#                 if not lines: continue
#                 topic_title = lines
#                 if any(x in topic_title for x in ["Discussion topics", "Class conversation", "Chat", "Home", "Dashboard"]): continue

#                 if topic_title not in knowledge["completed_topics"][subject_code]:
#                     target_topic_name = topic_title
#                     target_element = topic_locators.nth(i)
#                     break

#             if not target_topic_name:
#                 print("✨ All threads processed.")
#                 save_knowledge_base(knowledge)
#                 return

#             print(f"📢 CLAIMED CHAT: [{target_topic_name}]")
#             knowledge["completed_topics"][subject_code].append(target_topic_name)
#             save_knowledge_base(knowledge)

#             await target_element.scroll_into_view_if_needed()
#             await target_element.click(force=True)
#             await asyncio.sleep(8) 
#             await page.screenshot(path="step3_entered_room.png")

#             await scroll_to_absolute_top_of_chat(page)
            
#             snap_path = "genesis_chat_message.png"
#             await page.screenshot(path=snap_path)
            
#             ai_prompt = (
#                 "Review this classroom discussion chat. Locate the message box that belongs to the 'Instructor'. "
#                 "Read the question or prompt asked by the Instructor carefully. "
#                 "Compose an accurate, brief response answering that question. "
#                 "CRUCIAL RULE: Write your response in a natural, friendly, human tone, like an elite student explaining a concept to a peer. Do not sound robotic."
#             )
#             initial_answer = await ask_qwen(ai_prompt, snap_path)
            
#             if "SYSTEM_ERROR_SIGNAL" in initial_answer or "incomplete" in initial_answer:
#                 print("⚠️ Vision failed. Using text fallback parsing matching Instructor elements...")
#                 try:
#                     instructor_msg_bubble = page.locator("div:has(span:has-text('Instructor')) + div, div:has-text('Instructor') ~ p, .instructor-message").first
#                     first_message_text = await instructor_msg_bubble.inner_text()
#                     print(f"📄 Pulled instructor text: '{first_message_text[:120]}...'")
                    
#                     text_prompt = (
#                         f"Read this instructor's question carefully: '{first_message_text}'. "
#                         "Compose a high-quality answer to it. CRUCIAL RULE: Keep your response brief, highly accurate, "
#                         "and write it in a natural, conversational, human tone like a real student."
#                     )
#                     initial_answer = await ask_qwen(text_prompt)
#                 except Exception as text_err:
#                     print(f"❌ Fallback text scraper crashed: {text_err}")
            
#             print(f"🤖 Final Verified Answer Token:\n'{initial_answer}'\n")
#             if os.path.exists(snap_path): os.remove(snap_path)

#             await send_chat_message(page, initial_answer)

#             # --- TWO-HOUR STANDBY MONITORING PHASE ---
#             print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
#             monitor_start_time = time.time()

#             while (time.time() - monitor_start_time) < two_hours_in_seconds:
#                 remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
#                 print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
#                 await page.evaluate("""() => {
#                     let chatDiv = document.querySelector('.chat-history, .message-list-container, main');
#                     if(chatDiv) chatDiv.scrollTop = chatDiv.scrollHeight;
#                 }""")
#                 await asyncio.sleep(2)
                
#                 messages_data = await page.evaluate("""() => {
#                     return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
#                         .map(el => el.innerText)
#                         .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
#                 }""")
                
#                 for msg in messages_data:
#                     if MY_IDENTITY_NAME in msg:
#                         print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
#                         reply_frame = "target_reply_context.png"
#                         await page.screenshot(path=reply_frame)
                        
#                         followup_prompt = f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. Review this conversation context and formulate a precise, brief follow-up response in a conversational human tone."
#                         followup_answer = await ask_qwen(followup_prompt, reply_frame)
                        
#                         if "SYSTEM_ERROR_SIGNAL" in followup_answer:
#                             followup_answer = await ask_qwen(f"Scholar just asked you a question in a class forum thread. Respond to it briefly, professionally, and in a human tone. Context: {msg}")
                            
#                         print(f"🤖 Formulated Followup Response: '{followup_answer}'")
#                         await send_chat_message(page, followup_answer)
#                         if os.path.exists(reply_frame): os.remove(reply_frame)
#                         break
                
#                 await asyncio.sleep(120)
#             print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

#         except Exception as e:
#             print(f"❌ Automation workflow run encountered an exception: {e}")
#             try: save_knowledge_base(knowledge)
#             except: pass
#         finally:
#             await context.close()
#             await browser.close()

# if __name__ == "__main__":
#     asyncio.run(run_ai_automation())





import asyncio
import os
import sys
import json
import httpx
import base64
import time
import re
from playwright.async_api import async_playwright

KNOWLEDGE_FILE = "complete-interact.json"
BASE_URL = "https://learner.saveetha.in"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:3b"
COOKIE_FILE = "cookies.json"
MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

if len(sys.argv) < 2:
    print("❌ Error: Missing destination URL target input argument.")
    sys.exit(1)
TARGET_URL = sys.argv[1]

def load_knowledge_base():
    if os.path.exists(KNOWLEDGE_FILE):
        try:
            with open(KNOWLEDGE_FILE, 'r') as f:
                data = json.load(f)
                if "completed_topics" not in data:
                    data["completed_topics"] = {}
                return data
        except Exception:
            pass
    return {"completed_topics": {}}

def save_knowledge_base(data):
    with open(KNOWLEDGE_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"💾 File updated: Logs saved straight to '{KNOWLEDGE_FILE}'")

def image_to_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode('utf-8')

async def ask_qwen(prompt, image_path=None):
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    if image_path and os.path.exists(image_path):
        try:
            payload["images"] = [image_to_base64(image_path)]
        except Exception as e:
            print(f"⚠️ Image conversion notice: {e}")
            
    async with httpx.AsyncClient(timeout=300.0) as client:
        try:
            response = await client.post(OLLAMA_URL, json=payload)
            if response.status_code == 200:
                res_text = response.json().get("response", "").strip()
                if res_text:
                    return res_text
        except Exception as e:
            return f"SYSTEM_ERROR_SIGNAL: {str(e)}"
    return "SYSTEM_ERROR_SIGNAL: Blank layout response"
async def trigger_full_page_sensory_scan(page):
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
                    window.scrollTo(0, 0);
                    resolve();
                }
            }, 40);
        });
    }""")
    await asyncio.sleep(2)

async def scroll_inner_discussion_panel(page):
    try:
        feed_panel = page.locator("div[class*='conversation'], div[class*='list'], .chat-sidebar, nav").first
        if await feed_panel.count() > 0:
            box = await feed_panel.bounding_box()
            if box:
                await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                for _ in range(4):
                    await page.mouse.wheel(0, 250)
                    await asyncio.sleep(1)
        else:
            await page.evaluate("window.scrollBy(0, 300);")
    except Exception as e:
        print(f"⚠️ Sidebar scroll notification: {e}")
    await asyncio.sleep(2)

# ✅ UPGRADED: Implements continuous environmental monitoring, physical-interaction scrolling, and lazy-load stabilizers
async def scroll_to_absolute_top_of_chat(page):
    print("📜 STEP 3: Activating Interactive Touch Scroller. Hunting for Instructor thread endpoint...")
    
    # 1. Target the actual chat panel workspace container bounding region box
    chat_panel = page.locator(".chat-history, .message-list-container, main, [class*='chat-content']").first
    await chat_panel.wait_for(timeout=10000)
    box = await chat_panel.bounding_box()
    
    if box:
        # Position the mouse pointer right in the middle of the chat area to engage interactive physical focus
        await page.mouse.move(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
        await page.mouse.click(box["x"] + box["width"]/2, box["y"] + box["height"]/2)
    
    # 2. Continuous scrolling loop block
    for step in range(1, 150):
        # Scan if an Instructor badge element is actively visible on-screen right now
        instructor_badge = page.locator("span:has-text('Instructor'), div:has-text('Instructor'), .instructor").first
        if await instructor_badge.is_visible():
            print(f"🎯 [Touch Scroller] Instructor question node successfully brought into viewport frame (Step {step})!")
            break
            
        # 🚨 LAZY-LOAD DETECTOR: Check if the interface is streaming or shows loading elements
        is_loading = await page.evaluate("""() => {
            const text = document.body.innerText.toLowerCase();
            return text.includes("loading") || text.includes("load previous") || !!document.querySelector('.spinner, .loading-indicator');
        }""")
        
        if is_loading:
            print("⏳ [Sensor Notice] Chat stream lazy-load activity detected. Holding scrolling thread to let rows stabilize...")
            await asyncio.sleep(3) # Pause 3 seconds to clear buffer network delays
            continue
            
        # Simulate an incremental physical scroll wheel action upward
        await page.mouse.wheel(0, -180)
        await asyncio.sleep(0.4) # Fast but orderly interval step speed

    await asyncio.sleep(2)

async def send_chat_message(page, message_text):
    if not message_text or any(err in message_text for err in ["SYSTEM_ERROR_SIGNAL", "Error:", "I do not know", "fault", "offline"]):
        print("🛑 SECURITY FILTER WARNING: Blocked faulty or empty text string payload to protect your profile dashboard!")
        return False

    print(f"✍️ Initiating event monitoring input sequence for message submission...")
    chat_box = page.get_by_placeholder("Write a message...")
    
    input_ready = False
    for attempt in range(1, 11):
        if await chat_box.is_visible() and await chat_box.is_enabled():
            input_ready = True
            break
        await asyncio.sleep(3)

    if not input_ready:
        print("❌ Event Monitor Alert: Input container box missed stability windows.")
        return False

    try:
        await chat_box.fill(message_text)
        await asyncio.sleep(1)
        send_btn = page.locator("button.btn-primary.faculty-chat-send").or_(page.locator("button:has-text('Send')")).first
        await send_btn.click()
        print("🚀 Response successfully sent directly to the chat board!")
        return True
    except Exception as e:
        print(f"❌ Submission encountered a processing exception: {e}")
        return False
async def run_ai_automation():
    knowledge = load_knowledge_base()
    start_time = time.time()
    two_hours_in_seconds = 2 * 60 * 60

    print("🚀 Booting sandbox-compliant cloud worker matrix...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
        )
        context = await browser.new_context(storage_state=COOKIE_FILE if os.path.exists(COOKIE_FILE) else None, viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font"] else route.continue_())

        try:
            print(f"🌐 Accessing target endpoint string: {TARGET_URL}")
            await page.goto(TARGET_URL, timeout=60000, wait_until="load")
            await asyncio.sleep(5)

            await page.screenshot(path="step0_landing_page.png")
            subject_header = await page.locator("h1, h2, .subject-title").first.inner_text()
            subject_header = subject_header.strip().replace('\n', ' ')
            match = re.search(r'([0-9]{2}[A-Z]{2}[0-9]{3})', subject_header)
            subject_code = match.group(1) if match else "UNKNOWN_SUBJECT"
            print(f"📚 Subject Identity Mapped: Code Key -> [{subject_code}]")

            if subject_code not in knowledge["completed_topics"]:
                knowledge["completed_topics"][subject_code] = []
            knowledge["last_run_timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

            # STEP 1: Click Chat Tab
            print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
            chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
            await chat_tab.wait_for(timeout=15000)
            await chat_tab.click()
            await asyncio.sleep(5)
            await page.screenshot(path="step1_clicked_chat.png")

            # STEP 2: Open Discussion Topics
            print("🔍 STEP 2: Sensing for the 'Discussion topics' region...")
            discussion_topics_tab = page.locator("a:has-text('Discussion topics'), button:has-text('Discussion topics'), div:has-text('Discussion topics')").last
            
            tab_located = False
            for sensor_try in range(1, 11):
                if await discussion_topics_tab.is_visible():
                    tab_located = True
                    break
                await asyncio.sleep(3)

            if not tab_located:
                print("❌ Fatal: Sidebar failed to render 'Discussion topics' block.")
                return

            await discussion_topics_tab.click(force=True)
            await asyncio.sleep(6)
            await page.screenshot(path="step2_clicked_discussion.png")

            print("⏳ Holding canvas context for nested item components to initialize...")
            for load_try in range(5):
                list_rows = page.locator("a[href*='topic'], .discussion-list-item a, [class*='topic'] a")
                if await list_rows.count() > 0: break
                await asyncio.sleep(3)

            await scroll_inner_discussion_panel(page)
            topic_locators = page.locator("a[href*='topic'], [class*='topic'] a, div[style*='background-color'] + div a")
            count = await topic_locators.count()

            target_topic_name = None
            target_element = None

            for i in range(count - 1, -1, -1):
                raw_text = await topic_locators.nth(i).inner_text()
                lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
                if not lines: continue
                topic_title = lines
                if any(x in topic_title for x in ["Discussion topics", "Class conversation", "Chat", "Home", "Dashboard"]): continue

                if topic_title not in knowledge["completed_topics"][subject_code]:
                    target_topic_name = topic_title
                    target_element = topic_locators.nth(i)
                    break

            if not target_topic_name:
                print("✨ All threads processed.")
                save_knowledge_base(knowledge)
                return

            print(f"📢 CLAIMED CHAT: [{target_topic_name}]")
            knowledge["completed_topics"][subject_code].append(target_topic_name)
            save_knowledge_base(knowledge)

            await target_element.scroll_into_view_if_needed()
            await target_element.click(force=True)
            await asyncio.sleep(8) 
            await page.screenshot(path="step3_entered_room.png")

            # ✅ TRIGGER INTERACTIVE TOUCH HUNT: Run the physical-interaction mouse wheel upward sequence
            await scroll_to_absolute_top_of_chat(page)
            
            snap_path = "genesis_chat_message.png"
            await page.screenshot(path=snap_path)
            print("📸 Visual snapshot saved: 'genesis_chat_message.png' contains the true instructor post layout.")
            
            ai_prompt = (
                "Review this classroom discussion chat. Locate the message box that belongs to the 'Instructor'. "
                "Read the question or prompt asked by the Instructor carefully. "
                "Compose an accurate, brief response answering that question. "
                "CRUCIAL RULE: Write your response in a natural, friendly, human tone, like an elite student explaining a concept to a peer. Do not sound robotic."
            )
            initial_answer = await ask_qwen(ai_prompt, snap_path)
            
            if "SYSTEM_ERROR_SIGNAL" in initial_answer or "incomplete" in initial_answer:
                print("⚠️ Vision channel missed target boundary fields. Pulling raw markup text...")
                try:
                    instructor_msg_bubble = page.locator("div:has(span:has-text('Instructor')) + div, div:has-text('Instructor') ~ p, .instructor-message").first
                    first_message_text = await instructor_msg_bubble.inner_text()
                    print(f"📄 Successfully pulled instructor prompt text context: '{first_message_text[:120]}...'")
                    
                    text_prompt = (
                        f"Read this instructor's question carefully: '{first_message_text}'. "
                        "Compose a high-quality answer to it. CRUCIAL RULE: Keep your response brief, highly accurate, "
                        "and write it in a natural, conversational, human tone like a real student."
                    )
                    initial_answer = await ask_qwen(text_prompt)
                except Exception as text_err:
                    print(f"❌ Fallback text scraper crashed: {text_err}")
            
            print(f"🤖 Final Verified Answer Token:\n'{initial_answer}'\n")
            if os.path.exists(snap_path): os.remove(snap_path)

            await send_chat_message(page, initial_answer)

            # --- TWO-HOUR STANDBY MONITORING PHASE ---
            print(f"⏳ Entering 2-Hour Standby Verification phase looking for 'Scholar' tagging updates...")
            monitor_start_time = time.time()

            while (time.time() - monitor_start_time) < two_hours_in_seconds:
                remaining_minutes = (two_hours_in_seconds - (time.time() - monitor_start_time)) / 60
                print(f"🔄 Checking chat landscape updates... ({remaining_minutes:.1f} minutes remaining)")
                
                await page.evaluate("""() => {
                    let chatDiv = document.querySelector('.chat-history, .message-list-container, main');
                    if(chatDiv) chatDiv.scrollTop = chatDiv.scrollHeight;
                }""")
                await asyncio.sleep(2)
                
                messages_data = await page.evaluate("""() => {
                    return Array.from(document.querySelectorAll('.message, .chat-item, p, span'))
                        .map(el => el.innerText)
                        .filter(txt => txt.includes('Scholar') || txt.includes('scholar'));
                }""")
                
                for msg in messages_data:
                    if MY_IDENTITY_NAME in msg:
                        print(f"🎯 Match Registered! 'Scholar' explicitly addressed identity tag context: '{MY_IDENTITY_NAME}'")
                        reply_frame = "target_reply_context.png"
                        await page.screenshot(path=reply_frame)
                        
                        followup_prompt = f"A chat member named Scholar has replied directly to you, explicitly mentioning your name '{MY_IDENTITY_NAME}'. Review this conversation context and formulate a precise, brief follow-up response in a conversational human tone."
                        followup_answer = await ask_qwen(followup_prompt, reply_frame)
                        
                        if "SYSTEM_ERROR_SIGNAL" in followup_answer:
                            followup_answer = await ask_qwen(f"Scholar just asked you a question in a class forum thread. Respond to it briefly, professionally, and in a human tone. Context: {msg}")
                            
                        print(f"🤖 Formulated Followup Response: '{followup_answer}'")
                        await send_chat_message(page, followup_answer)
                        if os.path.exists(reply_frame): os.remove(reply_frame)
                        break
                
                await asyncio.sleep(120)
            print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

        except Exception as e:
            print(f"❌ Automation workflow run encountered an exception: {e}")
            try: save_knowledge_base(knowledge)
            except: pass
        finally:
            await context.close()
            await browser.close()

if __name__ == "__main__":
        asyncio.run(run_ai_automation())
