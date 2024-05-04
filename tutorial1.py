import requests, json, info

url = info.hostName + "/rest/api/latest/issue"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
payload = json.dumps(
    {
        "fields": {
            "project": {"key": "TTS"},
            "summary": "created for test",
            "description": "Created for test11",
            "issuetype": {"name": "Task"},
        }
    }
)
response = requests.post(
    url,
    headers=headers,
    data=payload,
    auth=(info.user, info.pwd),
)
data = response.json()
print(data["id"])