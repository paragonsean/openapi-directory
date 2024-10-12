# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.listings_post_request_shipping_rates_inner import ListingsPostRequestShippingRatesInner
from openapi_server import util


class ListingsPostRequestShipping(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, local: bool=None, rates: List[ListingsPostRequestShippingRatesInner]=None):
        """ListingsPostRequestShipping - a model defined in OpenAPI

        :param local: The local of this ListingsPostRequestShipping.
        :param rates: The rates of this ListingsPostRequestShipping.
        """
        self.openapi_types = {
            'local': bool,
            'rates': List[ListingsPostRequestShippingRatesInner]
        }

        self.attribute_map = {
            'local': 'local',
            'rates': 'rates'
        }

        self._local = local
        self._rates = rates

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ListingsPostRequestShipping':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _listings_post_request_shipping of this ListingsPostRequestShipping.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def local(self):
        """Gets the local of this ListingsPostRequestShipping.

        True if you offer local pickup

        :return: The local of this ListingsPostRequestShipping.
        :rtype: bool
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this ListingsPostRequestShipping.

        True if you offer local pickup

        :param local: The local of this ListingsPostRequestShipping.
        :type local: bool
        """

        self._local = local

    @property
    def rates(self):
        """Gets the rates of this ListingsPostRequestShipping.

        List of shipping rates. Set to null to clear rates.

        :return: The rates of this ListingsPostRequestShipping.
        :rtype: List[ListingsPostRequestShippingRatesInner]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this ListingsPostRequestShipping.

        List of shipping rates. Set to null to clear rates.

        :param rates: The rates of this ListingsPostRequestShipping.
        :type rates: List[ListingsPostRequestShippingRatesInner]
        """

        self._rates = rates
