# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.ssh_key import SSHKey
from openapi_server.models.user import User
from openapi_server import util


class SSHKeyResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: SSHKey=None, included: List[User]=None, response_status: int=None):
        """SSHKeyResponse - a model defined in OpenAPI

        :param data: The data of this SSHKeyResponse.
        :param included: The included of this SSHKeyResponse.
        :param response_status: The response_status of this SSHKeyResponse.
        """
        self.openapi_types = {
            'data': SSHKey,
            'included': List[User],
            'response_status': int
        }

        self.attribute_map = {
            'data': 'data',
            'included': 'included',
            'response_status': 'responseStatus'
        }

        self._data = data
        self._included = included
        self._response_status = response_status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SSHKeyResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SSHKeyResponse of this SSHKeyResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this SSHKeyResponse.


        :return: The data of this SSHKeyResponse.
        :rtype: SSHKey
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SSHKeyResponse.


        :param data: The data of this SSHKeyResponse.
        :type data: SSHKey
        """

        self._data = data

    @property
    def included(self):
        """Gets the included of this SSHKeyResponse.


        :return: The included of this SSHKeyResponse.
        :rtype: List[User]
        """
        return self._included

    @included.setter
    def included(self, included):
        """Sets the included of this SSHKeyResponse.


        :param included: The included of this SSHKeyResponse.
        :type included: List[User]
        """

        self._included = included

    @property
    def response_status(self):
        """Gets the response_status of this SSHKeyResponse.

        Http status code of the response.

        :return: The response_status of this SSHKeyResponse.
        :rtype: int
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        """Sets the response_status of this SSHKeyResponse.

        Http status code of the response.

        :param response_status: The response_status of this SSHKeyResponse.
        :type response_status: int
        """

        self._response_status = response_status
