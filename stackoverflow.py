import requests
from pprint import pprint

url = 'https://api.stackexchange.com///2.3/questions?min=1626825600&max=1626998400&tagged=python&site=stackoverflow'



def get_questhions(url):
    resp = requests.get(url=url)
    #pprint(resp.json())

    questhions = resp.json()['items']

    #pprint(questhions)

    for item in questhions:
        print(item['title'])

get_questhions(url)