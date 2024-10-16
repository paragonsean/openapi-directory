# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PreviewFileAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image: str=None, image_hash: str=None, page_count: int=None, size: int=None):
        """PreviewFileAttributes - a model defined in OpenAPI

        :param image: The image of this PreviewFileAttributes.
        :param image_hash: The image_hash of this PreviewFileAttributes.
        :param page_count: The page_count of this PreviewFileAttributes.
        :param size: The size of this PreviewFileAttributes.
        """
        self.openapi_types = {
            'image': str,
            'image_hash': str,
            'page_count': int,
            'size': int
        }

        self.attribute_map = {
            'image': 'image',
            'image_hash': 'imageHash',
            'page_count': 'pageCount',
            'size': 'size'
        }

        self._image = image
        self._image_hash = image_hash
        self._page_count = page_count
        self._size = size

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PreviewFileAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PreviewFile_attributes of this PreviewFileAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image(self):
        """Gets the image of this PreviewFileAttributes.

        Binary image content, base64 encoded.

        :return: The image of this PreviewFileAttributes.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PreviewFileAttributes.

        Binary image content, base64 encoded.

        :param image: The image of this PreviewFileAttributes.
        :type image: str
        """

        self._image = image

    @property
    def image_hash(self):
        """Gets the image_hash of this PreviewFileAttributes.

        hash of the image.

        :return: The image_hash of this PreviewFileAttributes.
        :rtype: str
        """
        return self._image_hash

    @image_hash.setter
    def image_hash(self, image_hash):
        """Sets the image_hash of this PreviewFileAttributes.

        hash of the image.

        :param image_hash: The image_hash of this PreviewFileAttributes.
        :type image_hash: str
        """

        self._image_hash = image_hash

    @property
    def page_count(self):
        """Gets the page_count of this PreviewFileAttributes.

        Amount of pages available in the file. Used only for multipage documents.

        :return: The page_count of this PreviewFileAttributes.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this PreviewFileAttributes.

        Amount of pages available in the file. Used only for multipage documents.

        :param page_count: The page_count of this PreviewFileAttributes.
        :type page_count: int
        """

        self._page_count = page_count

    @property
    def size(self):
        """Gets the size of this PreviewFileAttributes.

        Size of the image in bytes.

        :return: The size of this PreviewFileAttributes.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PreviewFileAttributes.

        Size of the image in bytes.

        :param size: The size of this PreviewFileAttributes.
        :type size: int
        """

        self._size = size
