import requests
import json
import io
base_url = "https://yatheeswar1611.atlassian.net/rest/api/latest/issue/KAN-1/comment"
user = "yatheeswar1611@gmail.com"
pwd = "ATATT3xFfGF0bt4b6ul93bRfnTzhgvO_9RQJqvPbDdaO5mmgdqyZVsARVLlI52l-sqYsYqst_Gnyk8Ia_sLTqwi6lBfk3u7mAiX59AilqGXsR2byI19ZwIDGGHEFtyWhTjYtQjjO8Bc0L68JMXZlPzPTNE-uAk9KxFAeCVCnR0Rex5qtmcajxPk=A30219BD"
 
project_key = "KAN"

headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}

data=json.dumps({

  "body": "trial comment"
})

response=requests.post(base_url,headers=headers,data=data,auth=(user,pwd),verify=False)
print(response.text)