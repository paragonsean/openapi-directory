# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ImportRDBParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, files: List[str]=None, format: str=None):
        """ImportRDBParameters - a model defined in OpenAPI

        :param files: The files of this ImportRDBParameters.
        :param format: The format of this ImportRDBParameters.
        """
        self.openapi_types = {
            'files': List[str],
            'format': str
        }

        self.attribute_map = {
            'files': 'files',
            'format': 'format'
        }

        self._files = files
        self._format = format

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImportRDBParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImportRDBParameters of this ImportRDBParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def files(self):
        """Gets the files of this ImportRDBParameters.

        files to import.

        :return: The files of this ImportRDBParameters.
        :rtype: List[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ImportRDBParameters.

        files to import.

        :param files: The files of this ImportRDBParameters.
        :type files: List[str]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")

        self._files = files

    @property
    def format(self):
        """Gets the format of this ImportRDBParameters.

        File format.

        :return: The format of this ImportRDBParameters.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ImportRDBParameters.

        File format.

        :param format: The format of this ImportRDBParameters.
        :type format: str
        """

        self._format = format
