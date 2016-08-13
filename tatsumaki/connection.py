from motor import MotorClient
from tornado.gen import coroutine
from tornado.gen import Return
from .exc import TatsumakiException

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
        try:
            return cls._instance._connection
        except Exception:
            raise TatsumakiException("No database found")

    @classmethod
    def close(cls):
        cls._instance = None

    @classmethod
    def get_collection(cls, collection_name):
        try:
            client = cls._instance._connection
            name = client.get_default_database()
            database = client[name.name]
            if not database:
                raise TatsumakiException("Cannot establish connection to collection\
                                            :%s" % (collection_name))
        except AttributeError:
            raise TatsumakiException("Cannot establish connection to collection\
                                        :%s" % (collection_name))
        mongo_collection = getattr(database, collection_name)
        return mongo_collection


def connect(uri):
    return Connection.connect(uri)


def close():
    return Connection.close()
