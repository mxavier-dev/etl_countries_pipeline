import requests
from utils.logger import get_logger

logger = get_logger()

url = 'https://restcountries.com/v3.1/all?fields=name,population,capital,region,cioc'

def extract_data():
    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    else:
        logger.error('API ERROR')
        return []