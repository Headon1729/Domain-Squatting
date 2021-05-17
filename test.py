from geoip import geolite2
match = geolite2.lookup(bytes('17.0.0.1', 'utf-8'))
# match is not None
match.country
