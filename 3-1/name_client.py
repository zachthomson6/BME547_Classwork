import requests


#out_data = {"name": "Zach Thomson", "net_id": "zdt2", "e-mail": "zachary.thomson@duke.edu"}
#r = requests.post("http://vcm-21170.vm.duke.due:5000/student", json=out_data)
#print(r.status_code)
#print(r.text)


#out_data = {"user": "Zach Thomson", "message": "Yo, what's up rizzmaster 3000"}
#r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/gmoney")
print(r.text)

#out_data = {"user": "Your boy, skinny p", "message": "Call 877-GET-CASH-NOW"}
#r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)
