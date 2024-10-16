# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateNetworkWirelessRfProfileRequestTransmission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None):
        """CreateNetworkWirelessRfProfileRequestTransmission - a model defined in OpenAPI

        :param enabled: The enabled of this CreateNetworkWirelessRfProfileRequestTransmission.
        """
        self.openapi_types = {
            'enabled': bool
        }

        self.attribute_map = {
            'enabled': 'enabled'
        }

        self._enabled = enabled

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkWirelessRfProfileRequestTransmission':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkWirelessRfProfile_request_transmission of this CreateNetworkWirelessRfProfileRequestTransmission.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this CreateNetworkWirelessRfProfileRequestTransmission.

        Toggle for radio transmission. When false, radios will not transmit at all.

        :return: The enabled of this CreateNetworkWirelessRfProfileRequestTransmission.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateNetworkWirelessRfProfileRequestTransmission.

        Toggle for radio transmission. When false, radios will not transmit at all.

        :param enabled: The enabled of this CreateNetworkWirelessRfProfileRequestTransmission.
        :type enabled: bool
        """

        self._enabled = enabled
