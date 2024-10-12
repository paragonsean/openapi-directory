# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.schedule1 import Schedule1
from openapi_server import util


class DisableSchedule200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, schedule: Schedule1=None):
        """DisableSchedule200Response - a model defined in OpenAPI

        :param schedule: The schedule of this DisableSchedule200Response.
        """
        self.openapi_types = {
            'schedule': Schedule1
        }

        self.attribute_map = {
            'schedule': 'schedule'
        }

        self._schedule = schedule

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DisableSchedule200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The disableSchedule_200_response of this DisableSchedule200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def schedule(self):
        """Gets the schedule of this DisableSchedule200Response.


        :return: The schedule of this DisableSchedule200Response.
        :rtype: Schedule1
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this DisableSchedule200Response.


        :param schedule: The schedule of this DisableSchedule200Response.
        :type schedule: Schedule1
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")

        self._schedule = schedule
