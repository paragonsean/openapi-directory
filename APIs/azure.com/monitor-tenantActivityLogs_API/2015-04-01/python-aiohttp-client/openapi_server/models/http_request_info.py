# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class HttpRequestInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_ip_address: str=None, client_request_id: str=None, method: str=None, uri: str=None):
        """HttpRequestInfo - a model defined in OpenAPI

        :param client_ip_address: The client_ip_address of this HttpRequestInfo.
        :param client_request_id: The client_request_id of this HttpRequestInfo.
        :param method: The method of this HttpRequestInfo.
        :param uri: The uri of this HttpRequestInfo.
        """
        self.openapi_types = {
            'client_ip_address': str,
            'client_request_id': str,
            'method': str,
            'uri': str
        }

        self.attribute_map = {
            'client_ip_address': 'clientIpAddress',
            'client_request_id': 'clientRequestId',
            'method': 'method',
            'uri': 'uri'
        }

        self._client_ip_address = client_ip_address
        self._client_request_id = client_request_id
        self._method = method
        self._uri = uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HttpRequestInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HttpRequestInfo of this HttpRequestInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_ip_address(self):
        """Gets the client_ip_address of this HttpRequestInfo.

        the client Ip Address

        :return: The client_ip_address of this HttpRequestInfo.
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address):
        """Sets the client_ip_address of this HttpRequestInfo.

        the client Ip Address

        :param client_ip_address: The client_ip_address of this HttpRequestInfo.
        :type client_ip_address: str
        """

        self._client_ip_address = client_ip_address

    @property
    def client_request_id(self):
        """Gets the client_request_id of this HttpRequestInfo.

        the client request id.

        :return: The client_request_id of this HttpRequestInfo.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this HttpRequestInfo.

        the client request id.

        :param client_request_id: The client_request_id of this HttpRequestInfo.
        :type client_request_id: str
        """

        self._client_request_id = client_request_id

    @property
    def method(self):
        """Gets the method of this HttpRequestInfo.

        the Http request method.

        :return: The method of this HttpRequestInfo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this HttpRequestInfo.

        the Http request method.

        :param method: The method of this HttpRequestInfo.
        :type method: str
        """

        self._method = method

    @property
    def uri(self):
        """Gets the uri of this HttpRequestInfo.

        the Uri.

        :return: The uri of this HttpRequestInfo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this HttpRequestInfo.

        the Uri.

        :param uri: The uri of this HttpRequestInfo.
        :type uri: str
        """

        self._uri = uri
