from schematics.types import *
from schematics.types.compound import *

try:
    from pymongo.dbref import DBRef
except ImportError:
    from bson.dbref import DBRef


class ReferenceType(BaseType):
    def __init__(self, *args, **kwds):
        self._model = args[0]
        super(ReferenceType, self).__init__(*args, **kwds)

    def to_primitive(self, value, context=None):
        return DBRef(self._model.__name__, str(value.id))

    def to_native(self, value, context=None):
        return DBRef(self._model.__name__, str(value.id))
