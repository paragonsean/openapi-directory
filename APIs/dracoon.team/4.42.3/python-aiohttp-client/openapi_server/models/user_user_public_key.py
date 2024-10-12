# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.public_key_container import PublicKeyContainer
from openapi_server import util


class UserUserPublicKey(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, public_key_container: PublicKeyContainer=None):
        """UserUserPublicKey - a model defined in OpenAPI

        :param id: The id of this UserUserPublicKey.
        :param public_key_container: The public_key_container of this UserUserPublicKey.
        """
        self.openapi_types = {
            'id': int,
            'public_key_container': PublicKeyContainer
        }

        self.attribute_map = {
            'id': 'id',
            'public_key_container': 'publicKeyContainer'
        }

        self._id = id
        self._public_key_container = public_key_container

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserUserPublicKey':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserUserPublicKey of this UserUserPublicKey.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this UserUserPublicKey.

        Unique identifier for the user

        :return: The id of this UserUserPublicKey.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserUserPublicKey.

        Unique identifier for the user

        :param id: The id of this UserUserPublicKey.
        :type id: int
        """

        self._id = id

    @property
    def public_key_container(self):
        """Gets the public_key_container of this UserUserPublicKey.


        :return: The public_key_container of this UserUserPublicKey.
        :rtype: PublicKeyContainer
        """
        return self._public_key_container

    @public_key_container.setter
    def public_key_container(self, public_key_container):
        """Sets the public_key_container of this UserUserPublicKey.


        :param public_key_container: The public_key_container of this UserUserPublicKey.
        :type public_key_container: PublicKeyContainer
        """

        self._public_key_container = public_key_container
