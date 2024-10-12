# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.entity_type import EntityType
from openapi_server.models.group import Group
from openapi_server.models.reference import Reference
from openapi_server import util


class BaseServiceGroup(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_id: str=None, entity_type: EntityType=None, name: str=None, members: List[Reference]=None):
        """BaseServiceGroup - a model defined in OpenAPI

        :param entity_id: The entity_id of this BaseServiceGroup.
        :param entity_type: The entity_type of this BaseServiceGroup.
        :param name: The name of this BaseServiceGroup.
        :param members: The members of this BaseServiceGroup.
        """
        self.openapi_types = {
            'entity_id': str,
            'entity_type': EntityType,
            'name': str,
            'members': List[Reference]
        }

        self.attribute_map = {
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'name': 'name',
            'members': 'members'
        }

        self._entity_id = entity_id
        self._entity_type = entity_type
        self._name = name
        self._members = members

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BaseServiceGroup':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BaseServiceGroup of this BaseServiceGroup.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_id(self):
        """Gets the entity_id of this BaseServiceGroup.


        :return: The entity_id of this BaseServiceGroup.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this BaseServiceGroup.


        :param entity_id: The entity_id of this BaseServiceGroup.
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this BaseServiceGroup.


        :return: The entity_type of this BaseServiceGroup.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this BaseServiceGroup.


        :param entity_type: The entity_type of this BaseServiceGroup.
        :type entity_type: EntityType
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this BaseServiceGroup.


        :return: The name of this BaseServiceGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseServiceGroup.


        :param name: The name of this BaseServiceGroup.
        :type name: str
        """

        self._name = name

    @property
    def members(self):
        """Gets the members of this BaseServiceGroup.


        :return: The members of this BaseServiceGroup.
        :rtype: List[Reference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this BaseServiceGroup.


        :param members: The members of this BaseServiceGroup.
        :type members: List[Reference]
        """

        self._members = members
