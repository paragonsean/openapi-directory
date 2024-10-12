# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SdsServerTime(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, time: datetime=None):
        """SdsServerTime - a model defined in OpenAPI

        :param time: The time of this SdsServerTime.
        """
        self.openapi_types = {
            'time': datetime
        }

        self.attribute_map = {
            'time': 'time'
        }

        self._time = time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SdsServerTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SdsServerTime of this SdsServerTime.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time(self):
        """Gets the time of this SdsServerTime.

        DRACOON server time

        :return: The time of this SdsServerTime.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SdsServerTime.

        DRACOON server time

        :param time: The time of this SdsServerTime.
        :type time: datetime
        """

        self._time = time
