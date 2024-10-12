# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Meta(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, communication_expiry: str=None, communication_hint: str=None, communication_medium: str=None):
        """Meta - a model defined in OpenAPI

        :param communication_expiry: The communication_expiry of this Meta.
        :param communication_hint: The communication_hint of this Meta.
        :param communication_medium: The communication_medium of this Meta.
        """
        self.openapi_types = {
            'communication_expiry': str,
            'communication_hint': str,
            'communication_medium': str
        }

        self.attribute_map = {
            'communication_expiry': 'communicationExpiry',
            'communication_hint': 'communicationHint',
            'communication_medium': 'communicationMedium'
        }

        self._communication_expiry = communication_expiry
        self._communication_hint = communication_hint
        self._communication_medium = communication_medium

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Meta':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Meta of this Meta.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def communication_expiry(self):
        """Gets the communication_expiry of this Meta.


        :return: The communication_expiry of this Meta.
        :rtype: str
        """
        return self._communication_expiry

    @communication_expiry.setter
    def communication_expiry(self, communication_expiry):
        """Sets the communication_expiry of this Meta.


        :param communication_expiry: The communication_expiry of this Meta.
        :type communication_expiry: str
        """

        self._communication_expiry = communication_expiry

    @property
    def communication_hint(self):
        """Gets the communication_hint of this Meta.


        :return: The communication_hint of this Meta.
        :rtype: str
        """
        return self._communication_hint

    @communication_hint.setter
    def communication_hint(self, communication_hint):
        """Sets the communication_hint of this Meta.


        :param communication_hint: The communication_hint of this Meta.
        :type communication_hint: str
        """

        self._communication_hint = communication_hint

    @property
    def communication_medium(self):
        """Gets the communication_medium of this Meta.


        :return: The communication_medium of this Meta.
        :rtype: str
        """
        return self._communication_medium

    @communication_medium.setter
    def communication_medium(self, communication_medium):
        """Sets the communication_medium of this Meta.


        :param communication_medium: The communication_medium of this Meta.
        :type communication_medium: str
        """
        allowed_values = ["MOBILE", "EMAIL"]  # noqa: E501
        if communication_medium not in allowed_values:
            raise ValueError(
                "Invalid value for `communication_medium` ({0}), must be one of {1}"
                .format(communication_medium, allowed_values)
            )

        self._communication_medium = communication_medium
