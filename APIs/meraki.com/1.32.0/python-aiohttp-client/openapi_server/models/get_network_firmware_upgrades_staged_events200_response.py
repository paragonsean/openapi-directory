# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_firmware_upgrades_rollback200_response_reasons_inner import CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response_products import GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response_stages_inner import GetNetworkFirmwareUpgradesStagedEvents200ResponseStagesInner
from openapi_server import util


class GetNetworkFirmwareUpgradesStagedEvents200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, products: GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts=None, reasons: List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner]=None, stages: List[GetNetworkFirmwareUpgradesStagedEvents200ResponseStagesInner]=None):
        """GetNetworkFirmwareUpgradesStagedEvents200Response - a model defined in OpenAPI

        :param products: The products of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :param reasons: The reasons of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :param stages: The stages of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        """
        self.openapi_types = {
            'products': GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts,
            'reasons': List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner],
            'stages': List[GetNetworkFirmwareUpgradesStagedEvents200ResponseStagesInner]
        }

        self.attribute_map = {
            'products': 'products',
            'reasons': 'reasons',
            'stages': 'stages'
        }

        self._products = products
        self._reasons = reasons
        self._stages = stages

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkFirmwareUpgradesStagedEvents200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkFirmwareUpgradesStagedEvents_200_response of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def products(self):
        """Gets the products of this GetNetworkFirmwareUpgradesStagedEvents200Response.


        :return: The products of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :rtype: GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this GetNetworkFirmwareUpgradesStagedEvents200Response.


        :param products: The products of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :type products: GetNetworkFirmwareUpgradesStagedEvents200ResponseProducts
        """

        self._products = products

    @property
    def reasons(self):
        """Gets the reasons of this GetNetworkFirmwareUpgradesStagedEvents200Response.

        Reasons for the rollback

        :return: The reasons of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :rtype: List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this GetNetworkFirmwareUpgradesStagedEvents200Response.

        Reasons for the rollback

        :param reasons: The reasons of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :type reasons: List[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner]
        """

        self._reasons = reasons

    @property
    def stages(self):
        """Gets the stages of this GetNetworkFirmwareUpgradesStagedEvents200Response.

        The ordered stages in the network

        :return: The stages of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :rtype: List[GetNetworkFirmwareUpgradesStagedEvents200ResponseStagesInner]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this GetNetworkFirmwareUpgradesStagedEvents200Response.

        The ordered stages in the network

        :param stages: The stages of this GetNetworkFirmwareUpgradesStagedEvents200Response.
        :type stages: List[GetNetworkFirmwareUpgradesStagedEvents200ResponseStagesInner]
        """

        self._stages = stages
