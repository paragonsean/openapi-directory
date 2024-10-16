# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkApplianceSingleLan200ResponseMandatoryDhcp(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None):
        """GetNetworkApplianceSingleLan200ResponseMandatoryDhcp - a model defined in OpenAPI

        :param enabled: The enabled of this GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.
        """
        self.openapi_types = {
            'enabled': bool
        }

        self.attribute_map = {
            'enabled': 'enabled'
        }

        self._enabled = enabled

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkApplianceSingleLan200ResponseMandatoryDhcp':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkApplianceSingleLan_200_response_mandatoryDhcp of this GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.

        Enable Mandatory DHCP on single LAN.

        :return: The enabled of this GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.

        Enable Mandatory DHCP on single LAN.

        :param enabled: The enabled of this GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.
        :type enabled: bool
        """

        self._enabled = enabled
