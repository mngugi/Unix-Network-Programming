import urllib.request 
try:
    import json 
except ImportError: # for Python 2.5 
    import simplejson as json

params = {'q': '207 N. Defiance St, Archbold, OH','output': 'json', 'oe': 'utf8'}
url = 'http://maps.google.com/maps/geo?'
with urllib.request.urlopen(url) as response:
    html = response.read()

print(reply['Placemark'][0]['Point']['coordinates'][:-1])
print(html)
