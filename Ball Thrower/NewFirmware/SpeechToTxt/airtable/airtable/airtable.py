import secrets
from urllib.parse import quote
import ujson, urequests


def AT_setup():
     urlBase = "https://api.airtable.com/v0/"
     Key = secrets.ATappkey
     headers = {"Accept":"application/json","Content-Type":"application/json","Authorization":"Bearer " + Key}
     return urlBase, headers
     
def Put_AT(Table_name,Field_Name,Value):
     urlBase, headers = AT_setup()
     urlTag = urlBase + Field_Name
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table_name) 
     propValue={"records": [{"fields": {  Field_Name: Value}} ]}
     try:
          value = urequests.post(urlValue,headers=headers, json=propValue).text
          data = ujson.loads(value)
          result = data.get("records")[-1].get("id")
     except Exception as e:
          print(e)
          result = 'failed'
     return result

def Get_AT(Table_name,Field_name):
     urlBase, headers = AT_setup()
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table_name) + "?view=Grid%20view"

     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          result = data.get("records")[-1].get("fields").get(Field_name)
     except Exception as e:
          print(e)
          result = 'failed'
     return  result

def Get_AT_field(Table_name,Field_name):
     urlBase, headers = AT_setup()
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table_name) + "?view=Grid%20view"

     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          result=['']
          for i in data.get("records"):
              print(i.get("fields").get(Field_name))
              result.append(i.get("fields").get(Field_name))
          
     except Exception as e:
          print(e)
          result = ['failed']
     return  result


def Delete_AT(Table_name,ID):
     urlBase, headers = AT_setup()
     urlValue = urlBase + secrets.ATdocID + "/" + quote(Table_name) + "?" + "records[]=" + quote(ID)
     print(urlValue)
     try:
          value = urequests.delete(urlValue,headers=headers).text
          data = ujson.loads(value)
          print(data)
          result = data.get("records")[-1].get("deleted")
     except Exception as e:
          print(e)
          result = 'failed'
     return  result

