# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SubscriptionTier(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """SubscriptionTier - a model defined in OpenAPI

        :param name: The name of this SubscriptionTier.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SubscriptionTier':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Subscription_Tier of this SubscriptionTier.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this SubscriptionTier.

        The name of the tier

        :return: The name of this SubscriptionTier.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionTier.

        The name of the tier

        :param name: The name of this SubscriptionTier.
        :type name: str
        """

        self._name = name
