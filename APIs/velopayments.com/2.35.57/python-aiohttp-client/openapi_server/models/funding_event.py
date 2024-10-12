# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FundingEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event_date_time: datetime=None, event_id: str=None, funding_event_type: str=None, principal: str=None):
        """FundingEvent - a model defined in OpenAPI

        :param event_date_time: The event_date_time of this FundingEvent.
        :param event_id: The event_id of this FundingEvent.
        :param funding_event_type: The funding_event_type of this FundingEvent.
        :param principal: The principal of this FundingEvent.
        """
        self.openapi_types = {
            'event_date_time': datetime,
            'event_id': str,
            'funding_event_type': str,
            'principal': str
        }

        self.attribute_map = {
            'event_date_time': 'eventDateTime',
            'event_id': 'eventId',
            'funding_event_type': 'fundingEventType',
            'principal': 'principal'
        }

        self._event_date_time = event_date_time
        self._event_id = event_id
        self._funding_event_type = funding_event_type
        self._principal = principal

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FundingEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FundingEvent of this FundingEvent.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_date_time(self):
        """Gets the event_date_time of this FundingEvent.


        :return: The event_date_time of this FundingEvent.
        :rtype: datetime
        """
        return self._event_date_time

    @event_date_time.setter
    def event_date_time(self, event_date_time):
        """Sets the event_date_time of this FundingEvent.


        :param event_date_time: The event_date_time of this FundingEvent.
        :type event_date_time: datetime
        """

        self._event_date_time = event_date_time

    @property
    def event_id(self):
        """Gets the event_id of this FundingEvent.


        :return: The event_id of this FundingEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this FundingEvent.


        :param event_id: The event_id of this FundingEvent.
        :type event_id: str
        """

        self._event_id = event_id

    @property
    def funding_event_type(self):
        """Gets the funding_event_type of this FundingEvent.

        Funding event type. One of the following values: PAYOR_FUNDING_DETECTED, PAYOR_FUNDING_REQUESTED, PAYOR_FUNDING_RETURN_RECEIVED, FUNDING_RETURN_DETECTED, PAYOR_FUNDING_REQUEST_SUBMITTED, PAYOR_FUNDING_ENTRY_DETAIL_RECEIVED, FUNDING_DEALLOCATED

        :return: The funding_event_type of this FundingEvent.
        :rtype: str
        """
        return self._funding_event_type

    @funding_event_type.setter
    def funding_event_type(self, funding_event_type):
        """Sets the funding_event_type of this FundingEvent.

        Funding event type. One of the following values: PAYOR_FUNDING_DETECTED, PAYOR_FUNDING_REQUESTED, PAYOR_FUNDING_RETURN_RECEIVED, FUNDING_RETURN_DETECTED, PAYOR_FUNDING_REQUEST_SUBMITTED, PAYOR_FUNDING_ENTRY_DETAIL_RECEIVED, FUNDING_DEALLOCATED

        :param funding_event_type: The funding_event_type of this FundingEvent.
        :type funding_event_type: str
        """

        self._funding_event_type = funding_event_type

    @property
    def principal(self):
        """Gets the principal of this FundingEvent.


        :return: The principal of this FundingEvent.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this FundingEvent.


        :param principal: The principal of this FundingEvent.
        :type principal: str
        """

        self._principal = principal
