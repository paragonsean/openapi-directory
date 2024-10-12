# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CompanyDataHierarchyInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entity_id: int=None, entity_type: str=None, extension_attributes: object=None, structure_id: int=None, structure_parent_id: int=None):
        """CompanyDataHierarchyInterface - a model defined in OpenAPI

        :param entity_id: The entity_id of this CompanyDataHierarchyInterface.
        :param entity_type: The entity_type of this CompanyDataHierarchyInterface.
        :param extension_attributes: The extension_attributes of this CompanyDataHierarchyInterface.
        :param structure_id: The structure_id of this CompanyDataHierarchyInterface.
        :param structure_parent_id: The structure_parent_id of this CompanyDataHierarchyInterface.
        """
        self.openapi_types = {
            'entity_id': int,
            'entity_type': str,
            'extension_attributes': object,
            'structure_id': int,
            'structure_parent_id': int
        }

        self.attribute_map = {
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'extension_attributes': 'extension_attributes',
            'structure_id': 'structure_id',
            'structure_parent_id': 'structure_parent_id'
        }

        self._entity_id = entity_id
        self._entity_type = entity_type
        self._extension_attributes = extension_attributes
        self._structure_id = structure_id
        self._structure_parent_id = structure_parent_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CompanyDataHierarchyInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The company-data-hierarchy-interface of this CompanyDataHierarchyInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entity_id(self):
        """Gets the entity_id of this CompanyDataHierarchyInterface.

        Entity ID.

        :return: The entity_id of this CompanyDataHierarchyInterface.
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this CompanyDataHierarchyInterface.

        Entity ID.

        :param entity_id: The entity_id of this CompanyDataHierarchyInterface.
        :type entity_id: int
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this CompanyDataHierarchyInterface.

        Entity type.

        :return: The entity_type of this CompanyDataHierarchyInterface.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this CompanyDataHierarchyInterface.

        Entity type.

        :param entity_type: The entity_type of this CompanyDataHierarchyInterface.
        :type entity_type: str
        """

        self._entity_type = entity_type

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this CompanyDataHierarchyInterface.

        ExtensionInterface class for @see \\Magento\\Company\\Api\\Data\\HierarchyInterface

        :return: The extension_attributes of this CompanyDataHierarchyInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this CompanyDataHierarchyInterface.

        ExtensionInterface class for @see \\Magento\\Company\\Api\\Data\\HierarchyInterface

        :param extension_attributes: The extension_attributes of this CompanyDataHierarchyInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def structure_id(self):
        """Gets the structure_id of this CompanyDataHierarchyInterface.

        Structure ID.

        :return: The structure_id of this CompanyDataHierarchyInterface.
        :rtype: int
        """
        return self._structure_id

    @structure_id.setter
    def structure_id(self, structure_id):
        """Sets the structure_id of this CompanyDataHierarchyInterface.

        Structure ID.

        :param structure_id: The structure_id of this CompanyDataHierarchyInterface.
        :type structure_id: int
        """

        self._structure_id = structure_id

    @property
    def structure_parent_id(self):
        """Gets the structure_parent_id of this CompanyDataHierarchyInterface.

        Structure parent ID.

        :return: The structure_parent_id of this CompanyDataHierarchyInterface.
        :rtype: int
        """
        return self._structure_parent_id

    @structure_parent_id.setter
    def structure_parent_id(self, structure_parent_id):
        """Sets the structure_parent_id of this CompanyDataHierarchyInterface.

        Structure parent ID.

        :param structure_parent_id: The structure_parent_id of this CompanyDataHierarchyInterface.
        :type structure_parent_id: int
        """

        self._structure_parent_id = structure_parent_id
