import requests, info


base_url = info.hostName + "/rest/api/latest/search"

headers = {"Accept": "application/json", "Content-Type": "application/json"}

query = {"jql": "project = KAN"}

response = requests.get(
    base_url, headers=headers, params=query, auth=(info.user, info.pwd), verify=False
)
data = response.json()
issues = data["issues"]
for issue in issues:
    print(issue["key"])
