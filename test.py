from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes":10, "name":'Tim', "views":10000},
        {"likes":24, "name":'How to make REST APIS', "views":30000},
        {"likes":12, "name":'joe', "views":1400}]


# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())



input()
response = requests.get(BASE + "video/2")
print(response.json())

input()
response = requests.delete(BASE + "video/2")
print(response)

# input()
# response = requests.patch(BASE + "video/2", {"views":99})
# print(response.json())