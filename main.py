import http.client
import json

def GetFutureMeetings(userid):
  
  conn = http.client.HTTPSConnection("api.zoom.us")
  
  headers = {
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IkVDUzVDWUltVDZhMGJVR1BUMVpzTHciLCJleHAiOjE2MDYyOTc3MTQsImlhdCI6MTYwNTY5MjkxM30.XepgGLhNkxAdYjXVTC9T_zhMJjqV1Ko9MKBVfyTsPEU",
    'content-type': "application/json"
    }

  conn.request("GET", f"/v2/users/{userid}/meetings?type=scheduled&page_size=300&page_number=1", headers=headers)

  res = conn.getresponse()

  if res.status==404:
    return f"The user {userid} wasn't found in Zoom"
  if res.status==401:
    return "The token was expired"
  if res.status!=200:
    return f"An error was occur. error no.{res.status}"

  data = json.loads(res.read().decode('utf-8'))
  
  if data["total_records"]>0:
    return f"The user {userid} currently have {data['total_records']} future meetings in Zoom"
  else:
    return f"The user {userid} have no future meetings in Zoom"

  

user=input("please enter your Zoom Email: ")
print(GetFutureMeetings(user))