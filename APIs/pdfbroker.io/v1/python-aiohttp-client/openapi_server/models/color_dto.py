# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ColorDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, b: int=None, g: int=None, r: int=None):
        """ColorDto - a model defined in OpenAPI

        :param b: The b of this ColorDto.
        :param g: The g of this ColorDto.
        :param r: The r of this ColorDto.
        """
        self.openapi_types = {
            'b': int,
            'g': int,
            'r': int
        }

        self.attribute_map = {
            'b': 'b',
            'g': 'g',
            'r': 'r'
        }

        self._b = b
        self._g = g
        self._r = r

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ColorDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ColorDto of this ColorDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def b(self):
        """Gets the b of this ColorDto.

        Get or sets B value of RGB color

        :return: The b of this ColorDto.
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this ColorDto.

        Get or sets B value of RGB color

        :param b: The b of this ColorDto.
        :type b: int
        """
        if b is not None and b > 255:
            raise ValueError("Invalid value for `b`, must be a value less than or equal to `255`")
        if b is not None and b < 0:
            raise ValueError("Invalid value for `b`, must be a value greater than or equal to `0`")

        self._b = b

    @property
    def g(self):
        """Gets the g of this ColorDto.

        Get or sets G value of RGB color

        :return: The g of this ColorDto.
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this ColorDto.

        Get or sets G value of RGB color

        :param g: The g of this ColorDto.
        :type g: int
        """
        if g is not None and g > 255:
            raise ValueError("Invalid value for `g`, must be a value less than or equal to `255`")
        if g is not None and g < 0:
            raise ValueError("Invalid value for `g`, must be a value greater than or equal to `0`")

        self._g = g

    @property
    def r(self):
        """Gets the r of this ColorDto.

        Get or sets R value of RGB color

        :return: The r of this ColorDto.
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this ColorDto.

        Get or sets R value of RGB color

        :param r: The r of this ColorDto.
        :type r: int
        """
        if r is not None and r > 255:
            raise ValueError("Invalid value for `r`, must be a value less than or equal to `255`")
        if r is not None and r < 0:
            raise ValueError("Invalid value for `r`, must be a value greater than or equal to `0`")

        self._r = r
