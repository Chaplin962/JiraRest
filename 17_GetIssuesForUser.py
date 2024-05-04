import requests, info

# Make Changes Here
assignee = "Yatheeswar"

base_url = info.hostName + "/rest/api/latest/search"
headers = {
    "Accept": "application/json",
    "Content": "application/json",
}

# Fetch Issues of user
api_url = f"{base_url}?jql=assignee='{assignee}'"
response = requests.get(
    api_url, headers=headers, auth=(info.user, info.pwd), verify=False
)
issues = response.json()["issues"]
for issue in issues:
    print(issue["key"], issue["fields"]["summary"])
