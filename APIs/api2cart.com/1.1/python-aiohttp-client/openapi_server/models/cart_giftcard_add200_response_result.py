# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CartGiftcardAdd200ResponseResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, id: str=None):
        """CartGiftcardAdd200ResponseResult - a model defined in OpenAPI

        :param code: The code of this CartGiftcardAdd200ResponseResult.
        :param id: The id of this CartGiftcardAdd200ResponseResult.
        """
        self.openapi_types = {
            'code': str,
            'id': str
        }

        self.attribute_map = {
            'code': 'code',
            'id': 'id'
        }

        self._code = code
        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CartGiftcardAdd200ResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CartGiftcardAdd_200_response_result of this CartGiftcardAdd200ResponseResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this CartGiftcardAdd200ResponseResult.


        :return: The code of this CartGiftcardAdd200ResponseResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CartGiftcardAdd200ResponseResult.


        :param code: The code of this CartGiftcardAdd200ResponseResult.
        :type code: str
        """

        self._code = code

    @property
    def id(self):
        """Gets the id of this CartGiftcardAdd200ResponseResult.


        :return: The id of this CartGiftcardAdd200ResponseResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CartGiftcardAdd200ResponseResult.


        :param id: The id of this CartGiftcardAdd200ResponseResult.
        :type id: str
        """

        self._id = id
