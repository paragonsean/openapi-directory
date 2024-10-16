# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.moderation_action import ModerationAction
from openapi_server import util


class ModerationHistoryItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action: ModerationAction=None, _date: datetime=None, notes: str=None):
        """ModerationHistoryItem - a model defined in OpenAPI

        :param action: The action of this ModerationHistoryItem.
        :param _date: The _date of this ModerationHistoryItem.
        :param notes: The notes of this ModerationHistoryItem.
        """
        self.openapi_types = {
            'action': ModerationAction,
            '_date': datetime,
            'notes': str
        }

        self.attribute_map = {
            'action': 'action',
            '_date': 'date',
            'notes': 'notes'
        }

        self._action = action
        self.__date = _date
        self._notes = notes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ModerationHistoryItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ModerationHistoryItem of this ModerationHistoryItem.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self):
        """Gets the action of this ModerationHistoryItem.


        :return: The action of this ModerationHistoryItem.
        :rtype: ModerationAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ModerationHistoryItem.


        :param action: The action of this ModerationHistoryItem.
        :type action: ModerationAction
        """

        self._action = action

    @property
    def _date(self):
        """Gets the _date of this ModerationHistoryItem.


        :return: The _date of this ModerationHistoryItem.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ModerationHistoryItem.


        :param _date: The _date of this ModerationHistoryItem.
        :type _date: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")

        self.__date = _date

    @property
    def notes(self):
        """Gets the notes of this ModerationHistoryItem.


        :return: The notes of this ModerationHistoryItem.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ModerationHistoryItem.


        :param notes: The notes of this ModerationHistoryItem.
        :type notes: str
        """

        self._notes = notes
