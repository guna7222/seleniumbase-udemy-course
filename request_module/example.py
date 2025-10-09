import requests

r = requests.get("https://reqres.in/api/users?page=2") # sends a GET request and stores the response in r
# print(r.text) # prints the text of the response it is a string
json_data = r.json() # it is a python dictionary
print(json_data) # prints the json data

# passing url parameters or query parameters
# first way
response = requests.get("https://requestb.in/wpo4xjwp?key1=value1&key2=value2") # key1=value1&key2=value2 are called query strings

# another way
payload = {
    "key1": "value1",
    "key2": "value2"
}

response1 = requests.get("https://requestb.in/wpo4xjwp", params=payload) # params is used to pass the query parameters

# custom headers

headers = {
    "bearer":"hgy739vnvhfhdjd83839djdjhdvhe8e0den89k"
}

rs = requests.get("https://reqres.in/api/users?page=2", headers=headers)

