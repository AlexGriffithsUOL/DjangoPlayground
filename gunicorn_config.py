from multiprocessing import cpu_count
from os import environ

logger_verbosity = environ['LOGGER_VERBOSITY']

max_requests = environ['MAX_REQUESTS_GUNICORN']
work_class = 'sync'