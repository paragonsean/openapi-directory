# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Metadata1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bearing: str=None, columns: List[str]=None, name: str=None, rows: List[str]=None, segment_id: str=None, state: str=None):
        """Metadata1 - a model defined in OpenAPI

        :param bearing: The bearing of this Metadata1.
        :param columns: The columns of this Metadata1.
        :param name: The name of this Metadata1.
        :param rows: The rows of this Metadata1.
        :param segment_id: The segment_id of this Metadata1.
        :param state: The state of this Metadata1.
        """
        self.openapi_types = {
            'bearing': str,
            'columns': List[str],
            'name': str,
            'rows': List[str],
            'segment_id': str,
            'state': str
        }

        self.attribute_map = {
            'bearing': 'bearing',
            'columns': 'columns',
            'name': 'name',
            'rows': 'rows',
            'segment_id': 'segment_id',
            'state': 'state'
        }

        self._bearing = bearing
        self._columns = columns
        self._name = name
        self._rows = rows
        self._segment_id = segment_id
        self._state = state

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Metadata1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Metadata1 of this Metadata1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bearing(self):
        """Gets the bearing of this Metadata1.


        :return: The bearing of this Metadata1.
        :rtype: str
        """
        return self._bearing

    @bearing.setter
    def bearing(self, bearing):
        """Sets the bearing of this Metadata1.


        :param bearing: The bearing of this Metadata1.
        :type bearing: str
        """
        if bearing is None:
            raise ValueError("Invalid value for `bearing`, must not be `None`")

        self._bearing = bearing

    @property
    def columns(self):
        """Gets the columns of this Metadata1.


        :return: The columns of this Metadata1.
        :rtype: List[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Metadata1.


        :param columns: The columns of this Metadata1.
        :type columns: List[str]
        """
        if columns is None:
            raise ValueError("Invalid value for `columns`, must not be `None`")

        self._columns = columns

    @property
    def name(self):
        """Gets the name of this Metadata1.


        :return: The name of this Metadata1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metadata1.


        :param name: The name of this Metadata1.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def rows(self):
        """Gets the rows of this Metadata1.


        :return: The rows of this Metadata1.
        :rtype: List[str]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this Metadata1.


        :param rows: The rows of this Metadata1.
        :type rows: List[str]
        """
        if rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")

        self._rows = rows

    @property
    def segment_id(self):
        """Gets the segment_id of this Metadata1.


        :return: The segment_id of this Metadata1.
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this Metadata1.


        :param segment_id: The segment_id of this Metadata1.
        :type segment_id: str
        """
        if segment_id is None:
            raise ValueError("Invalid value for `segment_id`, must not be `None`")

        self._segment_id = segment_id

    @property
    def state(self):
        """Gets the state of this Metadata1.


        :return: The state of this Metadata1.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Metadata1.


        :param state: The state of this Metadata1.
        :type state: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")

        self._state = state
