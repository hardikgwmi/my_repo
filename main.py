import requests
import json

from sqlalchemy import null, true

## create class

class 
def send_post_request(url, data):
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJiX21peUs5dERpc0QtLWxTdGo0blg1QW1hb1gzRUhzcnZHeXNBOVRWRDhjIn0.eyJleHAiOjE3MTE0NzUzMjYsImlhdCI6MTcxMTQ3NDcyNiwiYXV0aF90aW1lIjoxNzExNDc0NzI1LCJqdGkiOiJlNzA5MTQxZS1kNjY5LTRlZmYtOWYzNy03OTNkZDQzMmIyODIiLCJpc3MiOiJodHRwOi8vYWU0OWQ5Y2FmYjEyNTQzM2NiYzhjODkwZWQzNDM0MzEtMTEwMTA4OTcyMy5hcC1zb3V0aC0xLmVsYi5hbWF6b25hd3MuY29tL2F1dGgvcmVhbG1zL0JOVFYiLCJzdWIiOiJlMDZmN2FiYS00YjAwLTQ2YjEtYmM2ZC1kMGFjMTY0MzY5OTkiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJib290bmV4dCIsIm5vbmNlIjoiM2QwNGY1YmYtYzVlMi00NzBjLWI2ZmMtYjFhNjA0Yjg0YjQ0Iiwic2Vzc2lvbl9zdGF0ZSI6IjcyMzdkNDNmLWFjMGQtNDFjNi04NjE2LTRjNWQ0ZWYzZjk1NSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI3MjM3ZDQzZi1hYzBkLTQxYzYtODYxNi00YzVkNGVmM2Y5NTUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IlBhdGlsIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiZGV2IiwiZ2l2ZW5fbmFtZSI6IlBhdGlsIiwiZmFtaWx5X25hbWUiOiIiLCJlbWFpbCI6ImhpY2VnNzk2ODJAYXZpZGFwcm8uY29tIn0.HxzkW_BUn2QJ8X6G7Sc_AEw7M2caQCve8I4d357xuMEoO0ai-L8RcOB0A_QO9_NTdBs17gL6yFNWL2fYxHYau25E3OoAIXkCzm-tx3X2ba3DHMRPX89p_swRlqe1zluIZvPNka3L3UuxZNrbDORQSAd3JEmoszmTMj_l2Fj3DNGpSrbagRijcvFCUAEcFtpg5N-RTeZRO6QBahKEpWBX81JE0MwteAGbtqMznztI5tDBee0YBSkR8PO_6Vv39-g3VoKRy4SIWQX93ey6d501p9TpBJoRg0NwEZFWkOCCZp8xlMzL-BbYmEi3Jf3t-foTSXOxLNho1a1aPI6jpCnLMA'
        ,'Content-Type': 'application/json'
        }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

# Example usage:
url = 'http://ae49d9cafb125433cbc8c890ed343431-1101089723.ap-south-1.elb.amazonaws.com/apim/audit-service/1.0.0/rest/audit/createAuditWithKafka'
data = {
  "auditId": 12345,
  "userId": 9876,
  "userName": "john_doe",
  "auditActionName": "Login",
  "auditActionType": "LOGIN",
  "date": "2024-03-26T12:30:00Z",
  "action": "User login",
  "parameter": "{\"username\":\"john_doe\",\"password\":\"password123\"}",
  "success": True,
  "remoteHost": "192.168.1.100",
  "sessionid": "abc123xyz456",
  "host": "example.com",
  "page": "/login",
  "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
  "exceptionDetail": None,
  "componentName": "Authentication",
  "lastLoginTime": "2024-03-25T18:00:00Z"
}
  # Your JSON data here

response = send_post_request(url, data)

if response.status_code == 200:
    print("Request was successful.")
    print("Response:")
    print(response.json())  # Print response data if it's JSON
else:
    print("Request failed with status code:", response.status_code)
