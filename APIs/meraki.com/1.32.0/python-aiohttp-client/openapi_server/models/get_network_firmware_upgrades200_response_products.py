# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_firmware_upgrades200_response_products_appliance import GetNetworkFirmwareUpgrades200ResponseProductsAppliance
from openapi_server import util


class GetNetworkFirmwareUpgrades200ResponseProducts(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, appliance: GetNetworkFirmwareUpgrades200ResponseProductsAppliance=None, camera: GetNetworkFirmwareUpgrades200ResponseProductsAppliance=None, cellular_gateway: GetNetworkFirmwareUpgrades200ResponseProductsAppliance=None, sensor: GetNetworkFirmwareUpgrades200ResponseProductsAppliance=None, switch: GetNetworkFirmwareUpgrades200ResponseProductsAppliance=None, wireless: GetNetworkFirmwareUpgrades200ResponseProductsAppliance=None):
        """GetNetworkFirmwareUpgrades200ResponseProducts - a model defined in OpenAPI

        :param appliance: The appliance of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :param camera: The camera of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :param cellular_gateway: The cellular_gateway of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :param sensor: The sensor of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :param switch: The switch of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :param wireless: The wireless of this GetNetworkFirmwareUpgrades200ResponseProducts.
        """
        self.openapi_types = {
            'appliance': GetNetworkFirmwareUpgrades200ResponseProductsAppliance,
            'camera': GetNetworkFirmwareUpgrades200ResponseProductsAppliance,
            'cellular_gateway': GetNetworkFirmwareUpgrades200ResponseProductsAppliance,
            'sensor': GetNetworkFirmwareUpgrades200ResponseProductsAppliance,
            'switch': GetNetworkFirmwareUpgrades200ResponseProductsAppliance,
            'wireless': GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        }

        self.attribute_map = {
            'appliance': 'appliance',
            'camera': 'camera',
            'cellular_gateway': 'cellularGateway',
            'sensor': 'sensor',
            'switch': 'switch',
            'wireless': 'wireless'
        }

        self._appliance = appliance
        self._camera = camera
        self._cellular_gateway = cellular_gateway
        self._sensor = sensor
        self._switch = switch
        self._wireless = wireless

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkFirmwareUpgrades200ResponseProducts':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkFirmwareUpgrades_200_response_products of this GetNetworkFirmwareUpgrades200ResponseProducts.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def appliance(self):
        """Gets the appliance of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :return: The appliance of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :rtype: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :param appliance: The appliance of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :type appliance: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """

        self._appliance = appliance

    @property
    def camera(self):
        """Gets the camera of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :return: The camera of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :rtype: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """
        return self._camera

    @camera.setter
    def camera(self, camera):
        """Sets the camera of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :param camera: The camera of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :type camera: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """

        self._camera = camera

    @property
    def cellular_gateway(self):
        """Gets the cellular_gateway of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :return: The cellular_gateway of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :rtype: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """
        return self._cellular_gateway

    @cellular_gateway.setter
    def cellular_gateway(self, cellular_gateway):
        """Sets the cellular_gateway of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :param cellular_gateway: The cellular_gateway of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :type cellular_gateway: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """

        self._cellular_gateway = cellular_gateway

    @property
    def sensor(self):
        """Gets the sensor of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :return: The sensor of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :rtype: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """
        return self._sensor

    @sensor.setter
    def sensor(self, sensor):
        """Sets the sensor of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :param sensor: The sensor of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :type sensor: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """

        self._sensor = sensor

    @property
    def switch(self):
        """Gets the switch of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :return: The switch of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :rtype: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :param switch: The switch of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :type switch: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """

        self._switch = switch

    @property
    def wireless(self):
        """Gets the wireless of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :return: The wireless of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :rtype: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """
        return self._wireless

    @wireless.setter
    def wireless(self, wireless):
        """Sets the wireless of this GetNetworkFirmwareUpgrades200ResponseProducts.


        :param wireless: The wireless of this GetNetworkFirmwareUpgrades200ResponseProducts.
        :type wireless: GetNetworkFirmwareUpgrades200ResponseProductsAppliance
        """

        self._wireless = wireless
