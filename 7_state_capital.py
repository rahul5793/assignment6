import json
	
# Data to be written
dictionary = {
 "state": "capital",
 "up": "lko",
 "bihar": "patna",
 "westbengal": "kolkata",
 "uk":"dehradoon"
 "mp":"bhopal",
 "raj":"jaipur",
 "hariyana":"punjab",

},
	
# Serializing json
json_object = json.dumps(dictionary, indent = 7)
print(json_object)
