import json

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}

json_str = json.dumps(data)

# Writing JSON data
with open('data.json', 'w') as f:
     json.dump(data, f)
