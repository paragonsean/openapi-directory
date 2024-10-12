# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, child_auth_algo: List[str]=None, child_cipher_algo: List[str]=None, child_lifetime: int=None, child_pfs_group: List[str]=None, ike_auth_algo: List[str]=None, ike_cipher_algo: List[str]=None, ike_diffie_hellman_group: List[str]=None, ike_lifetime: int=None, ike_prf_algo: List[str]=None):
        """GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies - a model defined in OpenAPI

        :param child_auth_algo: The child_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param child_cipher_algo: The child_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param child_lifetime: The child_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param child_pfs_group: The child_pfs_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param ike_auth_algo: The ike_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param ike_cipher_algo: The ike_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param ike_diffie_hellman_group: The ike_diffie_hellman_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param ike_lifetime: The ike_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :param ike_prf_algo: The ike_prf_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        """
        self.openapi_types = {
            'child_auth_algo': List[str],
            'child_cipher_algo': List[str],
            'child_lifetime': int,
            'child_pfs_group': List[str],
            'ike_auth_algo': List[str],
            'ike_cipher_algo': List[str],
            'ike_diffie_hellman_group': List[str],
            'ike_lifetime': int,
            'ike_prf_algo': List[str]
        }

        self.attribute_map = {
            'child_auth_algo': 'childAuthAlgo',
            'child_cipher_algo': 'childCipherAlgo',
            'child_lifetime': 'childLifetime',
            'child_pfs_group': 'childPfsGroup',
            'ike_auth_algo': 'ikeAuthAlgo',
            'ike_cipher_algo': 'ikeCipherAlgo',
            'ike_diffie_hellman_group': 'ikeDiffieHellmanGroup',
            'ike_lifetime': 'ikeLifetime',
            'ike_prf_algo': 'ikePrfAlgo'
        }

        self._child_auth_algo = child_auth_algo
        self._child_cipher_algo = child_cipher_algo
        self._child_lifetime = child_lifetime
        self._child_pfs_group = child_pfs_group
        self._ike_auth_algo = ike_auth_algo
        self._ike_cipher_algo = ike_cipher_algo
        self._ike_diffie_hellman_group = ike_diffie_hellman_group
        self._ike_lifetime = ike_lifetime
        self._ike_prf_algo = ike_prf_algo

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationApplianceVpnThirdPartyVPNPeers_200_response_peers_inner_ipsecPolicies of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def child_auth_algo(self):
        """Gets the child_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the authentication algorithms to be used in Phase 2. The value should be an array with one of the following algorithms: 'sha256', 'sha1', 'md5'

        :return: The child_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: List[str]
        """
        return self._child_auth_algo

    @child_auth_algo.setter
    def child_auth_algo(self, child_auth_algo):
        """Sets the child_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the authentication algorithms to be used in Phase 2. The value should be an array with one of the following algorithms: 'sha256', 'sha1', 'md5'

        :param child_auth_algo: The child_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type child_auth_algo: List[str]
        """
        allowed_values = ["md5", "sha1", "sha256"]  # noqa: E501
        if not set(child_auth_algo).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `child_auth_algo` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(child_auth_algo) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._child_auth_algo = child_auth_algo

    @property
    def child_cipher_algo(self):
        """Gets the child_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the cipher algorithms to be used in Phase 2. The value should be an array with one or more of the following algorithms: 'aes256', 'aes192', 'aes128', 'tripledes', 'des', 'null'

        :return: The child_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: List[str]
        """
        return self._child_cipher_algo

    @child_cipher_algo.setter
    def child_cipher_algo(self, child_cipher_algo):
        """Sets the child_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the cipher algorithms to be used in Phase 2. The value should be an array with one or more of the following algorithms: 'aes256', 'aes192', 'aes128', 'tripledes', 'des', 'null'

        :param child_cipher_algo: The child_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type child_cipher_algo: List[str]
        """
        allowed_values = ["aes128", "aes192", "aes256", "des", "null", "tripledes"]  # noqa: E501
        if not set(child_cipher_algo).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `child_cipher_algo` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(child_cipher_algo) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._child_cipher_algo = child_cipher_algo

    @property
    def child_lifetime(self):
        """Gets the child_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        The lifetime of the Phase 2 SA in seconds.

        :return: The child_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: int
        """
        return self._child_lifetime

    @child_lifetime.setter
    def child_lifetime(self, child_lifetime):
        """Sets the child_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        The lifetime of the Phase 2 SA in seconds.

        :param child_lifetime: The child_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type child_lifetime: int
        """

        self._child_lifetime = child_lifetime

    @property
    def child_pfs_group(self):
        """Gets the child_pfs_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the Diffie-Hellman group to be used for Perfect Forward Secrecy in Phase 2. The value should be an array with one of the following values: 'disabled','group14', 'group5', 'group2', 'group1'

        :return: The child_pfs_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: List[str]
        """
        return self._child_pfs_group

    @child_pfs_group.setter
    def child_pfs_group(self, child_pfs_group):
        """Sets the child_pfs_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the Diffie-Hellman group to be used for Perfect Forward Secrecy in Phase 2. The value should be an array with one of the following values: 'disabled','group14', 'group5', 'group2', 'group1'

        :param child_pfs_group: The child_pfs_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type child_pfs_group: List[str]
        """

        self._child_pfs_group = child_pfs_group

    @property
    def ike_auth_algo(self):
        """Gets the ike_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the authentication algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: 'sha256', 'sha1', 'md5'

        :return: The ike_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: List[str]
        """
        return self._ike_auth_algo

    @ike_auth_algo.setter
    def ike_auth_algo(self, ike_auth_algo):
        """Sets the ike_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the authentication algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: 'sha256', 'sha1', 'md5'

        :param ike_auth_algo: The ike_auth_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type ike_auth_algo: List[str]
        """
        allowed_values = ["md5", "sha1", "sha256"]  # noqa: E501
        if not set(ike_auth_algo).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `ike_auth_algo` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(ike_auth_algo) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._ike_auth_algo = ike_auth_algo

    @property
    def ike_cipher_algo(self):
        """Gets the ike_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the cipher algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: 'aes256', 'aes192', 'aes128', 'tripledes', 'des'

        :return: The ike_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: List[str]
        """
        return self._ike_cipher_algo

    @ike_cipher_algo.setter
    def ike_cipher_algo(self, ike_cipher_algo):
        """Sets the ike_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the cipher algorithm to be used in Phase 1. The value should be an array with one of the following algorithms: 'aes256', 'aes192', 'aes128', 'tripledes', 'des'

        :param ike_cipher_algo: The ike_cipher_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type ike_cipher_algo: List[str]
        """
        allowed_values = ["aes128", "aes192", "aes256", "des", "tripledes"]  # noqa: E501
        if not set(ike_cipher_algo).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `ike_cipher_algo` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(ike_cipher_algo) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._ike_cipher_algo = ike_cipher_algo

    @property
    def ike_diffie_hellman_group(self):
        """Gets the ike_diffie_hellman_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the Diffie-Hellman group to be used in Phase 1. The value should be an array with one of the following algorithms: 'group14', 'group5', 'group2', 'group1'

        :return: The ike_diffie_hellman_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: List[str]
        """
        return self._ike_diffie_hellman_group

    @ike_diffie_hellman_group.setter
    def ike_diffie_hellman_group(self, ike_diffie_hellman_group):
        """Sets the ike_diffie_hellman_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        This is the Diffie-Hellman group to be used in Phase 1. The value should be an array with one of the following algorithms: 'group14', 'group5', 'group2', 'group1'

        :param ike_diffie_hellman_group: The ike_diffie_hellman_group of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type ike_diffie_hellman_group: List[str]
        """

        self._ike_diffie_hellman_group = ike_diffie_hellman_group

    @property
    def ike_lifetime(self):
        """Gets the ike_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        The lifetime of the Phase 1 SA in seconds.

        :return: The ike_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: int
        """
        return self._ike_lifetime

    @ike_lifetime.setter
    def ike_lifetime(self, ike_lifetime):
        """Sets the ike_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        The lifetime of the Phase 1 SA in seconds.

        :param ike_lifetime: The ike_lifetime of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type ike_lifetime: int
        """

        self._ike_lifetime = ike_lifetime

    @property
    def ike_prf_algo(self):
        """Gets the ike_prf_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        [optional] This is the pseudo-random function to be used in IKE_SA. The value should be an array with one of the following algorithms: 'prfsha256', 'prfsha1', 'prfmd5', 'default'. The 'default' option can be used to default to the Authentication algorithm.

        :return: The ike_prf_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :rtype: List[str]
        """
        return self._ike_prf_algo

    @ike_prf_algo.setter
    def ike_prf_algo(self, ike_prf_algo):
        """Sets the ike_prf_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.

        [optional] This is the pseudo-random function to be used in IKE_SA. The value should be an array with one of the following algorithms: 'prfsha256', 'prfsha1', 'prfmd5', 'default'. The 'default' option can be used to default to the Authentication algorithm.

        :param ike_prf_algo: The ike_prf_algo of this GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.
        :type ike_prf_algo: List[str]
        """
        allowed_values = ["default", "prfmd5", "prfsha1", "prfsha256"]  # noqa: E501
        if not set(ike_prf_algo).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `ike_prf_algo` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(ike_prf_algo) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._ike_prf_algo = ike_prf_algo
