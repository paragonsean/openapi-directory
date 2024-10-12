# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DocumentType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, file_extension: str=None, id: str=None, mime_type: str=None, name: str=None, ooxml_package_type: str=None, type_id: int=None):
        """DocumentType - a model defined in OpenAPI

        :param description: The description of this DocumentType.
        :param file_extension: The file_extension of this DocumentType.
        :param id: The id of this DocumentType.
        :param mime_type: The mime_type of this DocumentType.
        :param name: The name of this DocumentType.
        :param ooxml_package_type: The ooxml_package_type of this DocumentType.
        :param type_id: The type_id of this DocumentType.
        """
        self.openapi_types = {
            'description': str,
            'file_extension': str,
            'id': str,
            'mime_type': str,
            'name': str,
            'ooxml_package_type': str,
            'type_id': int
        }

        self.attribute_map = {
            'description': 'description',
            'file_extension': 'fileExtension',
            'id': 'id',
            'mime_type': 'mimeType',
            'name': 'name',
            'ooxml_package_type': 'ooxmlPackageType',
            'type_id': 'typeId'
        }

        self._description = description
        self._file_extension = file_extension
        self._id = id
        self._mime_type = mime_type
        self._name = name
        self._ooxml_package_type = ooxml_package_type
        self._type_id = type_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DocumentType':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DocumentType of this DocumentType.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this DocumentType.


        :return: The description of this DocumentType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentType.


        :param description: The description of this DocumentType.
        :type description: str
        """

        self._description = description

    @property
    def file_extension(self):
        """Gets the file_extension of this DocumentType.


        :return: The file_extension of this DocumentType.
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this DocumentType.


        :param file_extension: The file_extension of this DocumentType.
        :type file_extension: str
        """

        self._file_extension = file_extension

    @property
    def id(self):
        """Gets the id of this DocumentType.


        :return: The id of this DocumentType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentType.


        :param id: The id of this DocumentType.
        :type id: str
        """

        self._id = id

    @property
    def mime_type(self):
        """Gets the mime_type of this DocumentType.


        :return: The mime_type of this DocumentType.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this DocumentType.


        :param mime_type: The mime_type of this DocumentType.
        :type mime_type: str
        """

        self._mime_type = mime_type

    @property
    def name(self):
        """Gets the name of this DocumentType.


        :return: The name of this DocumentType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentType.


        :param name: The name of this DocumentType.
        :type name: str
        """

        self._name = name

    @property
    def ooxml_package_type(self):
        """Gets the ooxml_package_type of this DocumentType.


        :return: The ooxml_package_type of this DocumentType.
        :rtype: str
        """
        return self._ooxml_package_type

    @ooxml_package_type.setter
    def ooxml_package_type(self, ooxml_package_type):
        """Sets the ooxml_package_type of this DocumentType.


        :param ooxml_package_type: The ooxml_package_type of this DocumentType.
        :type ooxml_package_type: str
        """

        self._ooxml_package_type = ooxml_package_type

    @property
    def type_id(self):
        """Gets the type_id of this DocumentType.


        :return: The type_id of this DocumentType.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this DocumentType.


        :param type_id: The type_id of this DocumentType.
        :type type_id: int
        """

        self._type_id = type_id
