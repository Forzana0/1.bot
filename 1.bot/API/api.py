import requests

def get_random_duck():
    end_point = 'https://random-d.uk/api/random'
    response = requests.get(end_point)
    print(response.status_code)
    print(response.json())