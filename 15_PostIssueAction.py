import requests, json, info

# Make Changes Here
issue_id = "KAN-1"

url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/transitions"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Get all Actions ID
response = requests.get(url, headers=headers, auth=(info.user, info.pwd), verify=False)
print(response.text)

# Post a change to issue
payload = json.dumps({"transition": {"id": "11"}})
response = requests.post(
    url, headers=headers, data=payload, auth=(info.user, info.pwd), verify=False
)

# Returns No response if success
print(response.text)
