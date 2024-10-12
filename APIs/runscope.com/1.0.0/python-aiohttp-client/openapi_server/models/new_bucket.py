# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class NewBucket(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, team_id: str=None):
        """NewBucket - a model defined in OpenAPI

        :param name: The name of this NewBucket.
        :param team_id: The team_id of this NewBucket.
        """
        self.openapi_types = {
            'name': str,
            'team_id': str
        }

        self.attribute_map = {
            'name': 'name',
            'team_id': 'team_id'
        }

        self._name = name
        self._team_id = team_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NewBucket':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NewBucket of this NewBucket.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this NewBucket.

        Name of this bucket

        :return: The name of this NewBucket.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewBucket.

        Name of this bucket

        :param name: The name of this NewBucket.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def team_id(self):
        """Gets the team_id of this NewBucket.

        Unique identifier for the team to create this bucket for.

        :return: The team_id of this NewBucket.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this NewBucket.

        Unique identifier for the team to create this bucket for.

        :param team_id: The team_id of this NewBucket.
        :type team_id: str
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")

        self._team_id = team_id
