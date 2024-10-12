# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.customer_address import CustomerAddress
from openapi_server import util


class CartWarehouse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_fields: object=None, address: CustomerAddress=None, avail: bool=None, carriers_ids: List[str]=None, custom_fields: object=None, description: str=None, id: str=None, name: str=None, stores_ids: List[str]=None):
        """CartWarehouse - a model defined in OpenAPI

        :param additional_fields: The additional_fields of this CartWarehouse.
        :param address: The address of this CartWarehouse.
        :param avail: The avail of this CartWarehouse.
        :param carriers_ids: The carriers_ids of this CartWarehouse.
        :param custom_fields: The custom_fields of this CartWarehouse.
        :param description: The description of this CartWarehouse.
        :param id: The id of this CartWarehouse.
        :param name: The name of this CartWarehouse.
        :param stores_ids: The stores_ids of this CartWarehouse.
        """
        self.openapi_types = {
            'additional_fields': object,
            'address': CustomerAddress,
            'avail': bool,
            'carriers_ids': List[str],
            'custom_fields': object,
            'description': str,
            'id': str,
            'name': str,
            'stores_ids': List[str]
        }

        self.attribute_map = {
            'additional_fields': 'additional_fields',
            'address': 'address',
            'avail': 'avail',
            'carriers_ids': 'carriers_ids',
            'custom_fields': 'custom_fields',
            'description': 'description',
            'id': 'id',
            'name': 'name',
            'stores_ids': 'stores_ids'
        }

        self._additional_fields = additional_fields
        self._address = address
        self._avail = avail
        self._carriers_ids = carriers_ids
        self._custom_fields = custom_fields
        self._description = description
        self._id = id
        self._name = name
        self._stores_ids = stores_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CartWarehouse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Cart_Warehouse of this CartWarehouse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_fields(self):
        """Gets the additional_fields of this CartWarehouse.


        :return: The additional_fields of this CartWarehouse.
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this CartWarehouse.


        :param additional_fields: The additional_fields of this CartWarehouse.
        :type additional_fields: object
        """

        self._additional_fields = additional_fields

    @property
    def address(self):
        """Gets the address of this CartWarehouse.


        :return: The address of this CartWarehouse.
        :rtype: CustomerAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CartWarehouse.


        :param address: The address of this CartWarehouse.
        :type address: CustomerAddress
        """

        self._address = address

    @property
    def avail(self):
        """Gets the avail of this CartWarehouse.


        :return: The avail of this CartWarehouse.
        :rtype: bool
        """
        return self._avail

    @avail.setter
    def avail(self, avail):
        """Sets the avail of this CartWarehouse.


        :param avail: The avail of this CartWarehouse.
        :type avail: bool
        """

        self._avail = avail

    @property
    def carriers_ids(self):
        """Gets the carriers_ids of this CartWarehouse.


        :return: The carriers_ids of this CartWarehouse.
        :rtype: List[str]
        """
        return self._carriers_ids

    @carriers_ids.setter
    def carriers_ids(self, carriers_ids):
        """Sets the carriers_ids of this CartWarehouse.


        :param carriers_ids: The carriers_ids of this CartWarehouse.
        :type carriers_ids: List[str]
        """

        self._carriers_ids = carriers_ids

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CartWarehouse.


        :return: The custom_fields of this CartWarehouse.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CartWarehouse.


        :param custom_fields: The custom_fields of this CartWarehouse.
        :type custom_fields: object
        """

        self._custom_fields = custom_fields

    @property
    def description(self):
        """Gets the description of this CartWarehouse.


        :return: The description of this CartWarehouse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CartWarehouse.


        :param description: The description of this CartWarehouse.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this CartWarehouse.


        :return: The id of this CartWarehouse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CartWarehouse.


        :param id: The id of this CartWarehouse.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CartWarehouse.


        :return: The name of this CartWarehouse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CartWarehouse.


        :param name: The name of this CartWarehouse.
        :type name: str
        """

        self._name = name

    @property
    def stores_ids(self):
        """Gets the stores_ids of this CartWarehouse.


        :return: The stores_ids of this CartWarehouse.
        :rtype: List[str]
        """
        return self._stores_ids

    @stores_ids.setter
    def stores_ids(self, stores_ids):
        """Sets the stores_ids of this CartWarehouse.


        :param stores_ids: The stores_ids of this CartWarehouse.
        :type stores_ids: List[str]
        """

        self._stores_ids = stores_ids
