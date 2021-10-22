from time import time_ns
from uuid import uuid4


def uploads_url_with_instance(obj, name: str):
    return uploads_url(name)


def uploads_url(name: str):
    ext: str = name.split('.')[-1]
    return "{0}.{1}".format(str(time_ns())[:9], ext)


def gen_uuid():
    return str(uuid4()).replace("-", "")