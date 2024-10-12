# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Region(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, height: float=None, left: float=None, tag_id: str=None, top: float=None, width: float=None):
        """Region - a model defined in OpenAPI

        :param height: The height of this Region.
        :param left: The left of this Region.
        :param tag_id: The tag_id of this Region.
        :param top: The top of this Region.
        :param width: The width of this Region.
        """
        self.openapi_types = {
            'height': float,
            'left': float,
            'tag_id': str,
            'top': float,
            'width': float
        }

        self.attribute_map = {
            'height': 'height',
            'left': 'left',
            'tag_id': 'tagId',
            'top': 'top',
            'width': 'width'
        }

        self._height = height
        self._left = left
        self._tag_id = tag_id
        self._top = top
        self._width = width

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Region':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Region of this Region.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def height(self):
        """Gets the height of this Region.

        Height.

        :return: The height of this Region.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Region.

        Height.

        :param height: The height of this Region.
        :type height: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")

        self._height = height

    @property
    def left(self):
        """Gets the left of this Region.

        Coordinate of the left boundary.

        :return: The left of this Region.
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this Region.

        Coordinate of the left boundary.

        :param left: The left of this Region.
        :type left: float
        """
        if left is None:
            raise ValueError("Invalid value for `left`, must not be `None`")

        self._left = left

    @property
    def tag_id(self):
        """Gets the tag_id of this Region.

        Id of the tag associated with this region.

        :return: The tag_id of this Region.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this Region.

        Id of the tag associated with this region.

        :param tag_id: The tag_id of this Region.
        :type tag_id: str
        """
        if tag_id is None:
            raise ValueError("Invalid value for `tag_id`, must not be `None`")

        self._tag_id = tag_id

    @property
    def top(self):
        """Gets the top of this Region.

        Coordinate of the top boundary.

        :return: The top of this Region.
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this Region.

        Coordinate of the top boundary.

        :param top: The top of this Region.
        :type top: float
        """
        if top is None:
            raise ValueError("Invalid value for `top`, must not be `None`")

        self._top = top

    @property
    def width(self):
        """Gets the width of this Region.

        Width.

        :return: The width of this Region.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Region.

        Width.

        :param width: The width of this Region.
        :type width: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")

        self._width = width
