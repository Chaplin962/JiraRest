import requests, info

url = info.hostName + "/rest/api/latest/users/search"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Get data from Jira
response = requests.get(url, headers=headers, auth=(info.user, info.pwd), verify=False)
data = response.json()

print(len(data))
print(data)

# Print user data
for users in data:
    print(users["displayName"])
