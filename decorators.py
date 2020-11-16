from functools import wraps
# this import allows for decorators to wrap each other

def timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper_func(*args, **kwargs):
		start = time.time()
		result = orig_func(*args, **kwargs)
		stop = time.time() - start
		print(f"Time elapsed: {stop}")
		return result

	return wrapper_func

def logger(orig_func):
	''' This guys is having problems when it's used multiple
	times in the same file. '''
	import logging
	logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

	@wraps(orig_func)
	def wrapper_func(*args, **kwargs):
		logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")
		return orig_func(*args, **kwargs)

	return wrapper_func

@timer
@logger
def print_boof():
	print('BOOF')

print_boof()

@timer
@logger
def print_info(name, age=32):
	print(f"My name is {name} and I'm {age} years old")

print_info('Bo')