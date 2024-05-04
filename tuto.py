
import requests, json, io
 
base_url = "https://yatheeswar1611.atlassian.net/rest/api/latest/search"
user = "yatheeswar1611@gmail.com"
pwd = "ATATT3xFfGF0bt4b6ul93bRfnTzhgvO_9RQJqvPbDdaO5mmgdqyZVsARVLlI52l-sqYsYqst_Gnyk8Ia_sLTqwi6lBfk3u7mAiX59AilqGXsR2byI19ZwIDGGHEFtyWhTjYtQjjO8Bc0L68JMXZlPzPTNE-uAk9KxFAeCVCnR0Rex5qtmcajxPk=A30219BD"
 
project_key = "KAN"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
 
api_url = f"{base_url}?jql=project={project_key}"
# to get the total number of issues
 
response = requests.get(api_url, auth=(user, pwd), verify=False)
#response = requests.get(api_url, verify=False)
data = response.json()
total = data["total"]
 
# setup the pagination
batch_size = 100
nor = (total + batch_size - 1) // batch_size
print(nor)
 
# looping
all = []
for n in range(nor):
    s = n * batch_size
    query = {"jql": "project=KAN", "startAt": s, "maxResults": batch_size}
    response = requests.get(base_url, headers=headers, params=query, auth=(user, pwd), verify=False)
    data = response.json()
    issues = data.get("issues", [])
    all.extend(issues)
 
    #write result in file
with io.open("results.csv", "w", encoding="utf-8") as f1:
    for one in all:
        f1.write(one["id"] + "," + one["key"] + "\n")
    f1.close()
 