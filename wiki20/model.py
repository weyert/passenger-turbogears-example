import pkg_resources
pkg_resources.require("SQLObject>=0.8,<=0.10.0")
from turbogears.database import PackageHub
# import some basic SQLObject classes for declaring the data model
# (see http://www.sqlobject.org/SQLObject.html#declaring-the-class)
from sqlobject import SQLObject, SQLObjectNotFound, RelatedJoin
# import some datatypes for table columns from SQLObject
# (see http://www.sqlobject.org/SQLObject.html#column-types for more)
from sqlobject import StringCol, UnicodeCol, IntCol, DateTimeCol

__connection__ = hub = PackageHub('wiki20')


# your data model
class Page(SQLObject):
    pagename = UnicodeCol(alternateID=True, length=30)
    data = UnicodeCol()

# class YourDataClass(SQLObject):
#     pass


