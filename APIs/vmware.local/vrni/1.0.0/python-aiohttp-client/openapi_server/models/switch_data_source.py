# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.base_data_source import BaseDataSource
from openapi_server.models.data_source_type import DataSourceType
from openapi_server.models.password_credentials import PasswordCredentials
from openapi_server import util


class SwitchDataSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=True, entity_id: str=None, entity_type: DataSourceType=None, fqdn: str=None, ip: str=None, nickname: str=None, notes: str=None, proxy_id: str=None, credentials: PasswordCredentials=None):
        """SwitchDataSource - a model defined in OpenAPI

        :param enabled: The enabled of this SwitchDataSource.
        :param entity_id: The entity_id of this SwitchDataSource.
        :param entity_type: The entity_type of this SwitchDataSource.
        :param fqdn: The fqdn of this SwitchDataSource.
        :param ip: The ip of this SwitchDataSource.
        :param nickname: The nickname of this SwitchDataSource.
        :param notes: The notes of this SwitchDataSource.
        :param proxy_id: The proxy_id of this SwitchDataSource.
        :param credentials: The credentials of this SwitchDataSource.
        """
        self.openapi_types = {
            'enabled': bool,
            'entity_id': str,
            'entity_type': DataSourceType,
            'fqdn': str,
            'ip': str,
            'nickname': str,
            'notes': str,
            'proxy_id': str,
            'credentials': PasswordCredentials
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'entity_id': 'entity_id',
            'entity_type': 'entity_type',
            'fqdn': 'fqdn',
            'ip': 'ip',
            'nickname': 'nickname',
            'notes': 'notes',
            'proxy_id': 'proxy_id',
            'credentials': 'credentials'
        }

        self._enabled = enabled
        self._entity_id = entity_id
        self._entity_type = entity_type
        self._fqdn = fqdn
        self._ip = ip
        self._nickname = nickname
        self._notes = notes
        self._proxy_id = proxy_id
        self._credentials = credentials

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SwitchDataSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SwitchDataSource of this SwitchDataSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self):
        """Gets the enabled of this SwitchDataSource.


        :return: The enabled of this SwitchDataSource.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SwitchDataSource.


        :param enabled: The enabled of this SwitchDataSource.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def entity_id(self):
        """Gets the entity_id of this SwitchDataSource.


        :return: The entity_id of this SwitchDataSource.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this SwitchDataSource.


        :param entity_id: The entity_id of this SwitchDataSource.
        :type entity_id: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this SwitchDataSource.


        :return: The entity_type of this SwitchDataSource.
        :rtype: DataSourceType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this SwitchDataSource.


        :param entity_type: The entity_type of this SwitchDataSource.
        :type entity_type: DataSourceType
        """

        self._entity_type = entity_type

    @property
    def fqdn(self):
        """Gets the fqdn of this SwitchDataSource.


        :return: The fqdn of this SwitchDataSource.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this SwitchDataSource.


        :param fqdn: The fqdn of this SwitchDataSource.
        :type fqdn: str
        """

        self._fqdn = fqdn

    @property
    def ip(self):
        """Gets the ip of this SwitchDataSource.


        :return: The ip of this SwitchDataSource.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SwitchDataSource.


        :param ip: The ip of this SwitchDataSource.
        :type ip: str
        """

        self._ip = ip

    @property
    def nickname(self):
        """Gets the nickname of this SwitchDataSource.


        :return: The nickname of this SwitchDataSource.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this SwitchDataSource.


        :param nickname: The nickname of this SwitchDataSource.
        :type nickname: str
        """

        self._nickname = nickname

    @property
    def notes(self):
        """Gets the notes of this SwitchDataSource.


        :return: The notes of this SwitchDataSource.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this SwitchDataSource.


        :param notes: The notes of this SwitchDataSource.
        :type notes: str
        """

        self._notes = notes

    @property
    def proxy_id(self):
        """Gets the proxy_id of this SwitchDataSource.

        proxy vm which should register this vcenter

        :return: The proxy_id of this SwitchDataSource.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """Sets the proxy_id of this SwitchDataSource.

        proxy vm which should register this vcenter

        :param proxy_id: The proxy_id of this SwitchDataSource.
        :type proxy_id: str
        """

        self._proxy_id = proxy_id

    @property
    def credentials(self):
        """Gets the credentials of this SwitchDataSource.


        :return: The credentials of this SwitchDataSource.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this SwitchDataSource.


        :param credentials: The credentials of this SwitchDataSource.
        :type credentials: PasswordCredentials
        """

        self._credentials = credentials
