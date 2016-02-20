__author__ = "Shiven"
import logging

logger = logging.getLogger("PyJIRA."+__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger_main = logging.getLogger("PyJIRA."+"retrieve.main")
logger_main.setLevel(logging.DEBUG)
handler_main = logging.StreamHandler()
handler_main.setLevel(logging.DEBUG)
logger_main.addHandler(handler_main)
handler_main.setFormatter(formatter)

logger_parse = logging.getLogger("PyJIRA."+"retrieve.parse")
logger_parse.setLevel(logging.DEBUG)
handler_parse = logging.StreamHandler()
handler_parse.setLevel(logging.DEBUG)
logger_parse.addHandler(handler_parse)
handler_parse.setFormatter(formatter)

logger_pool = logging.getLogger("PyJIRA."+"retrieve.pool")
logger_pool.setLevel(logging.DEBUG)
handler_pool = logging.StreamHandler()
handler_pool.setLevel(logging.DEBUG)
logger_pool.addHandler(handler_pool)
handler_pool.setFormatter(formatter)

logger_file = logging.getLogger("PyJIRA."+"retrieve.file_manager")
logger_file.setLevel(logging.DEBUG)
handler_file = logging.StreamHandler()
handler_file.setLevel(logging.DEBUG)
logger_file.addHandler(handler_file)
handler_file.setFormatter(formatter)

logger_connect = logging.getLogger("PyJIRA."+"retrieve.connect")
logger_connect.setLevel(logging.DEBUG)
handler_connect = logging.StreamHandler()
handler_connect.setLevel(logging.DEBUG)
logger_connect.addHandler(handler_connect)
handler_connect.setFormatter(formatter)

#Decorator for loggers across the app
def simple_decorator(func):

	def wrapper(*args, **kwargs):
		'''Prints before and after'''
		logger.debug("Entering %s.%s " % (args[0].__class__.__name__, func.__name__))
		func(*args, **kwargs)
		logger.debug("Exiting %s.%s " % (args[0].__class__.__name__, func.__name__))

	return wrapper