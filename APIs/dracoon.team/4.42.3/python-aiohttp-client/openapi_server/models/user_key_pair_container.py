# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.private_key_container import PrivateKeyContainer
from openapi_server.models.public_key_container import PublicKeyContainer
from openapi_server import util


class UserKeyPairContainer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, private_key_container: PrivateKeyContainer=None, public_key_container: PublicKeyContainer=None):
        """UserKeyPairContainer - a model defined in OpenAPI

        :param private_key_container: The private_key_container of this UserKeyPairContainer.
        :param public_key_container: The public_key_container of this UserKeyPairContainer.
        """
        self.openapi_types = {
            'private_key_container': PrivateKeyContainer,
            'public_key_container': PublicKeyContainer
        }

        self.attribute_map = {
            'private_key_container': 'privateKeyContainer',
            'public_key_container': 'publicKeyContainer'
        }

        self._private_key_container = private_key_container
        self._public_key_container = public_key_container

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserKeyPairContainer':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserKeyPairContainer of this UserKeyPairContainer.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def private_key_container(self):
        """Gets the private_key_container of this UserKeyPairContainer.


        :return: The private_key_container of this UserKeyPairContainer.
        :rtype: PrivateKeyContainer
        """
        return self._private_key_container

    @private_key_container.setter
    def private_key_container(self, private_key_container):
        """Sets the private_key_container of this UserKeyPairContainer.


        :param private_key_container: The private_key_container of this UserKeyPairContainer.
        :type private_key_container: PrivateKeyContainer
        """
        if private_key_container is None:
            raise ValueError("Invalid value for `private_key_container`, must not be `None`")

        self._private_key_container = private_key_container

    @property
    def public_key_container(self):
        """Gets the public_key_container of this UserKeyPairContainer.


        :return: The public_key_container of this UserKeyPairContainer.
        :rtype: PublicKeyContainer
        """
        return self._public_key_container

    @public_key_container.setter
    def public_key_container(self, public_key_container):
        """Sets the public_key_container of this UserKeyPairContainer.


        :param public_key_container: The public_key_container of this UserKeyPairContainer.
        :type public_key_container: PublicKeyContainer
        """
        if public_key_container is None:
            raise ValueError("Invalid value for `public_key_container`, must not be `None`")

        self._public_key_container = public_key_container
