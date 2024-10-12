# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ServicePrincipalProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_id: str=None, secret: str=None):
        """ServicePrincipalProperties - a model defined in OpenAPI

        :param client_id: The client_id of this ServicePrincipalProperties.
        :param secret: The secret of this ServicePrincipalProperties.
        """
        self.openapi_types = {
            'client_id': str,
            'secret': str
        }

        self.attribute_map = {
            'client_id': 'clientId',
            'secret': 'secret'
        }

        self._client_id = client_id
        self._secret = secret

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServicePrincipalProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ServicePrincipalProperties of this ServicePrincipalProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_id(self):
        """Gets the client_id of this ServicePrincipalProperties.

        The service principal client ID

        :return: The client_id of this ServicePrincipalProperties.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ServicePrincipalProperties.

        The service principal client ID

        :param client_id: The client_id of this ServicePrincipalProperties.
        :type client_id: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this ServicePrincipalProperties.

        The service principal secret. This is not returned in response of GET/PUT on the resource. To see this please call listKeys.

        :return: The secret of this ServicePrincipalProperties.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this ServicePrincipalProperties.

        The service principal secret. This is not returned in response of GET/PUT on the resource. To see this please call listKeys.

        :param secret: The secret of this ServicePrincipalProperties.
        :type secret: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")

        self._secret = secret
