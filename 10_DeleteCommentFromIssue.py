import requests, info

# Make changes here
issue_id = "KAN-1"
comment_id = "10009"

url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/comment/" + comment_id
headers = {"Accept": "application/json", "Content-Type": "application/json"}

response = requests.delete(
    url, headers=headers, auth=(info.user, info.pwd), verify=False
)
print(response.text)
