import urllib.request
val = urllib.request.urlopen("https://www.google.com").read()
print(val)
