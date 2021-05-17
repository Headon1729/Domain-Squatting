import geoip2.database
# This creates a Reader object. You should use the same object
# across multiple requests as creation of it is expensive.
with geoip2.database.Reader('/home/lakshya/.local/lib/python3.8/site-packages/_geoip_geolite2/GeoLite2-City.mmdb') as reader:
    # Replace "city" with the method corresponding to the database
    # that you are using, e.g., "country".
    response = reader.city('207.228.238.7')
    # Would print United States
    print(response.country.iso_code)
