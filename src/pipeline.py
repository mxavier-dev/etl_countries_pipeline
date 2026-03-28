from extract import extract_data
from transform import transform_data
from load import insert_countries, save_raw, save_processed
from utils.logger import get_logger

logger = get_logger()

logger.info('--- Iniciando Pipeline ---')
def main():
    try:
        logger.info('Iniciando extração')
        data = extract_data()

        logger.info('Salvando dados brutos')
        save_raw(data)

        logger.info('Transformando dados')
        df = transform_data(data)

        logger.info('Salvando dados transformados')
        save_processed(df)
        
        logger.info('Carregando dados ao banco')
        insert_countries(df)

        logger.info('Pipeline finalizado com sucesso')
    except Exception as e:
        logger.error(f'Erro no pipeline: {e}')
        raise

if __name__ == '__main__':
    main()