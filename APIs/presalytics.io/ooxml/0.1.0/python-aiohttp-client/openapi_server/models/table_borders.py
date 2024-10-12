# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TableBorders(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cell_id: str=None, id: str=None):
        """TableBorders - a model defined in OpenAPI

        :param cell_id: The cell_id of this TableBorders.
        :param id: The id of this TableBorders.
        """
        self.openapi_types = {
            'cell_id': str,
            'id': str
        }

        self.attribute_map = {
            'cell_id': 'cellId',
            'id': 'id'
        }

        self._cell_id = cell_id
        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TableBorders':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Table.Borders of this TableBorders.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cell_id(self):
        """Gets the cell_id of this TableBorders.


        :return: The cell_id of this TableBorders.
        :rtype: str
        """
        return self._cell_id

    @cell_id.setter
    def cell_id(self, cell_id):
        """Sets the cell_id of this TableBorders.


        :param cell_id: The cell_id of this TableBorders.
        :type cell_id: str
        """

        self._cell_id = cell_id

    @property
    def id(self):
        """Gets the id of this TableBorders.


        :return: The id of this TableBorders.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TableBorders.


        :param id: The id of this TableBorders.
        :type id: str
        """

        self._id = id
