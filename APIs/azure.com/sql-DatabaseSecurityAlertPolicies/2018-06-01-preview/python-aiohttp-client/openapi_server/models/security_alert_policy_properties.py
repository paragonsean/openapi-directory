# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SecurityAlertPolicyProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, creation_time: datetime=None, disabled_alerts: List[str]=None, email_account_admins: bool=None, email_addresses: List[str]=None, retention_days: int=None, state: str=None, storage_account_access_key: str=None, storage_endpoint: str=None):
        """SecurityAlertPolicyProperties - a model defined in OpenAPI

        :param creation_time: The creation_time of this SecurityAlertPolicyProperties.
        :param disabled_alerts: The disabled_alerts of this SecurityAlertPolicyProperties.
        :param email_account_admins: The email_account_admins of this SecurityAlertPolicyProperties.
        :param email_addresses: The email_addresses of this SecurityAlertPolicyProperties.
        :param retention_days: The retention_days of this SecurityAlertPolicyProperties.
        :param state: The state of this SecurityAlertPolicyProperties.
        :param storage_account_access_key: The storage_account_access_key of this SecurityAlertPolicyProperties.
        :param storage_endpoint: The storage_endpoint of this SecurityAlertPolicyProperties.
        """
        self.openapi_types = {
            'creation_time': datetime,
            'disabled_alerts': List[str],
            'email_account_admins': bool,
            'email_addresses': List[str],
            'retention_days': int,
            'state': str,
            'storage_account_access_key': str,
            'storage_endpoint': str
        }

        self.attribute_map = {
            'creation_time': 'creationTime',
            'disabled_alerts': 'disabledAlerts',
            'email_account_admins': 'emailAccountAdmins',
            'email_addresses': 'emailAddresses',
            'retention_days': 'retentionDays',
            'state': 'state',
            'storage_account_access_key': 'storageAccountAccessKey',
            'storage_endpoint': 'storageEndpoint'
        }

        self._creation_time = creation_time
        self._disabled_alerts = disabled_alerts
        self._email_account_admins = email_account_admins
        self._email_addresses = email_addresses
        self._retention_days = retention_days
        self._state = state
        self._storage_account_access_key = storage_account_access_key
        self._storage_endpoint = storage_endpoint

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SecurityAlertPolicyProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SecurityAlertPolicyProperties of this SecurityAlertPolicyProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def creation_time(self):
        """Gets the creation_time of this SecurityAlertPolicyProperties.

        Specifies the UTC creation time of the policy.

        :return: The creation_time of this SecurityAlertPolicyProperties.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SecurityAlertPolicyProperties.

        Specifies the UTC creation time of the policy.

        :param creation_time: The creation_time of this SecurityAlertPolicyProperties.
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def disabled_alerts(self):
        """Gets the disabled_alerts of this SecurityAlertPolicyProperties.

        Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action

        :return: The disabled_alerts of this SecurityAlertPolicyProperties.
        :rtype: List[str]
        """
        return self._disabled_alerts

    @disabled_alerts.setter
    def disabled_alerts(self, disabled_alerts):
        """Sets the disabled_alerts of this SecurityAlertPolicyProperties.

        Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action

        :param disabled_alerts: The disabled_alerts of this SecurityAlertPolicyProperties.
        :type disabled_alerts: List[str]
        """

        self._disabled_alerts = disabled_alerts

    @property
    def email_account_admins(self):
        """Gets the email_account_admins of this SecurityAlertPolicyProperties.

        Specifies that the alert is sent to the account administrators.

        :return: The email_account_admins of this SecurityAlertPolicyProperties.
        :rtype: bool
        """
        return self._email_account_admins

    @email_account_admins.setter
    def email_account_admins(self, email_account_admins):
        """Sets the email_account_admins of this SecurityAlertPolicyProperties.

        Specifies that the alert is sent to the account administrators.

        :param email_account_admins: The email_account_admins of this SecurityAlertPolicyProperties.
        :type email_account_admins: bool
        """

        self._email_account_admins = email_account_admins

    @property
    def email_addresses(self):
        """Gets the email_addresses of this SecurityAlertPolicyProperties.

        Specifies an array of e-mail addresses to which the alert is sent.

        :return: The email_addresses of this SecurityAlertPolicyProperties.
        :rtype: List[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this SecurityAlertPolicyProperties.

        Specifies an array of e-mail addresses to which the alert is sent.

        :param email_addresses: The email_addresses of this SecurityAlertPolicyProperties.
        :type email_addresses: List[str]
        """

        self._email_addresses = email_addresses

    @property
    def retention_days(self):
        """Gets the retention_days of this SecurityAlertPolicyProperties.

        Specifies the number of days to keep in the Threat Detection audit logs.

        :return: The retention_days of this SecurityAlertPolicyProperties.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        """Sets the retention_days of this SecurityAlertPolicyProperties.

        Specifies the number of days to keep in the Threat Detection audit logs.

        :param retention_days: The retention_days of this SecurityAlertPolicyProperties.
        :type retention_days: int
        """

        self._retention_days = retention_days

    @property
    def state(self):
        """Gets the state of this SecurityAlertPolicyProperties.

        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.

        :return: The state of this SecurityAlertPolicyProperties.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SecurityAlertPolicyProperties.

        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.

        :param state: The state of this SecurityAlertPolicyProperties.
        :type state: str
        """
        allowed_values = ["New", "Enabled", "Disabled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def storage_account_access_key(self):
        """Gets the storage_account_access_key of this SecurityAlertPolicyProperties.

        Specifies the identifier key of the Threat Detection audit storage account.

        :return: The storage_account_access_key of this SecurityAlertPolicyProperties.
        :rtype: str
        """
        return self._storage_account_access_key

    @storage_account_access_key.setter
    def storage_account_access_key(self, storage_account_access_key):
        """Sets the storage_account_access_key of this SecurityAlertPolicyProperties.

        Specifies the identifier key of the Threat Detection audit storage account.

        :param storage_account_access_key: The storage_account_access_key of this SecurityAlertPolicyProperties.
        :type storage_account_access_key: str
        """

        self._storage_account_access_key = storage_account_access_key

    @property
    def storage_endpoint(self):
        """Gets the storage_endpoint of this SecurityAlertPolicyProperties.

        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs.

        :return: The storage_endpoint of this SecurityAlertPolicyProperties.
        :rtype: str
        """
        return self._storage_endpoint

    @storage_endpoint.setter
    def storage_endpoint(self, storage_endpoint):
        """Sets the storage_endpoint of this SecurityAlertPolicyProperties.

        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs.

        :param storage_endpoint: The storage_endpoint of this SecurityAlertPolicyProperties.
        :type storage_endpoint: str
        """

        self._storage_endpoint = storage_endpoint
