# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.table_cells_details import TableCellsDetails
from openapi_server.models.table_tables_details import TableTablesDetails
from openapi_server import util


class TableColumnsDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cells: List[TableCellsDetails]=None, date_created: datetime=None, date_modified: datetime=None, id: str=None, index: int=None, table: TableTablesDetails=None, table_id: str=None, user_created: str=None, user_modified: str=None, width: int=None):
        """TableColumnsDetails - a model defined in OpenAPI

        :param cells: The cells of this TableColumnsDetails.
        :param date_created: The date_created of this TableColumnsDetails.
        :param date_modified: The date_modified of this TableColumnsDetails.
        :param id: The id of this TableColumnsDetails.
        :param index: The index of this TableColumnsDetails.
        :param table: The table of this TableColumnsDetails.
        :param table_id: The table_id of this TableColumnsDetails.
        :param user_created: The user_created of this TableColumnsDetails.
        :param user_modified: The user_modified of this TableColumnsDetails.
        :param width: The width of this TableColumnsDetails.
        """
        self.openapi_types = {
            'cells': List[TableCellsDetails],
            'date_created': datetime,
            'date_modified': datetime,
            'id': str,
            'index': int,
            'table': TableTablesDetails,
            'table_id': str,
            'user_created': str,
            'user_modified': str,
            'width': int
        }

        self.attribute_map = {
            'cells': 'cells',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'id': 'id',
            'index': 'index',
            'table': 'table',
            'table_id': 'tableId',
            'user_created': 'userCreated',
            'user_modified': 'userModified',
            'width': 'width'
        }

        self._cells = cells
        self._date_created = date_created
        self._date_modified = date_modified
        self._id = id
        self._index = index
        self._table = table
        self._table_id = table_id
        self._user_created = user_created
        self._user_modified = user_modified
        self._width = width

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TableColumnsDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Table.Columns.Details of this TableColumnsDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cells(self):
        """Gets the cells of this TableColumnsDetails.


        :return: The cells of this TableColumnsDetails.
        :rtype: List[TableCellsDetails]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """Sets the cells of this TableColumnsDetails.


        :param cells: The cells of this TableColumnsDetails.
        :type cells: List[TableCellsDetails]
        """

        self._cells = cells

    @property
    def date_created(self):
        """Gets the date_created of this TableColumnsDetails.


        :return: The date_created of this TableColumnsDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TableColumnsDetails.


        :param date_created: The date_created of this TableColumnsDetails.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this TableColumnsDetails.


        :return: The date_modified of this TableColumnsDetails.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this TableColumnsDetails.


        :param date_modified: The date_modified of this TableColumnsDetails.
        :type date_modified: datetime
        """

        self._date_modified = date_modified

    @property
    def id(self):
        """Gets the id of this TableColumnsDetails.


        :return: The id of this TableColumnsDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableColumnsDetails.


        :param id: The id of this TableColumnsDetails.
        :type id: str
        """

        self._id = id

    @property
    def index(self):
        """Gets the index of this TableColumnsDetails.


        :return: The index of this TableColumnsDetails.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TableColumnsDetails.


        :param index: The index of this TableColumnsDetails.
        :type index: int
        """

        self._index = index

    @property
    def table(self):
        """Gets the table of this TableColumnsDetails.


        :return: The table of this TableColumnsDetails.
        :rtype: TableTablesDetails
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this TableColumnsDetails.


        :param table: The table of this TableColumnsDetails.
        :type table: TableTablesDetails
        """

        self._table = table

    @property
    def table_id(self):
        """Gets the table_id of this TableColumnsDetails.


        :return: The table_id of this TableColumnsDetails.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this TableColumnsDetails.


        :param table_id: The table_id of this TableColumnsDetails.
        :type table_id: str
        """

        self._table_id = table_id

    @property
    def user_created(self):
        """Gets the user_created of this TableColumnsDetails.


        :return: The user_created of this TableColumnsDetails.
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this TableColumnsDetails.


        :param user_created: The user_created of this TableColumnsDetails.
        :type user_created: str
        """

        self._user_created = user_created

    @property
    def user_modified(self):
        """Gets the user_modified of this TableColumnsDetails.


        :return: The user_modified of this TableColumnsDetails.
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this TableColumnsDetails.


        :param user_modified: The user_modified of this TableColumnsDetails.
        :type user_modified: str
        """

        self._user_modified = user_modified

    @property
    def width(self):
        """Gets the width of this TableColumnsDetails.


        :return: The width of this TableColumnsDetails.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TableColumnsDetails.


        :param width: The width of this TableColumnsDetails.
        :type width: int
        """

        self._width = width
