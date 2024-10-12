# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sms200_response_messages_inner import Sms200ResponseMessagesInner
from openapi_server import util


class Sms200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, balance: float=None, debug: str=None, messages: List[Sms200ResponseMessagesInner]=None, sms_type: str=None, success: str=None, total_price: float=None):
        """Sms200Response - a model defined in OpenAPI

        :param balance: The balance of this Sms200Response.
        :param debug: The debug of this Sms200Response.
        :param messages: The messages of this Sms200Response.
        :param sms_type: The sms_type of this Sms200Response.
        :param success: The success of this Sms200Response.
        :param total_price: The total_price of this Sms200Response.
        """
        self.openapi_types = {
            'balance': float,
            'debug': str,
            'messages': List[Sms200ResponseMessagesInner],
            'sms_type': str,
            'success': str,
            'total_price': float
        }

        self.attribute_map = {
            'balance': 'balance',
            'debug': 'debug',
            'messages': 'messages',
            'sms_type': 'sms_type',
            'success': 'success',
            'total_price': 'total_price'
        }

        self._balance = balance
        self._debug = debug
        self._messages = messages
        self._sms_type = sms_type
        self._success = success
        self._total_price = total_price

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Sms200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Sms_200_response of this Sms200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def balance(self):
        """Gets the balance of this Sms200Response.


        :return: The balance of this Sms200Response.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Sms200Response.


        :param balance: The balance of this Sms200Response.
        :type balance: float
        """

        self._balance = balance

    @property
    def debug(self):
        """Gets the debug of this Sms200Response.


        :return: The debug of this Sms200Response.
        :rtype: str
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this Sms200Response.


        :param debug: The debug of this Sms200Response.
        :type debug: str
        """

        self._debug = debug

    @property
    def messages(self):
        """Gets the messages of this Sms200Response.


        :return: The messages of this Sms200Response.
        :rtype: List[Sms200ResponseMessagesInner]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Sms200Response.


        :param messages: The messages of this Sms200Response.
        :type messages: List[Sms200ResponseMessagesInner]
        """

        self._messages = messages

    @property
    def sms_type(self):
        """Gets the sms_type of this Sms200Response.


        :return: The sms_type of this Sms200Response.
        :rtype: str
        """
        return self._sms_type

    @sms_type.setter
    def sms_type(self, sms_type):
        """Sets the sms_type of this Sms200Response.


        :param sms_type: The sms_type of this Sms200Response.
        :type sms_type: str
        """
        allowed_values = ["economy", "direct"]  # noqa: E501
        if sms_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sms_type` ({0}), must be one of {1}"
                .format(sms_type, allowed_values)
            )

        self._sms_type = sms_type

    @property
    def success(self):
        """Gets the success of this Sms200Response.


        :return: The success of this Sms200Response.
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this Sms200Response.


        :param success: The success of this Sms200Response.
        :type success: str
        """

        self._success = success

    @property
    def total_price(self):
        """Gets the total_price of this Sms200Response.


        :return: The total_price of this Sms200Response.
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this Sms200Response.


        :param total_price: The total_price of this Sms200Response.
        :type total_price: float
        """

        self._total_price = total_price
