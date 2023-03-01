import requests
import json
import ast


r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/zdt2")
dictionary = ast.literal_eval(r.text)
print(dictionary)
don = dictionary['Donor']
rec = dictionary['Recipient']

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+don)
print(r.text)

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+rec)
print(r.text)

out_data = {"Name": "zdt2", "Match":  "Yes"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(r.text)
