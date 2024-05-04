import requests, json, info

# Make changes here
issue_id = "KAN-1"
user_id = "5ff7d2d91051d10075a65acb"

url = info.hostName + "/rest/api/3/issue/" + issue_id + "/assignee"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Assing user to issue
payload = json.dumps({"accountId": user_id})
response = requests.put(
    url, headers=headers, data=payload, auth=(info.user, info.pwd), verify=False
)
print(response.text)
