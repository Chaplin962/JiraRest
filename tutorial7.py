import requests, json, info

issue_id = "KAN-1"
base_url = info.hostName + "rest/api/latest/issue/" + issue_id + "/comment"

headers = {"Accept": "application/json", "Content-Type": "application/json"}

data = json.dumps({"body": "trial comment post"})

response = requests.put(
    base_url, headers=headers, data=data, auth=(info.user, info.pwd), verify=False
)
print(response.text)
