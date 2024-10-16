# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DeviceDimensions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, depth: object=None, height: object=None, width: object=None):
        """DeviceDimensions - a model defined in OpenAPI

        :param depth: The depth of this DeviceDimensions.
        :param height: The height of this DeviceDimensions.
        :param width: The width of this DeviceDimensions.
        """
        self.openapi_types = {
            'depth': object,
            'height': object,
            'width': object
        }

        self.attribute_map = {
            'depth': 'depth',
            'height': 'height',
            'width': 'width'
        }

        self._depth = depth
        self._height = height
        self._width = width

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeviceDimensions':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeviceDimensions of this DeviceDimensions.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def depth(self):
        """Gets the depth of this DeviceDimensions.


        :return: The depth of this DeviceDimensions.
        :rtype: object
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this DeviceDimensions.


        :param depth: The depth of this DeviceDimensions.
        :type depth: object
        """

        self._depth = depth

    @property
    def height(self):
        """Gets the height of this DeviceDimensions.


        :return: The height of this DeviceDimensions.
        :rtype: object
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DeviceDimensions.


        :param height: The height of this DeviceDimensions.
        :type height: object
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this DeviceDimensions.


        :return: The width of this DeviceDimensions.
        :rtype: object
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DeviceDimensions.


        :param width: The width of this DeviceDimensions.
        :type width: object
        """

        self._width = width
