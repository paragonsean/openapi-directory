# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.action_groups_information import ActionGroupsInformation
from openapi_server.models.detector import Detector
from openapi_server.models.throttling_information import ThrottlingInformation
from openapi_server import util


class AlertRuleProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_groups: ActionGroupsInformation=None, description: str=None, detector: Detector=None, frequency: str=None, scope: List[str]=None, severity: str=None, state: str=None, throttling: ThrottlingInformation=None):
        """AlertRuleProperties - a model defined in OpenAPI

        :param action_groups: The action_groups of this AlertRuleProperties.
        :param description: The description of this AlertRuleProperties.
        :param detector: The detector of this AlertRuleProperties.
        :param frequency: The frequency of this AlertRuleProperties.
        :param scope: The scope of this AlertRuleProperties.
        :param severity: The severity of this AlertRuleProperties.
        :param state: The state of this AlertRuleProperties.
        :param throttling: The throttling of this AlertRuleProperties.
        """
        self.openapi_types = {
            'action_groups': ActionGroupsInformation,
            'description': str,
            'detector': Detector,
            'frequency': str,
            'scope': List[str],
            'severity': str,
            'state': str,
            'throttling': ThrottlingInformation
        }

        self.attribute_map = {
            'action_groups': 'actionGroups',
            'description': 'description',
            'detector': 'detector',
            'frequency': 'frequency',
            'scope': 'scope',
            'severity': 'severity',
            'state': 'state',
            'throttling': 'throttling'
        }

        self._action_groups = action_groups
        self._description = description
        self._detector = detector
        self._frequency = frequency
        self._scope = scope
        self._severity = severity
        self._state = state
        self._throttling = throttling

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AlertRuleProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AlertRuleProperties of this AlertRuleProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_groups(self):
        """Gets the action_groups of this AlertRuleProperties.


        :return: The action_groups of this AlertRuleProperties.
        :rtype: ActionGroupsInformation
        """
        return self._action_groups

    @action_groups.setter
    def action_groups(self, action_groups):
        """Sets the action_groups of this AlertRuleProperties.


        :param action_groups: The action_groups of this AlertRuleProperties.
        :type action_groups: ActionGroupsInformation
        """
        if action_groups is None:
            raise ValueError("Invalid value for `action_groups`, must not be `None`")

        self._action_groups = action_groups

    @property
    def description(self):
        """Gets the description of this AlertRuleProperties.

        The alert rule description.

        :return: The description of this AlertRuleProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlertRuleProperties.

        The alert rule description.

        :param description: The description of this AlertRuleProperties.
        :type description: str
        """

        self._description = description

    @property
    def detector(self):
        """Gets the detector of this AlertRuleProperties.


        :return: The detector of this AlertRuleProperties.
        :rtype: Detector
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this AlertRuleProperties.


        :param detector: The detector of this AlertRuleProperties.
        :type detector: Detector
        """
        if detector is None:
            raise ValueError("Invalid value for `detector`, must not be `None`")

        self._detector = detector

    @property
    def frequency(self):
        """Gets the frequency of this AlertRuleProperties.

        The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes.

        :return: The frequency of this AlertRuleProperties.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this AlertRuleProperties.

        The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes.

        :param frequency: The frequency of this AlertRuleProperties.
        :type frequency: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")

        self._frequency = frequency

    @property
    def scope(self):
        """Gets the scope of this AlertRuleProperties.

        The alert rule resources scope.

        :return: The scope of this AlertRuleProperties.
        :rtype: List[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this AlertRuleProperties.

        The alert rule resources scope.

        :param scope: The scope of this AlertRuleProperties.
        :type scope: List[str]
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")

        self._scope = scope

    @property
    def severity(self):
        """Gets the severity of this AlertRuleProperties.

        The alert rule severity.

        :return: The severity of this AlertRuleProperties.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertRuleProperties.

        The alert rule severity.

        :param severity: The severity of this AlertRuleProperties.
        :type severity: str
        """
        allowed_values = ["Sev0", "Sev1", "Sev2", "Sev3", "Sev4"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def state(self):
        """Gets the state of this AlertRuleProperties.

        The alert rule state.

        :return: The state of this AlertRuleProperties.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AlertRuleProperties.

        The alert rule state.

        :param state: The state of this AlertRuleProperties.
        :type state: str
        """
        allowed_values = ["Enabled", "Disabled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def throttling(self):
        """Gets the throttling of this AlertRuleProperties.


        :return: The throttling of this AlertRuleProperties.
        :rtype: ThrottlingInformation
        """
        return self._throttling

    @throttling.setter
    def throttling(self, throttling):
        """Sets the throttling of this AlertRuleProperties.


        :param throttling: The throttling of this AlertRuleProperties.
        :type throttling: ThrottlingInformation
        """

        self._throttling = throttling
