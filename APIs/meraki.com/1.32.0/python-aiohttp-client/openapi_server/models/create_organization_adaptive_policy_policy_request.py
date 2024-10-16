# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_organization_adaptive_policy_policy_request_acls_inner import CreateOrganizationAdaptivePolicyPolicyRequestAclsInner
from openapi_server.models.create_organization_adaptive_policy_policy_request_destination_group import CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup
from openapi_server.models.create_organization_adaptive_policy_policy_request_source_group import CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup
from openapi_server import util


class CreateOrganizationAdaptivePolicyPolicyRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, acls: List[CreateOrganizationAdaptivePolicyPolicyRequestAclsInner]=None, destination_group: CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup=None, last_entry_rule: str=None, source_group: CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup=None):
        """CreateOrganizationAdaptivePolicyPolicyRequest - a model defined in OpenAPI

        :param acls: The acls of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :param destination_group: The destination_group of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :param last_entry_rule: The last_entry_rule of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :param source_group: The source_group of this CreateOrganizationAdaptivePolicyPolicyRequest.
        """
        self.openapi_types = {
            'acls': List[CreateOrganizationAdaptivePolicyPolicyRequestAclsInner],
            'destination_group': CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup,
            'last_entry_rule': str,
            'source_group': CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup
        }

        self.attribute_map = {
            'acls': 'acls',
            'destination_group': 'destinationGroup',
            'last_entry_rule': 'lastEntryRule',
            'source_group': 'sourceGroup'
        }

        self._acls = acls
        self._destination_group = destination_group
        self._last_entry_rule = last_entry_rule
        self._source_group = source_group

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateOrganizationAdaptivePolicyPolicyRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createOrganizationAdaptivePolicyPolicy_request of this CreateOrganizationAdaptivePolicyPolicyRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def acls(self):
        """Gets the acls of this CreateOrganizationAdaptivePolicyPolicyRequest.

        An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: [])

        :return: The acls of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :rtype: List[CreateOrganizationAdaptivePolicyPolicyRequestAclsInner]
        """
        return self._acls

    @acls.setter
    def acls(self, acls):
        """Sets the acls of this CreateOrganizationAdaptivePolicyPolicyRequest.

        An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: [])

        :param acls: The acls of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :type acls: List[CreateOrganizationAdaptivePolicyPolicyRequestAclsInner]
        """

        self._acls = acls

    @property
    def destination_group(self):
        """Gets the destination_group of this CreateOrganizationAdaptivePolicyPolicyRequest.


        :return: The destination_group of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :rtype: CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup
        """
        return self._destination_group

    @destination_group.setter
    def destination_group(self, destination_group):
        """Sets the destination_group of this CreateOrganizationAdaptivePolicyPolicyRequest.


        :param destination_group: The destination_group of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :type destination_group: CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup
        """
        if destination_group is None:
            raise ValueError("Invalid value for `destination_group`, must not be `None`")

        self._destination_group = destination_group

    @property
    def last_entry_rule(self):
        """Gets the last_entry_rule of this CreateOrganizationAdaptivePolicyPolicyRequest.

        The rule to apply if there is no matching ACL (default: \"default\")

        :return: The last_entry_rule of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :rtype: str
        """
        return self._last_entry_rule

    @last_entry_rule.setter
    def last_entry_rule(self, last_entry_rule):
        """Sets the last_entry_rule of this CreateOrganizationAdaptivePolicyPolicyRequest.

        The rule to apply if there is no matching ACL (default: \"default\")

        :param last_entry_rule: The last_entry_rule of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :type last_entry_rule: str
        """
        allowed_values = ["allow", "default", "deny"]  # noqa: E501
        if last_entry_rule not in allowed_values:
            raise ValueError(
                "Invalid value for `last_entry_rule` ({0}), must be one of {1}"
                .format(last_entry_rule, allowed_values)
            )

        self._last_entry_rule = last_entry_rule

    @property
    def source_group(self):
        """Gets the source_group of this CreateOrganizationAdaptivePolicyPolicyRequest.


        :return: The source_group of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :rtype: CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup
        """
        return self._source_group

    @source_group.setter
    def source_group(self, source_group):
        """Sets the source_group of this CreateOrganizationAdaptivePolicyPolicyRequest.


        :param source_group: The source_group of this CreateOrganizationAdaptivePolicyPolicyRequest.
        :type source_group: CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup
        """
        if source_group is None:
            raise ValueError("Invalid value for `source_group`, must not be `None`")

        self._source_group = source_group
