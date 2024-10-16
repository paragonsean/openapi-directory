# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_sensor_alerts_profile_request_schedule import CreateNetworkSensorAlertsProfileRequestSchedule
from openapi_server.models.get_network_sensor_alerts_profiles200_response_inner_conditions_inner import GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner
from openapi_server.models.get_network_sensor_alerts_profiles200_response_inner_recipients import GetNetworkSensorAlertsProfiles200ResponseInnerRecipients
from openapi_server import util


class UpdateNetworkSensorAlertsProfileRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, conditions: List[GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner]=None, name: str=None, recipients: GetNetworkSensorAlertsProfiles200ResponseInnerRecipients=None, schedule: CreateNetworkSensorAlertsProfileRequestSchedule=None, serials: List[str]=None):
        """UpdateNetworkSensorAlertsProfileRequest - a model defined in OpenAPI

        :param conditions: The conditions of this UpdateNetworkSensorAlertsProfileRequest.
        :param name: The name of this UpdateNetworkSensorAlertsProfileRequest.
        :param recipients: The recipients of this UpdateNetworkSensorAlertsProfileRequest.
        :param schedule: The schedule of this UpdateNetworkSensorAlertsProfileRequest.
        :param serials: The serials of this UpdateNetworkSensorAlertsProfileRequest.
        """
        self.openapi_types = {
            'conditions': List[GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner],
            'name': str,
            'recipients': GetNetworkSensorAlertsProfiles200ResponseInnerRecipients,
            'schedule': CreateNetworkSensorAlertsProfileRequestSchedule,
            'serials': List[str]
        }

        self.attribute_map = {
            'conditions': 'conditions',
            'name': 'name',
            'recipients': 'recipients',
            'schedule': 'schedule',
            'serials': 'serials'
        }

        self._conditions = conditions
        self._name = name
        self._recipients = recipients
        self._schedule = schedule
        self._serials = serials

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkSensorAlertsProfileRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkSensorAlertsProfile_request of this UpdateNetworkSensorAlertsProfileRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def conditions(self):
        """Gets the conditions of this UpdateNetworkSensorAlertsProfileRequest.

        List of conditions that will cause the profile to send an alert.

        :return: The conditions of this UpdateNetworkSensorAlertsProfileRequest.
        :rtype: List[GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateNetworkSensorAlertsProfileRequest.

        List of conditions that will cause the profile to send an alert.

        :param conditions: The conditions of this UpdateNetworkSensorAlertsProfileRequest.
        :type conditions: List[GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner]
        """

        self._conditions = conditions

    @property
    def name(self):
        """Gets the name of this UpdateNetworkSensorAlertsProfileRequest.

        Name of the sensor alert profile.

        :return: The name of this UpdateNetworkSensorAlertsProfileRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNetworkSensorAlertsProfileRequest.

        Name of the sensor alert profile.

        :param name: The name of this UpdateNetworkSensorAlertsProfileRequest.
        :type name: str
        """

        self._name = name

    @property
    def recipients(self):
        """Gets the recipients of this UpdateNetworkSensorAlertsProfileRequest.


        :return: The recipients of this UpdateNetworkSensorAlertsProfileRequest.
        :rtype: GetNetworkSensorAlertsProfiles200ResponseInnerRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this UpdateNetworkSensorAlertsProfileRequest.


        :param recipients: The recipients of this UpdateNetworkSensorAlertsProfileRequest.
        :type recipients: GetNetworkSensorAlertsProfiles200ResponseInnerRecipients
        """

        self._recipients = recipients

    @property
    def schedule(self):
        """Gets the schedule of this UpdateNetworkSensorAlertsProfileRequest.


        :return: The schedule of this UpdateNetworkSensorAlertsProfileRequest.
        :rtype: CreateNetworkSensorAlertsProfileRequestSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this UpdateNetworkSensorAlertsProfileRequest.


        :param schedule: The schedule of this UpdateNetworkSensorAlertsProfileRequest.
        :type schedule: CreateNetworkSensorAlertsProfileRequestSchedule
        """

        self._schedule = schedule

    @property
    def serials(self):
        """Gets the serials of this UpdateNetworkSensorAlertsProfileRequest.

        List of device serials assigned to this sensor alert profile.

        :return: The serials of this UpdateNetworkSensorAlertsProfileRequest.
        :rtype: List[str]
        """
        return self._serials

    @serials.setter
    def serials(self, serials):
        """Sets the serials of this UpdateNetworkSensorAlertsProfileRequest.

        List of device serials assigned to this sensor alert profile.

        :param serials: The serials of this UpdateNetworkSensorAlertsProfileRequest.
        :type serials: List[str]
        """

        self._serials = serials
