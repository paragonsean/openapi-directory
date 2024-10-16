# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_organization_summary_top_appliances_by_utilization200_response_inner_network import GetOrganizationSummaryTopAppliancesByUtilization200ResponseInnerNetwork
from openapi_server.models.get_organization_summary_top_devices_by_usage200_response_inner_clients import GetOrganizationSummaryTopDevicesByUsage200ResponseInnerClients
from openapi_server.models.get_organization_summary_top_devices_by_usage200_response_inner_usage import GetOrganizationSummaryTopDevicesByUsage200ResponseInnerUsage
from openapi_server import util


class GetOrganizationSummaryTopDevicesByUsage200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, clients: GetOrganizationSummaryTopDevicesByUsage200ResponseInnerClients=None, mac: str=None, model: str=None, name: str=None, network: GetOrganizationSummaryTopAppliancesByUtilization200ResponseInnerNetwork=None, product_type: str=None, serial: str=None, usage: GetOrganizationSummaryTopDevicesByUsage200ResponseInnerUsage=None):
        """GetOrganizationSummaryTopDevicesByUsage200ResponseInner - a model defined in OpenAPI

        :param clients: The clients of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :param mac: The mac of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :param model: The model of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :param name: The name of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :param network: The network of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :param product_type: The product_type of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :param serial: The serial of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :param usage: The usage of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        """
        self.openapi_types = {
            'clients': GetOrganizationSummaryTopDevicesByUsage200ResponseInnerClients,
            'mac': str,
            'model': str,
            'name': str,
            'network': GetOrganizationSummaryTopAppliancesByUtilization200ResponseInnerNetwork,
            'product_type': str,
            'serial': str,
            'usage': GetOrganizationSummaryTopDevicesByUsage200ResponseInnerUsage
        }

        self.attribute_map = {
            'clients': 'clients',
            'mac': 'mac',
            'model': 'model',
            'name': 'name',
            'network': 'network',
            'product_type': 'productType',
            'serial': 'serial',
            'usage': 'usage'
        }

        self._clients = clients
        self._mac = mac
        self._model = model
        self._name = name
        self._network = network
        self._product_type = product_type
        self._serial = serial
        self._usage = usage

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationSummaryTopDevicesByUsage200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationSummaryTopDevicesByUsage_200_response_inner of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def clients(self):
        """Gets the clients of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.


        :return: The clients of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: GetOrganizationSummaryTopDevicesByUsage200ResponseInnerClients
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.


        :param clients: The clients of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type clients: GetOrganizationSummaryTopDevicesByUsage200ResponseInnerClients
        """

        self._clients = clients

    @property
    def mac(self):
        """Gets the mac of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Mac address of the device

        :return: The mac of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Mac address of the device

        :param mac: The mac of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type mac: str
        """

        self._mac = mac

    @property
    def model(self):
        """Gets the model of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Model of the device

        :return: The model of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Model of the device

        :param model: The model of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type model: str
        """

        self._model = model

    @property
    def name(self):
        """Gets the name of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Name of the device

        :return: The name of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Name of the device

        :param name: The name of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type name: str
        """

        self._name = name

    @property
    def network(self):
        """Gets the network of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.


        :return: The network of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: GetOrganizationSummaryTopAppliancesByUtilization200ResponseInnerNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.


        :param network: The network of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type network: GetOrganizationSummaryTopAppliancesByUtilization200ResponseInnerNetwork
        """

        self._network = network

    @property
    def product_type(self):
        """Gets the product_type of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Product type of the device

        :return: The product_type of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Product type of the device

        :param product_type: The product_type of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type product_type: str
        """

        self._product_type = product_type

    @property
    def serial(self):
        """Gets the serial of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Serial number of the device

        :return: The serial of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.

        Serial number of the device

        :param serial: The serial of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type serial: str
        """

        self._serial = serial

    @property
    def usage(self):
        """Gets the usage of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.


        :return: The usage of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :rtype: GetOrganizationSummaryTopDevicesByUsage200ResponseInnerUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.


        :param usage: The usage of this GetOrganizationSummaryTopDevicesByUsage200ResponseInner.
        :type usage: GetOrganizationSummaryTopDevicesByUsage200ResponseInnerUsage
        """

        self._usage = usage
