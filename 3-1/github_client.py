import requests


r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(r)
print(type(r))
print(r.status_code)
print(r.text)
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])
    
