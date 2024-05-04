import requests, json, io, info

url = info.hostName + "/rest/api/latest/issue"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Read data from issue.csv
with io.open("issue.csv", "r", encoding="utf-8") as f1:
    data = f1.read()
    f1.close()

data = data.split("\n")
for rows in data:
    # Setting up csv rows as input
    payload = json.dumps(
        {
            "fields": {
                "project": {"key": rows.split(",")[0]},
                "summary": rows.split(",")[1],
                "description": rows.split(",")[2],
                "issuetype": {"name": "Task"},
            }
        }
    )

    # Adding new issues to project
    response = requests.post(
        url, headers=headers, data=payload, auth=(info.user, info.pwd), verify=False
    )
    print(response.text)
