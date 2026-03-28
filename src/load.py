from utils.connect.connection import connect
import json
from datetime import datetime

def save_raw(data):
    time = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    filename = f'Downloads/etl_countries_project/data/raw/raw_{time}.json'
    with open(filename, 'w', encoding='utf-8') as arq:
        json.dump(data, arq, indent=4)

def save_processed(data):
    time = datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
    filename = f'Downloads/etl_countries_project/data/processed/processed_{time}.json'
    data.to_json(filename, orient='records', indent=4, force_ascii=False)

def insert_countries(data):
    conn = connect()
    cursor = conn.cursor()

    query = """
    INSERT INTO countries (id_country, name, region, capital, population)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    id_country = VALUES(id_country),
    region = VALUES(region),
    capital = VALUES(capital),
    population = VALUES(population)
    """
    values = []

    for country in data.itertuples():
       values.append((
            country[1],
            country[2],
            country[3],
            country[4],
            country[5] if country[4] else None
        ))
    try:
        cursor.executemany(query, values)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

    cursor.close()
    conn.close()

    print(f"{len(values)} registros inseridos")