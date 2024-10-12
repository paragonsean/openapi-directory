# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_encryption_config import UpdateEncryptionConfig
from openapi_server.models.update_firewall_rule_with_account_parameters import UpdateFirewallRuleWithAccountParameters
from openapi_server.models.update_trusted_id_provider_with_account_parameters import UpdateTrustedIdProviderWithAccountParameters
from openapi_server.models.update_virtual_network_rule_with_account_parameters import UpdateVirtualNetworkRuleWithAccountParameters
from openapi_server import util


class UpdateDataLakeStoreAccountProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, default_group: str=None, encryption_config: UpdateEncryptionConfig=None, firewall_allow_azure_ips: str=None, firewall_rules: List[UpdateFirewallRuleWithAccountParameters]=None, firewall_state: str=None, new_tier: str=None, trusted_id_provider_state: str=None, trusted_id_providers: List[UpdateTrustedIdProviderWithAccountParameters]=None, virtual_network_rules: List[UpdateVirtualNetworkRuleWithAccountParameters]=None):
        """UpdateDataLakeStoreAccountProperties - a model defined in OpenAPI

        :param default_group: The default_group of this UpdateDataLakeStoreAccountProperties.
        :param encryption_config: The encryption_config of this UpdateDataLakeStoreAccountProperties.
        :param firewall_allow_azure_ips: The firewall_allow_azure_ips of this UpdateDataLakeStoreAccountProperties.
        :param firewall_rules: The firewall_rules of this UpdateDataLakeStoreAccountProperties.
        :param firewall_state: The firewall_state of this UpdateDataLakeStoreAccountProperties.
        :param new_tier: The new_tier of this UpdateDataLakeStoreAccountProperties.
        :param trusted_id_provider_state: The trusted_id_provider_state of this UpdateDataLakeStoreAccountProperties.
        :param trusted_id_providers: The trusted_id_providers of this UpdateDataLakeStoreAccountProperties.
        :param virtual_network_rules: The virtual_network_rules of this UpdateDataLakeStoreAccountProperties.
        """
        self.openapi_types = {
            'default_group': str,
            'encryption_config': UpdateEncryptionConfig,
            'firewall_allow_azure_ips': str,
            'firewall_rules': List[UpdateFirewallRuleWithAccountParameters],
            'firewall_state': str,
            'new_tier': str,
            'trusted_id_provider_state': str,
            'trusted_id_providers': List[UpdateTrustedIdProviderWithAccountParameters],
            'virtual_network_rules': List[UpdateVirtualNetworkRuleWithAccountParameters]
        }

        self.attribute_map = {
            'default_group': 'defaultGroup',
            'encryption_config': 'encryptionConfig',
            'firewall_allow_azure_ips': 'firewallAllowAzureIps',
            'firewall_rules': 'firewallRules',
            'firewall_state': 'firewallState',
            'new_tier': 'newTier',
            'trusted_id_provider_state': 'trustedIdProviderState',
            'trusted_id_providers': 'trustedIdProviders',
            'virtual_network_rules': 'virtualNetworkRules'
        }

        self._default_group = default_group
        self._encryption_config = encryption_config
        self._firewall_allow_azure_ips = firewall_allow_azure_ips
        self._firewall_rules = firewall_rules
        self._firewall_state = firewall_state
        self._new_tier = new_tier
        self._trusted_id_provider_state = trusted_id_provider_state
        self._trusted_id_providers = trusted_id_providers
        self._virtual_network_rules = virtual_network_rules

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateDataLakeStoreAccountProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateDataLakeStoreAccountProperties of this UpdateDataLakeStoreAccountProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def default_group(self):
        """Gets the default_group of this UpdateDataLakeStoreAccountProperties.

        The default owner group for all new folders and files created in the Data Lake Store account.

        :return: The default_group of this UpdateDataLakeStoreAccountProperties.
        :rtype: str
        """
        return self._default_group

    @default_group.setter
    def default_group(self, default_group):
        """Sets the default_group of this UpdateDataLakeStoreAccountProperties.

        The default owner group for all new folders and files created in the Data Lake Store account.

        :param default_group: The default_group of this UpdateDataLakeStoreAccountProperties.
        :type default_group: str
        """

        self._default_group = default_group

    @property
    def encryption_config(self):
        """Gets the encryption_config of this UpdateDataLakeStoreAccountProperties.


        :return: The encryption_config of this UpdateDataLakeStoreAccountProperties.
        :rtype: UpdateEncryptionConfig
        """
        return self._encryption_config

    @encryption_config.setter
    def encryption_config(self, encryption_config):
        """Sets the encryption_config of this UpdateDataLakeStoreAccountProperties.


        :param encryption_config: The encryption_config of this UpdateDataLakeStoreAccountProperties.
        :type encryption_config: UpdateEncryptionConfig
        """

        self._encryption_config = encryption_config

    @property
    def firewall_allow_azure_ips(self):
        """Gets the firewall_allow_azure_ips of this UpdateDataLakeStoreAccountProperties.

        The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.

        :return: The firewall_allow_azure_ips of this UpdateDataLakeStoreAccountProperties.
        :rtype: str
        """
        return self._firewall_allow_azure_ips

    @firewall_allow_azure_ips.setter
    def firewall_allow_azure_ips(self, firewall_allow_azure_ips):
        """Sets the firewall_allow_azure_ips of this UpdateDataLakeStoreAccountProperties.

        The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.

        :param firewall_allow_azure_ips: The firewall_allow_azure_ips of this UpdateDataLakeStoreAccountProperties.
        :type firewall_allow_azure_ips: str
        """
        allowed_values = ["Enabled", "Disabled"]  # noqa: E501
        if firewall_allow_azure_ips not in allowed_values:
            raise ValueError(
                "Invalid value for `firewall_allow_azure_ips` ({0}), must be one of {1}"
                .format(firewall_allow_azure_ips, allowed_values)
            )

        self._firewall_allow_azure_ips = firewall_allow_azure_ips

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this UpdateDataLakeStoreAccountProperties.

        The list of firewall rules associated with this Data Lake Store account.

        :return: The firewall_rules of this UpdateDataLakeStoreAccountProperties.
        :rtype: List[UpdateFirewallRuleWithAccountParameters]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this UpdateDataLakeStoreAccountProperties.

        The list of firewall rules associated with this Data Lake Store account.

        :param firewall_rules: The firewall_rules of this UpdateDataLakeStoreAccountProperties.
        :type firewall_rules: List[UpdateFirewallRuleWithAccountParameters]
        """

        self._firewall_rules = firewall_rules

    @property
    def firewall_state(self):
        """Gets the firewall_state of this UpdateDataLakeStoreAccountProperties.

        The current state of the IP address firewall for this Data Lake Store account. Disabling the firewall does not remove existing rules, they will just be ignored until the firewall is re-enabled.

        :return: The firewall_state of this UpdateDataLakeStoreAccountProperties.
        :rtype: str
        """
        return self._firewall_state

    @firewall_state.setter
    def firewall_state(self, firewall_state):
        """Sets the firewall_state of this UpdateDataLakeStoreAccountProperties.

        The current state of the IP address firewall for this Data Lake Store account. Disabling the firewall does not remove existing rules, they will just be ignored until the firewall is re-enabled.

        :param firewall_state: The firewall_state of this UpdateDataLakeStoreAccountProperties.
        :type firewall_state: str
        """
        allowed_values = ["Enabled", "Disabled"]  # noqa: E501
        if firewall_state not in allowed_values:
            raise ValueError(
                "Invalid value for `firewall_state` ({0}), must be one of {1}"
                .format(firewall_state, allowed_values)
            )

        self._firewall_state = firewall_state

    @property
    def new_tier(self):
        """Gets the new_tier of this UpdateDataLakeStoreAccountProperties.

        The commitment tier to use for next month.

        :return: The new_tier of this UpdateDataLakeStoreAccountProperties.
        :rtype: str
        """
        return self._new_tier

    @new_tier.setter
    def new_tier(self, new_tier):
        """Sets the new_tier of this UpdateDataLakeStoreAccountProperties.

        The commitment tier to use for next month.

        :param new_tier: The new_tier of this UpdateDataLakeStoreAccountProperties.
        :type new_tier: str
        """
        allowed_values = ["Consumption", "Commitment_1TB", "Commitment_10TB", "Commitment_100TB", "Commitment_500TB", "Commitment_1PB", "Commitment_5PB"]  # noqa: E501
        if new_tier not in allowed_values:
            raise ValueError(
                "Invalid value for `new_tier` ({0}), must be one of {1}"
                .format(new_tier, allowed_values)
            )

        self._new_tier = new_tier

    @property
    def trusted_id_provider_state(self):
        """Gets the trusted_id_provider_state of this UpdateDataLakeStoreAccountProperties.

        The current state of the trusted identity provider feature for this Data Lake Store account. Disabling trusted identity provider functionality does not remove the providers, they will just be ignored until this feature is re-enabled.

        :return: The trusted_id_provider_state of this UpdateDataLakeStoreAccountProperties.
        :rtype: str
        """
        return self._trusted_id_provider_state

    @trusted_id_provider_state.setter
    def trusted_id_provider_state(self, trusted_id_provider_state):
        """Sets the trusted_id_provider_state of this UpdateDataLakeStoreAccountProperties.

        The current state of the trusted identity provider feature for this Data Lake Store account. Disabling trusted identity provider functionality does not remove the providers, they will just be ignored until this feature is re-enabled.

        :param trusted_id_provider_state: The trusted_id_provider_state of this UpdateDataLakeStoreAccountProperties.
        :type trusted_id_provider_state: str
        """
        allowed_values = ["Enabled", "Disabled"]  # noqa: E501
        if trusted_id_provider_state not in allowed_values:
            raise ValueError(
                "Invalid value for `trusted_id_provider_state` ({0}), must be one of {1}"
                .format(trusted_id_provider_state, allowed_values)
            )

        self._trusted_id_provider_state = trusted_id_provider_state

    @property
    def trusted_id_providers(self):
        """Gets the trusted_id_providers of this UpdateDataLakeStoreAccountProperties.

        The list of trusted identity providers associated with this Data Lake Store account.

        :return: The trusted_id_providers of this UpdateDataLakeStoreAccountProperties.
        :rtype: List[UpdateTrustedIdProviderWithAccountParameters]
        """
        return self._trusted_id_providers

    @trusted_id_providers.setter
    def trusted_id_providers(self, trusted_id_providers):
        """Sets the trusted_id_providers of this UpdateDataLakeStoreAccountProperties.

        The list of trusted identity providers associated with this Data Lake Store account.

        :param trusted_id_providers: The trusted_id_providers of this UpdateDataLakeStoreAccountProperties.
        :type trusted_id_providers: List[UpdateTrustedIdProviderWithAccountParameters]
        """

        self._trusted_id_providers = trusted_id_providers

    @property
    def virtual_network_rules(self):
        """Gets the virtual_network_rules of this UpdateDataLakeStoreAccountProperties.

        The list of virtual network rules associated with this Data Lake Store account.

        :return: The virtual_network_rules of this UpdateDataLakeStoreAccountProperties.
        :rtype: List[UpdateVirtualNetworkRuleWithAccountParameters]
        """
        return self._virtual_network_rules

    @virtual_network_rules.setter
    def virtual_network_rules(self, virtual_network_rules):
        """Sets the virtual_network_rules of this UpdateDataLakeStoreAccountProperties.

        The list of virtual network rules associated with this Data Lake Store account.

        :param virtual_network_rules: The virtual_network_rules of this UpdateDataLakeStoreAccountProperties.
        :type virtual_network_rules: List[UpdateVirtualNetworkRuleWithAccountParameters]
        """

        self._virtual_network_rules = virtual_network_rules
