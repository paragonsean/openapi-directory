# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateStoreSecretResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, secret_id: str=None):
        """CreateStoreSecretResponse - a model defined in OpenAPI

        :param secret_id: The secret_id of this CreateStoreSecretResponse.
        """
        self.openapi_types = {
            'secret_id': str
        }

        self.attribute_map = {
            'secret_id': 'secret_id'
        }

        self._secret_id = secret_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateStoreSecretResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateStoreSecretResponse of this CreateStoreSecretResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def secret_id(self):
        """Gets the secret_id of this CreateStoreSecretResponse.

        the secret id for store secret

        :return: The secret_id of this CreateStoreSecretResponse.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """Sets the secret_id of this CreateStoreSecretResponse.

        the secret id for store secret

        :param secret_id: The secret_id of this CreateStoreSecretResponse.
        :type secret_id: str
        """

        self._secret_id = secret_id
