import mysql.connector

from utilities.Resources import *
from utilities.payload import *
from utilities.Configuration import *
import requests

burl = getconfig()['API']['endpoint']+Resources.addbookresource
query = "select * from Books"


res=requests.post(burl,json=addbook(query))
print(res.text)
print(res.status_code)
res_json = res.json()
id = res_json['ID']

durl = getconfig()['API']['endpoint']+Resources.deletebookresource

re = requests.post(durl,json=delbook(id))
print(re.text)