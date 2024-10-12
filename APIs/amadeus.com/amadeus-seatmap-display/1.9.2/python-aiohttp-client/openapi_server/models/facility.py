# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.coordinates import Coordinates
from openapi_server import util


class Facility(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, column: str=None, coordinates: Coordinates=None, position: str=None, row: str=None):
        """Facility - a model defined in OpenAPI

        :param code: The code of this Facility.
        :param column: The column of this Facility.
        :param coordinates: The coordinates of this Facility.
        :param position: The position of this Facility.
        :param row: The row of this Facility.
        """
        self.openapi_types = {
            'code': str,
            'column': str,
            'coordinates': Coordinates,
            'position': str,
            'row': str
        }

        self.attribute_map = {
            'code': 'code',
            'column': 'column',
            'coordinates': 'coordinates',
            'position': 'position',
            'row': 'row'
        }

        self._code = code
        self._column = column
        self._coordinates = coordinates
        self._position = position
        self._row = row

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Facility':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Facility of this Facility.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this Facility.

        Facility code, as described in the facility dictionary

        :return: The code of this Facility.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Facility.

        Facility code, as described in the facility dictionary

        :param code: The code of this Facility.
        :type code: str
        """

        self._code = code

    @property
    def column(self):
        """Gets the column of this Facility.


        :return: The column of this Facility.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this Facility.


        :param column: The column of this Facility.
        :type column: str
        """

        self._column = column

    @property
    def coordinates(self):
        """Gets the coordinates of this Facility.


        :return: The coordinates of this Facility.
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Facility.


        :param coordinates: The coordinates of this Facility.
        :type coordinates: Coordinates
        """

        self._coordinates = coordinates

    @property
    def position(self):
        """Gets the position of this Facility.

        Position is either front, rear or seat (in case the facility takes the place of a seat)

        :return: The position of this Facility.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Facility.

        Position is either front, rear or seat (in case the facility takes the place of a seat)

        :param position: The position of this Facility.
        :type position: str
        """
        allowed_values = ["FRONT", "REAR", "SEAT"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"
                .format(position, allowed_values)
            )

        self._position = position

    @property
    def row(self):
        """Gets the row of this Facility.


        :return: The row of this Facility.
        :rtype: str
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this Facility.


        :param row: The row of this Facility.
        :type row: str
        """

        self._row = row
