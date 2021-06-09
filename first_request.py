import requests
from random import randint
url = "http://icanhazdadjoke.com/search"
s = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params={"term": s})
response.raise_for_status()
data = response.json()
if (data['total_jokes'] == 0):
    print(f"Sorry, I don`t have any jokes about {s}! Please, try again.")
elif data['total_jokes'] > 1:
        n = int(randint(0, data['total_jokes']-1))
        print(f"I`ve got {data['total_jokes']} jokes about {s}. ")
        print(f"Here`s one: {data['results'][n]['joke']}")
else:
    print(f"I`ve got one joke about {s}. ")
    print(f"Here it is: {data['results'][0]['joke']}")

 