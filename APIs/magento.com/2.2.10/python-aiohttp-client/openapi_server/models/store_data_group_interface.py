# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class StoreDataGroupInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, default_store_id: int=None, extension_attributes: object=None, id: int=None, name: str=None, root_category_id: int=None, website_id: int=None):
        """StoreDataGroupInterface - a model defined in OpenAPI

        :param code: The code of this StoreDataGroupInterface.
        :param default_store_id: The default_store_id of this StoreDataGroupInterface.
        :param extension_attributes: The extension_attributes of this StoreDataGroupInterface.
        :param id: The id of this StoreDataGroupInterface.
        :param name: The name of this StoreDataGroupInterface.
        :param root_category_id: The root_category_id of this StoreDataGroupInterface.
        :param website_id: The website_id of this StoreDataGroupInterface.
        """
        self.openapi_types = {
            'code': str,
            'default_store_id': int,
            'extension_attributes': object,
            'id': int,
            'name': str,
            'root_category_id': int,
            'website_id': int
        }

        self.attribute_map = {
            'code': 'code',
            'default_store_id': 'default_store_id',
            'extension_attributes': 'extension_attributes',
            'id': 'id',
            'name': 'name',
            'root_category_id': 'root_category_id',
            'website_id': 'website_id'
        }

        self._code = code
        self._default_store_id = default_store_id
        self._extension_attributes = extension_attributes
        self._id = id
        self._name = name
        self._root_category_id = root_category_id
        self._website_id = website_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StoreDataGroupInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The store-data-group-interface of this StoreDataGroupInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this StoreDataGroupInterface.

        Group code.

        :return: The code of this StoreDataGroupInterface.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StoreDataGroupInterface.

        Group code.

        :param code: The code of this StoreDataGroupInterface.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def default_store_id(self):
        """Gets the default_store_id of this StoreDataGroupInterface.


        :return: The default_store_id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._default_store_id

    @default_store_id.setter
    def default_store_id(self, default_store_id):
        """Sets the default_store_id of this StoreDataGroupInterface.


        :param default_store_id: The default_store_id of this StoreDataGroupInterface.
        :type default_store_id: int
        """
        if default_store_id is None:
            raise ValueError("Invalid value for `default_store_id`, must not be `None`")

        self._default_store_id = default_store_id

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this StoreDataGroupInterface.

        ExtensionInterface class for @see \\Magento\\Store\\Api\\Data\\GroupInterface

        :return: The extension_attributes of this StoreDataGroupInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this StoreDataGroupInterface.

        ExtensionInterface class for @see \\Magento\\Store\\Api\\Data\\GroupInterface

        :param extension_attributes: The extension_attributes of this StoreDataGroupInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def id(self):
        """Gets the id of this StoreDataGroupInterface.


        :return: The id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoreDataGroupInterface.


        :param id: The id of this StoreDataGroupInterface.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this StoreDataGroupInterface.


        :return: The name of this StoreDataGroupInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoreDataGroupInterface.


        :param name: The name of this StoreDataGroupInterface.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def root_category_id(self):
        """Gets the root_category_id of this StoreDataGroupInterface.


        :return: The root_category_id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._root_category_id

    @root_category_id.setter
    def root_category_id(self, root_category_id):
        """Sets the root_category_id of this StoreDataGroupInterface.


        :param root_category_id: The root_category_id of this StoreDataGroupInterface.
        :type root_category_id: int
        """
        if root_category_id is None:
            raise ValueError("Invalid value for `root_category_id`, must not be `None`")

        self._root_category_id = root_category_id

    @property
    def website_id(self):
        """Gets the website_id of this StoreDataGroupInterface.


        :return: The website_id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._website_id

    @website_id.setter
    def website_id(self, website_id):
        """Sets the website_id of this StoreDataGroupInterface.


        :param website_id: The website_id of this StoreDataGroupInterface.
        :type website_id: int
        """
        if website_id is None:
            raise ValueError("Invalid value for `website_id`, must not be `None`")

        self._website_id = website_id
