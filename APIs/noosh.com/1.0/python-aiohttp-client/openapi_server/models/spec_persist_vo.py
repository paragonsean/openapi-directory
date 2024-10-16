# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.spec_version_persist_vo import SpecVersionPersistVO
from openapi_server import util


class SpecPersistVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, json_body: bool=None, product_type_id: int=None, quantity_1: int=None, quantity_2: int=None, quantity_3: int=None, quantity_4: int=None, quantity_5: int=None, sku: str=None, spec_name: str=None, spec_template_id: int=None, spec_type_id: int=None, versions: List[SpecVersionPersistVO]=None):
        """SpecPersistVO - a model defined in OpenAPI

        :param json_body: The json_body of this SpecPersistVO.
        :param product_type_id: The product_type_id of this SpecPersistVO.
        :param quantity_1: The quantity_1 of this SpecPersistVO.
        :param quantity_2: The quantity_2 of this SpecPersistVO.
        :param quantity_3: The quantity_3 of this SpecPersistVO.
        :param quantity_4: The quantity_4 of this SpecPersistVO.
        :param quantity_5: The quantity_5 of this SpecPersistVO.
        :param sku: The sku of this SpecPersistVO.
        :param spec_name: The spec_name of this SpecPersistVO.
        :param spec_template_id: The spec_template_id of this SpecPersistVO.
        :param spec_type_id: The spec_type_id of this SpecPersistVO.
        :param versions: The versions of this SpecPersistVO.
        """
        self.openapi_types = {
            'json_body': bool,
            'product_type_id': int,
            'quantity_1': int,
            'quantity_2': int,
            'quantity_3': int,
            'quantity_4': int,
            'quantity_5': int,
            'sku': str,
            'spec_name': str,
            'spec_template_id': int,
            'spec_type_id': int,
            'versions': List[SpecVersionPersistVO]
        }

        self.attribute_map = {
            'json_body': 'jsonBody',
            'product_type_id': 'product_type_id',
            'quantity_1': 'quantity_1',
            'quantity_2': 'quantity_2',
            'quantity_3': 'quantity_3',
            'quantity_4': 'quantity_4',
            'quantity_5': 'quantity_5',
            'sku': 'sku',
            'spec_name': 'spec_name',
            'spec_template_id': 'spec_template_id',
            'spec_type_id': 'spec_type_id',
            'versions': 'versions'
        }

        self._json_body = json_body
        self._product_type_id = product_type_id
        self._quantity_1 = quantity_1
        self._quantity_2 = quantity_2
        self._quantity_3 = quantity_3
        self._quantity_4 = quantity_4
        self._quantity_5 = quantity_5
        self._sku = sku
        self._spec_name = spec_name
        self._spec_template_id = spec_template_id
        self._spec_type_id = spec_type_id
        self._versions = versions

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SpecPersistVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SpecPersistVO of this SpecPersistVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def json_body(self):
        """Gets the json_body of this SpecPersistVO.

        

        :return: The json_body of this SpecPersistVO.
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this SpecPersistVO.

        

        :param json_body: The json_body of this SpecPersistVO.
        :type json_body: bool
        """

        self._json_body = json_body

    @property
    def product_type_id(self):
        """Gets the product_type_id of this SpecPersistVO.

        

        :return: The product_type_id of this SpecPersistVO.
        :rtype: int
        """
        return self._product_type_id

    @product_type_id.setter
    def product_type_id(self, product_type_id):
        """Sets the product_type_id of this SpecPersistVO.

        

        :param product_type_id: The product_type_id of this SpecPersistVO.
        :type product_type_id: int
        """

        self._product_type_id = product_type_id

    @property
    def quantity_1(self):
        """Gets the quantity_1 of this SpecPersistVO.

        

        :return: The quantity_1 of this SpecPersistVO.
        :rtype: int
        """
        return self._quantity_1

    @quantity_1.setter
    def quantity_1(self, quantity_1):
        """Sets the quantity_1 of this SpecPersistVO.

        

        :param quantity_1: The quantity_1 of this SpecPersistVO.
        :type quantity_1: int
        """

        self._quantity_1 = quantity_1

    @property
    def quantity_2(self):
        """Gets the quantity_2 of this SpecPersistVO.

        

        :return: The quantity_2 of this SpecPersistVO.
        :rtype: int
        """
        return self._quantity_2

    @quantity_2.setter
    def quantity_2(self, quantity_2):
        """Sets the quantity_2 of this SpecPersistVO.

        

        :param quantity_2: The quantity_2 of this SpecPersistVO.
        :type quantity_2: int
        """

        self._quantity_2 = quantity_2

    @property
    def quantity_3(self):
        """Gets the quantity_3 of this SpecPersistVO.

        

        :return: The quantity_3 of this SpecPersistVO.
        :rtype: int
        """
        return self._quantity_3

    @quantity_3.setter
    def quantity_3(self, quantity_3):
        """Sets the quantity_3 of this SpecPersistVO.

        

        :param quantity_3: The quantity_3 of this SpecPersistVO.
        :type quantity_3: int
        """

        self._quantity_3 = quantity_3

    @property
    def quantity_4(self):
        """Gets the quantity_4 of this SpecPersistVO.

        

        :return: The quantity_4 of this SpecPersistVO.
        :rtype: int
        """
        return self._quantity_4

    @quantity_4.setter
    def quantity_4(self, quantity_4):
        """Sets the quantity_4 of this SpecPersistVO.

        

        :param quantity_4: The quantity_4 of this SpecPersistVO.
        :type quantity_4: int
        """

        self._quantity_4 = quantity_4

    @property
    def quantity_5(self):
        """Gets the quantity_5 of this SpecPersistVO.

        

        :return: The quantity_5 of this SpecPersistVO.
        :rtype: int
        """
        return self._quantity_5

    @quantity_5.setter
    def quantity_5(self, quantity_5):
        """Sets the quantity_5 of this SpecPersistVO.

        

        :param quantity_5: The quantity_5 of this SpecPersistVO.
        :type quantity_5: int
        """

        self._quantity_5 = quantity_5

    @property
    def sku(self):
        """Gets the sku of this SpecPersistVO.

        

        :return: The sku of this SpecPersistVO.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this SpecPersistVO.

        

        :param sku: The sku of this SpecPersistVO.
        :type sku: str
        """

        self._sku = sku

    @property
    def spec_name(self):
        """Gets the spec_name of this SpecPersistVO.

        

        :return: The spec_name of this SpecPersistVO.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        """Sets the spec_name of this SpecPersistVO.

        

        :param spec_name: The spec_name of this SpecPersistVO.
        :type spec_name: str
        """

        self._spec_name = spec_name

    @property
    def spec_template_id(self):
        """Gets the spec_template_id of this SpecPersistVO.

        

        :return: The spec_template_id of this SpecPersistVO.
        :rtype: int
        """
        return self._spec_template_id

    @spec_template_id.setter
    def spec_template_id(self, spec_template_id):
        """Sets the spec_template_id of this SpecPersistVO.

        

        :param spec_template_id: The spec_template_id of this SpecPersistVO.
        :type spec_template_id: int
        """

        self._spec_template_id = spec_template_id

    @property
    def spec_type_id(self):
        """Gets the spec_type_id of this SpecPersistVO.

        

        :return: The spec_type_id of this SpecPersistVO.
        :rtype: int
        """
        return self._spec_type_id

    @spec_type_id.setter
    def spec_type_id(self, spec_type_id):
        """Sets the spec_type_id of this SpecPersistVO.

        

        :param spec_type_id: The spec_type_id of this SpecPersistVO.
        :type spec_type_id: int
        """

        self._spec_type_id = spec_type_id

    @property
    def versions(self):
        """Gets the versions of this SpecPersistVO.

        

        :return: The versions of this SpecPersistVO.
        :rtype: List[SpecVersionPersistVO]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this SpecPersistVO.

        

        :param versions: The versions of this SpecPersistVO.
        :type versions: List[SpecVersionPersistVO]
        """

        self._versions = versions
