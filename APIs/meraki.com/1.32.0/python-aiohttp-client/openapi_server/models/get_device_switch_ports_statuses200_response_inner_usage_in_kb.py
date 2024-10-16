# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, recv: int=None, sent: int=None, total: int=None):
        """GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb - a model defined in OpenAPI

        :param recv: The recv of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :param sent: The sent of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :param total: The total of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        """
        self.openapi_types = {
            'recv': int,
            'sent': int,
            'total': int
        }

        self.attribute_map = {
            'recv': 'recv',
            'sent': 'sent',
            'total': 'total'
        }

        self._recv = recv
        self._sent = sent
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getDeviceSwitchPortsStatuses_200_response_inner_usageInKb of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recv(self):
        """Gets the recv of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.

        The amount of data received (in kilobytes).

        :return: The recv of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :rtype: int
        """
        return self._recv

    @recv.setter
    def recv(self, recv):
        """Sets the recv of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.

        The amount of data received (in kilobytes).

        :param recv: The recv of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :type recv: int
        """

        self._recv = recv

    @property
    def sent(self):
        """Gets the sent of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.

        The amount of data sent (in kilobytes).

        :return: The sent of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :rtype: int
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.

        The amount of data sent (in kilobytes).

        :param sent: The sent of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :type sent: int
        """

        self._sent = sent

    @property
    def total(self):
        """Gets the total of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.

        The total amount of data sent and received (in kilobytes).

        :return: The total of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.

        The total amount of data sent and received (in kilobytes).

        :param total: The total of this GetDeviceSwitchPortsStatuses200ResponseInnerUsageInKb.
        :type total: int
        """

        self._total = total
