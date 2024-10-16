# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.live_endpoint import LiveEndpoint
from openapi_server.models.live_event1 import LiveEvent1
from openapi_server.models.match import Match
from openapi_server import util


class Live(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, endpoints: List[LiveEndpoint]=None, event: LiveEvent1=None, match: Match=None):
        """Live - a model defined in OpenAPI

        :param endpoints: The endpoints of this Live.
        :param event: The event of this Live.
        :param match: The match of this Live.
        """
        self.openapi_types = {
            'endpoints': List[LiveEndpoint],
            'event': LiveEvent1,
            'match': Match
        }

        self.attribute_map = {
            'endpoints': 'endpoints',
            'event': 'event',
            'match': 'match'
        }

        self._endpoints = endpoints
        self._event = event
        self._match = match

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Live':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Live of this Live.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def endpoints(self):
        """Gets the endpoints of this Live.


        :return: The endpoints of this Live.
        :rtype: List[LiveEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this Live.


        :param endpoints: The endpoints of this Live.
        :type endpoints: List[LiveEndpoint]
        """
        if endpoints is None:
            raise ValueError("Invalid value for `endpoints`, must not be `None`")

        self._endpoints = endpoints

    @property
    def event(self):
        """Gets the event of this Live.


        :return: The event of this Live.
        :rtype: LiveEvent1
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this Live.


        :param event: The event of this Live.
        :type event: LiveEvent1
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")

        self._event = event

    @property
    def match(self):
        """Gets the match of this Live.


        :return: The match of this Live.
        :rtype: Match
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this Live.


        :param match: The match of this Live.
        :type match: Match
        """
        if match is None:
            raise ValueError("Invalid value for `match`, must not be `None`")

        self._match = match
