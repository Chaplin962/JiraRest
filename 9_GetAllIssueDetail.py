import requests, info

# Make changes here
project_key = "KAN"

url = info.hostName + "/rest/api/latest/search"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

query = {"jql": "project = " + project_key}

response = requests.get(
    url, headers=headers, params=query, auth=(info.user, info.pwd), verify=False
)

data = response.json()
# Stores all issues under project
issues = data["issues"]

for issue in issues:
    issue_key = issue["key"]
    url1 = info.hostName + "/rest/api/latest/issue/" + issue_key

    # Get data per issue
    response = requests.get(
        url1, headers=headers, auth=(info.user, info.pwd), verify=False
    )
    data = response.json()
    print(f'issue id is {issue_key} and status is {data["fields"]["status"]["name"]}')
