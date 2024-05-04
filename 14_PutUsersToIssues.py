import requests, json, io, info

# Make changes here
issue_id = "KAN-1"

url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/assignee"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Fetches Issue ID and User ID from issue_user.csv
with io.open("issue_user.csv", "r", encoding="utf-8") as f1:
    data = f1.read()
    f1.close()
data = data.split("\n")
for row in data:
    issue_id = row.split(",")[0]
    user_id = row.split(",")[1]

    # Assigns Users to issue
    url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/assignee"
    payload = json.dumps({"accountId": user_id})
    response = requests.put(
        url, headers=headers, data=payload, auth=(info.user, info.pwd), verify=False
    )
    print(response.text)
