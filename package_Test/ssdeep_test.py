import requests
import ssdeep
import socket

ip_add = socket.gethostbyname("stopatnothing.com")
print(ip_add)
# hash1 = ssdeep.hash(
#     'Also called fuzzy hashes, Ctph can matchcan matchcan matchcan match inputs that have homologies.')
# print(hash1)
# # '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'
# hash2 = ssdeep.hash(
#     'Also called fuzzy hashes, CTPH can matchcan matchcan matchcan match inputs that have homologies.')
# print(hash2)
# # '3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C'
# val = ssdeep.compare(hash1, hash2)
# print("answer ", val)

# web1 = requests.get("https://www.medium.com")
# web2 = requests.get("https://www.medium.com")
# hash1 = ssdeep.hash(web1.text)
# hash2 = ssdeep.hash(web2.text)
# print(hash1)
# print(hash2)
# val = ssdeep.compare(hash1, hash2)
# print("answer ", val)
