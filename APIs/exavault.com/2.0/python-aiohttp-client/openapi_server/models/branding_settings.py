# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BrandingSettings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, company_name: str=None, custom_email: str=None, logo: str=None, logo_ext: str=None, theme: str=None, verified_domain: str=None, verified_domain_id: str=None, verified_domain_valid: bool=None):
        """BrandingSettings - a model defined in OpenAPI

        :param company_name: The company_name of this BrandingSettings.
        :param custom_email: The custom_email of this BrandingSettings.
        :param logo: The logo of this BrandingSettings.
        :param logo_ext: The logo_ext of this BrandingSettings.
        :param theme: The theme of this BrandingSettings.
        :param verified_domain: The verified_domain of this BrandingSettings.
        :param verified_domain_id: The verified_domain_id of this BrandingSettings.
        :param verified_domain_valid: The verified_domain_valid of this BrandingSettings.
        """
        self.openapi_types = {
            'company_name': str,
            'custom_email': str,
            'logo': str,
            'logo_ext': str,
            'theme': str,
            'verified_domain': str,
            'verified_domain_id': str,
            'verified_domain_valid': bool
        }

        self.attribute_map = {
            'company_name': 'companyName',
            'custom_email': 'customEmail',
            'logo': 'logo',
            'logo_ext': 'logoExt',
            'theme': 'theme',
            'verified_domain': 'verifiedDomain',
            'verified_domain_id': 'verifiedDomainId',
            'verified_domain_valid': 'verifiedDomainValid'
        }

        self._company_name = company_name
        self._custom_email = custom_email
        self._logo = logo
        self._logo_ext = logo_ext
        self._theme = theme
        self._verified_domain = verified_domain
        self._verified_domain_id = verified_domain_id
        self._verified_domain_valid = verified_domain_valid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BrandingSettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BrandingSettings of this BrandingSettings.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def company_name(self):
        """Gets the company_name of this BrandingSettings.


        :return: The company_name of this BrandingSettings.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this BrandingSettings.


        :param company_name: The company_name of this BrandingSettings.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def custom_email(self):
        """Gets the custom_email of this BrandingSettings.


        :return: The custom_email of this BrandingSettings.
        :rtype: str
        """
        return self._custom_email

    @custom_email.setter
    def custom_email(self, custom_email):
        """Sets the custom_email of this BrandingSettings.


        :param custom_email: The custom_email of this BrandingSettings.
        :type custom_email: str
        """

        self._custom_email = custom_email

    @property
    def logo(self):
        """Gets the logo of this BrandingSettings.


        :return: The logo of this BrandingSettings.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this BrandingSettings.


        :param logo: The logo of this BrandingSettings.
        :type logo: str
        """

        self._logo = logo

    @property
    def logo_ext(self):
        """Gets the logo_ext of this BrandingSettings.


        :return: The logo_ext of this BrandingSettings.
        :rtype: str
        """
        return self._logo_ext

    @logo_ext.setter
    def logo_ext(self, logo_ext):
        """Sets the logo_ext of this BrandingSettings.


        :param logo_ext: The logo_ext of this BrandingSettings.
        :type logo_ext: str
        """

        self._logo_ext = logo_ext

    @property
    def theme(self):
        """Gets the theme of this BrandingSettings.


        :return: The theme of this BrandingSettings.
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this BrandingSettings.


        :param theme: The theme of this BrandingSettings.
        :type theme: str
        """

        self._theme = theme

    @property
    def verified_domain(self):
        """Gets the verified_domain of this BrandingSettings.


        :return: The verified_domain of this BrandingSettings.
        :rtype: str
        """
        return self._verified_domain

    @verified_domain.setter
    def verified_domain(self, verified_domain):
        """Sets the verified_domain of this BrandingSettings.


        :param verified_domain: The verified_domain of this BrandingSettings.
        :type verified_domain: str
        """

        self._verified_domain = verified_domain

    @property
    def verified_domain_id(self):
        """Gets the verified_domain_id of this BrandingSettings.


        :return: The verified_domain_id of this BrandingSettings.
        :rtype: str
        """
        return self._verified_domain_id

    @verified_domain_id.setter
    def verified_domain_id(self, verified_domain_id):
        """Sets the verified_domain_id of this BrandingSettings.


        :param verified_domain_id: The verified_domain_id of this BrandingSettings.
        :type verified_domain_id: str
        """

        self._verified_domain_id = verified_domain_id

    @property
    def verified_domain_valid(self):
        """Gets the verified_domain_valid of this BrandingSettings.


        :return: The verified_domain_valid of this BrandingSettings.
        :rtype: bool
        """
        return self._verified_domain_valid

    @verified_domain_valid.setter
    def verified_domain_valid(self, verified_domain_valid):
        """Sets the verified_domain_valid of this BrandingSettings.


        :param verified_domain_valid: The verified_domain_valid of this BrandingSettings.
        :type verified_domain_valid: bool
        """

        self._verified_domain_valid = verified_domain_valid
