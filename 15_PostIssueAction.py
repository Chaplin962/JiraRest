import requests, json, info

# Make Changes Here
issue_id = "KAN-4"

url = info.hostName + "/rest/api/latest/issue/" + issue_id + "/transitions"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Get all Actions ID
response = requests.get(url, headers=headers, auth=(info.user, info.pwd), verify=False)
print(response.text)

# Post a change to issue
payload = json.dumps({"transition": {"id": "21"}})
response = requests.post(
    url, headers=headers, data=payload, auth=(info.user, info.pwd), verify=False
)

# Returns No response if success
print(response.text)


# {
#     "expand": "transitions",
#     "transitions": [
#         {
#             "id": "11",
#             "name": "To Do",
#             "to": {
#                 "self": "https://yatheeswar1611.atlassian.net/rest/api/2/status/10000",
#                 "description": "",
#                 "iconUrl": "https://yatheeswar1611.atlassian.net/",
#                 "name": "To Do",
#                 "id": "10000",
#                 "statusCategory": {
#                     "self": "https://yatheeswar1611.atlassian.net/rest/api/2/statuscategory/2",
#                     "id": 2,
#                     "key": "new",
#                     "colorName": "blue-gray",
#                     "name": "To Do",
#                 },
#             },
#             "hasScreen": false,
#             "isGlobal": true,
#             "isInitial": false,
#             "isAvailable": true,
#             "isConditional": false,
#             "isLooped": false,
#         },
#         {
#             "id": "21",
#             "name": "In Progress",
#             "to": {
#                 "self": "https://yatheeswar1611.atlassian.net/rest/api/2/status/10001",
#                 "description": "",
#                 "iconUrl": "https://yatheeswar1611.atlassian.net/",
#                 "name": "In Progress",
#                 "id": "10001",
#                 "statusCategory": {
#                     "self": "https://yatheeswar1611.atlassian.net/rest/api/2/statuscategory/4",
#                     "id": 4,
#                     "key": "indeterminate",
#                     "colorName": "yellow",
#                     "name": "In Progress",
#                 },
#             },
#             "hasScreen": false,
#             "isGlobal": true,
#             "isInitial": false,
#             "isAvailable": true,
#             "isConditional": false,
#             "isLooped": false,
#         },
#         {
#             "id": "31",
#             "name": "Done",
#             "to": {
#                 "self": "https://yatheeswar1611.atlassian.net/rest/api/2/status/10002",
#                 "description": "",
#                 "iconUrl": "https://yatheeswar1611.atlassian.net/",
#                 "name": "Done",
#                 "id": "10002",
#                 "statusCategory": {
#                     "self": "https://yatheeswar1611.atlassian.net/rest/api/2/statuscategory/3",
#                     "id": 3,
#                     "key": "done",
#                     "colorName": "green",
#                     "name": "Done",
#                 },
#             },
#             "hasScreen": false,
#             "isGlobal": true,
#             "isInitial": false,
#             "isAvailable": true,
#             "isConditional": false,
#             "isLooped": false,
#         },
#     ],
# }
