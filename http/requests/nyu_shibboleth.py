import requests
import json

r = requests.post('https://shibboleth.nyu.edu/idp/Authn/UserPassword', data=json.dumps({'j_username': '', 'j_password': ''}))

print r.status_code
print r.headers['content-type']
print r.encoding
print r.text
