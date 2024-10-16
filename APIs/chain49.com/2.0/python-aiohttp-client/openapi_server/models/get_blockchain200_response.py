# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_blockchain200_response_backend import GetBlockchain200ResponseBackend
from openapi_server.models.get_blockchain200_response_blockbook import GetBlockchain200ResponseBlockbook
from openapi_server import util


class GetBlockchain200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, backend: GetBlockchain200ResponseBackend=None, blockbook: GetBlockchain200ResponseBlockbook=None):
        """GetBlockchain200Response - a model defined in OpenAPI

        :param backend: The backend of this GetBlockchain200Response.
        :param blockbook: The blockbook of this GetBlockchain200Response.
        """
        self.openapi_types = {
            'backend': GetBlockchain200ResponseBackend,
            'blockbook': GetBlockchain200ResponseBlockbook
        }

        self.attribute_map = {
            'backend': 'backend',
            'blockbook': 'blockbook'
        }

        self._backend = backend
        self._blockbook = blockbook

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetBlockchain200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getBlockchain_200_response of this GetBlockchain200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def backend(self):
        """Gets the backend of this GetBlockchain200Response.


        :return: The backend of this GetBlockchain200Response.
        :rtype: GetBlockchain200ResponseBackend
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """Sets the backend of this GetBlockchain200Response.


        :param backend: The backend of this GetBlockchain200Response.
        :type backend: GetBlockchain200ResponseBackend
        """

        self._backend = backend

    @property
    def blockbook(self):
        """Gets the blockbook of this GetBlockchain200Response.


        :return: The blockbook of this GetBlockchain200Response.
        :rtype: GetBlockchain200ResponseBlockbook
        """
        return self._blockbook

    @blockbook.setter
    def blockbook(self, blockbook):
        """Sets the blockbook of this GetBlockchain200Response.


        :param blockbook: The blockbook of this GetBlockchain200Response.
        :type blockbook: GetBlockchain200ResponseBlockbook
        """

        self._blockbook = blockbook
