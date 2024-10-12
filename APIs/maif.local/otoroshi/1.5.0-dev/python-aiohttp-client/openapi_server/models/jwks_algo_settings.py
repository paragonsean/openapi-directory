# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class JWKSAlgoSettings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, headers: Dict[str, str]=None, kty: str=None, timeout: int=None, ttl: int=None, type: str=None, url: str=None):
        """JWKSAlgoSettings - a model defined in OpenAPI

        :param headers: The headers of this JWKSAlgoSettings.
        :param kty: The kty of this JWKSAlgoSettings.
        :param timeout: The timeout of this JWKSAlgoSettings.
        :param ttl: The ttl of this JWKSAlgoSettings.
        :param type: The type of this JWKSAlgoSettings.
        :param url: The url of this JWKSAlgoSettings.
        """
        self.openapi_types = {
            'headers': Dict[str, str],
            'kty': str,
            'timeout': int,
            'ttl': int,
            'type': str,
            'url': str
        }

        self.attribute_map = {
            'headers': 'headers',
            'kty': 'kty',
            'timeout': 'timeout',
            'ttl': 'ttl',
            'type': 'type',
            'url': 'url'
        }

        self._headers = headers
        self._kty = kty
        self._timeout = timeout
        self._ttl = ttl
        self._type = type
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JWKSAlgoSettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JWKSAlgoSettings of this JWKSAlgoSettings.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def headers(self):
        """Gets the headers of this JWKSAlgoSettings.

        The headers for the http call

        :return: The headers of this JWKSAlgoSettings.
        :rtype: Dict[str, str]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this JWKSAlgoSettings.

        The headers for the http call

        :param headers: The headers of this JWKSAlgoSettings.
        :type headers: Dict[str, str]
        """

        self._headers = headers

    @property
    def kty(self):
        """Gets the kty of this JWKSAlgoSettings.

        The type of key: RSA or EC

        :return: The kty of this JWKSAlgoSettings.
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """Sets the kty of this JWKSAlgoSettings.

        The type of key: RSA or EC

        :param kty: The kty of this JWKSAlgoSettings.
        :type kty: str
        """

        self._kty = kty

    @property
    def timeout(self):
        """Gets the timeout of this JWKSAlgoSettings.

        The timeout of the http call

        :return: The timeout of this JWKSAlgoSettings.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this JWKSAlgoSettings.

        The timeout of the http call

        :param timeout: The timeout of this JWKSAlgoSettings.
        :type timeout: int
        """

        self._timeout = timeout

    @property
    def ttl(self):
        """Gets the ttl of this JWKSAlgoSettings.

        The ttl of the keyset

        :return: The ttl of this JWKSAlgoSettings.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this JWKSAlgoSettings.

        The ttl of the keyset

        :param ttl: The ttl of this JWKSAlgoSettings.
        :type ttl: int
        """

        self._ttl = ttl

    @property
    def type(self):
        """Gets the type of this JWKSAlgoSettings.

        String with value JWKSAlgoSettings

        :return: The type of this JWKSAlgoSettings.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JWKSAlgoSettings.

        String with value JWKSAlgoSettings

        :param type: The type of this JWKSAlgoSettings.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def url(self):
        """Gets the url of this JWKSAlgoSettings.

        The url for the http call

        :return: The url of this JWKSAlgoSettings.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this JWKSAlgoSettings.

        The url for the http call

        :param url: The url of this JWKSAlgoSettings.
        :type url: str
        """

        self._url = url
