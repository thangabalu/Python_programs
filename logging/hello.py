import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


def hello():
    logger.info("hello")

def anotherhello():
    logger.debug("debug hello")


if __name__ == "__main__":
    hello()
    anotherhello()
