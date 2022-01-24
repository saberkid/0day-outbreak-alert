import types

from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.properties import ColumnProperty
from sqlalchemy.orm.attributes import InstrumentedAttribute

from sqlalchemy.ext.declarative import declarative_base


_Base = declarative_base()


class Base(_Base):
    __abstract__ = True

    def to_dict(self):
        if getattr(self, '_sa_free', None):
            return {k: v for k, v in self.__dict__.iteritems()}
        attr_names = getattr(self.__class__, '__attr_names', None)
        if not attr_names:
            attr_names = [prop.key for prop in
                            class_mapper(self.__class__).iterate_properties if
                            isinstance(prop, ColumnProperty) and not prop.key.startswith('_')]
            for attr in dir(self.__class__):
                if isinstance(getattr(self.__class__, attr), (InstrumentedAttribute, property)) \
                        and not attr.startswith('_'):
                    attr_names.append(attr)
            setattr(self.__class__, '__attr_names', list(set(attr_names)))

        return {attr: getattr(self, attr) for attr in attr_names}
