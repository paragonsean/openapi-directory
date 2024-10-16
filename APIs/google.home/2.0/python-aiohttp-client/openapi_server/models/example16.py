# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Example16(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bytes_received: int=None, response_code: int=None, time_for_data_fetch: int=None, time_for_http_response: int=None):
        """Example16 - a model defined in OpenAPI

        :param bytes_received: The bytes_received of this Example16.
        :param response_code: The response_code of this Example16.
        :param time_for_data_fetch: The time_for_data_fetch of this Example16.
        :param time_for_http_response: The time_for_http_response of this Example16.
        """
        self.openapi_types = {
            'bytes_received': int,
            'response_code': int,
            'time_for_data_fetch': int,
            'time_for_http_response': int
        }

        self.attribute_map = {
            'bytes_received': 'bytes_received',
            'response_code': 'response_code',
            'time_for_data_fetch': 'time_for_data_fetch',
            'time_for_http_response': 'time_for_http_response'
        }

        self._bytes_received = bytes_received
        self._response_code = response_code
        self._time_for_data_fetch = time_for_data_fetch
        self._time_for_http_response = time_for_http_response

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Example16':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Example16 of this Example16.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bytes_received(self):
        """Gets the bytes_received of this Example16.


        :return: The bytes_received of this Example16.
        :rtype: int
        """
        return self._bytes_received

    @bytes_received.setter
    def bytes_received(self, bytes_received):
        """Sets the bytes_received of this Example16.


        :param bytes_received: The bytes_received of this Example16.
        :type bytes_received: int
        """
        if bytes_received is None:
            raise ValueError("Invalid value for `bytes_received`, must not be `None`")

        self._bytes_received = bytes_received

    @property
    def response_code(self):
        """Gets the response_code of this Example16.


        :return: The response_code of this Example16.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this Example16.


        :param response_code: The response_code of this Example16.
        :type response_code: int
        """
        if response_code is None:
            raise ValueError("Invalid value for `response_code`, must not be `None`")

        self._response_code = response_code

    @property
    def time_for_data_fetch(self):
        """Gets the time_for_data_fetch of this Example16.


        :return: The time_for_data_fetch of this Example16.
        :rtype: int
        """
        return self._time_for_data_fetch

    @time_for_data_fetch.setter
    def time_for_data_fetch(self, time_for_data_fetch):
        """Sets the time_for_data_fetch of this Example16.


        :param time_for_data_fetch: The time_for_data_fetch of this Example16.
        :type time_for_data_fetch: int
        """
        if time_for_data_fetch is None:
            raise ValueError("Invalid value for `time_for_data_fetch`, must not be `None`")

        self._time_for_data_fetch = time_for_data_fetch

    @property
    def time_for_http_response(self):
        """Gets the time_for_http_response of this Example16.


        :return: The time_for_http_response of this Example16.
        :rtype: int
        """
        return self._time_for_http_response

    @time_for_http_response.setter
    def time_for_http_response(self, time_for_http_response):
        """Sets the time_for_http_response of this Example16.


        :param time_for_http_response: The time_for_http_response of this Example16.
        :type time_for_http_response: int
        """
        if time_for_http_response is None:
            raise ValueError("Invalid value for `time_for_http_response`, must not be `None`")

        self._time_for_http_response = time_for_http_response
