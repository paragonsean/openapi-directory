# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.upload_file_part import UploadFilePart
from openapi_server import util


class UploadInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, md5: str=None, name: str=None, parts: List[UploadFilePart]=None, size: int=None, status: str=None, token: str=None):
        """UploadInfo - a model defined in OpenAPI

        :param md5: The md5 of this UploadInfo.
        :param name: The name of this UploadInfo.
        :param parts: The parts of this UploadInfo.
        :param size: The size of this UploadInfo.
        :param status: The status of this UploadInfo.
        :param token: The token of this UploadInfo.
        """
        self.openapi_types = {
            'md5': str,
            'name': str,
            'parts': List[UploadFilePart],
            'size': int,
            'status': str,
            'token': str
        }

        self.attribute_map = {
            'md5': 'md5',
            'name': 'name',
            'parts': 'parts',
            'size': 'size',
            'status': 'status',
            'token': 'token'
        }

        self._md5 = md5
        self._name = name
        self._parts = parts
        self._size = size
        self._status = status
        self._token = token

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UploadInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UploadInfo of this UploadInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def md5(self):
        """Gets the md5 of this UploadInfo.

        md5 provided on upload initialization

        :return: The md5 of this UploadInfo.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this UploadInfo.

        md5 provided on upload initialization

        :param md5: The md5 of this UploadInfo.
        :type md5: str
        """

        self._md5 = md5

    @property
    def name(self):
        """Gets the name of this UploadInfo.

        name of file on upload server

        :return: The name of this UploadInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UploadInfo.

        name of file on upload server

        :param name: The name of this UploadInfo.
        :type name: str
        """

        self._name = name

    @property
    def parts(self):
        """Gets the parts of this UploadInfo.

        Uploads parts

        :return: The parts of this UploadInfo.
        :rtype: List[UploadFilePart]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this UploadInfo.

        Uploads parts

        :param parts: The parts of this UploadInfo.
        :type parts: List[UploadFilePart]
        """

        self._parts = parts

    @property
    def size(self):
        """Gets the size of this UploadInfo.

        size of file in bytes

        :return: The size of this UploadInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UploadInfo.

        size of file in bytes

        :param size: The size of this UploadInfo.
        :type size: int
        """

        self._size = size

    @property
    def status(self):
        """Gets the status of this UploadInfo.

        Upload status

        :return: The status of this UploadInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UploadInfo.

        Upload status

        :param status: The status of this UploadInfo.
        :type status: str
        """
        allowed_values = ["PENDING", "COMPLETED", "ABORTED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def token(self):
        """Gets the token of this UploadInfo.

        token received after initializing a file upload

        :return: The token of this UploadInfo.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UploadInfo.

        token received after initializing a file upload

        :param token: The token of this UploadInfo.
        :type token: str
        """

        self._token = token
