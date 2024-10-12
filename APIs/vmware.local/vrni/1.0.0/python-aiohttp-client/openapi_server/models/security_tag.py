# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.base_entity import BaseEntity
from openapi_server.models.entity_type import EntityType
from openapi_server.models.reference import Reference
from openapi_server import util


class SecurityTag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_id: str=None, entity_type: EntityType=None, name: str=None, description: str=None, direct_security_groups: List[Reference]=None, nsx_manager: Reference=None, security_groups: List[Reference]=None, vendor_id: str=None):
        """SecurityTag - a model defined in OpenAPI

        :param entity_id: The entity_id of this SecurityTag.
        :param entity_type: The entity_type of this SecurityTag.
        :param name: The name of this SecurityTag.
        :param description: The description of this SecurityTag.
        :param direct_security_groups: The direct_security_groups of this SecurityTag.
        :param nsx_manager: The nsx_manager of this SecurityTag.
        :param security_groups: The security_groups of this SecurityTag.
        :param vendor_id: The vendor_id of this SecurityTag.
        """
        self.openapi_types = {
            'entity_id': str,
            'entity_type': EntityType,
            'name': str,
            'description': str,
            'direct_security_groups': List[Reference],
            'nsx_manager': Reference,
            'security_groups': List[Reference],
            'vendor_id': str
        }

        self.attribute_map = {
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'name': 'name',
            'description': 'description',
            'direct_security_groups': 'direct_security_groups',
            'nsx_manager': 'nsx_manager',
            'security_groups': 'security_groups',
            'vendor_id': 'vendor_id'
        }

        self._entity_id = entity_id
        self._entity_type = entity_type
        self._name = name
        self._description = description
        self._direct_security_groups = direct_security_groups
        self._nsx_manager = nsx_manager
        self._security_groups = security_groups
        self._vendor_id = vendor_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SecurityTag':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SecurityTag of this SecurityTag.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_id(self):
        """Gets the entity_id of this SecurityTag.


        :return: The entity_id of this SecurityTag.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this SecurityTag.


        :param entity_id: The entity_id of this SecurityTag.
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this SecurityTag.


        :return: The entity_type of this SecurityTag.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this SecurityTag.


        :param entity_type: The entity_type of this SecurityTag.
        :type entity_type: EntityType
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """Gets the name of this SecurityTag.


        :return: The name of this SecurityTag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityTag.


        :param name: The name of this SecurityTag.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SecurityTag.


        :return: The description of this SecurityTag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityTag.


        :param description: The description of this SecurityTag.
        :type description: str
        """

        self._description = description

    @property
    def direct_security_groups(self):
        """Gets the direct_security_groups of this SecurityTag.


        :return: The direct_security_groups of this SecurityTag.
        :rtype: List[Reference]
        """
        return self._direct_security_groups

    @direct_security_groups.setter
    def direct_security_groups(self, direct_security_groups):
        """Sets the direct_security_groups of this SecurityTag.


        :param direct_security_groups: The direct_security_groups of this SecurityTag.
        :type direct_security_groups: List[Reference]
        """

        self._direct_security_groups = direct_security_groups

    @property
    def nsx_manager(self):
        """Gets the nsx_manager of this SecurityTag.


        :return: The nsx_manager of this SecurityTag.
        :rtype: Reference
        """
        return self._nsx_manager

    @nsx_manager.setter
    def nsx_manager(self, nsx_manager):
        """Sets the nsx_manager of this SecurityTag.


        :param nsx_manager: The nsx_manager of this SecurityTag.
        :type nsx_manager: Reference
        """

        self._nsx_manager = nsx_manager

    @property
    def security_groups(self):
        """Gets the security_groups of this SecurityTag.


        :return: The security_groups of this SecurityTag.
        :rtype: List[Reference]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this SecurityTag.


        :param security_groups: The security_groups of this SecurityTag.
        :type security_groups: List[Reference]
        """

        self._security_groups = security_groups

    @property
    def vendor_id(self):
        """Gets the vendor_id of this SecurityTag.


        :return: The vendor_id of this SecurityTag.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this SecurityTag.


        :param vendor_id: The vendor_id of this SecurityTag.
        :type vendor_id: str
        """

        self._vendor_id = vendor_id
