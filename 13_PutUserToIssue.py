import requests, json, info

# Make changes here
issue_id = "KAN-8"
user_id = "70121:265af059-1ced-4e50-8134-39e128aa68e6"

url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/assignee"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Assing user to issue
payload = json.dumps({"accountId": user_id})
response = requests.put(
    url, headers=headers, data=payload, auth=(info.user, info.pwd), verify=False
)
print(response.text)
