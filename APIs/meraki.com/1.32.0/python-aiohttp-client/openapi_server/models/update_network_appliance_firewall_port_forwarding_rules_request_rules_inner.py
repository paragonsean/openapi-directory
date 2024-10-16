# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allowed_ips: List[str]=None, lan_ip: str=None, local_port: str=None, name: str=None, protocol: str=None, public_port: str=None, uplink: str=None):
        """UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner - a model defined in OpenAPI

        :param allowed_ips: The allowed_ips of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :param lan_ip: The lan_ip of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :param local_port: The local_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :param name: The name of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :param protocol: The protocol of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :param public_port: The public_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :param uplink: The uplink of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        """
        self.openapi_types = {
            'allowed_ips': List[str],
            'lan_ip': str,
            'local_port': str,
            'name': str,
            'protocol': str,
            'public_port': str,
            'uplink': str
        }

        self.attribute_map = {
            'allowed_ips': 'allowedIps',
            'lan_ip': 'lanIp',
            'local_port': 'localPort',
            'name': 'name',
            'protocol': 'protocol',
            'public_port': 'publicPort',
            'uplink': 'uplink'
        }

        self._allowed_ips = allowed_ips
        self._lan_ip = lan_ip
        self._local_port = local_port
        self._name = name
        self._protocol = protocol
        self._public_port = public_port
        self._uplink = uplink

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkApplianceFirewallPortForwardingRules_request_rules_inner of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allowed_ips(self):
        """Gets the allowed_ips of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges (or any)

        :return: The allowed_ips of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :rtype: List[str]
        """
        return self._allowed_ips

    @allowed_ips.setter
    def allowed_ips(self, allowed_ips):
        """Sets the allowed_ips of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges (or any)

        :param allowed_ips: The allowed_ips of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :type allowed_ips: List[str]
        """
        if allowed_ips is None:
            raise ValueError("Invalid value for `allowed_ips`, must not be `None`")

        self._allowed_ips = allowed_ips

    @property
    def lan_ip(self):
        """Gets the lan_ip of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN

        :return: The lan_ip of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._lan_ip

    @lan_ip.setter
    def lan_ip(self, lan_ip):
        """Sets the lan_ip of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN

        :param lan_ip: The lan_ip of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :type lan_ip: str
        """
        if lan_ip is None:
            raise ValueError("Invalid value for `lan_ip`, must not be `None`")

        self._lan_ip = lan_ip

    @property
    def local_port(self):
        """Gets the local_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        A port or port ranges that will receive the forwarded traffic from the WAN

        :return: The local_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._local_port

    @local_port.setter
    def local_port(self, local_port):
        """Sets the local_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        A port or port ranges that will receive the forwarded traffic from the WAN

        :param local_port: The local_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :type local_port: str
        """
        if local_port is None:
            raise ValueError("Invalid value for `local_port`, must not be `None`")

        self._local_port = local_port

    @property
    def name(self):
        """Gets the name of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        A descriptive name for the rule

        :return: The name of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        A descriptive name for the rule

        :param name: The name of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :type name: str
        """

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        TCP or UDP

        :return: The protocol of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        TCP or UDP

        :param protocol: The protocol of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :type protocol: str
        """
        allowed_values = ["tcp", "udp"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def public_port(self):
        """Gets the public_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        A port or port ranges that will be forwarded to the host on the LAN

        :return: The public_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._public_port

    @public_port.setter
    def public_port(self, public_port):
        """Sets the public_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        A port or port ranges that will be forwarded to the host on the LAN

        :param public_port: The public_port of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :type public_port: str
        """
        if public_port is None:
            raise ValueError("Invalid value for `public_port`, must not be `None`")

        self._public_port = public_port

    @property
    def uplink(self):
        """Gets the uplink of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        The physical WAN interface on which the traffic will arrive ('internet1' or, if available, 'internet2' or 'both')

        :return: The uplink of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._uplink

    @uplink.setter
    def uplink(self, uplink):
        """Sets the uplink of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.

        The physical WAN interface on which the traffic will arrive ('internet1' or, if available, 'internet2' or 'both')

        :param uplink: The uplink of this UpdateNetworkApplianceFirewallPortForwardingRulesRequestRulesInner.
        :type uplink: str
        """
        allowed_values = ["both", "internet1", "internet2"]  # noqa: E501
        if uplink not in allowed_values:
            raise ValueError(
                "Invalid value for `uplink` ({0}), must be one of {1}"
                .format(uplink, allowed_values)
            )

        self._uplink = uplink
