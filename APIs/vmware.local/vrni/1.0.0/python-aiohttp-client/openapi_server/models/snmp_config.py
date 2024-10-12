# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.snmp2c_config import SNMP2cConfig
from openapi_server.models.snmp3_config import SNMP3Config
from openapi_server import util


class SNMPConfig(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, config_snmp_2c: SNMP2cConfig=None, config_snmp_3: SNMP3Config=None, snmp_enabled: bool=False, snmp_version: str=None):
        """SNMPConfig - a model defined in OpenAPI

        :param config_snmp_2c: The config_snmp_2c of this SNMPConfig.
        :param config_snmp_3: The config_snmp_3 of this SNMPConfig.
        :param snmp_enabled: The snmp_enabled of this SNMPConfig.
        :param snmp_version: The snmp_version of this SNMPConfig.
        """
        self.openapi_types = {
            'config_snmp_2c': SNMP2cConfig,
            'config_snmp_3': SNMP3Config,
            'snmp_enabled': bool,
            'snmp_version': str
        }

        self.attribute_map = {
            'config_snmp_2c': 'config_snmp_2c',
            'config_snmp_3': 'config_snmp_3',
            'snmp_enabled': 'snmp_enabled',
            'snmp_version': 'snmp_version'
        }

        self._config_snmp_2c = config_snmp_2c
        self._config_snmp_3 = config_snmp_3
        self._snmp_enabled = snmp_enabled
        self._snmp_version = snmp_version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SNMPConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SNMPConfig of this SNMPConfig.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config_snmp_2c(self):
        """Gets the config_snmp_2c of this SNMPConfig.


        :return: The config_snmp_2c of this SNMPConfig.
        :rtype: SNMP2cConfig
        """
        return self._config_snmp_2c

    @config_snmp_2c.setter
    def config_snmp_2c(self, config_snmp_2c):
        """Sets the config_snmp_2c of this SNMPConfig.


        :param config_snmp_2c: The config_snmp_2c of this SNMPConfig.
        :type config_snmp_2c: SNMP2cConfig
        """

        self._config_snmp_2c = config_snmp_2c

    @property
    def config_snmp_3(self):
        """Gets the config_snmp_3 of this SNMPConfig.


        :return: The config_snmp_3 of this SNMPConfig.
        :rtype: SNMP3Config
        """
        return self._config_snmp_3

    @config_snmp_3.setter
    def config_snmp_3(self, config_snmp_3):
        """Sets the config_snmp_3 of this SNMPConfig.


        :param config_snmp_3: The config_snmp_3 of this SNMPConfig.
        :type config_snmp_3: SNMP3Config
        """

        self._config_snmp_3 = config_snmp_3

    @property
    def snmp_enabled(self):
        """Gets the snmp_enabled of this SNMPConfig.


        :return: The snmp_enabled of this SNMPConfig.
        :rtype: bool
        """
        return self._snmp_enabled

    @snmp_enabled.setter
    def snmp_enabled(self, snmp_enabled):
        """Sets the snmp_enabled of this SNMPConfig.


        :param snmp_enabled: The snmp_enabled of this SNMPConfig.
        :type snmp_enabled: bool
        """

        self._snmp_enabled = snmp_enabled

    @property
    def snmp_version(self):
        """Gets the snmp_version of this SNMPConfig.


        :return: The snmp_version of this SNMPConfig.
        :rtype: str
        """
        return self._snmp_version

    @snmp_version.setter
    def snmp_version(self, snmp_version):
        """Sets the snmp_version of this SNMPConfig.


        :param snmp_version: The snmp_version of this SNMPConfig.
        :type snmp_version: str
        """
        allowed_values = ["v2c", "v3"]  # noqa: E501
        if snmp_version not in allowed_values:
            raise ValueError(
                "Invalid value for `snmp_version` ({0}), must be one of {1}"
                .format(snmp_version, allowed_values)
            )

        self._snmp_version = snmp_version
