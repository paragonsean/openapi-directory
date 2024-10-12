# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TokenAuth1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None, trusted_shared_secret: str=None):
        """TokenAuth1 - a model defined in OpenAPI

        :param enabled: The enabled of this TokenAuth1.
        :param trusted_shared_secret: The trusted_shared_secret of this TokenAuth1.
        """
        self.openapi_types = {
            'enabled': bool,
            'trusted_shared_secret': str
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'trusted_shared_secret': 'trusted_shared_secret'
        }

        self._enabled = enabled
        self._trusted_shared_secret = trusted_shared_secret

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TokenAuth1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The token_auth_1 of this TokenAuth1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this TokenAuth1.

        Specify <strong>true</strong> to enable token authorization or <strong>false</strong> to disable.

        :return: The enabled of this TokenAuth1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this TokenAuth1.

        Specify <strong>true</strong> to enable token authorization or <strong>false</strong> to disable.

        :param enabled: The enabled of this TokenAuth1.
        :type enabled: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")

        self._enabled = enabled

    @property
    def trusted_shared_secret(self):
        """Gets the trusted_shared_secret of this TokenAuth1.

        The trusted shared secret of the token authorization. Must contain only hexadecimal characters and be an even number of total characters not exceeding 32.

        :return: The trusted_shared_secret of this TokenAuth1.
        :rtype: str
        """
        return self._trusted_shared_secret

    @trusted_shared_secret.setter
    def trusted_shared_secret(self, trusted_shared_secret):
        """Sets the trusted_shared_secret of this TokenAuth1.

        The trusted shared secret of the token authorization. Must contain only hexadecimal characters and be an even number of total characters not exceeding 32.

        :param trusted_shared_secret: The trusted_shared_secret of this TokenAuth1.
        :type trusted_shared_secret: str
        """
        if trusted_shared_secret is None:
            raise ValueError("Invalid value for `trusted_shared_secret`, must not be `None`")

        self._trusted_shared_secret = trusted_shared_secret
