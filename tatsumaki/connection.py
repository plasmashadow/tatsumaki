from motor import MotorClient


class Connection(object):
    """connection bridge for motor client"""
    _instance = None

    def __new__(cls, *args, **kwds):
        if not cls._instance:
            cls._instance = \
                      super(Connection, cls).__new__(cls, *args, **kwds)
        return cls._instance

    @classmethod
    def connect(cls, uri):
        conn = Connection()
        conn._connection = MotorClient(uri)
        return conn

    @classmethod
    def get_connection(cls):
        return cls._instance

    @classmethod
    def close(cls):
        cls._instance = None


def connect(uri):
    return Connection.connect(uri)


def close():
    return Connection.close()
