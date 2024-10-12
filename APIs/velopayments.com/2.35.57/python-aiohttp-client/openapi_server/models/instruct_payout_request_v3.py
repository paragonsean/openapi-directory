# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InstructPayoutRequestV3(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fx_rate_degredation_threshold_percentage: float=None):
        """InstructPayoutRequestV3 - a model defined in OpenAPI

        :param fx_rate_degredation_threshold_percentage: The fx_rate_degredation_threshold_percentage of this InstructPayoutRequestV3.
        """
        self.openapi_types = {
            'fx_rate_degredation_threshold_percentage': float
        }

        self.attribute_map = {
            'fx_rate_degredation_threshold_percentage': 'fxRateDegredationThresholdPercentage'
        }

        self._fx_rate_degredation_threshold_percentage = fx_rate_degredation_threshold_percentage

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InstructPayoutRequestV3':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InstructPayoutRequestV3 of this InstructPayoutRequestV3.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fx_rate_degredation_threshold_percentage(self):
        """Gets the fx_rate_degredation_threshold_percentage of this InstructPayoutRequestV3.

        Halt instruction if the FX rates have become worse since the last quote

        :return: The fx_rate_degredation_threshold_percentage of this InstructPayoutRequestV3.
        :rtype: float
        """
        return self._fx_rate_degredation_threshold_percentage

    @fx_rate_degredation_threshold_percentage.setter
    def fx_rate_degredation_threshold_percentage(self, fx_rate_degredation_threshold_percentage):
        """Sets the fx_rate_degredation_threshold_percentage of this InstructPayoutRequestV3.

        Halt instruction if the FX rates have become worse since the last quote

        :param fx_rate_degredation_threshold_percentage: The fx_rate_degredation_threshold_percentage of this InstructPayoutRequestV3.
        :type fx_rate_degredation_threshold_percentage: float
        """

        self._fx_rate_degredation_threshold_percentage = fx_rate_degredation_threshold_percentage
