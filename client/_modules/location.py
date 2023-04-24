
def init():
    global _geo, _loc, raw_loc, country, country_code, postal_code, timezone, region, city, ip
    
    import geocoder as _geocoder
    import geopy as _geopy

    _geo = _geopy.Nominatim(user_agent='urmom')
    _loc = _geocoder.ip('me').raw

    raw_loc = _loc
    country = _geo.reverse(_loc['loc'],zoom=1)
    country_code = _loc['country']
    postal_code = _loc['postal']
    timezone = _loc['timezone']
    region = _loc['region']
    city = _loc['city']
    ip = _loc['ip']
    
    

