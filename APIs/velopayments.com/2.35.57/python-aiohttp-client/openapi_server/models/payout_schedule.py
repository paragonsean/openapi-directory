# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PayoutSchedule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, notifications_enabled: bool=None, schedule_status: str=None, scheduled_at: datetime=None, scheduled_by: str=None, scheduled_by_principal_id: str=None, scheduled_for: datetime=None):
        """PayoutSchedule - a model defined in OpenAPI

        :param notifications_enabled: The notifications_enabled of this PayoutSchedule.
        :param schedule_status: The schedule_status of this PayoutSchedule.
        :param scheduled_at: The scheduled_at of this PayoutSchedule.
        :param scheduled_by: The scheduled_by of this PayoutSchedule.
        :param scheduled_by_principal_id: The scheduled_by_principal_id of this PayoutSchedule.
        :param scheduled_for: The scheduled_for of this PayoutSchedule.
        """
        self.openapi_types = {
            'notifications_enabled': bool,
            'schedule_status': str,
            'scheduled_at': datetime,
            'scheduled_by': str,
            'scheduled_by_principal_id': str,
            'scheduled_for': datetime
        }

        self.attribute_map = {
            'notifications_enabled': 'notificationsEnabled',
            'schedule_status': 'scheduleStatus',
            'scheduled_at': 'scheduledAt',
            'scheduled_by': 'scheduledBy',
            'scheduled_by_principal_id': 'scheduledByPrincipalId',
            'scheduled_for': 'scheduledFor'
        }

        self._notifications_enabled = notifications_enabled
        self._schedule_status = schedule_status
        self._scheduled_at = scheduled_at
        self._scheduled_by = scheduled_by
        self._scheduled_by_principal_id = scheduled_by_principal_id
        self._scheduled_for = scheduled_for

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PayoutSchedule':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PayoutSchedule of this PayoutSchedule.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notifications_enabled(self):
        """Gets the notifications_enabled of this PayoutSchedule.


        :return: The notifications_enabled of this PayoutSchedule.
        :rtype: bool
        """
        return self._notifications_enabled

    @notifications_enabled.setter
    def notifications_enabled(self, notifications_enabled):
        """Sets the notifications_enabled of this PayoutSchedule.


        :param notifications_enabled: The notifications_enabled of this PayoutSchedule.
        :type notifications_enabled: bool
        """
        if notifications_enabled is None:
            raise ValueError("Invalid value for `notifications_enabled`, must not be `None`")

        self._notifications_enabled = notifications_enabled

    @property
    def schedule_status(self):
        """Gets the schedule_status of this PayoutSchedule.

        Current status of the payout schedule. One of the following values: SCHEDULED, EXECUTED, FAILED

        :return: The schedule_status of this PayoutSchedule.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this PayoutSchedule.

        Current status of the payout schedule. One of the following values: SCHEDULED, EXECUTED, FAILED

        :param schedule_status: The schedule_status of this PayoutSchedule.
        :type schedule_status: str
        """
        if schedule_status is None:
            raise ValueError("Invalid value for `schedule_status`, must not be `None`")

        self._schedule_status = schedule_status

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this PayoutSchedule.


        :return: The scheduled_at of this PayoutSchedule.
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this PayoutSchedule.


        :param scheduled_at: The scheduled_at of this PayoutSchedule.
        :type scheduled_at: datetime
        """
        if scheduled_at is None:
            raise ValueError("Invalid value for `scheduled_at`, must not be `None`")

        self._scheduled_at = scheduled_at

    @property
    def scheduled_by(self):
        """Gets the scheduled_by of this PayoutSchedule.

        Optional display name as a hint for who scheduled the payout. Not populated if payout was scheduled by an application.

        :return: The scheduled_by of this PayoutSchedule.
        :rtype: str
        """
        return self._scheduled_by

    @scheduled_by.setter
    def scheduled_by(self, scheduled_by):
        """Sets the scheduled_by of this PayoutSchedule.

        Optional display name as a hint for who scheduled the payout. Not populated if payout was scheduled by an application.

        :param scheduled_by: The scheduled_by of this PayoutSchedule.
        :type scheduled_by: str
        """

        self._scheduled_by = scheduled_by

    @property
    def scheduled_by_principal_id(self):
        """Gets the scheduled_by_principal_id of this PayoutSchedule.

        ID of the user or application that scheduled the payout

        :return: The scheduled_by_principal_id of this PayoutSchedule.
        :rtype: str
        """
        return self._scheduled_by_principal_id

    @scheduled_by_principal_id.setter
    def scheduled_by_principal_id(self, scheduled_by_principal_id):
        """Sets the scheduled_by_principal_id of this PayoutSchedule.

        ID of the user or application that scheduled the payout

        :param scheduled_by_principal_id: The scheduled_by_principal_id of this PayoutSchedule.
        :type scheduled_by_principal_id: str
        """
        if scheduled_by_principal_id is None:
            raise ValueError("Invalid value for `scheduled_by_principal_id`, must not be `None`")

        self._scheduled_by_principal_id = scheduled_by_principal_id

    @property
    def scheduled_for(self):
        """Gets the scheduled_for of this PayoutSchedule.


        :return: The scheduled_for of this PayoutSchedule.
        :rtype: datetime
        """
        return self._scheduled_for

    @scheduled_for.setter
    def scheduled_for(self, scheduled_for):
        """Sets the scheduled_for of this PayoutSchedule.


        :param scheduled_for: The scheduled_for of this PayoutSchedule.
        :type scheduled_for: datetime
        """
        if scheduled_for is None:
            raise ValueError("Invalid value for `scheduled_for`, must not be `None`")

        self._scheduled_for = scheduled_for
