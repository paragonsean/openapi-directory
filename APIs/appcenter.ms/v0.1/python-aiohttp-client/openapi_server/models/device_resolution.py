# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DeviceResolution(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, height: str=None, ppi: str=None, width: str=None):
        """DeviceResolution - a model defined in OpenAPI

        :param height: The height of this DeviceResolution.
        :param ppi: The ppi of this DeviceResolution.
        :param width: The width of this DeviceResolution.
        """
        self.openapi_types = {
            'height': str,
            'ppi': str,
            'width': str
        }

        self.attribute_map = {
            'height': 'height',
            'ppi': 'ppi',
            'width': 'width'
        }

        self._height = height
        self._ppi = ppi
        self._width = width

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeviceResolution':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeviceResolution of this DeviceResolution.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def height(self):
        """Gets the height of this DeviceResolution.


        :return: The height of this DeviceResolution.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DeviceResolution.


        :param height: The height of this DeviceResolution.
        :type height: str
        """

        self._height = height

    @property
    def ppi(self):
        """Gets the ppi of this DeviceResolution.


        :return: The ppi of this DeviceResolution.
        :rtype: str
        """
        return self._ppi

    @ppi.setter
    def ppi(self, ppi):
        """Sets the ppi of this DeviceResolution.


        :param ppi: The ppi of this DeviceResolution.
        :type ppi: str
        """

        self._ppi = ppi

    @property
    def width(self):
        """Gets the width of this DeviceResolution.


        :return: The width of this DeviceResolution.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DeviceResolution.


        :param width: The width of this DeviceResolution.
        :type width: str
        """

        self._width = width
