import logging.config
import os.path

import yaml


def init(file='./conf/logger.yaml'):
    print(f'load logger configuration from {file}')
    if not os.path.exists(file):
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logger.yaml')
        print(f'logger configuration not found, will use default configuration: {file}')
    with open(file, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


# load logger configuration
init()


def get_logger(name):
    return logging.getLogger(name)


if __name__ == '__main__':
    init(file="../conf/logger.yaml")
    logger = logging.getLogger(__name__)
    logger.info("some message...........")
