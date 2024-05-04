import requests
import json
import io

#basic autentication
base_url = "https://yatheeswar1611.atlassian.net/rest/api/latest/issue/KAN-2/attachments"
user = "yatheeswar1611@gmail.com"
pwd="ATATT3xFfGF0DsS_5XHdisbHe9I_QtZQQ49kB0jMjfubQEtTiXgFhFsK1DiAkbniZPvtJvd8N57iyw5dk3lsS-3Show0rVi4AaLj_c39CnfjJ35QVVSzvnxekbQCtmCwmv2jKWcm3MtUlp3A-hUkHmv9QqX5hLKW7g5ATaVLFHxNgeoT2YKGTYA=83565BB9"
project_key="KAN"
headers={
    "X-Atlassian-Token": "no-check"
}
#attaching the files 
files={
    "file":("blacklist.csv",open("blacklist.csv","rb"))
}

#sending the response

response=requests.post(base_url,headers=headers,files=files,auth=(user,pwd),verify=False)
print(response.text) 