# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.key_value_pair import KeyValuePair
from openapi_server import util


class SetWorkflowRequestPairsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, value: str=None):
        """SetWorkflowRequestPairsInner - a model defined in OpenAPI

        :param key: The key of this SetWorkflowRequestPairsInner.
        :param value: The value of this SetWorkflowRequestPairsInner.
        """
        self.openapi_types = {
            'key': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value'
        }

        self._key = key
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SetWorkflowRequestPairsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SetWorkflowRequest_pairs_inner of this SetWorkflowRequestPairsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this SetWorkflowRequestPairsInner.


        :return: The key of this SetWorkflowRequestPairsInner.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SetWorkflowRequestPairsInner.


        :param key: The key of this SetWorkflowRequestPairsInner.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def value(self):
        """Gets the value of this SetWorkflowRequestPairsInner.


        :return: The value of this SetWorkflowRequestPairsInner.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SetWorkflowRequestPairsInner.


        :param value: The value of this SetWorkflowRequestPairsInner.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
