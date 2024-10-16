# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response_products_switch import GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitch
from openapi_server import util


class GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, switch: GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitch=None):
        """GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts - a model defined in OpenAPI

        :param switch: The switch of this GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts.
        """
        self.openapi_types = {
            'switch': GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitch
        }

        self.attribute_map = {
            'switch': 'switch'
        }

        self._switch = switch

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkFirmwareUpgradesStagedEvents_200_response_products of this GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def switch(self):
        """Gets the switch of this GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts.


        :return: The switch of this GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts.
        :rtype: GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitch
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts.


        :param switch: The switch of this GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts.
        :type switch: GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitch
        """

        self._switch = switch
