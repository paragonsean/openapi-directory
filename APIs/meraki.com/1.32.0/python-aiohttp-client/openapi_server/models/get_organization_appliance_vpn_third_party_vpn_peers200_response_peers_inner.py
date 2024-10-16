# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_organization_appliance_vpn_third_party_vpn_peers200_response_peers_inner_ipsec_policies import GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies
from openapi_server import util


class GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ike_version: str='1', ipsec_policies: GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies=None, ipsec_policies_preset: str=None, local_id: str=None, name: str=None, network_tags: List[str]=None, private_subnets: List[str]=None, public_ip: str=None, remote_id: str=None, secret: str=None):
        """GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner - a model defined in OpenAPI

        :param ike_version: The ike_version of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param ipsec_policies: The ipsec_policies of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param ipsec_policies_preset: The ipsec_policies_preset of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param local_id: The local_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param name: The name of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param network_tags: The network_tags of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param private_subnets: The private_subnets of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param public_ip: The public_ip of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param remote_id: The remote_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :param secret: The secret of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        """
        self.openapi_types = {
            'ike_version': str,
            'ipsec_policies': GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies,
            'ipsec_policies_preset': str,
            'local_id': str,
            'name': str,
            'network_tags': List[str],
            'private_subnets': List[str],
            'public_ip': str,
            'remote_id': str,
            'secret': str
        }

        self.attribute_map = {
            'ike_version': 'ikeVersion',
            'ipsec_policies': 'ipsecPolicies',
            'ipsec_policies_preset': 'ipsecPoliciesPreset',
            'local_id': 'localId',
            'name': 'name',
            'network_tags': 'networkTags',
            'private_subnets': 'privateSubnets',
            'public_ip': 'publicIp',
            'remote_id': 'remoteId',
            'secret': 'secret'
        }

        self._ike_version = ike_version
        self._ipsec_policies = ipsec_policies
        self._ipsec_policies_preset = ipsec_policies_preset
        self._local_id = local_id
        self._name = name
        self._network_tags = network_tags
        self._private_subnets = private_subnets
        self._public_ip = public_ip
        self._remote_id = remote_id
        self._secret = secret

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationApplianceVpnThirdPartyVPNPeers_200_response_peers_inner of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ike_version(self):
        """Gets the ike_version of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The IKE version to be used for the IPsec VPN peer configuration. Defaults to '1' when omitted.

        :return: The ike_version of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: str
        """
        return self._ike_version

    @ike_version.setter
    def ike_version(self, ike_version):
        """Sets the ike_version of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The IKE version to be used for the IPsec VPN peer configuration. Defaults to '1' when omitted.

        :param ike_version: The ike_version of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type ike_version: str
        """
        allowed_values = ["1", "2"]  # noqa: E501
        if ike_version not in allowed_values:
            raise ValueError(
                "Invalid value for `ike_version` ({0}), must be one of {1}"
                .format(ike_version, allowed_values)
            )

        self._ike_version = ike_version

    @property
    def ipsec_policies(self):
        """Gets the ipsec_policies of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.


        :return: The ipsec_policies of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies
        """
        return self._ipsec_policies

    @ipsec_policies.setter
    def ipsec_policies(self, ipsec_policies):
        """Sets the ipsec_policies of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.


        :param ipsec_policies: The ipsec_policies of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type ipsec_policies: GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies
        """

        self._ipsec_policies = ipsec_policies

    @property
    def ipsec_policies_preset(self):
        """Gets the ipsec_policies_preset of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        One of the following available presets: 'default', 'aws', 'azure'. If this is provided, the 'ipsecPolicies' parameter is ignored.

        :return: The ipsec_policies_preset of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: str
        """
        return self._ipsec_policies_preset

    @ipsec_policies_preset.setter
    def ipsec_policies_preset(self, ipsec_policies_preset):
        """Sets the ipsec_policies_preset of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        One of the following available presets: 'default', 'aws', 'azure'. If this is provided, the 'ipsecPolicies' parameter is ignored.

        :param ipsec_policies_preset: The ipsec_policies_preset of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type ipsec_policies_preset: str
        """

        self._ipsec_policies_preset = ipsec_policies_preset

    @property
    def local_id(self):
        """Gets the local_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The local ID is used to identify the MX to the peer. This will apply to all MXs this peer applies to.

        :return: The local_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The local ID is used to identify the MX to the peer. This will apply to all MXs this peer applies to.

        :param local_id: The local_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        The name of the VPN peer

        :return: The name of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        The name of the VPN peer

        :param name: The name of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type name: str
        """

        self._name = name

    @property
    def network_tags(self):
        """Gets the network_tags of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        A list of network tags that will connect with this peer. Use ['all'] for all networks. Use ['none'] for no networks. If not included, the default is ['all'].

        :return: The network_tags of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: List[str]
        """
        return self._network_tags

    @network_tags.setter
    def network_tags(self, network_tags):
        """Sets the network_tags of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        A list of network tags that will connect with this peer. Use ['all'] for all networks. Use ['none'] for no networks. If not included, the default is ['all'].

        :param network_tags: The network_tags of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type network_tags: List[str]
        """

        self._network_tags = network_tags

    @property
    def private_subnets(self):
        """Gets the private_subnets of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        The list of the private subnets of the VPN peer

        :return: The private_subnets of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: List[str]
        """
        return self._private_subnets

    @private_subnets.setter
    def private_subnets(self, private_subnets):
        """Sets the private_subnets of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        The list of the private subnets of the VPN peer

        :param private_subnets: The private_subnets of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type private_subnets: List[str]
        """

        self._private_subnets = private_subnets

    @property
    def public_ip(self):
        """Gets the public_ip of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The public IP of the VPN peer

        :return: The public_ip of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The public IP of the VPN peer

        :param public_ip: The public_ip of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type public_ip: str
        """

        self._public_ip = public_ip

    @property
    def remote_id(self):
        """Gets the remote_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The remote ID is used to identify the connecting VPN peer. This can either be a valid IPv4 Address, FQDN or User FQDN.

        :return: The remote_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        [optional] The remote ID is used to identify the connecting VPN peer. This can either be a valid IPv4 Address, FQDN or User FQDN.

        :param remote_id: The remote_id of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type remote_id: str
        """

        self._remote_id = remote_id

    @property
    def secret(self):
        """Gets the secret of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        The shared secret with the VPN peer

        :return: The secret of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.

        The shared secret with the VPN peer

        :param secret: The secret of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInner.
        :type secret: str
        """

        self._secret = secret
