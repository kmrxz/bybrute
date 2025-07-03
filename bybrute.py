# noqa: W605
import time
import random
import sys
import os
import requests

# ANSI Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Title Art
print(f"""{CYAN}

  ____          ____  ____  _   _ _____ _____ 
 | __ ) _   _  | __ )|  _ \| | | |_   _| ____|
 |  _ \| | | | |  _ \| |_) | | | | | | |  _|  
 | |_) | |_| | | |_) |  _ <| |_| | | | | |___ 
 |____/ \__, | |____/|_| \_\ ___/  |_| |_____|.PRO
        |___/                                 
                                   {RED}v:9.83
                             
""" + RESET)
print(GREEN + "AUROMATION TOOL FOR INSTAGRAM" + RESET)

def type_with_typos(text, typo_rate=0.07, delay_range=(0.01, 0.04)):
    for char in text:
        if random.random() < typo_rate and char.isalpha():
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            sys.stdout.write(wrong_char)
            sys.stdout.flush()
            time.sleep(random.uniform(0.05, 0.1))
            sys.stdout.write('\b \b')  # simulate backspace
            sys.stdout.flush()
            time.sleep(random.uniform(0.03, 0.08))
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(*delay_range))
    print()

disclaimer = f"""{GREEN}
[{RED}!{GREEN}]{RED} LEGAL NOTICE:
{YELLOW}This tool is strictly for educational and ethical use.
Designed to identify weak passwords and strengthen your security posture.
Any misuse is your own responsibility.
The developer {RED}does not condone{YELLOW} illegal activity.
{RESET}
"""
type_with_typos(disclaimer)

# Input section
while True:
    print(f"{CYAN}>{BLUE}>{YELLOW}Choose input type:{RESET}")
    print(f"1.{BLUE} Instagram Username {RESET}")
    print(f"2.{BLUE} Phone Number {RESET}")
    print(f"3.{BLUE} Email Address {RESET}")
    choice = input(f"{YELLOW}Enter choice ({RESET}1{YELLOW}/{RESET}2{YELLOW}/{RESET}3{YELLOW}): {RESET}")
    if choice == '1':
        target = input(f"{CYAN}Enter Instagram username:@ ")
        break
    elif choice == '2':
        target = input(f"{CYAN}Enter phone number:+91 ")
        break
    elif choice == '3':
        target = input(f"{CYAN}Enter email address: ")
        break
    else:
        print(RED + "Oops...Invalid input. Try again.\n" + RESET)

# Fake log message
time.sleep(random.uniform(0.5, 2))
print(YELLOW + "\n[+] Saved to 0/self/emulated/com.termux.bybrute/logs/userdata.bin" + RESET)
time.sleep(random.uniform(2, 4))
print(YELLOW + f"\n[+] Connecting to Instagram server for {RED}{target}" + RESET)
time.sleep(random.uniform(3, 5))
print(GREEN + "[+] Connection established." + RESET)
time.sleep(1)
print(BLUE + "[+] Initializing brute force attack...\n" + RESET)
time.sleep(2)

# Fake loading messages
loading_msgs = [
    "Footprints...", "Bypassing 2FA...", "Loading credentials.bin",
    "Fetching hashed credentials...", "Injecting payload...", "Spoofing IP address..."
]

print(RED + f"//Processing..." + RESET)
time.sleep(random.uniform(2, 4))

latency = random.randint(49, 999)
print(f"{RED}[{GREEN}!{RED}]{GREEN} Access gained!\n{RED}[{GREEN}!{RED}]{YELLOW} ByBrute server latency: {RED}{latency}+ms{RESET}")

# Delay logic based on latency
if latency <= 200:
    time.sleep(0.5)
elif latency <= 499:
    time.sleep(1)
elif latency <= 699:
    time.sleep(2.5)
    print(f"{RED}[{GREEN}!{RED}]{YELLOW} Warning: Server latency is high ({BLUE}{latency}+ms{YELLOW}).{RESET}")
elif latency <= 949:
    time.sleep(3.5)
    print(f"{RED}[{GREEN}!{RED}]{YELLOW} Critical latency detected.\n  {RED}[{GREEN}!{RED}]{YELLOW} Connection adjusted!{RESET}")
    time.sleep(1)
else:
    time.sleep(5)
    print(f"{RED}[x] Timeout. Retrying request...{RESET}")
    time.sleep(random.uniform(2, 3))
    print(f"{GREEN}[✓] Reconnected to server.{RESET}")

# Animation
for msg in loading_msgs:
    print(f"{RED}[{GREEN}loading{RED}]{YELLOW} {msg}{RESET}")
    time.sleep(random.uniform(1, 2.5))

print(f"{RED}\n<{GREEN}<{BLUE}<{YELLOW}PLEASE NOTE{RED}>{GREEN}>{BLUE}>{RESET}")
time.sleep(2)

usage = f"""{GREEN}[{RED}!{GREEN}]{YELLOW}This tool is designed to identify vulnerable passwords and strengthen your defenses — for ethical testing only.
Use it to harden, not to harm :) {RESET}
"""
type_with_typos(usage)

print(f"\n{GREEN}[{RED}!{GREEN}]{BLUE} Process has started. This might take a while...\n\n{YELLOW}Take a cup of Tea and sit back like a\n" + RESET)

logo = f""" {CYAN} _   _    _    ____ _  _______ ____  
{RED} | | | |  / \\  / ___| |/ / ____|  _ \\ 
 {GREEN}| |_| | / _ \\| |   | ' /|  _| | |_) |
{BLUE} |  _  |/ ___ \\ |___| . \\| |___|  _ < 
{YELLOW} |_| |_/_/   \\_\\____|_|\\_\\_____|_| \\_\\
   {RESET}"""
type_with_typos(logo)
time.sleep(1)

# Passwords
def get_top_1000_passwords():
    try:
        r = requests.get("https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt")
        return r.text.splitlines()[:1000]
    except:
        return []

base_passwords = ["123456", "password", "admin", "iloveyou", "qwerty", "abc123"]
top_1000 = get_top_1000_passwords()
common_passwords = list(set(base_passwords + top_1000))
random.shuffle(common_passwords)

def generate_random_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%'
    return ''.join(random.choice(chars) for _ in range(random.randint(6, 12)))

# Brute-force loop
attempts = 0
while True:
    attempts += 1
    pwd = random.choice(common_passwords) + str(random.randint(10, 999)) if random.random() < 0.5 else generate_random_password()
    ping = random.randint(640, 999)

    sys.stdout.write(f"\r{GREEN}[{RED}*{GREEN}]{CYAN} Trying password {attempts}: {YELLOW}{pwd} {CYAN}| Status: {RED}Failed {CYAN}| Ping: {BLUE}{ping}ms{RESET}   ")
    sys.stdout.flush()
    time.sleep(random.uniform(0.5, 1.5))

    if attempts % 100 == 0:
        print(f"\n\n{CYAN}Attempted {attempts} passwords so far.{RESET}")
        confirm = input(f"{GREEN}Continue? ({RESET}Y{GREEN}/{RESET}N{GREEN}): {YELLOW}").strip().lower()
        if confirm != 'y':
            print(RED + "\n[x] Attack aborted by user." + RESET)
            break

# Final line
print(f"\n{GREEN}[✓] Session complete. Consider donating to charity.{RESET}")
