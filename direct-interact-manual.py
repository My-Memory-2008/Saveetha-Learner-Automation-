
import asyncio
import os
import sys
import json
import httpx
import base64
import time
import re
from playwright.async_api import async_playwright

BASE_URL = "https://saveetha.in"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5vl:3b"
COOKIE_FILE = "cookies.json"
MY_IDENTITY_NAME = "MUHAMMAD ASJAD E"

if len(sys.argv) < 2:
    print("❌ Error: Missing destination URL target input argument.")
    sys.exit(1)

RAW_ARGS_STRING = " ".join(sys.argv[1:])
URL_MATCH = re.search(r'(https?://[^\s\'"\]]+)', RAW_ARGS_STRING)
TARGET_URL = URL_MATCH.group(1).strip() if URL_MATCH else str(sys.argv[-1]).strip("[]'\", ")
print(f"🎯 Sanitized Target URL Path Token: '{TARGET_URL}'")

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

async def send_chat_message(page, message_text):
    if not message_text or any(err in message_text for err in ["SYSTEM_ERROR_SIGNAL", "Error:", "I do not know", "fault", "offline"]):
        print("🛑 SECURITY FILTER WARNING: Blocked faulty text payload.")
        return False

    print(f"✍️ Initiating input sequence for message submission...")
    chat_box = page.get_by_placeholder("Write a message...")
    
    if await chat_box.is_visible() and await chat_box.is_enabled():
        await chat_box.fill(message_text)
        send_btn = page.locator("button.btn-primary.faculty-chat-send").or_(page.locator("button:has-text('Send')")).first
        await send_btn.click()
        print("🚀 Response successfully sent directly to the chat board!")
        return True
    return False

async def capture_instructor_question_via_api(page, target_element, preview_card_question):
    print("📡 STEP 3: Initializing Network API Interceptor...")
    captured_payloads = []

    async def handle_response(response):
        url = response.url.lower()
        if any(kw in url for kw in ["chat", "message", "topic", "discussion", "get_messages", "vhtcx"]):
            try:
                text_content = await response.text()
                if text_content and ("instructor" in text_content or "msg" in text_content or "[" in text_content):
                    captured_payloads.append(text_content)
            except:
                pass

    page.on("response", handle_response)
    await target_element.scroll_into_view_if_needed()
    await target_element.click(force=True)
    await asyncio.sleep(8) 
    page.remove_listener("response", handle_response)
    
    instructor_prompt = None

    for raw_data in captured_payloads:
        try:
            parsed_json = json.loads(raw_data)
            messages_list = []
            if isinstance(parsed_json, list): messages_list = parsed_json
            elif isinstance(parsed_json, dict):
                for key, val in parsed_json.items():
                    if isinstance(val, list): messages_list = val; break
            
            if messages_list:
                for candidate in messages_list:
                    cand_str = str(candidate).lower()
                    if ("instructor" in cand_str or "dinesh" in cand_str) and not any(x in cand_str for x in ["scales better", "that's correct", "by observing"]):
                        if isinstance(candidate, dict):
                            for text_prop in ["message", "content", "msg_text", "text", "body"]:
                                if text_prop in candidate and len(str(candidate[text_prop])) > 15:
                                    instructor_prompt = str(candidate[text_prop])
                                    break
                        if instructor_prompt: break
                if instructor_prompt: break
        except:
            match = re.search(r'(?:instructor|dinesh)[^}]+(?:message|content|text)["\']:\s*["\']([^"\']{15,})', raw_data, re.IGNORECASE)
            if match: instructor_prompt = match.group(1); break

    if not instructor_prompt:
        print("⚠️ API payloads empty. Running DOM backup scan...")
        instructor_prompt = await page.evaluate("""() => {
            const bubbles = Array.from(document.querySelectorAll('div, li, [class*="message"]'));
            for (let b of bubbles) {
                if (b.innerText && b.innerText.includes("Instructor")) {
                    const paragraphs = Array.from(b.querySelectorAll('p, [class*="text"], [class*="content"]'));
                    for(let p of paragraphs) {
                        const txt = p.innerText.trim();
                        if(txt.length > 15 && !txt.includes("Instructor") && !txt.includes("scales better")) return txt;
                    }
                }
            }
            return null;
        }""")

    if not instructor_prompt or len(instructor_prompt) < 5 or "Back to Subjects" in instructor_prompt:
        print("🚨 Activating Card Memory Fallback: Using question extracted from list view...")
        instructor_prompt = preview_card_question

    print("\n" + "❓" * 30)
    print(f"🎯 CLEAN ISOLATED INSTRUCTOR QUESTION:\n'{instructor_prompt}'")
    print("❓" * 30 + "\n")
    return instructor_prompt
async def run_ai_automation():
    two_hours_in_seconds = 2 * 60 * 60

    print("🚀 Booting sandbox-compliant cloud worker matrix...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--disable-gpu"])
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

            print("🎯 STEP 1: Locating and opening Chat Tab channel layout blocks...")
            chat_tab = page.locator("a:has-text('Chat')").or_(page.locator("button:has-text('Chat')")).first
            await chat_tab.wait_for(timeout=15000)
            await chat_tab.click()
            await asyncio.sleep(5)
            await page.screenshot(path="step1_clicked_chat.png")

            print("🔍 STEP 2: Sensing for the 'Discussion topics' region...")
            discussion_topics_tab = page.locator("a:has-text('Discussion topics'), button:has-text('Discussion topics'), div:has-text('Discussion topics')").last
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

                # ✅ MANUAL BYPASS: Targets the first valid chat room instantly without checking historical arrays
                target_topic_name = topic_title
                target_element = topic_locators.nth(i)
                break

            if not target_topic_name:
                print("❌ Error: No valid interaction threads found inside current active layout view room.")
                return

            print(f"📝 Extracting topic preview metadata details for node: [{target_topic_name}]")
            card_raw_text = await target_element.inner_text()
            card_text_clean = " ".join([l.strip() for l in card_raw_text.split("\n") if l.strip()])
            print(f"💾 Card View Title Saved to Memory: '{card_text_clean[:120]}...'")

            print(f"📢 CLAIMED CHAT: [{target_topic_name}]")
            await page.screenshot(path="step3_entered_room.png")
            instructor_prompt_string = await capture_instructor_question_via_api(page, target_element, card_text_clean)
            snap_path = "genesis_chat_message.png"
            await page.screenshot(path=snap_path)
            
            ai_prompt = (
                f"The Instructor asked this exact technical assignment question: '{instructor_prompt_string}'. "
                "Compose an accurate, high-quality solution explaining this concept comprehensively. "
                "STRICT PRESENTATION RULES:\n"
                "1. Output your answer directly starting with the technical explanation text. \n"
                "2. Do NOT include greetings (like hello, hey), prefaces, or meta-commentary text blocks.\n"
                "3. Write the response in a confident, conversational, natural human tone, exactly like an elite student."
            )
            initial_answer = await ask_qwen(ai_prompt, snap_path)
            
            if "SYSTEM_ERROR_SIGNAL" in initial_answer or len(initial_answer) < 5:
                print("⚠️ Vision failed on prompt engine. Requesting fallback text compilation...")
                text_prompt = (
                    f"Answer this technical question carefully: '{instructor_prompt_string}'. "
                    "STRICT RULE: Output only the explanation directly. Do not include greetings or prefaces. Use a conversational human tone."
                )
                initial_answer = await ask_qwen(text_prompt)
            
            print(f"🤖 Final Direct Answer Token:\n'{initial_answer}'\n")
            if os.path.exists(snap_path): os.remove(snap_path)

            await send_chat_message(page, initial_answer)

            # --- QUESTION-FOCUSED SURVEILLANCE ENGINE LOOP ---
            print("⏳ Entering Python-Native Speaker-Identity Sentinel Loop. Monitoring Scholar...")
            monitor_start_time = time.time()
            processed_scholar_signatures = set()
            last_logged_minute = -1

            while (time.time() - monitor_start_time) < two_hours_in_seconds:
                current_elapsed = time.time() - monitor_start_time
                remaining_minutes = (two_hours_in_seconds - current_elapsed) / 60
                current_minute_floor = int(remaining_minutes)
                
                if current_minute_floor % 5 == 0 and current_minute_floor != last_logged_minute:
                    print(f"🔄 Surveillance Engine Status Ticker: {remaining_minutes:.1f} minutes remaining...")
                    last_logged_minute = current_minute_floor

                try:
                    await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
                except:
                    pass
                await asyncio.sleep(2)
                
                messages_data = []
                try:
                    elements_loc = page.locator(".message, .chat-item, li, div[class*='msg'], div[class*='content']")
                    loc_count = await elements_loc.count()
                    for idx in range(max(0, loc_count - 20), loc_count):
                        loc = elements_loc.nth(idx)
                        if await loc.is_visible():
                            txt = (await loc.inner_text()).strip()
                            if txt and ("Scholar" in txt or "scholar" in txt):
                                messages_data.append(txt)
                except:
                    pass
                
                for msg in messages_data:
                    if not msg or any(x in msg for x in ["Student", "MUHAMMAD ASJAD", "Thank you, Scholar!", "I appreciate your guidance"]):
                        continue
                        
                    msg_sig = "".join(msg.split())[-60:]
                    
                    if msg_sig not in processed_scholar_signatures and any(keyword in msg.lower() for keyword in ["scholar", "teaching assistant"]):
                        print("\n" + "🚨" * 30)
                        print(f"🎯 SENTINEL INTERCEPT: Scholar published a fresh feedback question block!\nPayload text content:\n'{msg[:200]}...'")
                        
                        processed_scholar_signatures.add(msg_sig)
                        reply_frame = "target_reply_context.png"
                        await page.screenshot(path=reply_frame)
                        
                        followup_prompt = (
                            f"An AI Teaching Assistant named Scholar has just reviewed your submission and asked you this specific follow-up question or assignment task: '{msg}'. "
                            f"Isolate the question or code table they are asking for and solve it completely with full accurate details. "
                            f"STRICT PRESENTATION RULES:\n"
                            f"1. Output your answer directly starting with the technical explanation, solution data, or drafted checklist table requested. \n"
                            f"2. Do NOT include polite acknowledgments, thank-you sentences, greetings, or introductory prefaces.\n"
                            f"3. Write the response in a confident, professional, highly advanced technical human student tone."
                        )
                        followup_answer = await ask_qwen(followup_prompt, reply_frame)
                        
                        if "SYSTEM_ERROR_SIGNAL" in followup_answer or len(followup_answer) < 5:
                            print("⚠️ Vision channel busy. Processing high-speed textual synthesis fallback...")
                            fallback_prompt = (
                                f"An AI Assistant named Scholar just submitted a question on your board: '{msg}'. "
                                f"Provide the direct technical answer, solution, or required matrix data to answer their question completely. Output only the answer text directly with no greetings or prefaces."
                            )
                            followup_answer = await ask_qwen(fallback_prompt)
                            
                        print(f"🤖 Formulated Technical Solution Response:\n'{followup_answer}'\n")
                        await send_chat_message(page, followup_answer)
                        if os.path.exists(reply_frame): os.remove(reply_frame)
                        
                        asyncio.create_task(context.storage_state(path=COOKIE_FILE))
                        break 

            print("🏁 Finished 2-Hour continuous discussion tracker sequence step successfully.")

        except Exception as e:
            print(f"❌ Automation workflow run encountered an exception: {e}")
        finally:
            await context.close()
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run_ai_automation())
