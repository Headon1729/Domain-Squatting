import whois
w = whois.whois('webscraping.com')
print(w.expiration_date)  # dates converted to datetime object
# would print datetime.datetime(2013, 6, 26, 0, 0)

print(w.text)  # the content downloaded from whois server

print(w)  # print values of all found attributes like mentioned below
# creation_date: 2004-06-26 00:00:00
# domain_name: [u'WEBSCRAPING.COM', u'WEBSCRAPING.COM']
# emails: [u'WEBSCRAPING.COM@domainsbyproxy.com', u'WEBSCRAPING.COM@domainsbyproxy.com']
# expiration_date: 2013-06-26 00:00:00
