# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.identity_provider_list_by_service200_response_value_inner import IdentityProviderListByService200ResponseValueInner
from openapi_server import util


class IdentityProviderListByService200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_link: str=None, value: List[IdentityProviderListByService200ResponseValueInner]=None):
        """IdentityProviderListByService200Response - a model defined in OpenAPI

        :param next_link: The next_link of this IdentityProviderListByService200Response.
        :param value: The value of this IdentityProviderListByService200Response.
        """
        self.openapi_types = {
            'next_link': str,
            'value': List[IdentityProviderListByService200ResponseValueInner]
        }

        self.attribute_map = {
            'next_link': 'nextLink',
            'value': 'value'
        }

        self._next_link = next_link
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IdentityProviderListByService200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IdentityProvider_ListByService_200_response of this IdentityProviderListByService200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_link(self):
        """Gets the next_link of this IdentityProviderListByService200Response.

        Next page link if any.

        :return: The next_link of this IdentityProviderListByService200Response.
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this IdentityProviderListByService200Response.

        Next page link if any.

        :param next_link: The next_link of this IdentityProviderListByService200Response.
        :type next_link: str
        """

        self._next_link = next_link

    @property
    def value(self):
        """Gets the value of this IdentityProviderListByService200Response.

        Identity Provider configuration values.

        :return: The value of this IdentityProviderListByService200Response.
        :rtype: List[IdentityProviderListByService200ResponseValueInner]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IdentityProviderListByService200Response.

        Identity Provider configuration values.

        :param value: The value of this IdentityProviderListByService200Response.
        :type value: List[IdentityProviderListByService200ResponseValueInner]
        """

        self._value = value
