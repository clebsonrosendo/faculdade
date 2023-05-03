import sys
import secrets


url = 'https://mydomain.com/' + secrets.token_urlsafe(4).upper()
print (url)