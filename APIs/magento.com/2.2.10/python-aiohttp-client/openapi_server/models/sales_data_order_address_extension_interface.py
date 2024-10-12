# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.framework_attribute_interface import FrameworkAttributeInterface
from openapi_server import util


class SalesDataOrderAddressExtensionInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, checkout_fields: List[FrameworkAttributeInterface]=None):
        """SalesDataOrderAddressExtensionInterface - a model defined in OpenAPI

        :param checkout_fields: The checkout_fields of this SalesDataOrderAddressExtensionInterface.
        """
        self.openapi_types = {
            'checkout_fields': List[FrameworkAttributeInterface]
        }

        self.attribute_map = {
            'checkout_fields': 'checkout_fields'
        }

        self._checkout_fields = checkout_fields

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesDataOrderAddressExtensionInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-data-order-address-extension-interface of this SalesDataOrderAddressExtensionInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def checkout_fields(self):
        """Gets the checkout_fields of this SalesDataOrderAddressExtensionInterface.


        :return: The checkout_fields of this SalesDataOrderAddressExtensionInterface.
        :rtype: List[FrameworkAttributeInterface]
        """
        return self._checkout_fields

    @checkout_fields.setter
    def checkout_fields(self, checkout_fields):
        """Sets the checkout_fields of this SalesDataOrderAddressExtensionInterface.


        :param checkout_fields: The checkout_fields of this SalesDataOrderAddressExtensionInterface.
        :type checkout_fields: List[FrameworkAttributeInterface]
        """

        self._checkout_fields = checkout_fields
