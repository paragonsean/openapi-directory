# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateNetworkGroupPolicyRequestSchedulingFriday(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, active: bool=None, _from: str=None, to: str=None):
        """CreateNetworkGroupPolicyRequestSchedulingFriday - a model defined in OpenAPI

        :param active: The active of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :param _from: The _from of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :param to: The to of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        """
        self.openapi_types = {
            'active': bool,
            '_from': str,
            'to': str
        }

        self.attribute_map = {
            'active': 'active',
            '_from': 'from',
            'to': 'to'
        }

        self._active = active
        self.__from = _from
        self._to = to

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkGroupPolicyRequestSchedulingFriday':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkGroupPolicy_request_scheduling_friday of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def active(self):
        """Gets the active of this CreateNetworkGroupPolicyRequestSchedulingFriday.

        Whether the schedule is active (true) or inactive (false) during the time specified between 'from' and 'to'. Defaults to true.

        :return: The active of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this CreateNetworkGroupPolicyRequestSchedulingFriday.

        Whether the schedule is active (true) or inactive (false) during the time specified between 'from' and 'to'. Defaults to true.

        :param active: The active of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :type active: bool
        """

        self._active = active

    @property
    def _from(self):
        """Gets the _from of this CreateNetworkGroupPolicyRequestSchedulingFriday.

        The time, from '00:00' to '24:00'. Must be less than the time specified in 'to'. Defaults to '00:00'. Only 30 minute increments are allowed.

        :return: The _from of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this CreateNetworkGroupPolicyRequestSchedulingFriday.

        The time, from '00:00' to '24:00'. Must be less than the time specified in 'to'. Defaults to '00:00'. Only 30 minute increments are allowed.

        :param _from: The _from of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :type _from: str
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this CreateNetworkGroupPolicyRequestSchedulingFriday.

        The time, from '00:00' to '24:00'. Must be greater than the time specified in 'from'. Defaults to '24:00'. Only 30 minute increments are allowed.

        :return: The to of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this CreateNetworkGroupPolicyRequestSchedulingFriday.

        The time, from '00:00' to '24:00'. Must be greater than the time specified in 'from'. Defaults to '24:00'. Only 30 minute increments are allowed.

        :param to: The to of this CreateNetworkGroupPolicyRequestSchedulingFriday.
        :type to: str
        """

        self._to = to
