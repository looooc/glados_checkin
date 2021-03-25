import requests
import json

url = 'https://glados.rocks/api/user/checkin'

status_url = 'https://glados.rocks/api/user/status'

headers = {
    'cookie': 'koa:sess=eyJ1c2VySWQiOjQxMDM2LCJfZXhwaXJlIjoxNjM3NzQ0MTY1ODc4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=DYQ1OzTj-cbsi73GmxrReovM1k4; __cfduid=d643de9527ece24fcd7b233a55dd1f2a71616640247',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

data = {"token": "glados_network"}

res = requests.post(url=url, data=data, headers=headers, verify=False)

status_res = requests.get(url=status_url, headers=headers, verify=False)


print(json.loads(res.content)['message'])
print(json.loads(status_res.content)['data']['leftDays'])
