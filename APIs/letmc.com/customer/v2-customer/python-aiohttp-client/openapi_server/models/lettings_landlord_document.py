# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LettingsLandlordDocument(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_name: str=None, file_size: int=None, id: str=None, mime_type: str=None, note: str=None):
        """LettingsLandlordDocument - a model defined in OpenAPI

        :param file_name: The file_name of this LettingsLandlordDocument.
        :param file_size: The file_size of this LettingsLandlordDocument.
        :param id: The id of this LettingsLandlordDocument.
        :param mime_type: The mime_type of this LettingsLandlordDocument.
        :param note: The note of this LettingsLandlordDocument.
        """
        self.openapi_types = {
            'file_name': str,
            'file_size': int,
            'id': str,
            'mime_type': str,
            'note': str
        }

        self.attribute_map = {
            'file_name': 'FileName',
            'file_size': 'FileSize',
            'id': 'ID',
            'mime_type': 'MIMEType',
            'note': 'Note'
        }

        self._file_name = file_name
        self._file_size = file_size
        self._id = id
        self._mime_type = mime_type
        self._note = note

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LettingsLandlordDocument':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LettingsLandlordDocument of this LettingsLandlordDocument.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_name(self):
        """Gets the file_name of this LettingsLandlordDocument.

        File Name

        :return: The file_name of this LettingsLandlordDocument.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this LettingsLandlordDocument.

        File Name

        :param file_name: The file_name of this LettingsLandlordDocument.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this LettingsLandlordDocument.

        File Size Bytes

        :return: The file_size of this LettingsLandlordDocument.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this LettingsLandlordDocument.

        File Size Bytes

        :param file_size: The file_size of this LettingsLandlordDocument.
        :type file_size: int
        """

        self._file_size = file_size

    @property
    def id(self):
        """Gets the id of this LettingsLandlordDocument.

        ID

        :return: The id of this LettingsLandlordDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LettingsLandlordDocument.

        ID

        :param id: The id of this LettingsLandlordDocument.
        :type id: str
        """

        self._id = id

    @property
    def mime_type(self):
        """Gets the mime_type of this LettingsLandlordDocument.

        MIME Type

        :return: The mime_type of this LettingsLandlordDocument.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this LettingsLandlordDocument.

        MIME Type

        :param mime_type: The mime_type of this LettingsLandlordDocument.
        :type mime_type: str
        """

        self._mime_type = mime_type

    @property
    def note(self):
        """Gets the note of this LettingsLandlordDocument.

        Document Note

        :return: The note of this LettingsLandlordDocument.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this LettingsLandlordDocument.

        Document Note

        :param note: The note of this LettingsLandlordDocument.
        :type note: str
        """

        self._note = note
