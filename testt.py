import requests
from bs4 import BeautifulSoup
import json
link='https://osmcha.org/api/v1/changesets/?page_size=75&page=1&date__lte=2021-06-11&date__gte=2021-05-01&users=GrabVN_Nha'
header={'Authorization':'Token 7d4516adbcbdb128e0f84f69615236ff65783053'}
html= requests.get(link,headers=header).text


a=json.loads(html)
features=a['features']
id_list=[]
for id in features:
    id_list.append(id['id'])

print(id_list)
def OSMCha_name_query(Start,End,User):
    link='https://osmcha.org/api/v1/changesets/?page_size=75&page=1&date__lte={Start}&date__gte={End}}&users={User}'
    header={'Authorization':'Token 7d4516adbcbdb128e0f84f69615236ff65783053'}
    html= requests.get(link,headers=header).text
    a=json.loads(html)
    features=a['features']
    id_list=[]
    
    for id in features:
        id_list.append(id['id'])
    
    return id_list

print("hello")
print("hello")