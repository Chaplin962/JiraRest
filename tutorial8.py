import requests
import json
import io
base_url = "https://yatheeswar1611.atlassian.net/rest/api/latest/search"
user = "yatheeswar1611@gmail.com"
pwd="ATATT3xFfGF0DsS_5XHdisbHe9I_QtZQQ49kB0jMjfubQEtTiXgFhFsK1DiAkbniZPvtJvd8N57iyw5dk3lsS-3Show0rVi4AaLj_c39CnfjJ35QVVSzvnxekbQCtmCwmv2jKWcm3MtUlp3A-hUkHmv9QqX5hLKW7g5ATaVLFHxNgeoT2YKGTYA=83565BB9"

headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}

query = {
   'jql': 'project = KAN'
}

response=requests.get(base_url,headers=headers,params=query,auth=(user,pwd),verify=False)
data=response.json()
issues=data["issues"]
for issue in issues:
    print(issue["key"])
