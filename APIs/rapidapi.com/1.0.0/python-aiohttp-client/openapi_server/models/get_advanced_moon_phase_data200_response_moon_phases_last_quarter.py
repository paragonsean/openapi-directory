# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_advanced_moon_phase_data200_response_moon_phases_last_quarter_current import GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent
from openapi_server.models.get_advanced_moon_phase_data200_response_moon_phases_last_quarter_next import GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext
from openapi_server import util


class GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current: GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent=None, next: GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext=None):
        """GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter - a model defined in OpenAPI

        :param current: The current of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.
        :param next: The next of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.
        """
        self.openapi_types = {
            'current': GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent,
            'next': GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext
        }

        self.attribute_map = {
            'current': 'current',
            'next': 'next'
        }

        self._current = current
        self._next = next

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getAdvancedMoonPhaseData_200_response_moon_phases_last_quarter of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current(self):
        """Gets the current of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.


        :return: The current of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.
        :rtype: GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.


        :param current: The current of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.
        :type current: GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterCurrent
        """

        self._current = current

    @property
    def next(self):
        """Gets the next of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.


        :return: The next of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.
        :rtype: GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.


        :param next: The next of this GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarter.
        :type next: GetAdvancedMoonPhaseData200ResponseMoonPhasesLastQuarterNext
        """

        self._next = next
