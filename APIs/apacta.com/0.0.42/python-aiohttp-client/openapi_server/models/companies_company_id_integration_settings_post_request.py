# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CompaniesCompanyIdIntegrationSettingsPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, integration_setting_id: str=None, value: str=None):
        """CompaniesCompanyIdIntegrationSettingsPostRequest - a model defined in OpenAPI

        :param integration_setting_id: The integration_setting_id of this CompaniesCompanyIdIntegrationSettingsPostRequest.
        :param value: The value of this CompaniesCompanyIdIntegrationSettingsPostRequest.
        """
        self.openapi_types = {
            'integration_setting_id': str,
            'value': str
        }

        self.attribute_map = {
            'integration_setting_id': 'integration_setting_id',
            'value': 'value'
        }

        self._integration_setting_id = integration_setting_id
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CompaniesCompanyIdIntegrationSettingsPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _companies__company_id__integration_settings_post_request of this CompaniesCompanyIdIntegrationSettingsPostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def integration_setting_id(self):
        """Gets the integration_setting_id of this CompaniesCompanyIdIntegrationSettingsPostRequest.


        :return: The integration_setting_id of this CompaniesCompanyIdIntegrationSettingsPostRequest.
        :rtype: str
        """
        return self._integration_setting_id

    @integration_setting_id.setter
    def integration_setting_id(self, integration_setting_id):
        """Sets the integration_setting_id of this CompaniesCompanyIdIntegrationSettingsPostRequest.


        :param integration_setting_id: The integration_setting_id of this CompaniesCompanyIdIntegrationSettingsPostRequest.
        :type integration_setting_id: str
        """

        self._integration_setting_id = integration_setting_id

    @property
    def value(self):
        """Gets the value of this CompaniesCompanyIdIntegrationSettingsPostRequest.


        :return: The value of this CompaniesCompanyIdIntegrationSettingsPostRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CompaniesCompanyIdIntegrationSettingsPostRequest.


        :param value: The value of this CompaniesCompanyIdIntegrationSettingsPostRequest.
        :type value: str
        """

        self._value = value
