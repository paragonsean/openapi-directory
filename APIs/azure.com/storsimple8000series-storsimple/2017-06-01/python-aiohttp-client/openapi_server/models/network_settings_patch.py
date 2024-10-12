# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.network_settings_patch_properties import NetworkSettingsPatchProperties
from openapi_server import util


class NetworkSettingsPatch(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: NetworkSettingsPatchProperties=None):
        """NetworkSettingsPatch - a model defined in OpenAPI

        :param properties: The properties of this NetworkSettingsPatch.
        """
        self.openapi_types = {
            'properties': NetworkSettingsPatchProperties
        }

        self.attribute_map = {
            'properties': 'properties'
        }

        self._properties = properties

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NetworkSettingsPatch':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The NetworkSettingsPatch of this NetworkSettingsPatch.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this NetworkSettingsPatch.


        :return: The properties of this NetworkSettingsPatch.
        :rtype: NetworkSettingsPatchProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this NetworkSettingsPatch.


        :param properties: The properties of this NetworkSettingsPatch.
        :type properties: NetworkSettingsPatchProperties
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties
