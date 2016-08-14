from schematics.types import *
from schematics.types.compound import *

try:
    from pymongo.dbref import DBRef
except ImportError:
    from bson.dbref import DBRef

class TypeBase(BaseType):

    def __le__(self, value):
        pass

    def __ge__(self, value):
        pass

    def __lt__(self, value):
        pass

    def __gt__(self, value):
        pass

    def __eq__(self, value):
        pass

class ReferenceType(TypeBase):
    def __init__(self, *args, **kwds):
        self._model = args[0]
        super(ReferenceType, self).__init__(*args, **kwds)

    def to_primitive(self, value, context=None):
        return DBRef(self._model.__name__, str(value.id))

    def to_native(self, value, context=None):
        return DBRef(self._model.__name__, str(value.id))
