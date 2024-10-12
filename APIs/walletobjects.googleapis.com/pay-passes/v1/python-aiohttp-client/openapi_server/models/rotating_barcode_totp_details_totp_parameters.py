# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class RotatingBarcodeTotpDetailsTotpParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, value_length: int=None):
        """RotatingBarcodeTotpDetailsTotpParameters - a model defined in OpenAPI

        :param key: The key of this RotatingBarcodeTotpDetailsTotpParameters.
        :param value_length: The value_length of this RotatingBarcodeTotpDetailsTotpParameters.
        """
        self.openapi_types = {
            'key': str,
            'value_length': int
        }

        self.attribute_map = {
            'key': 'key',
            'value_length': 'valueLength'
        }

        self._key = key
        self._value_length = value_length

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RotatingBarcodeTotpDetailsTotpParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RotatingBarcodeTotpDetailsTotpParameters of this RotatingBarcodeTotpDetailsTotpParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this RotatingBarcodeTotpDetailsTotpParameters.

        The secret key used for the TOTP value generation, encoded as a Base16 string.

        :return: The key of this RotatingBarcodeTotpDetailsTotpParameters.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RotatingBarcodeTotpDetailsTotpParameters.

        The secret key used for the TOTP value generation, encoded as a Base16 string.

        :param key: The key of this RotatingBarcodeTotpDetailsTotpParameters.
        :type key: str
        """

        self._key = key

    @property
    def value_length(self):
        """Gets the value_length of this RotatingBarcodeTotpDetailsTotpParameters.

        The length of the TOTP value in decimal digits.

        :return: The value_length of this RotatingBarcodeTotpDetailsTotpParameters.
        :rtype: int
        """
        return self._value_length

    @value_length.setter
    def value_length(self, value_length):
        """Sets the value_length of this RotatingBarcodeTotpDetailsTotpParameters.

        The length of the TOTP value in decimal digits.

        :param value_length: The value_length of this RotatingBarcodeTotpDetailsTotpParameters.
        :type value_length: int
        """

        self._value_length = value_length
