import logging as lg

def get_logger():
    lg.basicConfig(
        level=lg.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        filename='Downloads/etl_countries_project/src/utils/pipeline.log'
    )
    return lg.getLogger()