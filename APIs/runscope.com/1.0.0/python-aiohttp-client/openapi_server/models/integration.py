# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Integration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, id: str=None, type: str=None, uuid: str=None):
        """Integration - a model defined in OpenAPI

        :param description: The description of this Integration.
        :param id: The id of this Integration.
        :param type: The type of this Integration.
        :param uuid: The uuid of this Integration.
        """
        self.openapi_types = {
            'description': str,
            'id': str,
            'type': str,
            'uuid': str
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'type': 'type',
            'uuid': 'uuid'
        }

        self._description = description
        self._id = id
        self._type = type
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Integration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Integration of this Integration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Integration.


        :return: The description of this Integration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Integration.


        :param description: The description of this Integration.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Integration.


        :return: The id of this Integration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Integration.


        :param id: The id of this Integration.
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Integration.


        :return: The type of this Integration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Integration.


        :param type: The type of this Integration.
        :type type: str
        """

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this Integration.


        :return: The uuid of this Integration.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Integration.


        :param uuid: The uuid of this Integration.
        :type uuid: str
        """

        self._uuid = uuid
