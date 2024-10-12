# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.gift_card_class import GiftCardClass
from openapi_server import util


class GiftCardClassAddMessageResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource: GiftCardClass=None):
        """GiftCardClassAddMessageResponse - a model defined in OpenAPI

        :param resource: The resource of this GiftCardClassAddMessageResponse.
        """
        self.openapi_types = {
            'resource': GiftCardClass
        }

        self.attribute_map = {
            'resource': 'resource'
        }

        self._resource = resource

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GiftCardClassAddMessageResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GiftCardClassAddMessageResponse of this GiftCardClassAddMessageResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource(self):
        """Gets the resource of this GiftCardClassAddMessageResponse.


        :return: The resource of this GiftCardClassAddMessageResponse.
        :rtype: GiftCardClass
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this GiftCardClassAddMessageResponse.


        :param resource: The resource of this GiftCardClassAddMessageResponse.
        :type resource: GiftCardClass
        """

        self._resource = resource
