# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.quote_data_address_interface import QuoteDataAddressInterface
from openapi_server import util


class QuoteBillingAddressManagementV1AssignPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: QuoteDataAddressInterface=None, use_for_shipping: bool=None):
        """QuoteBillingAddressManagementV1AssignPostRequest - a model defined in OpenAPI

        :param address: The address of this QuoteBillingAddressManagementV1AssignPostRequest.
        :param use_for_shipping: The use_for_shipping of this QuoteBillingAddressManagementV1AssignPostRequest.
        """
        self.openapi_types = {
            'address': QuoteDataAddressInterface,
            'use_for_shipping': bool
        }

        self.attribute_map = {
            'address': 'address',
            'use_for_shipping': 'useForShipping'
        }

        self._address = address
        self._use_for_shipping = use_for_shipping

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QuoteBillingAddressManagementV1AssignPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The quoteBillingAddressManagementV1AssignPost_request of this QuoteBillingAddressManagementV1AssignPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this QuoteBillingAddressManagementV1AssignPostRequest.


        :return: The address of this QuoteBillingAddressManagementV1AssignPostRequest.
        :rtype: QuoteDataAddressInterface
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this QuoteBillingAddressManagementV1AssignPostRequest.


        :param address: The address of this QuoteBillingAddressManagementV1AssignPostRequest.
        :type address: QuoteDataAddressInterface
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")

        self._address = address

    @property
    def use_for_shipping(self):
        """Gets the use_for_shipping of this QuoteBillingAddressManagementV1AssignPostRequest.


        :return: The use_for_shipping of this QuoteBillingAddressManagementV1AssignPostRequest.
        :rtype: bool
        """
        return self._use_for_shipping

    @use_for_shipping.setter
    def use_for_shipping(self, use_for_shipping):
        """Sets the use_for_shipping of this QuoteBillingAddressManagementV1AssignPostRequest.


        :param use_for_shipping: The use_for_shipping of this QuoteBillingAddressManagementV1AssignPostRequest.
        :type use_for_shipping: bool
        """

        self._use_for_shipping = use_for_shipping
