# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MasterUserMasterUserData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, type: str=None):
        """MasterUserMasterUserData - a model defined in OpenAPI

        :param id: The id of this MasterUserMasterUserData.
        :param type: The type of this MasterUserMasterUserData.
        """
        self.openapi_types = {
            'id': int,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type'
        }

        self._id = id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MasterUserMasterUserData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MasterUser_masterUser_data of this MasterUserMasterUserData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this MasterUserMasterUserData.

        ID of master user for account

        :return: The id of this MasterUserMasterUserData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MasterUserMasterUserData.

        ID of master user for account

        :param id: The id of this MasterUserMasterUserData.
        :type id: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this MasterUserMasterUserData.


        :return: The type of this MasterUserMasterUserData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MasterUserMasterUserData.


        :param type: The type of this MasterUserMasterUserData.
        :type type: str
        """
        allowed_values = ["user"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
