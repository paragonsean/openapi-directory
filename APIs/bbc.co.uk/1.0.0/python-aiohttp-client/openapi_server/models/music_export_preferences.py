# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MusicExportPreferences(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_expires_at: str=None, access_token: str=None, add_plus_export: bool=None, authorization_code: str=None, last_export: str=None, legacy_state: str=None, partner_id: str=None, refresh_token: str=None, terms: bool=None, vendor: str=None):
        """MusicExportPreferences - a model defined in OpenAPI

        :param access_expires_at: The access_expires_at of this MusicExportPreferences.
        :param access_token: The access_token of this MusicExportPreferences.
        :param add_plus_export: The add_plus_export of this MusicExportPreferences.
        :param authorization_code: The authorization_code of this MusicExportPreferences.
        :param last_export: The last_export of this MusicExportPreferences.
        :param legacy_state: The legacy_state of this MusicExportPreferences.
        :param partner_id: The partner_id of this MusicExportPreferences.
        :param refresh_token: The refresh_token of this MusicExportPreferences.
        :param terms: The terms of this MusicExportPreferences.
        :param vendor: The vendor of this MusicExportPreferences.
        """
        self.openapi_types = {
            'access_expires_at': str,
            'access_token': str,
            'add_plus_export': bool,
            'authorization_code': str,
            'last_export': str,
            'legacy_state': str,
            'partner_id': str,
            'refresh_token': str,
            'terms': bool,
            'vendor': str
        }

        self.attribute_map = {
            'access_expires_at': 'access_expires_at',
            'access_token': 'access_token',
            'add_plus_export': 'add_plus_export',
            'authorization_code': 'authorization_code',
            'last_export': 'last_export',
            'legacy_state': 'legacy_state',
            'partner_id': 'partner_id',
            'refresh_token': 'refresh_token',
            'terms': 'terms',
            'vendor': 'vendor'
        }

        self._access_expires_at = access_expires_at
        self._access_token = access_token
        self._add_plus_export = add_plus_export
        self._authorization_code = authorization_code
        self._last_export = last_export
        self._legacy_state = legacy_state
        self._partner_id = partner_id
        self._refresh_token = refresh_token
        self._terms = terms
        self._vendor = vendor

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MusicExportPreferences':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MusicExportPreferences of this MusicExportPreferences.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_expires_at(self):
        """Gets the access_expires_at of this MusicExportPreferences.


        :return: The access_expires_at of this MusicExportPreferences.
        :rtype: str
        """
        return self._access_expires_at

    @access_expires_at.setter
    def access_expires_at(self, access_expires_at):
        """Sets the access_expires_at of this MusicExportPreferences.


        :param access_expires_at: The access_expires_at of this MusicExportPreferences.
        :type access_expires_at: str
        """
        if access_expires_at is None:
            raise ValueError("Invalid value for `access_expires_at`, must not be `None`")

        self._access_expires_at = access_expires_at

    @property
    def access_token(self):
        """Gets the access_token of this MusicExportPreferences.


        :return: The access_token of this MusicExportPreferences.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this MusicExportPreferences.


        :param access_token: The access_token of this MusicExportPreferences.
        :type access_token: str
        """
        if access_token is None:
            raise ValueError("Invalid value for `access_token`, must not be `None`")

        self._access_token = access_token

    @property
    def add_plus_export(self):
        """Gets the add_plus_export of this MusicExportPreferences.


        :return: The add_plus_export of this MusicExportPreferences.
        :rtype: bool
        """
        return self._add_plus_export

    @add_plus_export.setter
    def add_plus_export(self, add_plus_export):
        """Sets the add_plus_export of this MusicExportPreferences.


        :param add_plus_export: The add_plus_export of this MusicExportPreferences.
        :type add_plus_export: bool
        """
        if add_plus_export is None:
            raise ValueError("Invalid value for `add_plus_export`, must not be `None`")

        self._add_plus_export = add_plus_export

    @property
    def authorization_code(self):
        """Gets the authorization_code of this MusicExportPreferences.


        :return: The authorization_code of this MusicExportPreferences.
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this MusicExportPreferences.


        :param authorization_code: The authorization_code of this MusicExportPreferences.
        :type authorization_code: str
        """
        if authorization_code is None:
            raise ValueError("Invalid value for `authorization_code`, must not be `None`")

        self._authorization_code = authorization_code

    @property
    def last_export(self):
        """Gets the last_export of this MusicExportPreferences.


        :return: The last_export of this MusicExportPreferences.
        :rtype: str
        """
        return self._last_export

    @last_export.setter
    def last_export(self, last_export):
        """Sets the last_export of this MusicExportPreferences.


        :param last_export: The last_export of this MusicExportPreferences.
        :type last_export: str
        """
        if last_export is None:
            raise ValueError("Invalid value for `last_export`, must not be `None`")

        self._last_export = last_export

    @property
    def legacy_state(self):
        """Gets the legacy_state of this MusicExportPreferences.


        :return: The legacy_state of this MusicExportPreferences.
        :rtype: str
        """
        return self._legacy_state

    @legacy_state.setter
    def legacy_state(self, legacy_state):
        """Sets the legacy_state of this MusicExportPreferences.


        :param legacy_state: The legacy_state of this MusicExportPreferences.
        :type legacy_state: str
        """
        if legacy_state is None:
            raise ValueError("Invalid value for `legacy_state`, must not be `None`")

        self._legacy_state = legacy_state

    @property
    def partner_id(self):
        """Gets the partner_id of this MusicExportPreferences.


        :return: The partner_id of this MusicExportPreferences.
        :rtype: str
        """
        return self._partner_id

    @partner_id.setter
    def partner_id(self, partner_id):
        """Sets the partner_id of this MusicExportPreferences.


        :param partner_id: The partner_id of this MusicExportPreferences.
        :type partner_id: str
        """
        if partner_id is None:
            raise ValueError("Invalid value for `partner_id`, must not be `None`")

        self._partner_id = partner_id

    @property
    def refresh_token(self):
        """Gets the refresh_token of this MusicExportPreferences.


        :return: The refresh_token of this MusicExportPreferences.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this MusicExportPreferences.


        :param refresh_token: The refresh_token of this MusicExportPreferences.
        :type refresh_token: str
        """
        if refresh_token is None:
            raise ValueError("Invalid value for `refresh_token`, must not be `None`")

        self._refresh_token = refresh_token

    @property
    def terms(self):
        """Gets the terms of this MusicExportPreferences.


        :return: The terms of this MusicExportPreferences.
        :rtype: bool
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this MusicExportPreferences.


        :param terms: The terms of this MusicExportPreferences.
        :type terms: bool
        """
        if terms is None:
            raise ValueError("Invalid value for `terms`, must not be `None`")

        self._terms = terms

    @property
    def vendor(self):
        """Gets the vendor of this MusicExportPreferences.


        :return: The vendor of this MusicExportPreferences.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this MusicExportPreferences.


        :param vendor: The vendor of this MusicExportPreferences.
        :type vendor: str
        """
        if vendor is None:
            raise ValueError("Invalid value for `vendor`, must not be `None`")

        self._vendor = vendor
