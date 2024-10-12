# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BrowseResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_mode: str=None, filename: str=None, last_modified: str=None, path: str=None, size: int=None, status_message: str=None, unreadable: int=None):
        """BrowseResponse - a model defined in OpenAPI

        :param file_mode: The file_mode of this BrowseResponse.
        :param filename: The filename of this BrowseResponse.
        :param last_modified: The last_modified of this BrowseResponse.
        :param path: The path of this BrowseResponse.
        :param size: The size of this BrowseResponse.
        :param status_message: The status_message of this BrowseResponse.
        :param unreadable: The unreadable of this BrowseResponse.
        """
        self.openapi_types = {
            'file_mode': str,
            'filename': str,
            'last_modified': str,
            'path': str,
            'size': int,
            'status_message': str,
            'unreadable': int
        }

        self.attribute_map = {
            'file_mode': 'fileMode',
            'filename': 'filename',
            'last_modified': 'lastModified',
            'path': 'path',
            'size': 'size',
            'status_message': 'statusMessage',
            'unreadable': 'unreadable'
        }

        self._file_mode = file_mode
        self._filename = filename
        self._last_modified = last_modified
        self._path = path
        self._size = size
        self._status_message = status_message
        self._unreadable = unreadable

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BrowseResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BrowseResponse of this BrowseResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_mode(self):
        """Gets the file_mode of this BrowseResponse.

        The type of file, either a regular file or a directory.

        :return: The file_mode of this BrowseResponse.
        :rtype: str
        """
        return self._file_mode

    @file_mode.setter
    def file_mode(self, file_mode):
        """Sets the file_mode of this BrowseResponse.

        The type of file, either a regular file or a directory.

        :param file_mode: The file_mode of this BrowseResponse.
        :type file_mode: str
        """

        self._file_mode = file_mode

    @property
    def filename(self):
        """Gets the filename of this BrowseResponse.

        The name of the file.

        :return: The filename of this BrowseResponse.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BrowseResponse.

        The name of the file.

        :param filename: The filename of this BrowseResponse.
        :type filename: str
        """

        self._filename = filename

    @property
    def last_modified(self):
        """Gets the last_modified of this BrowseResponse.


        :return: The last_modified of this BrowseResponse.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this BrowseResponse.


        :param last_modified: The last_modified of this BrowseResponse.
        :type last_modified: str
        """

        self._last_modified = last_modified

    @property
    def path(self):
        """Gets the path of this BrowseResponse.

        The complete path of the file.

        :return: The path of this BrowseResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BrowseResponse.

        The complete path of the file.

        :param path: The path of this BrowseResponse.
        :type path: str
        """

        self._path = path

    @property
    def size(self):
        """Gets the size of this BrowseResponse.


        :return: The size of this BrowseResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BrowseResponse.


        :param size: The size of this BrowseResponse.
        :type size: int
        """

        self._size = size

    @property
    def status_message(self):
        """Gets the status_message of this BrowseResponse.

        Description about the status.

        :return: The status_message of this BrowseResponse.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this BrowseResponse.

        Description about the status.

        :param status_message: The status_message of this BrowseResponse.
        :type status_message: str
        """

        self._status_message = status_message

    @property
    def unreadable(self):
        """Gets the unreadable of this BrowseResponse.

        Reason the file is unreadable. Undefined if the file is readable.

        :return: The unreadable of this BrowseResponse.
        :rtype: int
        """
        return self._unreadable

    @unreadable.setter
    def unreadable(self, unreadable):
        """Sets the unreadable of this BrowseResponse.

        Reason the file is unreadable. Undefined if the file is readable.

        :param unreadable: The unreadable of this BrowseResponse.
        :type unreadable: int
        """

        self._unreadable = unreadable
