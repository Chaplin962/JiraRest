import requests
import json
import io
base_url = "https://yatheeswar1611.atlassian.net/rest/api/latest/issue/KAN-1/comment"
user = "yatheeswar1611@gmail.com"
pwd="ATATT3xFfGF0DsS_5XHdisbHe9I_QtZQQ49kB0jMjfubQEtTiXgFhFsK1DiAkbniZPvtJvd8N57iyw5dk3lsS-3Show0rVi4AaLj_c39CnfjJ35QVVSzvnxekbQCtmCwmv2jKWcm3MtUlp3A-hUkHmv9QqX5hLKW7g5ATaVLFHxNgeoT2YKGTYA=83565BB9"
project_key = "KAN"

headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}

data=json.dumps({

  "body": "trial comment post"
})

response=requests.put(base_url,headers=headers,data=data,auth=(user,pwd),verify=False)
print(response.text)