import requests

r = requests.get("http://google.com")
print(r.status_code)

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.status_code)
# # 200
# print(r.headers['content-type'])
# # 'application/json; charset=utf8'
# print(r.encoding)
# # 'utf-8'
# print(r.text)
# # '{"type":"User"...'
# print(r.json())
# # {'disk_usage': 368627, 'private_gists': 484, ...}
