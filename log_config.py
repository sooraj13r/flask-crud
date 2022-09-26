import logging
def config_log():
    logging.basicConfig(level=logging.INFO, filename='devlog.log',format='%(asctime)s %(levelname)-8s %(message)s',filemode='a')
