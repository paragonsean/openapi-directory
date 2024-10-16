# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.alias import Alias
from openapi_server.models.anti_spam import AntiSpam
from openapi_server.models.catch_all import CatchAll
from openapi_server.models.mail_zone_account import MailZoneAccount
from openapi_server.models.smtp_domain import SmtpDomain
from openapi_server import util


class MailZone(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aliases: List[Alias]=None, anti_spam: AntiSpam=None, available_accounts: List[MailZoneAccount]=None, catch_all: CatchAll=None, enabled: bool=None, name: str=None, smtp_domains: List[SmtpDomain]=None):
        """MailZone - a model defined in OpenAPI

        :param aliases: The aliases of this MailZone.
        :param anti_spam: The anti_spam of this MailZone.
        :param available_accounts: The available_accounts of this MailZone.
        :param catch_all: The catch_all of this MailZone.
        :param enabled: The enabled of this MailZone.
        :param name: The name of this MailZone.
        :param smtp_domains: The smtp_domains of this MailZone.
        """
        self.openapi_types = {
            'aliases': List[Alias],
            'anti_spam': AntiSpam,
            'available_accounts': List[MailZoneAccount],
            'catch_all': CatchAll,
            'enabled': bool,
            'name': str,
            'smtp_domains': List[SmtpDomain]
        }

        self.attribute_map = {
            'aliases': 'aliases',
            'anti_spam': 'anti_spam',
            'available_accounts': 'available_accounts',
            'catch_all': 'catch_all',
            'enabled': 'enabled',
            'name': 'name',
            'smtp_domains': 'smtp_domains'
        }

        self._aliases = aliases
        self._anti_spam = anti_spam
        self._available_accounts = available_accounts
        self._catch_all = catch_all
        self._enabled = enabled
        self._name = name
        self._smtp_domains = smtp_domains

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MailZone':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MailZone of this MailZone.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aliases(self):
        """Gets the aliases of this MailZone.

        List of aliases on the mail zone<br />  An alias is an e-mail address (alias) that automatically forwards received e-mails to another e-mail address (destination).

        :return: The aliases of this MailZone.
        :rtype: List[Alias]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this MailZone.

        List of aliases on the mail zone<br />  An alias is an e-mail address (alias) that automatically forwards received e-mails to another e-mail address (destination).

        :param aliases: The aliases of this MailZone.
        :type aliases: List[Alias]
        """

        self._aliases = aliases

    @property
    def anti_spam(self):
        """Gets the anti_spam of this MailZone.


        :return: The anti_spam of this MailZone.
        :rtype: AntiSpam
        """
        return self._anti_spam

    @anti_spam.setter
    def anti_spam(self, anti_spam):
        """Sets the anti_spam of this MailZone.


        :param anti_spam: The anti_spam of this MailZone.
        :type anti_spam: AntiSpam
        """

        self._anti_spam = anti_spam

    @property
    def available_accounts(self):
        """Gets the available_accounts of this MailZone.

        List of mail zone accounts with their mailbox size.

        :return: The available_accounts of this MailZone.
        :rtype: List[MailZoneAccount]
        """
        return self._available_accounts

    @available_accounts.setter
    def available_accounts(self, available_accounts):
        """Sets the available_accounts of this MailZone.

        List of mail zone accounts with their mailbox size.

        :param available_accounts: The available_accounts of this MailZone.
        :type available_accounts: List[MailZoneAccount]
        """

        self._available_accounts = available_accounts

    @property
    def catch_all(self):
        """Gets the catch_all of this MailZone.


        :return: The catch_all of this MailZone.
        :rtype: CatchAll
        """
        return self._catch_all

    @catch_all.setter
    def catch_all(self, catch_all):
        """Sets the catch_all of this MailZone.


        :param catch_all: The catch_all of this MailZone.
        :type catch_all: CatchAll
        """

        self._catch_all = catch_all

    @property
    def enabled(self):
        """Gets the enabled of this MailZone.

        Indicates whether the mail zone is enabled.

        :return: The enabled of this MailZone.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MailZone.

        Indicates whether the mail zone is enabled.

        :param enabled: The enabled of this MailZone.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def name(self):
        """Gets the name of this MailZone.


        :return: The name of this MailZone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MailZone.


        :param name: The name of this MailZone.
        :type name: str
        """

        self._name = name

    @property
    def smtp_domains(self):
        """Gets the smtp_domains of this MailZone.

        List of extra smtp domains on the mail zone<br />  SMTP domain names allow you to link multiple domain names to a single e-mail address.<br />  E-mails sent to an SMTP domain will be caught by the respective e-mail address on the main domain name.

        :return: The smtp_domains of this MailZone.
        :rtype: List[SmtpDomain]
        """
        return self._smtp_domains

    @smtp_domains.setter
    def smtp_domains(self, smtp_domains):
        """Sets the smtp_domains of this MailZone.

        List of extra smtp domains on the mail zone<br />  SMTP domain names allow you to link multiple domain names to a single e-mail address.<br />  E-mails sent to an SMTP domain will be caught by the respective e-mail address on the main domain name.

        :param smtp_domains: The smtp_domains of this MailZone.
        :type smtp_domains: List[SmtpDomain]
        """

        self._smtp_domains = smtp_domains
