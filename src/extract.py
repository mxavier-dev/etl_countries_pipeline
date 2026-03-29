import requests

url = 'https://restcountries.com/v3.1/all?fields=name,population,capital,region,cioc'

def extract_data():
    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception('API ERROR')