import pandas as pd

def transform_data(dados):
    list = []

    for country in dados:
        code = None
        name = country['name']['common']
        region = country['region']
        capital = None
        population = country['population']
    
        if 'capital' in country and len(country['capital']) > 0:
            capital = country['capital'][0]
        if 'cioc' in country and len(country['cioc']) > 0:
            code = country['cioc']

        list.append({
            'id_country': code,
            'name': name,
            'region': region,
            'capital': capital,
            'population': population
            })

    df = pd.DataFrame(list)
    return df