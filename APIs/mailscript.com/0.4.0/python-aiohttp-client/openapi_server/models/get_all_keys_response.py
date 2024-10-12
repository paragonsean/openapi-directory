# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_all_keys_response_list_inner import GetAllKeysResponseListInner
from openapi_server import util


class GetAllKeysResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, list: List[GetAllKeysResponseListInner]=None):
        """GetAllKeysResponse - a model defined in OpenAPI

        :param list: The list of this GetAllKeysResponse.
        """
        self.openapi_types = {
            'list': List[GetAllKeysResponseListInner]
        }

        self.attribute_map = {
            'list': 'list'
        }

        self._list = list

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetAllKeysResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GetAllKeysResponse of this GetAllKeysResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def list(self):
        """Gets the list of this GetAllKeysResponse.


        :return: The list of this GetAllKeysResponse.
        :rtype: List[GetAllKeysResponseListInner]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this GetAllKeysResponse.


        :param list: The list of this GetAllKeysResponse.
        :type list: List[GetAllKeysResponseListInner]
        """
        if list is None:
            raise ValueError("Invalid value for `list`, must not be `None`")

        self._list = list
