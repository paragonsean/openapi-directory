# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class StoreDataStoreInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, extension_attributes: object=None, id: int=None, name: str=None, store_group_id: int=None, website_id: int=None):
        """StoreDataStoreInterface - a model defined in OpenAPI

        :param code: The code of this StoreDataStoreInterface.
        :param extension_attributes: The extension_attributes of this StoreDataStoreInterface.
        :param id: The id of this StoreDataStoreInterface.
        :param name: The name of this StoreDataStoreInterface.
        :param store_group_id: The store_group_id of this StoreDataStoreInterface.
        :param website_id: The website_id of this StoreDataStoreInterface.
        """
        self.openapi_types = {
            'code': str,
            'extension_attributes': object,
            'id': int,
            'name': str,
            'store_group_id': int,
            'website_id': int
        }

        self.attribute_map = {
            'code': 'code',
            'extension_attributes': 'extension_attributes',
            'id': 'id',
            'name': 'name',
            'store_group_id': 'store_group_id',
            'website_id': 'website_id'
        }

        self._code = code
        self._extension_attributes = extension_attributes
        self._id = id
        self._name = name
        self._store_group_id = store_group_id
        self._website_id = website_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StoreDataStoreInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The store-data-store-interface of this StoreDataStoreInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this StoreDataStoreInterface.


        :return: The code of this StoreDataStoreInterface.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StoreDataStoreInterface.


        :param code: The code of this StoreDataStoreInterface.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this StoreDataStoreInterface.

        ExtensionInterface class for @see \\Magento\\Store\\Api\\Data\\StoreInterface

        :return: The extension_attributes of this StoreDataStoreInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this StoreDataStoreInterface.

        ExtensionInterface class for @see \\Magento\\Store\\Api\\Data\\StoreInterface

        :param extension_attributes: The extension_attributes of this StoreDataStoreInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def id(self):
        """Gets the id of this StoreDataStoreInterface.


        :return: The id of this StoreDataStoreInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoreDataStoreInterface.


        :param id: The id of this StoreDataStoreInterface.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this StoreDataStoreInterface.

        Store name

        :return: The name of this StoreDataStoreInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoreDataStoreInterface.

        Store name

        :param name: The name of this StoreDataStoreInterface.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def store_group_id(self):
        """Gets the store_group_id of this StoreDataStoreInterface.


        :return: The store_group_id of this StoreDataStoreInterface.
        :rtype: int
        """
        return self._store_group_id

    @store_group_id.setter
    def store_group_id(self, store_group_id):
        """Sets the store_group_id of this StoreDataStoreInterface.


        :param store_group_id: The store_group_id of this StoreDataStoreInterface.
        :type store_group_id: int
        """
        if store_group_id is None:
            raise ValueError("Invalid value for `store_group_id`, must not be `None`")

        self._store_group_id = store_group_id

    @property
    def website_id(self):
        """Gets the website_id of this StoreDataStoreInterface.


        :return: The website_id of this StoreDataStoreInterface.
        :rtype: int
        """
        return self._website_id

    @website_id.setter
    def website_id(self, website_id):
        """Sets the website_id of this StoreDataStoreInterface.


        :param website_id: The website_id of this StoreDataStoreInterface.
        :type website_id: int
        """
        if website_id is None:
            raise ValueError("Invalid value for `website_id`, must not be `None`")

        self._website_id = website_id
