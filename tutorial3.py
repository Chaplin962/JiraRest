import requests
import json
import io
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
base_url = "https://yatheeswar1611.atlassian.net/rest/api/latest/user"
user = "yatheeswar1611@gmail.com"
pwd="ATATT3xFfGF0DsS_5XHdisbHe9I_QtZQQ49kB0jMjfubQEtTiXgFhFsK1DiAkbniZPvtJvd8N57iyw5dk3lsS-3Show0rVi4AaLj_c39CnfjJ35QVVSzvnxekbQCtmCwmv2jKWcm3MtUlp3A-hUkHmv9QqX5hLKW7g5ATaVLFHxNgeoT2YKGTYA=83565BB9"
project_key="KAN"

'''
with io.open("userlist.csv","r",encoding="utf-8")as f1:
    user_data=f1.read()
    f1.close()
user_data=user_data.split("\n")[1:]
for users in user_data:
    displayname=users.split(",")[0]
    pwd=users.split(",")[1]
    email=users.split(",")[2]
    name=users.split(",")[2]
    payload=json.dumps(
    {
        "password": pwd,
        "emailAddress": email,
        "displayName": displayname,
        "name": name
   }
   )
    response=requests.post(base_url,headers=headers,data=payload,auth=(user,pwd),verify=False)
    print(response.text) 
'''


payload=json.dumps(
    {
    "password": "test@1234",
  "emailAddress": "tesuser1@atlassian.com",
  "displayName": "test1 user1",
  "name": "test1user1"
}
)
response=requests.post(base_url,headers=headers,data=payload,auth=(user,pwd) ,verify=False)
print(response.text) 


