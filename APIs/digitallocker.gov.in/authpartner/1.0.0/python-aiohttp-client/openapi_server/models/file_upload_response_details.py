# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FileUploadResponseDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, path: str=None, size: str=None):
        """FileUploadResponseDetails - a model defined in OpenAPI

        :param path: The path of this FileUploadResponseDetails.
        :param size: The size of this FileUploadResponseDetails.
        """
        self.openapi_types = {
            'path': str,
            'size': str
        }

        self.attribute_map = {
            'path': 'Path',
            'size': 'size'
        }

        self._path = path
        self._size = size

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FileUploadResponseDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FileUploadResponse_details of this FileUploadResponseDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def path(self):
        """Gets the path of this FileUploadResponseDetails.

        The destination path of the file in DigiLocker including filename.

        :return: The path of this FileUploadResponseDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileUploadResponseDetails.

        The destination path of the file in DigiLocker including filename.

        :param path: The path of this FileUploadResponseDetails.
        :type path: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def size(self):
        """Gets the size of this FileUploadResponseDetails.

        Size of file.

        :return: The size of this FileUploadResponseDetails.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileUploadResponseDetails.

        Size of file.

        :param size: The size of this FileUploadResponseDetails.
        :type size: str
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size
