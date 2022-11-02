
import json

file=open("E:\\DS290822B\\json\\employees.json","r")
print(file)
#jason into dict
data = json.loads(file.read())

for i in data["emp_details"]:
    print(i)

file.close()
