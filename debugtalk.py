import time
import uuid

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def gen_memberId():
    return "2752571224732123"


def gen_nodeId():
    return str(uuid.uuid4())


def get_timestamp():
    return int(time.time() * 1000)
