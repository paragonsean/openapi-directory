# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ImageRegionCreateResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: datetime=None, height: float=None, image_id: str=None, left: float=None, region_id: str=None, tag_id: str=None, tag_name: str=None, top: float=None, width: float=None):
        """ImageRegionCreateResult - a model defined in OpenAPI

        :param created: The created of this ImageRegionCreateResult.
        :param height: The height of this ImageRegionCreateResult.
        :param image_id: The image_id of this ImageRegionCreateResult.
        :param left: The left of this ImageRegionCreateResult.
        :param region_id: The region_id of this ImageRegionCreateResult.
        :param tag_id: The tag_id of this ImageRegionCreateResult.
        :param tag_name: The tag_name of this ImageRegionCreateResult.
        :param top: The top of this ImageRegionCreateResult.
        :param width: The width of this ImageRegionCreateResult.
        """
        self.openapi_types = {
            'created': datetime,
            'height': float,
            'image_id': str,
            'left': float,
            'region_id': str,
            'tag_id': str,
            'tag_name': str,
            'top': float,
            'width': float
        }

        self.attribute_map = {
            'created': 'created',
            'height': 'height',
            'image_id': 'imageId',
            'left': 'left',
            'region_id': 'regionId',
            'tag_id': 'tagId',
            'tag_name': 'tagName',
            'top': 'top',
            'width': 'width'
        }

        self._created = created
        self._height = height
        self._image_id = image_id
        self._left = left
        self._region_id = region_id
        self._tag_id = tag_id
        self._tag_name = tag_name
        self._top = top
        self._width = width

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImageRegionCreateResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImageRegionCreateResult of this ImageRegionCreateResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this ImageRegionCreateResult.


        :return: The created of this ImageRegionCreateResult.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ImageRegionCreateResult.


        :param created: The created of this ImageRegionCreateResult.
        :type created: datetime
        """

        self._created = created

    @property
    def height(self):
        """Gets the height of this ImageRegionCreateResult.


        :return: The height of this ImageRegionCreateResult.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ImageRegionCreateResult.


        :param height: The height of this ImageRegionCreateResult.
        :type height: float
        """

        self._height = height

    @property
    def image_id(self):
        """Gets the image_id of this ImageRegionCreateResult.


        :return: The image_id of this ImageRegionCreateResult.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageRegionCreateResult.


        :param image_id: The image_id of this ImageRegionCreateResult.
        :type image_id: str
        """

        self._image_id = image_id

    @property
    def left(self):
        """Gets the left of this ImageRegionCreateResult.


        :return: The left of this ImageRegionCreateResult.
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this ImageRegionCreateResult.


        :param left: The left of this ImageRegionCreateResult.
        :type left: float
        """

        self._left = left

    @property
    def region_id(self):
        """Gets the region_id of this ImageRegionCreateResult.


        :return: The region_id of this ImageRegionCreateResult.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ImageRegionCreateResult.


        :param region_id: The region_id of this ImageRegionCreateResult.
        :type region_id: str
        """

        self._region_id = region_id

    @property
    def tag_id(self):
        """Gets the tag_id of this ImageRegionCreateResult.


        :return: The tag_id of this ImageRegionCreateResult.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this ImageRegionCreateResult.


        :param tag_id: The tag_id of this ImageRegionCreateResult.
        :type tag_id: str
        """

        self._tag_id = tag_id

    @property
    def tag_name(self):
        """Gets the tag_name of this ImageRegionCreateResult.


        :return: The tag_name of this ImageRegionCreateResult.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this ImageRegionCreateResult.


        :param tag_name: The tag_name of this ImageRegionCreateResult.
        :type tag_name: str
        """

        self._tag_name = tag_name

    @property
    def top(self):
        """Gets the top of this ImageRegionCreateResult.


        :return: The top of this ImageRegionCreateResult.
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this ImageRegionCreateResult.


        :param top: The top of this ImageRegionCreateResult.
        :type top: float
        """

        self._top = top

    @property
    def width(self):
        """Gets the width of this ImageRegionCreateResult.


        :return: The width of this ImageRegionCreateResult.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ImageRegionCreateResult.


        :param width: The width of this ImageRegionCreateResult.
        :type width: float
        """

        self._width = width
