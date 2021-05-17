import idna
ans = idna.encode('ドメイン.テスト')
print(ans)
# b'xn--eckwd4c7c.xn--zckzah'
print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
# ドメイン.テスト
