# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.offer_class import OfferClass
from openapi_server import util


class OfferClassAddMessageResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, resource: OfferClass=None):
        """OfferClassAddMessageResponse - a model defined in OpenAPI

        :param resource: The resource of this OfferClassAddMessageResponse.
        """
        self.openapi_types = {
            'resource': OfferClass
        }

        self.attribute_map = {
            'resource': 'resource'
        }

        self._resource = resource

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OfferClassAddMessageResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OfferClassAddMessageResponse of this OfferClassAddMessageResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource(self):
        """Gets the resource of this OfferClassAddMessageResponse.


        :return: The resource of this OfferClassAddMessageResponse.
        :rtype: OfferClass
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this OfferClassAddMessageResponse.


        :param resource: The resource of this OfferClassAddMessageResponse.
        :type resource: OfferClass
        """

        self._resource = resource
