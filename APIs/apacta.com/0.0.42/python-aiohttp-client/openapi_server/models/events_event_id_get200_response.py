# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.event import Event
from openapi_server import util


class EventsEventIdGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: Event=None, success: bool=True):
        """EventsEventIdGet200Response - a model defined in OpenAPI

        :param data: The data of this EventsEventIdGet200Response.
        :param success: The success of this EventsEventIdGet200Response.
        """
        self.openapi_types = {
            'data': Event,
            'success': bool
        }

        self.attribute_map = {
            'data': 'data',
            'success': 'success'
        }

        self._data = data
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EventsEventIdGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _events__event_id__get_200_response of this EventsEventIdGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this EventsEventIdGet200Response.


        :return: The data of this EventsEventIdGet200Response.
        :rtype: Event
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EventsEventIdGet200Response.


        :param data: The data of this EventsEventIdGet200Response.
        :type data: Event
        """

        self._data = data

    @property
    def success(self):
        """Gets the success of this EventsEventIdGet200Response.


        :return: The success of this EventsEventIdGet200Response.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EventsEventIdGet200Response.


        :param success: The success of this EventsEventIdGet200Response.
        :type success: bool
        """

        self._success = success
