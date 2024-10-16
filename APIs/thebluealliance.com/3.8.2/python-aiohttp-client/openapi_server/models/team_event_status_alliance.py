# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.team_event_status_alliance_backup import TeamEventStatusAllianceBackup
from openapi_server import util


class TeamEventStatusAlliance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, backup: TeamEventStatusAllianceBackup=None, name: str=None, number: int=None, pick: int=None):
        """TeamEventStatusAlliance - a model defined in OpenAPI

        :param backup: The backup of this TeamEventStatusAlliance.
        :param name: The name of this TeamEventStatusAlliance.
        :param number: The number of this TeamEventStatusAlliance.
        :param pick: The pick of this TeamEventStatusAlliance.
        """
        self.openapi_types = {
            'backup': TeamEventStatusAllianceBackup,
            'name': str,
            'number': int,
            'pick': int
        }

        self.attribute_map = {
            'backup': 'backup',
            'name': 'name',
            'number': 'number',
            'pick': 'pick'
        }

        self._backup = backup
        self._name = name
        self._number = number
        self._pick = pick

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TeamEventStatusAlliance':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Team_Event_Status_alliance of this TeamEventStatusAlliance.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def backup(self):
        """Gets the backup of this TeamEventStatusAlliance.


        :return: The backup of this TeamEventStatusAlliance.
        :rtype: TeamEventStatusAllianceBackup
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """Sets the backup of this TeamEventStatusAlliance.


        :param backup: The backup of this TeamEventStatusAlliance.
        :type backup: TeamEventStatusAllianceBackup
        """

        self._backup = backup

    @property
    def name(self):
        """Gets the name of this TeamEventStatusAlliance.

        Alliance name, may be null.

        :return: The name of this TeamEventStatusAlliance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamEventStatusAlliance.

        Alliance name, may be null.

        :param name: The name of this TeamEventStatusAlliance.
        :type name: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this TeamEventStatusAlliance.

        Alliance number.

        :return: The number of this TeamEventStatusAlliance.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TeamEventStatusAlliance.

        Alliance number.

        :param number: The number of this TeamEventStatusAlliance.
        :type number: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")

        self._number = number

    @property
    def pick(self):
        """Gets the pick of this TeamEventStatusAlliance.

        Order the team was picked in the alliance from 0-2, with 0 being alliance captain.

        :return: The pick of this TeamEventStatusAlliance.
        :rtype: int
        """
        return self._pick

    @pick.setter
    def pick(self, pick):
        """Sets the pick of this TeamEventStatusAlliance.

        Order the team was picked in the alliance from 0-2, with 0 being alliance captain.

        :param pick: The pick of this TeamEventStatusAlliance.
        :type pick: int
        """
        if pick is None:
            raise ValueError("Invalid value for `pick`, must not be `None`")

        self._pick = pick
