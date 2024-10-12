# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.requisition_list_data_requisition_list_item_interface import RequisitionListDataRequisitionListItemInterface
from openapi_server import util


class RequisitionListDataRequisitionListInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, customer_id: int=None, description: str=None, extension_attributes: object=None, id: int=None, items: List[RequisitionListDataRequisitionListItemInterface]=None, name: str=None, updated_at: str=None):
        """RequisitionListDataRequisitionListInterface - a model defined in OpenAPI

        :param customer_id: The customer_id of this RequisitionListDataRequisitionListInterface.
        :param description: The description of this RequisitionListDataRequisitionListInterface.
        :param extension_attributes: The extension_attributes of this RequisitionListDataRequisitionListInterface.
        :param id: The id of this RequisitionListDataRequisitionListInterface.
        :param items: The items of this RequisitionListDataRequisitionListInterface.
        :param name: The name of this RequisitionListDataRequisitionListInterface.
        :param updated_at: The updated_at of this RequisitionListDataRequisitionListInterface.
        """
        self.openapi_types = {
            'customer_id': int,
            'description': str,
            'extension_attributes': object,
            'id': int,
            'items': List[RequisitionListDataRequisitionListItemInterface],
            'name': str,
            'updated_at': str
        }

        self.attribute_map = {
            'customer_id': 'customer_id',
            'description': 'description',
            'extension_attributes': 'extension_attributes',
            'id': 'id',
            'items': 'items',
            'name': 'name',
            'updated_at': 'updated_at'
        }

        self._customer_id = customer_id
        self._description = description
        self._extension_attributes = extension_attributes
        self._id = id
        self._items = items
        self._name = name
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RequisitionListDataRequisitionListInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The requisition-list-data-requisition-list-interface of this RequisitionListDataRequisitionListInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def customer_id(self):
        """Gets the customer_id of this RequisitionListDataRequisitionListInterface.

        Customer ID

        :return: The customer_id of this RequisitionListDataRequisitionListInterface.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this RequisitionListDataRequisitionListInterface.

        Customer ID

        :param customer_id: The customer_id of this RequisitionListDataRequisitionListInterface.
        :type customer_id: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")

        self._customer_id = customer_id

    @property
    def description(self):
        """Gets the description of this RequisitionListDataRequisitionListInterface.

        Requisition List Description

        :return: The description of this RequisitionListDataRequisitionListInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RequisitionListDataRequisitionListInterface.

        Requisition List Description

        :param description: The description of this RequisitionListDataRequisitionListInterface.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this RequisitionListDataRequisitionListInterface.

        ExtensionInterface class for @see \\Magento\\RequisitionList\\Api\\Data\\RequisitionListInterface

        :return: The extension_attributes of this RequisitionListDataRequisitionListInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this RequisitionListDataRequisitionListInterface.

        ExtensionInterface class for @see \\Magento\\RequisitionList\\Api\\Data\\RequisitionListInterface

        :param extension_attributes: The extension_attributes of this RequisitionListDataRequisitionListInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def id(self):
        """Gets the id of this RequisitionListDataRequisitionListInterface.

        Requisition List ID

        :return: The id of this RequisitionListDataRequisitionListInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RequisitionListDataRequisitionListInterface.

        Requisition List ID

        :param id: The id of this RequisitionListDataRequisitionListInterface.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def items(self):
        """Gets the items of this RequisitionListDataRequisitionListInterface.

        Requisition List Items

        :return: The items of this RequisitionListDataRequisitionListInterface.
        :rtype: List[RequisitionListDataRequisitionListItemInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this RequisitionListDataRequisitionListInterface.

        Requisition List Items

        :param items: The items of this RequisitionListDataRequisitionListInterface.
        :type items: List[RequisitionListDataRequisitionListItemInterface]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def name(self):
        """Gets the name of this RequisitionListDataRequisitionListInterface.

        Requisition List Name

        :return: The name of this RequisitionListDataRequisitionListInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RequisitionListDataRequisitionListInterface.

        Requisition List Name

        :param name: The name of this RequisitionListDataRequisitionListInterface.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this RequisitionListDataRequisitionListInterface.

        Requisition List Update Time

        :return: The updated_at of this RequisitionListDataRequisitionListInterface.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RequisitionListDataRequisitionListInterface.

        Requisition List Update Time

        :param updated_at: The updated_at of this RequisitionListDataRequisitionListInterface.
        :type updated_at: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at
