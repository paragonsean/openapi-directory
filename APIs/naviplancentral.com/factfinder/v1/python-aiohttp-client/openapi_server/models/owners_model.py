# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.owner_model import OwnerModel
from openapi_server import util


class OwnersModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, owners: List[OwnerModel]=None):
        """OwnersModel - a model defined in OpenAPI

        :param owners: The owners of this OwnersModel.
        """
        self.openapi_types = {
            'owners': List[OwnerModel]
        }

        self.attribute_map = {
            'owners': 'owners'
        }

        self._owners = owners

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OwnersModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OwnersModel of this OwnersModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def owners(self):
        """Gets the owners of this OwnersModel.


        :return: The owners of this OwnersModel.
        :rtype: List[OwnerModel]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this OwnersModel.


        :param owners: The owners of this OwnersModel.
        :type owners: List[OwnerModel]
        """

        self._owners = owners
