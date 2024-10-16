# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.account_attributes_allowed_ip_inner import AccountAttributesAllowedIpInner
from openapi_server.models.branding_settings import BrandingSettings
from openapi_server.models.plan_details import PlanDetails
from openapi_server.models.quota import Quota
from openapi_server import util


class AccountAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_name: str=None, account_onboarding: bool=None, allowed_ip: List[AccountAttributesAllowedIpInner]=None, branding: bool=None, branding_settings: BrandingSettings=None, client_id: int=None, complex_passwords: bool=None, created: datetime=None, custom_domain: bool=None, custom_signature: str=None, external_domains: List[str]=None, max_users: int=None, modified: datetime=None, plan_details: PlanDetails=None, quota: Quota=None, secure_only: bool=None, show_referral_links: bool=None, status: int=None, user_count: int=None, welcome_email_content: str=None, welcome_email_subject: str=None):
        """AccountAttributes - a model defined in OpenAPI

        :param account_name: The account_name of this AccountAttributes.
        :param account_onboarding: The account_onboarding of this AccountAttributes.
        :param allowed_ip: The allowed_ip of this AccountAttributes.
        :param branding: The branding of this AccountAttributes.
        :param branding_settings: The branding_settings of this AccountAttributes.
        :param client_id: The client_id of this AccountAttributes.
        :param complex_passwords: The complex_passwords of this AccountAttributes.
        :param created: The created of this AccountAttributes.
        :param custom_domain: The custom_domain of this AccountAttributes.
        :param custom_signature: The custom_signature of this AccountAttributes.
        :param external_domains: The external_domains of this AccountAttributes.
        :param max_users: The max_users of this AccountAttributes.
        :param modified: The modified of this AccountAttributes.
        :param plan_details: The plan_details of this AccountAttributes.
        :param quota: The quota of this AccountAttributes.
        :param secure_only: The secure_only of this AccountAttributes.
        :param show_referral_links: The show_referral_links of this AccountAttributes.
        :param status: The status of this AccountAttributes.
        :param user_count: The user_count of this AccountAttributes.
        :param welcome_email_content: The welcome_email_content of this AccountAttributes.
        :param welcome_email_subject: The welcome_email_subject of this AccountAttributes.
        """
        self.openapi_types = {
            'account_name': str,
            'account_onboarding': bool,
            'allowed_ip': List[AccountAttributesAllowedIpInner],
            'branding': bool,
            'branding_settings': BrandingSettings,
            'client_id': int,
            'complex_passwords': bool,
            'created': datetime,
            'custom_domain': bool,
            'custom_signature': str,
            'external_domains': List[str],
            'max_users': int,
            'modified': datetime,
            'plan_details': PlanDetails,
            'quota': Quota,
            'secure_only': bool,
            'show_referral_links': bool,
            'status': int,
            'user_count': int,
            'welcome_email_content': str,
            'welcome_email_subject': str
        }

        self.attribute_map = {
            'account_name': 'accountName',
            'account_onboarding': 'accountOnboarding',
            'allowed_ip': 'allowedIp',
            'branding': 'branding',
            'branding_settings': 'brandingSettings',
            'client_id': 'clientId',
            'complex_passwords': 'complexPasswords',
            'created': 'created',
            'custom_domain': 'customDomain',
            'custom_signature': 'customSignature',
            'external_domains': 'externalDomains',
            'max_users': 'maxUsers',
            'modified': 'modified',
            'plan_details': 'planDetails',
            'quota': 'quota',
            'secure_only': 'secureOnly',
            'show_referral_links': 'showReferralLinks',
            'status': 'status',
            'user_count': 'userCount',
            'welcome_email_content': 'welcomeEmailContent',
            'welcome_email_subject': 'welcomeEmailSubject'
        }

        self._account_name = account_name
        self._account_onboarding = account_onboarding
        self._allowed_ip = allowed_ip
        self._branding = branding
        self._branding_settings = branding_settings
        self._client_id = client_id
        self._complex_passwords = complex_passwords
        self._created = created
        self._custom_domain = custom_domain
        self._custom_signature = custom_signature
        self._external_domains = external_domains
        self._max_users = max_users
        self._modified = modified
        self._plan_details = plan_details
        self._quota = quota
        self._secure_only = secure_only
        self._show_referral_links = show_referral_links
        self._status = status
        self._user_count = user_count
        self._welcome_email_content = welcome_email_content
        self._welcome_email_subject = welcome_email_subject

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AccountAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AccountAttributes of this AccountAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_name(self):
        """Gets the account_name of this AccountAttributes.

        Name of the account

        :return: The account_name of this AccountAttributes.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AccountAttributes.

        Name of the account

        :param account_name: The account_name of this AccountAttributes.
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def account_onboarding(self):
        """Gets the account_onboarding of this AccountAttributes.

        Whether the web application onboarding help is enabled for new users in the account.

        :return: The account_onboarding of this AccountAttributes.
        :rtype: bool
        """
        return self._account_onboarding

    @account_onboarding.setter
    def account_onboarding(self, account_onboarding):
        """Sets the account_onboarding of this AccountAttributes.

        Whether the web application onboarding help is enabled for new users in the account.

        :param account_onboarding: The account_onboarding of this AccountAttributes.
        :type account_onboarding: bool
        """

        self._account_onboarding = account_onboarding

    @property
    def allowed_ip(self):
        """Gets the allowed_ip of this AccountAttributes.

        Range of IP addresses allowed to access this account.

        :return: The allowed_ip of this AccountAttributes.
        :rtype: List[AccountAttributesAllowedIpInner]
        """
        return self._allowed_ip

    @allowed_ip.setter
    def allowed_ip(self, allowed_ip):
        """Sets the allowed_ip of this AccountAttributes.

        Range of IP addresses allowed to access this account.

        :param allowed_ip: The allowed_ip of this AccountAttributes.
        :type allowed_ip: List[AccountAttributesAllowedIpInner]
        """

        self._allowed_ip = allowed_ip

    @property
    def branding(self):
        """Gets the branding of this AccountAttributes.

        Branding flag. Set to `true` if the account has branding functionality enabled.

        :return: The branding of this AccountAttributes.
        :rtype: bool
        """
        return self._branding

    @branding.setter
    def branding(self, branding):
        """Sets the branding of this AccountAttributes.

        Branding flag. Set to `true` if the account has branding functionality enabled.

        :param branding: The branding of this AccountAttributes.
        :type branding: bool
        """

        self._branding = branding

    @property
    def branding_settings(self):
        """Gets the branding_settings of this AccountAttributes.


        :return: The branding_settings of this AccountAttributes.
        :rtype: BrandingSettings
        """
        return self._branding_settings

    @branding_settings.setter
    def branding_settings(self, branding_settings):
        """Sets the branding_settings of this AccountAttributes.


        :param branding_settings: The branding_settings of this AccountAttributes.
        :type branding_settings: BrandingSettings
        """

        self._branding_settings = branding_settings

    @property
    def client_id(self):
        """Gets the client_id of this AccountAttributes.

        (ExaVault Use Only) Internal ID of the account in CMS.

        :return: The client_id of this AccountAttributes.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AccountAttributes.

        (ExaVault Use Only) Internal ID of the account in CMS.

        :param client_id: The client_id of this AccountAttributes.
        :type client_id: int
        """

        self._client_id = client_id

    @property
    def complex_passwords(self):
        """Gets the complex_passwords of this AccountAttributes.

        Flag to indicate whether the account requires complex passwords. Set to `true` to require complex passwords on all users and shares.

        :return: The complex_passwords of this AccountAttributes.
        :rtype: bool
        """
        return self._complex_passwords

    @complex_passwords.setter
    def complex_passwords(self, complex_passwords):
        """Sets the complex_passwords of this AccountAttributes.

        Flag to indicate whether the account requires complex passwords. Set to `true` to require complex passwords on all users and shares.

        :param complex_passwords: The complex_passwords of this AccountAttributes.
        :type complex_passwords: bool
        """

        self._complex_passwords = complex_passwords

    @property
    def created(self):
        """Gets the created of this AccountAttributes.

        Timestamp of account creation.

        :return: The created of this AccountAttributes.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AccountAttributes.

        Timestamp of account creation.

        :param created: The created of this AccountAttributes.
        :type created: datetime
        """

        self._created = created

    @property
    def custom_domain(self):
        """Gets the custom_domain of this AccountAttributes.

        Custom domain flag. Set to `true` if account type allows custom domain functionality.

        :return: The custom_domain of this AccountAttributes.
        :rtype: bool
        """
        return self._custom_domain

    @custom_domain.setter
    def custom_domain(self, custom_domain):
        """Sets the custom_domain of this AccountAttributes.

        Custom domain flag. Set to `true` if account type allows custom domain functionality.

        :param custom_domain: The custom_domain of this AccountAttributes.
        :type custom_domain: bool
        """

        self._custom_domain = custom_domain

    @property
    def custom_signature(self):
        """Gets the custom_signature of this AccountAttributes.

        Custom signature for all account emails users or recipients will receive.

        :return: The custom_signature of this AccountAttributes.
        :rtype: str
        """
        return self._custom_signature

    @custom_signature.setter
    def custom_signature(self, custom_signature):
        """Sets the custom_signature of this AccountAttributes.

        Custom signature for all account emails users or recipients will receive.

        :param custom_signature: The custom_signature of this AccountAttributes.
        :type custom_signature: str
        """

        self._custom_signature = custom_signature

    @property
    def external_domains(self):
        """Gets the external_domains of this AccountAttributes.

        Custom domain used to brand this account.

        :return: The external_domains of this AccountAttributes.
        :rtype: List[str]
        """
        return self._external_domains

    @external_domains.setter
    def external_domains(self, external_domains):
        """Sets the external_domains of this AccountAttributes.

        Custom domain used to brand this account.

        :param external_domains: The external_domains of this AccountAttributes.
        :type external_domains: List[str]
        """

        self._external_domains = external_domains

    @property
    def max_users(self):
        """Gets the max_users of this AccountAttributes.

        Maximum number of users the account can have. This can be increased by contacting ExaVault Support.

        :return: The max_users of this AccountAttributes.
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """Sets the max_users of this AccountAttributes.

        Maximum number of users the account can have. This can be increased by contacting ExaVault Support.

        :param max_users: The max_users of this AccountAttributes.
        :type max_users: int
        """

        self._max_users = max_users

    @property
    def modified(self):
        """Gets the modified of this AccountAttributes.

        Timestamp of account modification.

        :return: The modified of this AccountAttributes.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this AccountAttributes.

        Timestamp of account modification.

        :param modified: The modified of this AccountAttributes.
        :type modified: datetime
        """

        self._modified = modified

    @property
    def plan_details(self):
        """Gets the plan_details of this AccountAttributes.


        :return: The plan_details of this AccountAttributes.
        :rtype: PlanDetails
        """
        return self._plan_details

    @plan_details.setter
    def plan_details(self, plan_details):
        """Sets the plan_details of this AccountAttributes.


        :param plan_details: The plan_details of this AccountAttributes.
        :type plan_details: PlanDetails
        """

        self._plan_details = plan_details

    @property
    def quota(self):
        """Gets the quota of this AccountAttributes.


        :return: The quota of this AccountAttributes.
        :rtype: Quota
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this AccountAttributes.


        :param quota: The quota of this AccountAttributes.
        :type quota: Quota
        """

        self._quota = quota

    @property
    def secure_only(self):
        """Gets the secure_only of this AccountAttributes.

        Flag to indicate whether the account disables connections via insecure protocols (e.g. FTP). Set to `true` to disable all traffic over port 21.

        :return: The secure_only of this AccountAttributes.
        :rtype: bool
        """
        return self._secure_only

    @secure_only.setter
    def secure_only(self, secure_only):
        """Sets the secure_only of this AccountAttributes.

        Flag to indicate whether the account disables connections via insecure protocols (e.g. FTP). Set to `true` to disable all traffic over port 21.

        :param secure_only: The secure_only of this AccountAttributes.
        :type secure_only: bool
        """

        self._secure_only = secure_only

    @property
    def show_referral_links(self):
        """Gets the show_referral_links of this AccountAttributes.

        Flag to indicate showing of referrals links in the account. Set to `true` to include marketing messages in share invitations.

        :return: The show_referral_links of this AccountAttributes.
        :rtype: bool
        """
        return self._show_referral_links

    @show_referral_links.setter
    def show_referral_links(self, show_referral_links):
        """Sets the show_referral_links of this AccountAttributes.

        Flag to indicate showing of referrals links in the account. Set to `true` to include marketing messages in share invitations.

        :param show_referral_links: The show_referral_links of this AccountAttributes.
        :type show_referral_links: bool
        """

        self._show_referral_links = show_referral_links

    @property
    def status(self):
        """Gets the status of this AccountAttributes.

        Account status flag. A one (1) means the account is active; zero (0) means it is suspended.

        :return: The status of this AccountAttributes.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountAttributes.

        Account status flag. A one (1) means the account is active; zero (0) means it is suspended.

        :param status: The status of this AccountAttributes.
        :type status: int
        """
        allowed_values = [1, 0]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_count(self):
        """Gets the user_count of this AccountAttributes.

        Current number of users on the account.

        :return: The user_count of this AccountAttributes.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this AccountAttributes.

        Current number of users on the account.

        :param user_count: The user_count of this AccountAttributes.
        :type user_count: int
        """

        self._user_count = user_count

    @property
    def welcome_email_content(self):
        """Gets the welcome_email_content of this AccountAttributes.

        Content of welcome email each new user will receive.

        :return: The welcome_email_content of this AccountAttributes.
        :rtype: str
        """
        return self._welcome_email_content

    @welcome_email_content.setter
    def welcome_email_content(self, welcome_email_content):
        """Sets the welcome_email_content of this AccountAttributes.

        Content of welcome email each new user will receive.

        :param welcome_email_content: The welcome_email_content of this AccountAttributes.
        :type welcome_email_content: str
        """

        self._welcome_email_content = welcome_email_content

    @property
    def welcome_email_subject(self):
        """Gets the welcome_email_subject of this AccountAttributes.

        Subject of welcome email each new user will receive.

        :return: The welcome_email_subject of this AccountAttributes.
        :rtype: str
        """
        return self._welcome_email_subject

    @welcome_email_subject.setter
    def welcome_email_subject(self, welcome_email_subject):
        """Sets the welcome_email_subject of this AccountAttributes.

        Subject of welcome email each new user will receive.

        :param welcome_email_subject: The welcome_email_subject of this AccountAttributes.
        :type welcome_email_subject: str
        """

        self._welcome_email_subject = welcome_email_subject
