# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.wannabe_addon_provider_api_url import WannabeAddonProviderAPIUrl
from openapi_server import util


class WannabeAddonProviderAPI(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, config_vars: List[str]=None, password: str=None, production: WannabeAddonProviderAPIUrl=None, regions: List[str]=None, sso_salt: str=None, test: WannabeAddonProviderAPIUrl=None):
        """WannabeAddonProviderAPI - a model defined in OpenAPI

        :param config_vars: The config_vars of this WannabeAddonProviderAPI.
        :param password: The password of this WannabeAddonProviderAPI.
        :param production: The production of this WannabeAddonProviderAPI.
        :param regions: The regions of this WannabeAddonProviderAPI.
        :param sso_salt: The sso_salt of this WannabeAddonProviderAPI.
        :param test: The test of this WannabeAddonProviderAPI.
        """
        self.openapi_types = {
            'config_vars': List[str],
            'password': str,
            'production': WannabeAddonProviderAPIUrl,
            'regions': List[str],
            'sso_salt': str,
            'test': WannabeAddonProviderAPIUrl
        }

        self.attribute_map = {
            'config_vars': 'config_vars',
            'password': 'password',
            'production': 'production',
            'regions': 'regions',
            'sso_salt': 'sso_salt',
            'test': 'test'
        }

        self._config_vars = config_vars
        self._password = password
        self._production = production
        self._regions = regions
        self._sso_salt = sso_salt
        self._test = test

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WannabeAddonProviderAPI':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WannabeAddonProviderAPI of this WannabeAddonProviderAPI.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config_vars(self):
        """Gets the config_vars of this WannabeAddonProviderAPI.


        :return: The config_vars of this WannabeAddonProviderAPI.
        :rtype: List[str]
        """
        return self._config_vars

    @config_vars.setter
    def config_vars(self, config_vars):
        """Sets the config_vars of this WannabeAddonProviderAPI.


        :param config_vars: The config_vars of this WannabeAddonProviderAPI.
        :type config_vars: List[str]
        """
        if config_vars is None:
            raise ValueError("Invalid value for `config_vars`, must not be `None`")

        self._config_vars = config_vars

    @property
    def password(self):
        """Gets the password of this WannabeAddonProviderAPI.


        :return: The password of this WannabeAddonProviderAPI.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WannabeAddonProviderAPI.


        :param password: The password of this WannabeAddonProviderAPI.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")

        self._password = password

    @property
    def production(self):
        """Gets the production of this WannabeAddonProviderAPI.


        :return: The production of this WannabeAddonProviderAPI.
        :rtype: WannabeAddonProviderAPIUrl
        """
        return self._production

    @production.setter
    def production(self, production):
        """Sets the production of this WannabeAddonProviderAPI.


        :param production: The production of this WannabeAddonProviderAPI.
        :type production: WannabeAddonProviderAPIUrl
        """

        self._production = production

    @property
    def regions(self):
        """Gets the regions of this WannabeAddonProviderAPI.


        :return: The regions of this WannabeAddonProviderAPI.
        :rtype: List[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this WannabeAddonProviderAPI.


        :param regions: The regions of this WannabeAddonProviderAPI.
        :type regions: List[str]
        """

        self._regions = regions

    @property
    def sso_salt(self):
        """Gets the sso_salt of this WannabeAddonProviderAPI.


        :return: The sso_salt of this WannabeAddonProviderAPI.
        :rtype: str
        """
        return self._sso_salt

    @sso_salt.setter
    def sso_salt(self, sso_salt):
        """Sets the sso_salt of this WannabeAddonProviderAPI.


        :param sso_salt: The sso_salt of this WannabeAddonProviderAPI.
        :type sso_salt: str
        """
        if sso_salt is None:
            raise ValueError("Invalid value for `sso_salt`, must not be `None`")

        self._sso_salt = sso_salt

    @property
    def test(self):
        """Gets the test of this WannabeAddonProviderAPI.


        :return: The test of this WannabeAddonProviderAPI.
        :rtype: WannabeAddonProviderAPIUrl
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this WannabeAddonProviderAPI.


        :param test: The test of this WannabeAddonProviderAPI.
        :type test: WannabeAddonProviderAPIUrl
        """

        self._test = test
