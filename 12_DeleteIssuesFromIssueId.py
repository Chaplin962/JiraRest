import requests, io, info

headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Reads issues from issue_delete.csv
with io.open("issue_delete.csv", "r", encoding="utf-8") as f1:
    data = f1.read()
data = data.split("\n")

# Deletes Issues one by one
for id in data:
    url = info.hostName + "/rest/api/latest/issue/" + id
    response = requests.delete(
        url, headers=headers, auth=(info.user, info.pwd), verify=False
    )
