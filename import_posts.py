import requests, json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAEcg%2BQEAAAAASu%2BKl13p%2FxnLHRyPLJ4IMQHZ1QQ%3DvOX0p2yqqIBGpVxIWfRuhoCFf3qwLFMi0PQp38NJ74ynotcVRi"

search_query='https://api.x.com/2/tweets/search/recent?query="black""massachusetts"(woman OR women)'

headers = {"Authorization": f"Bearer {bearer_token}"}
response = requests.get(search_query, headers=headers)
destination = open("data.json", "w")

json.dump(response.json(), destination)