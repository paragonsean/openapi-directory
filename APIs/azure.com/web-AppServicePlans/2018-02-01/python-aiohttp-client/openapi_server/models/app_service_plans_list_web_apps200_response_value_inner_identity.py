# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_identity_user_assigned_identities_value import AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue
from openapi_server import util


class AppServicePlansListWebApps200ResponseValueInnerIdentity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, principal_id: str=None, tenant_id: str=None, type: str=None, user_assigned_identities: Dict[str, AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue]=None):
        """AppServicePlansListWebApps200ResponseValueInnerIdentity - a model defined in OpenAPI

        :param principal_id: The principal_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :param tenant_id: The tenant_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :param type: The type of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :param user_assigned_identities: The user_assigned_identities of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        """
        self.openapi_types = {
            'principal_id': str,
            'tenant_id': str,
            'type': str,
            'user_assigned_identities': Dict[str, AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue]
        }

        self.attribute_map = {
            'principal_id': 'principalId',
            'tenant_id': 'tenantId',
            'type': 'type',
            'user_assigned_identities': 'userAssignedIdentities'
        }

        self._principal_id = principal_id
        self._tenant_id = tenant_id
        self._type = type
        self._user_assigned_identities = user_assigned_identities

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansListWebApps200ResponseValueInnerIdentity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_ListWebApps_200_response_value_inner_identity of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def principal_id(self):
        """Gets the principal_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        Principal Id of managed service identity.

        :return: The principal_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        """Sets the principal_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        Principal Id of managed service identity.

        :param principal_id: The principal_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :type principal_id: str
        """

        self._principal_id = principal_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        Tenant of managed service identity.

        :return: The tenant_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        Tenant of managed service identity.

        :param tenant_id: The tenant_id of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :type tenant_id: str
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        Type of managed service identity.

        :return: The type of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        Type of managed service identity.

        :param type: The type of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :type type: str
        """
        allowed_values = ["SystemAssigned", "UserAssigned", "SystemAssigned, UserAssigned", "None"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user_assigned_identities(self):
        """Gets the user_assigned_identities of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        The list of user assigned identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}

        :return: The user_assigned_identities of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :rtype: Dict[str, AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue]
        """
        return self._user_assigned_identities

    @user_assigned_identities.setter
    def user_assigned_identities(self, user_assigned_identities):
        """Sets the user_assigned_identities of this AppServicePlansListWebApps200ResponseValueInnerIdentity.

        The list of user assigned identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}

        :param user_assigned_identities: The user_assigned_identities of this AppServicePlansListWebApps200ResponseValueInnerIdentity.
        :type user_assigned_identities: Dict[str, AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue]
        """

        self._user_assigned_identities = user_assigned_identities
