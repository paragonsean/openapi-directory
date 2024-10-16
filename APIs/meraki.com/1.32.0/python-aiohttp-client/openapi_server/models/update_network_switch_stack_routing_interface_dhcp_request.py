# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_device_switch_routing_interface_dhcp_request_dhcp_options_inner import UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner
from openapi_server.models.update_device_switch_routing_interface_dhcp_request_fixed_ip_assignments_inner import UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner
from openapi_server.models.update_device_switch_routing_interface_dhcp_request_reserved_ip_ranges_inner import UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner
from openapi_server import util


class UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, boot_file_name: str=None, boot_next_server: str=None, boot_options_enabled: bool=None, dhcp_lease_time: str=None, dhcp_mode: str=None, dhcp_options: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner]=None, dhcp_relay_server_ips: List[str]=None, dns_custom_nameservers: List[str]=None, dns_nameservers_option: str=None, fixed_ip_assignments: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner]=None, reserved_ip_ranges: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner]=None):
        """UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest - a model defined in OpenAPI

        :param boot_file_name: The boot_file_name of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param boot_next_server: The boot_next_server of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param boot_options_enabled: The boot_options_enabled of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param dhcp_lease_time: The dhcp_lease_time of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param dhcp_mode: The dhcp_mode of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param dhcp_options: The dhcp_options of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param dhcp_relay_server_ips: The dhcp_relay_server_ips of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param dns_custom_nameservers: The dns_custom_nameservers of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param dns_nameservers_option: The dns_nameservers_option of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param fixed_ip_assignments: The fixed_ip_assignments of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :param reserved_ip_ranges: The reserved_ip_ranges of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        """
        self.openapi_types = {
            'boot_file_name': str,
            'boot_next_server': str,
            'boot_options_enabled': bool,
            'dhcp_lease_time': str,
            'dhcp_mode': str,
            'dhcp_options': List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner],
            'dhcp_relay_server_ips': List[str],
            'dns_custom_nameservers': List[str],
            'dns_nameservers_option': str,
            'fixed_ip_assignments': List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner],
            'reserved_ip_ranges': List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner]
        }

        self.attribute_map = {
            'boot_file_name': 'bootFileName',
            'boot_next_server': 'bootNextServer',
            'boot_options_enabled': 'bootOptionsEnabled',
            'dhcp_lease_time': 'dhcpLeaseTime',
            'dhcp_mode': 'dhcpMode',
            'dhcp_options': 'dhcpOptions',
            'dhcp_relay_server_ips': 'dhcpRelayServerIps',
            'dns_custom_nameservers': 'dnsCustomNameservers',
            'dns_nameservers_option': 'dnsNameserversOption',
            'fixed_ip_assignments': 'fixedIpAssignments',
            'reserved_ip_ranges': 'reservedIpRanges'
        }

        self._boot_file_name = boot_file_name
        self._boot_next_server = boot_next_server
        self._boot_options_enabled = boot_options_enabled
        self._dhcp_lease_time = dhcp_lease_time
        self._dhcp_mode = dhcp_mode
        self._dhcp_options = dhcp_options
        self._dhcp_relay_server_ips = dhcp_relay_server_ips
        self._dns_custom_nameservers = dns_custom_nameservers
        self._dns_nameservers_option = dns_nameservers_option
        self._fixed_ip_assignments = fixed_ip_assignments
        self._reserved_ip_ranges = reserved_ip_ranges

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkSwitchStackRoutingInterfaceDhcp_request of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def boot_file_name(self):
        """Gets the boot_file_name of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The PXE boot server file name for the DHCP server running on the switch stack interface

        :return: The boot_file_name of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: str
        """
        return self._boot_file_name

    @boot_file_name.setter
    def boot_file_name(self, boot_file_name):
        """Sets the boot_file_name of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The PXE boot server file name for the DHCP server running on the switch stack interface

        :param boot_file_name: The boot_file_name of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type boot_file_name: str
        """

        self._boot_file_name = boot_file_name

    @property
    def boot_next_server(self):
        """Gets the boot_next_server of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The PXE boot server IP for the DHCP server running on the switch stack interface

        :return: The boot_next_server of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: str
        """
        return self._boot_next_server

    @boot_next_server.setter
    def boot_next_server(self, boot_next_server):
        """Sets the boot_next_server of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The PXE boot server IP for the DHCP server running on the switch stack interface

        :param boot_next_server: The boot_next_server of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type boot_next_server: str
        """

        self._boot_next_server = boot_next_server

    @property
    def boot_options_enabled(self):
        """Gets the boot_options_enabled of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface

        :return: The boot_options_enabled of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: bool
        """
        return self._boot_options_enabled

    @boot_options_enabled.setter
    def boot_options_enabled(self, boot_options_enabled):
        """Sets the boot_options_enabled of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface

        :param boot_options_enabled: The boot_options_enabled of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type boot_options_enabled: bool
        """

        self._boot_options_enabled = boot_options_enabled

    @property
    def dhcp_lease_time(self):
        """Gets the dhcp_lease_time of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP lease time config for the dhcp server running on switch stack interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')

        :return: The dhcp_lease_time of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: str
        """
        return self._dhcp_lease_time

    @dhcp_lease_time.setter
    def dhcp_lease_time(self, dhcp_lease_time):
        """Sets the dhcp_lease_time of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP lease time config for the dhcp server running on switch stack interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')

        :param dhcp_lease_time: The dhcp_lease_time of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type dhcp_lease_time: str
        """
        allowed_values = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]  # noqa: E501
        if dhcp_lease_time not in allowed_values:
            raise ValueError(
                "Invalid value for `dhcp_lease_time` ({0}), must be one of {1}"
                .format(dhcp_lease_time, allowed_values)
            )

        self._dhcp_lease_time = dhcp_lease_time

    @property
    def dhcp_mode(self):
        """Gets the dhcp_mode of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP mode options for the switch stack interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')

        :return: The dhcp_mode of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: str
        """
        return self._dhcp_mode

    @dhcp_mode.setter
    def dhcp_mode(self, dhcp_mode):
        """Sets the dhcp_mode of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP mode options for the switch stack interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')

        :param dhcp_mode: The dhcp_mode of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type dhcp_mode: str
        """
        allowed_values = ["dhcpDisabled", "dhcpRelay", "dhcpServer"]  # noqa: E501
        if dhcp_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `dhcp_mode` ({0}), must be one of {1}"
                .format(dhcp_mode, allowed_values)
            )

        self._dhcp_mode = dhcp_mode

    @property
    def dhcp_options(self):
        """Gets the dhcp_options of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface

        :return: The dhcp_options of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner]
        """
        return self._dhcp_options

    @dhcp_options.setter
    def dhcp_options(self, dhcp_options):
        """Sets the dhcp_options of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface

        :param dhcp_options: The dhcp_options of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type dhcp_options: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner]
        """

        self._dhcp_options = dhcp_options

    @property
    def dhcp_relay_server_ips(self):
        """Gets the dhcp_relay_server_ips of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface

        :return: The dhcp_relay_server_ips of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: List[str]
        """
        return self._dhcp_relay_server_ips

    @dhcp_relay_server_ips.setter
    def dhcp_relay_server_ips(self, dhcp_relay_server_ips):
        """Sets the dhcp_relay_server_ips of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface

        :param dhcp_relay_server_ips: The dhcp_relay_server_ips of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type dhcp_relay_server_ips: List[str]
        """

        self._dhcp_relay_server_ips = dhcp_relay_server_ips

    @property
    def dns_custom_nameservers(self):
        """Gets the dns_custom_nameservers of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP name server IPs when DHCP name server option is 'custom'

        :return: The dns_custom_nameservers of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: List[str]
        """
        return self._dns_custom_nameservers

    @dns_custom_nameservers.setter
    def dns_custom_nameservers(self, dns_custom_nameservers):
        """Sets the dns_custom_nameservers of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP name server IPs when DHCP name server option is 'custom'

        :param dns_custom_nameservers: The dns_custom_nameservers of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type dns_custom_nameservers: List[str]
        """

        self._dns_custom_nameservers = dns_custom_nameservers

    @property
    def dns_nameservers_option(self):
        """Gets the dns_nameservers_option of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP name server option for the dhcp server running on the switch stack interface ('googlePublicDns', 'openDns' or 'custom')

        :return: The dns_nameservers_option of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: str
        """
        return self._dns_nameservers_option

    @dns_nameservers_option.setter
    def dns_nameservers_option(self, dns_nameservers_option):
        """Sets the dns_nameservers_option of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        The DHCP name server option for the dhcp server running on the switch stack interface ('googlePublicDns', 'openDns' or 'custom')

        :param dns_nameservers_option: The dns_nameservers_option of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type dns_nameservers_option: str
        """
        allowed_values = ["custom", "googlePublicDns", "openDns"]  # noqa: E501
        if dns_nameservers_option not in allowed_values:
            raise ValueError(
                "Invalid value for `dns_nameservers_option` ({0}), must be one of {1}"
                .format(dns_nameservers_option, allowed_values)
            )

        self._dns_nameservers_option = dns_nameservers_option

    @property
    def fixed_ip_assignments(self):
        """Gets the fixed_ip_assignments of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface

        :return: The fixed_ip_assignments of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner]
        """
        return self._fixed_ip_assignments

    @fixed_ip_assignments.setter
    def fixed_ip_assignments(self, fixed_ip_assignments):
        """Sets the fixed_ip_assignments of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface

        :param fixed_ip_assignments: The fixed_ip_assignments of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type fixed_ip_assignments: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestFixedIpAssignmentsInner]
        """

        self._fixed_ip_assignments = fixed_ip_assignments

    @property
    def reserved_ip_ranges(self):
        """Gets the reserved_ip_ranges of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface

        :return: The reserved_ip_ranges of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :rtype: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner]
        """
        return self._reserved_ip_ranges

    @reserved_ip_ranges.setter
    def reserved_ip_ranges(self, reserved_ip_ranges):
        """Sets the reserved_ip_ranges of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.

        Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface

        :param reserved_ip_ranges: The reserved_ip_ranges of this UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.
        :type reserved_ip_ranges: List[UpdateDeviceSwitchRoutingInterfaceDhcpRequestReservedIpRangesInner]
        """

        self._reserved_ip_ranges = reserved_ip_ranges
