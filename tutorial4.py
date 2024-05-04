import requests, info

# Make changes here
issue_id = "KAN-2"

# basic autentication
base_url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/attachments"

headers = {"X-Atlassian-Token": "no-check"}
# attaching the files
files = {"file": ("blacklist.csv", open("blacklist.csv", "rb"))}

# sending the response

response = requests.post(
    base_url, headers=headers, files=files, auth=(info.user, info.pwd), verify=False
)
print(response.text)
