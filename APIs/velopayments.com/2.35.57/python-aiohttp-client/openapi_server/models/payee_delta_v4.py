# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class PayeeDeltaV4(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dba_name: str=None, display_name: str=None, email: str=None, onboarded_status: str=None, payee_country: str=None, payee_id: str=None, remote_id: str=None):
        """PayeeDeltaV4 - a model defined in OpenAPI

        :param dba_name: The dba_name of this PayeeDeltaV4.
        :param display_name: The display_name of this PayeeDeltaV4.
        :param email: The email of this PayeeDeltaV4.
        :param onboarded_status: The onboarded_status of this PayeeDeltaV4.
        :param payee_country: The payee_country of this PayeeDeltaV4.
        :param payee_id: The payee_id of this PayeeDeltaV4.
        :param remote_id: The remote_id of this PayeeDeltaV4.
        """
        self.openapi_types = {
            'dba_name': str,
            'display_name': str,
            'email': str,
            'onboarded_status': str,
            'payee_country': str,
            'payee_id': str,
            'remote_id': str
        }

        self.attribute_map = {
            'dba_name': 'dbaName',
            'display_name': 'displayName',
            'email': 'email',
            'onboarded_status': 'onboardedStatus',
            'payee_country': 'payeeCountry',
            'payee_id': 'payeeId',
            'remote_id': 'remoteId'
        }

        self._dba_name = dba_name
        self._display_name = display_name
        self._email = email
        self._onboarded_status = onboarded_status
        self._payee_country = payee_country
        self._payee_id = payee_id
        self._remote_id = remote_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PayeeDeltaV4':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PayeeDeltaV4 of this PayeeDeltaV4.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dba_name(self):
        """Gets the dba_name of this PayeeDeltaV4.


        :return: The dba_name of this PayeeDeltaV4.
        :rtype: str
        """
        return self._dba_name

    @dba_name.setter
    def dba_name(self, dba_name):
        """Sets the dba_name of this PayeeDeltaV4.


        :param dba_name: The dba_name of this PayeeDeltaV4.
        :type dba_name: str
        """

        self._dba_name = dba_name

    @property
    def display_name(self):
        """Gets the display_name of this PayeeDeltaV4.


        :return: The display_name of this PayeeDeltaV4.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PayeeDeltaV4.


        :param display_name: The display_name of this PayeeDeltaV4.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this PayeeDeltaV4.


        :return: The email of this PayeeDeltaV4.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayeeDeltaV4.


        :param email: The email of this PayeeDeltaV4.
        :type email: str
        """

        self._email = email

    @property
    def onboarded_status(self):
        """Gets the onboarded_status of this PayeeDeltaV4.

        Payee onboarded status. One of the following value: CREATED, INVITED, REGISTERED, ONBOARDED

        :return: The onboarded_status of this PayeeDeltaV4.
        :rtype: str
        """
        return self._onboarded_status

    @onboarded_status.setter
    def onboarded_status(self, onboarded_status):
        """Sets the onboarded_status of this PayeeDeltaV4.

        Payee onboarded status. One of the following value: CREATED, INVITED, REGISTERED, ONBOARDED

        :param onboarded_status: The onboarded_status of this PayeeDeltaV4.
        :type onboarded_status: str
        """

        self._onboarded_status = onboarded_status

    @property
    def payee_country(self):
        """Gets the payee_country of this PayeeDeltaV4.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.

        :return: The payee_country of this PayeeDeltaV4.
        :rtype: str
        """
        return self._payee_country

    @payee_country.setter
    def payee_country(self, payee_country):
        """Sets the payee_country of this PayeeDeltaV4.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.

        :param payee_country: The payee_country of this PayeeDeltaV4.
        :type payee_country: str
        """
        if payee_country is not None and len(payee_country) > 2:
            raise ValueError("Invalid value for `payee_country`, length must be less than or equal to `2`")
        if payee_country is not None and len(payee_country) < 2:
            raise ValueError("Invalid value for `payee_country`, length must be greater than or equal to `2`")
        if payee_country is not None and not re.search(r'^[A-Z]{2}$', payee_country):
            raise ValueError("Invalid value for `payee_country`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")

        self._payee_country = payee_country

    @property
    def payee_id(self):
        """Gets the payee_id of this PayeeDeltaV4.


        :return: The payee_id of this PayeeDeltaV4.
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this PayeeDeltaV4.


        :param payee_id: The payee_id of this PayeeDeltaV4.
        :type payee_id: str
        """
        if payee_id is None:
            raise ValueError("Invalid value for `payee_id`, must not be `None`")

        self._payee_id = payee_id

    @property
    def remote_id(self):
        """Gets the remote_id of this PayeeDeltaV4.


        :return: The remote_id of this PayeeDeltaV4.
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this PayeeDeltaV4.


        :param remote_id: The remote_id of this PayeeDeltaV4.
        :type remote_id: str
        """
        if remote_id is None:
            raise ValueError("Invalid value for `remote_id`, must not be `None`")
        if remote_id is not None and len(remote_id) > 100:
            raise ValueError("Invalid value for `remote_id`, length must be less than or equal to `100`")
        if remote_id is not None and len(remote_id) < 1:
            raise ValueError("Invalid value for `remote_id`, length must be greater than or equal to `1`")

        self._remote_id = remote_id
