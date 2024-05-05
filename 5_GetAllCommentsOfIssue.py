import requests, info, io

# Make changes here
issue_id = "KAN-1"

url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/comment"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

response = requests.get(url, headers=headers, auth=(info.user, info.pwd), verify=False)
data = response.json()

# gives the comment counts
print(data["total"])

# Notes all comments
with io.open("comments.csv", "w", encoding="utf-8") as f1:
    f1.write("comment id" + "," + "comment text" + "\n")
    for comments in data["comments"]:
        f1.write(comments["id"] + "," + comments["body"] + "\n")
    f1.close()
