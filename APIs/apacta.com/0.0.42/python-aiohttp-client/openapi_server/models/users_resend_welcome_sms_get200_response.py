# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.users_resend_welcome_sms_get200_response_data import UsersResendWelcomeSmsGet200ResponseData
from openapi_server import util


class UsersResendWelcomeSmsGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: UsersResendWelcomeSmsGet200ResponseData=None, status: str=None):
        """UsersResendWelcomeSmsGet200Response - a model defined in OpenAPI

        :param data: The data of this UsersResendWelcomeSmsGet200Response.
        :param status: The status of this UsersResendWelcomeSmsGet200Response.
        """
        self.openapi_types = {
            'data': UsersResendWelcomeSmsGet200ResponseData,
            'status': str
        }

        self.attribute_map = {
            'data': 'data',
            'status': 'status'
        }

        self._data = data
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UsersResendWelcomeSmsGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _users_resendWelcomeSms_get_200_response of this UsersResendWelcomeSmsGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this UsersResendWelcomeSmsGet200Response.


        :return: The data of this UsersResendWelcomeSmsGet200Response.
        :rtype: UsersResendWelcomeSmsGet200ResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UsersResendWelcomeSmsGet200Response.


        :param data: The data of this UsersResendWelcomeSmsGet200Response.
        :type data: UsersResendWelcomeSmsGet200ResponseData
        """

        self._data = data

    @property
    def status(self):
        """Gets the status of this UsersResendWelcomeSmsGet200Response.


        :return: The status of this UsersResendWelcomeSmsGet200Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UsersResendWelcomeSmsGet200Response.


        :param status: The status of this UsersResendWelcomeSmsGet200Response.
        :type status: str
        """
        allowed_values = ["success", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
