# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.webhook_events200_response_result import WebhookEvents200ResponseResult
from openapi_server import util


class WebhookEvents200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result: WebhookEvents200ResponseResult=None, return_code: int=None, return_message: str=None):
        """WebhookEvents200Response - a model defined in OpenAPI

        :param result: The result of this WebhookEvents200Response.
        :param return_code: The return_code of this WebhookEvents200Response.
        :param return_message: The return_message of this WebhookEvents200Response.
        """
        self.openapi_types = {
            'result': WebhookEvents200ResponseResult,
            'return_code': int,
            'return_message': str
        }

        self.attribute_map = {
            'result': 'result',
            'return_code': 'return_code',
            'return_message': 'return_message'
        }

        self._result = result
        self._return_code = return_code
        self._return_message = return_message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebhookEvents200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebhookEvents_200_response of this WebhookEvents200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this WebhookEvents200Response.


        :return: The result of this WebhookEvents200Response.
        :rtype: WebhookEvents200ResponseResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this WebhookEvents200Response.


        :param result: The result of this WebhookEvents200Response.
        :type result: WebhookEvents200ResponseResult
        """

        self._result = result

    @property
    def return_code(self):
        """Gets the return_code of this WebhookEvents200Response.


        :return: The return_code of this WebhookEvents200Response.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this WebhookEvents200Response.


        :param return_code: The return_code of this WebhookEvents200Response.
        :type return_code: int
        """

        self._return_code = return_code

    @property
    def return_message(self):
        """Gets the return_message of this WebhookEvents200Response.


        :return: The return_message of this WebhookEvents200Response.
        :rtype: str
        """
        return self._return_message

    @return_message.setter
    def return_message(self, return_message):
        """Sets the return_message of this WebhookEvents200Response.


        :param return_message: The return_message of this WebhookEvents200Response.
        :type return_message: str
        """

        self._return_message = return_message
