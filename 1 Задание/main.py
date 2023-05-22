import requests

url = "https://akabab.github.io/superhero-api/api//all.json"
response = requests.get(url)
hero_list = ['Hulk', 'Captain America', 'Thanos']
data = response.json()
intelligence = []


for value in data:
    result = value['powerstats']['intelligence']
    if value['name'] in hero_list:
        intelligence.append(result)


full_hero_list = dict(zip(hero_list, intelligence))
print(max(full_hero_list))