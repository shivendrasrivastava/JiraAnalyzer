__author__ = "Shiven"
import logging

logger = logging.getLogger("PyJIRA."+__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

#Decorator for loggers across the app
def simple_decorator(func):

	def wrapper(*args, **kwargs):
		'''Prints before and after'''
		logger.debug("Entering %s.%s " % (args[0].__class__.__name__, func.__name__))
		func(*args, **kwargs)
		logger.debug("Exiting %s.%s " % (args[0].__class__.__name__, func.__name__))

	return wrapper