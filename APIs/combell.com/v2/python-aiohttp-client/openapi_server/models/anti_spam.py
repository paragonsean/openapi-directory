# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.anti_spam_types import AntiSpamTypes
from openapi_server import util


class AntiSpam(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allowed_types: List[AntiSpamTypes]=None, type: AntiSpamTypes=None):
        """AntiSpam - a model defined in OpenAPI

        :param allowed_types: The allowed_types of this AntiSpam.
        :param type: The type of this AntiSpam.
        """
        self.openapi_types = {
            'allowed_types': List[AntiSpamTypes],
            'type': AntiSpamTypes
        }

        self.attribute_map = {
            'allowed_types': 'allowed_types',
            'type': 'type'
        }

        self._allowed_types = allowed_types
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AntiSpam':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AntiSpam of this AntiSpam.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allowed_types(self):
        """Gets the allowed_types of this AntiSpam.

        Allowed types of anti-spam scanning for this mail zone

        :return: The allowed_types of this AntiSpam.
        :rtype: List[AntiSpamTypes]
        """
        return self._allowed_types

    @allowed_types.setter
    def allowed_types(self, allowed_types):
        """Sets the allowed_types of this AntiSpam.

        Allowed types of anti-spam scanning for this mail zone

        :param allowed_types: The allowed_types of this AntiSpam.
        :type allowed_types: List[AntiSpamTypes]
        """

        self._allowed_types = allowed_types

    @property
    def type(self):
        """Gets the type of this AntiSpam.


        :return: The type of this AntiSpam.
        :rtype: AntiSpamTypes
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AntiSpam.


        :param type: The type of this AntiSpam.
        :type type: AntiSpamTypes
        """

        self._type = type
