# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ErgoSpecSimpleVO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_active: int=None, is_template: int=None, quantity_1: float=None, quantity_2: float=None, quantity_3: float=None, quantity_4: float=None, quantity_5: float=None, reference_number: str=None, spec_id: int=None, spec_name: str=None):
        """ErgoSpecSimpleVO - a model defined in OpenAPI

        :param is_active: The is_active of this ErgoSpecSimpleVO.
        :param is_template: The is_template of this ErgoSpecSimpleVO.
        :param quantity_1: The quantity_1 of this ErgoSpecSimpleVO.
        :param quantity_2: The quantity_2 of this ErgoSpecSimpleVO.
        :param quantity_3: The quantity_3 of this ErgoSpecSimpleVO.
        :param quantity_4: The quantity_4 of this ErgoSpecSimpleVO.
        :param quantity_5: The quantity_5 of this ErgoSpecSimpleVO.
        :param reference_number: The reference_number of this ErgoSpecSimpleVO.
        :param spec_id: The spec_id of this ErgoSpecSimpleVO.
        :param spec_name: The spec_name of this ErgoSpecSimpleVO.
        """
        self.openapi_types = {
            'is_active': int,
            'is_template': int,
            'quantity_1': float,
            'quantity_2': float,
            'quantity_3': float,
            'quantity_4': float,
            'quantity_5': float,
            'reference_number': str,
            'spec_id': int,
            'spec_name': str
        }

        self.attribute_map = {
            'is_active': 'is_active',
            'is_template': 'is_template',
            'quantity_1': 'quantity_1',
            'quantity_2': 'quantity_2',
            'quantity_3': 'quantity_3',
            'quantity_4': 'quantity_4',
            'quantity_5': 'quantity_5',
            'reference_number': 'reference_number',
            'spec_id': 'spec_id',
            'spec_name': 'spec_name'
        }

        self._is_active = is_active
        self._is_template = is_template
        self._quantity_1 = quantity_1
        self._quantity_2 = quantity_2
        self._quantity_3 = quantity_3
        self._quantity_4 = quantity_4
        self._quantity_5 = quantity_5
        self._reference_number = reference_number
        self._spec_id = spec_id
        self._spec_name = spec_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErgoSpecSimpleVO':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErgoSpecSimpleVO of this ErgoSpecSimpleVO.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_active(self):
        """Gets the is_active of this ErgoSpecSimpleVO.

        

        :return: The is_active of this ErgoSpecSimpleVO.
        :rtype: int
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ErgoSpecSimpleVO.

        

        :param is_active: The is_active of this ErgoSpecSimpleVO.
        :type is_active: int
        """

        self._is_active = is_active

    @property
    def is_template(self):
        """Gets the is_template of this ErgoSpecSimpleVO.

        

        :return: The is_template of this ErgoSpecSimpleVO.
        :rtype: int
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        """Sets the is_template of this ErgoSpecSimpleVO.

        

        :param is_template: The is_template of this ErgoSpecSimpleVO.
        :type is_template: int
        """

        self._is_template = is_template

    @property
    def quantity_1(self):
        """Gets the quantity_1 of this ErgoSpecSimpleVO.

        

        :return: The quantity_1 of this ErgoSpecSimpleVO.
        :rtype: float
        """
        return self._quantity_1

    @quantity_1.setter
    def quantity_1(self, quantity_1):
        """Sets the quantity_1 of this ErgoSpecSimpleVO.

        

        :param quantity_1: The quantity_1 of this ErgoSpecSimpleVO.
        :type quantity_1: float
        """

        self._quantity_1 = quantity_1

    @property
    def quantity_2(self):
        """Gets the quantity_2 of this ErgoSpecSimpleVO.

        

        :return: The quantity_2 of this ErgoSpecSimpleVO.
        :rtype: float
        """
        return self._quantity_2

    @quantity_2.setter
    def quantity_2(self, quantity_2):
        """Sets the quantity_2 of this ErgoSpecSimpleVO.

        

        :param quantity_2: The quantity_2 of this ErgoSpecSimpleVO.
        :type quantity_2: float
        """

        self._quantity_2 = quantity_2

    @property
    def quantity_3(self):
        """Gets the quantity_3 of this ErgoSpecSimpleVO.

        

        :return: The quantity_3 of this ErgoSpecSimpleVO.
        :rtype: float
        """
        return self._quantity_3

    @quantity_3.setter
    def quantity_3(self, quantity_3):
        """Sets the quantity_3 of this ErgoSpecSimpleVO.

        

        :param quantity_3: The quantity_3 of this ErgoSpecSimpleVO.
        :type quantity_3: float
        """

        self._quantity_3 = quantity_3

    @property
    def quantity_4(self):
        """Gets the quantity_4 of this ErgoSpecSimpleVO.

        

        :return: The quantity_4 of this ErgoSpecSimpleVO.
        :rtype: float
        """
        return self._quantity_4

    @quantity_4.setter
    def quantity_4(self, quantity_4):
        """Sets the quantity_4 of this ErgoSpecSimpleVO.

        

        :param quantity_4: The quantity_4 of this ErgoSpecSimpleVO.
        :type quantity_4: float
        """

        self._quantity_4 = quantity_4

    @property
    def quantity_5(self):
        """Gets the quantity_5 of this ErgoSpecSimpleVO.

        

        :return: The quantity_5 of this ErgoSpecSimpleVO.
        :rtype: float
        """
        return self._quantity_5

    @quantity_5.setter
    def quantity_5(self, quantity_5):
        """Sets the quantity_5 of this ErgoSpecSimpleVO.

        

        :param quantity_5: The quantity_5 of this ErgoSpecSimpleVO.
        :type quantity_5: float
        """

        self._quantity_5 = quantity_5

    @property
    def reference_number(self):
        """Gets the reference_number of this ErgoSpecSimpleVO.

        

        :return: The reference_number of this ErgoSpecSimpleVO.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this ErgoSpecSimpleVO.

        

        :param reference_number: The reference_number of this ErgoSpecSimpleVO.
        :type reference_number: str
        """

        self._reference_number = reference_number

    @property
    def spec_id(self):
        """Gets the spec_id of this ErgoSpecSimpleVO.

        

        :return: The spec_id of this ErgoSpecSimpleVO.
        :rtype: int
        """
        return self._spec_id

    @spec_id.setter
    def spec_id(self, spec_id):
        """Sets the spec_id of this ErgoSpecSimpleVO.

        

        :param spec_id: The spec_id of this ErgoSpecSimpleVO.
        :type spec_id: int
        """

        self._spec_id = spec_id

    @property
    def spec_name(self):
        """Gets the spec_name of this ErgoSpecSimpleVO.

        

        :return: The spec_name of this ErgoSpecSimpleVO.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        """Sets the spec_name of this ErgoSpecSimpleVO.

        

        :param spec_name: The spec_name of this ErgoSpecSimpleVO.
        :type spec_name: str
        """

        self._spec_name = spec_name
