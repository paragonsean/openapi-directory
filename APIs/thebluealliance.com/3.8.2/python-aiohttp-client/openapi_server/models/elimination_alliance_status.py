# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.wlt_record import WLTRecord
from openapi_server import util


class EliminationAllianceStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_level_record: WLTRecord=None, level: str=None, playoff_average: float=None, record: WLTRecord=None, status: str=None):
        """EliminationAllianceStatus - a model defined in OpenAPI

        :param current_level_record: The current_level_record of this EliminationAllianceStatus.
        :param level: The level of this EliminationAllianceStatus.
        :param playoff_average: The playoff_average of this EliminationAllianceStatus.
        :param record: The record of this EliminationAllianceStatus.
        :param status: The status of this EliminationAllianceStatus.
        """
        self.openapi_types = {
            'current_level_record': WLTRecord,
            'level': str,
            'playoff_average': float,
            'record': WLTRecord,
            'status': str
        }

        self.attribute_map = {
            'current_level_record': 'current_level_record',
            'level': 'level',
            'playoff_average': 'playoff_average',
            'record': 'record',
            'status': 'status'
        }

        self._current_level_record = current_level_record
        self._level = level
        self._playoff_average = playoff_average
        self._record = record
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EliminationAllianceStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Elimination_Alliance_status of this EliminationAllianceStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_level_record(self):
        """Gets the current_level_record of this EliminationAllianceStatus.


        :return: The current_level_record of this EliminationAllianceStatus.
        :rtype: WLTRecord
        """
        return self._current_level_record

    @current_level_record.setter
    def current_level_record(self, current_level_record):
        """Sets the current_level_record of this EliminationAllianceStatus.


        :param current_level_record: The current_level_record of this EliminationAllianceStatus.
        :type current_level_record: WLTRecord
        """

        self._current_level_record = current_level_record

    @property
    def level(self):
        """Gets the level of this EliminationAllianceStatus.


        :return: The level of this EliminationAllianceStatus.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this EliminationAllianceStatus.


        :param level: The level of this EliminationAllianceStatus.
        :type level: str
        """

        self._level = level

    @property
    def playoff_average(self):
        """Gets the playoff_average of this EliminationAllianceStatus.


        :return: The playoff_average of this EliminationAllianceStatus.
        :rtype: float
        """
        return self._playoff_average

    @playoff_average.setter
    def playoff_average(self, playoff_average):
        """Sets the playoff_average of this EliminationAllianceStatus.


        :param playoff_average: The playoff_average of this EliminationAllianceStatus.
        :type playoff_average: float
        """

        self._playoff_average = playoff_average

    @property
    def record(self):
        """Gets the record of this EliminationAllianceStatus.


        :return: The record of this EliminationAllianceStatus.
        :rtype: WLTRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this EliminationAllianceStatus.


        :param record: The record of this EliminationAllianceStatus.
        :type record: WLTRecord
        """

        self._record = record

    @property
    def status(self):
        """Gets the status of this EliminationAllianceStatus.


        :return: The status of this EliminationAllianceStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EliminationAllianceStatus.


        :param status: The status of this EliminationAllianceStatus.
        :type status: str
        """

        self._status = status
