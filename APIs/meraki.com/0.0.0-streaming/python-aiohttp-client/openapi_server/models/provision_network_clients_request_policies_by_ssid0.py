# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProvisionNetworkClientsRequestPoliciesBySsid0(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_policy: str=None, group_policy_id: str=None):
        """ProvisionNetworkClientsRequestPoliciesBySsid0 - a model defined in OpenAPI

        :param device_policy: The device_policy of this ProvisionNetworkClientsRequestPoliciesBySsid0.
        :param group_policy_id: The group_policy_id of this ProvisionNetworkClientsRequestPoliciesBySsid0.
        """
        self.openapi_types = {
            'device_policy': str,
            'group_policy_id': str
        }

        self.attribute_map = {
            'device_policy': 'devicePolicy',
            'group_policy_id': 'groupPolicyId'
        }

        self._device_policy = device_policy
        self._group_policy_id = group_policy_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProvisionNetworkClientsRequestPoliciesBySsid0':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The provisionNetworkClients_request_policiesBySsid_0 of this ProvisionNetworkClientsRequestPoliciesBySsid0.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_policy(self):
        """Gets the device_policy of this ProvisionNetworkClientsRequestPoliciesBySsid0.

        The policy to apply to the specified client. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.

        :return: The device_policy of this ProvisionNetworkClientsRequestPoliciesBySsid0.
        :rtype: str
        """
        return self._device_policy

    @device_policy.setter
    def device_policy(self, device_policy):
        """Sets the device_policy of this ProvisionNetworkClientsRequestPoliciesBySsid0.

        The policy to apply to the specified client. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.

        :param device_policy: The device_policy of this ProvisionNetworkClientsRequestPoliciesBySsid0.
        :type device_policy: str
        """
        allowed_values = ["Blocked", "Group policy", "Normal", "Whitelisted"]  # noqa: E501
        if device_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `device_policy` ({0}), must be one of {1}"
                .format(device_policy, allowed_values)
            )

        self._device_policy = device_policy

    @property
    def group_policy_id(self):
        """Gets the group_policy_id of this ProvisionNetworkClientsRequestPoliciesBySsid0.

        The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to \"Group policy\". Otherwise this is ignored.

        :return: The group_policy_id of this ProvisionNetworkClientsRequestPoliciesBySsid0.
        :rtype: str
        """
        return self._group_policy_id

    @group_policy_id.setter
    def group_policy_id(self, group_policy_id):
        """Sets the group_policy_id of this ProvisionNetworkClientsRequestPoliciesBySsid0.

        The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to \"Group policy\". Otherwise this is ignored.

        :param group_policy_id: The group_policy_id of this ProvisionNetworkClientsRequestPoliciesBySsid0.
        :type group_policy_id: str
        """

        self._group_policy_id = group_policy_id
