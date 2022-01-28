import sys
import requests

r = requests.get("http://google.com")
name = input('Your name?')
print("Hello,", name)