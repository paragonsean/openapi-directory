# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access: str=None, allowed_ips: List[str]=None, lan_ip: str=None, local_port: str=None, name: str=None, protocol: str=None, public_port: str=None):
        """UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner - a model defined in OpenAPI

        :param access: The access of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :param allowed_ips: The allowed_ips of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :param lan_ip: The lan_ip of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :param local_port: The local_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :param name: The name of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :param protocol: The protocol of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :param public_port: The public_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        """
        self.openapi_types = {
            'access': str,
            'allowed_ips': List[str],
            'lan_ip': str,
            'local_port': str,
            'name': str,
            'protocol': str,
            'public_port': str
        }

        self.attribute_map = {
            'access': 'access',
            'allowed_ips': 'allowedIps',
            'lan_ip': 'lanIp',
            'local_port': 'localPort',
            'name': 'name',
            'protocol': 'protocol',
            'public_port': 'publicPort'
        }

        self._access = access
        self._allowed_ips = allowed_ips
        self._lan_ip = lan_ip
        self._local_port = local_port
        self._name = name
        self._protocol = protocol
        self._public_port = public_port

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateDeviceCellularGatewayPortForwardingRules_request_rules_inner of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access(self):
        """Gets the access of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        `any` or `restricted`. Specify the right to make inbound connections on the specified ports or port ranges. If `restricted`, a list of allowed IPs is mandatory.

        :return: The access of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        `any` or `restricted`. Specify the right to make inbound connections on the specified ports or port ranges. If `restricted`, a list of allowed IPs is mandatory.

        :param access: The access of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :type access: str
        """
        if access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")

        self._access = access

    @property
    def allowed_ips(self):
        """Gets the allowed_ips of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges.

        :return: The allowed_ips of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :rtype: List[str]
        """
        return self._allowed_ips

    @allowed_ips.setter
    def allowed_ips(self, allowed_ips):
        """Sets the allowed_ips of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        An array of ranges of WAN IP addresses that are allowed to make inbound connections on the specified ports or port ranges.

        :param allowed_ips: The allowed_ips of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :type allowed_ips: List[str]
        """

        self._allowed_ips = allowed_ips

    @property
    def lan_ip(self):
        """Gets the lan_ip of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN

        :return: The lan_ip of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._lan_ip

    @lan_ip.setter
    def lan_ip(self, lan_ip):
        """Sets the lan_ip of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        The IP address of the server or device that hosts the internal resource that you wish to make available on the WAN

        :param lan_ip: The lan_ip of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :type lan_ip: str
        """
        if lan_ip is None:
            raise ValueError("Invalid value for `lan_ip`, must not be `None`")

        self._lan_ip = lan_ip

    @property
    def local_port(self):
        """Gets the local_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        A port or port ranges that will receive the forwarded traffic from the WAN

        :return: The local_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._local_port

    @local_port.setter
    def local_port(self, local_port):
        """Sets the local_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        A port or port ranges that will receive the forwarded traffic from the WAN

        :param local_port: The local_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :type local_port: str
        """
        if local_port is None:
            raise ValueError("Invalid value for `local_port`, must not be `None`")

        self._local_port = local_port

    @property
    def name(self):
        """Gets the name of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        A descriptive name for the rule

        :return: The name of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        A descriptive name for the rule

        :param name: The name of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :type name: str
        """

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        TCP or UDP

        :return: The protocol of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        TCP or UDP

        :param protocol: The protocol of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :type protocol: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")

        self._protocol = protocol

    @property
    def public_port(self):
        """Gets the public_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        A port or port ranges that will be forwarded to the host on the LAN

        :return: The public_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :rtype: str
        """
        return self._public_port

    @public_port.setter
    def public_port(self, public_port):
        """Sets the public_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.

        A port or port ranges that will be forwarded to the host on the LAN

        :param public_port: The public_port of this UpdateDeviceCellularGatewayPortForwardingRulesRequestRulesInner.
        :type public_port: str
        """
        if public_port is None:
            raise ValueError("Invalid value for `public_port`, must not be `None`")

        self._public_port = public_port
