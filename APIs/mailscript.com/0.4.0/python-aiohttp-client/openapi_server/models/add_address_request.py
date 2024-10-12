# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AddAddressRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: str=None):
        """AddAddressRequest - a model defined in OpenAPI

        :param address: The address of this AddAddressRequest.
        """
        self.openapi_types = {
            'address': str
        }

        self.attribute_map = {
            'address': 'address'
        }

        self._address = address

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AddAddressRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AddAddressRequest of this AddAddressRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this AddAddressRequest.


        :return: The address of this AddAddressRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AddAddressRequest.


        :param address: The address of this AddAddressRequest.
        :type address: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")

        self._address = address
