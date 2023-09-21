import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))     #this has str as a type
    categories = r.json()   #transform to json

    for category in categories:
        print(category["name"])