import requests, io, info

base_url = info.hostName + "/rest/api/latest/search"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
api_url = f"{base_url}?jql=project={info.project_key}"

# to get the total number of issues
response = requests.get(api_url, auth=(info.user, info.pwd), verify=False)
# response = requests.get(api_url, verify=False)
data = response.json()

# prints the dictionary keys
print(data.keys())

total = data["total"]

# setup the pagination
batch_size = 100
nor = (total + batch_size - 1) // batch_size
print(nor)

# fetch data for each page(acc to batch_size)
all = []
for n in range(nor):
    s = n * batch_size
    query = {"jql": "project=KAN", "startAt": s, "maxResults": batch_size}
    response = requests.get(
        base_url,
        headers=headers,
        params=query,
        auth=(info.user, info.pwd),
        verify=False,
    )
    data = response.json()
    issues = data.get("issues", [])
    all.extend(issues)

    # write result in file
with io.open("results.csv", "w", encoding="utf-8") as f1:
    for one in all:
        f1.write(one["id"] + "," + one["key"] + "\n")
    print("Success! Find Result in results.csv")
    f1.close()
