# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.payment_channel_rule import PaymentChannelRule
from openapi_server import util


class PaymentChannelCountry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, iso_country_code: str=None, rules: List[PaymentChannelRule]=None):
        """PaymentChannelCountry - a model defined in OpenAPI

        :param iso_country_code: The iso_country_code of this PaymentChannelCountry.
        :param rules: The rules of this PaymentChannelCountry.
        """
        self.openapi_types = {
            'iso_country_code': str,
            'rules': List[PaymentChannelRule]
        }

        self.attribute_map = {
            'iso_country_code': 'isoCountryCode',
            'rules': 'rules'
        }

        self._iso_country_code = iso_country_code
        self._rules = rules

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PaymentChannelCountry':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PaymentChannelCountry of this PaymentChannelCountry.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def iso_country_code(self):
        """Gets the iso_country_code of this PaymentChannelCountry.

        The ISO code for the country

        :return: The iso_country_code of this PaymentChannelCountry.
        :rtype: str
        """
        return self._iso_country_code

    @iso_country_code.setter
    def iso_country_code(self, iso_country_code):
        """Sets the iso_country_code of this PaymentChannelCountry.

        The ISO code for the country

        :param iso_country_code: The iso_country_code of this PaymentChannelCountry.
        :type iso_country_code: str
        """
        if iso_country_code is None:
            raise ValueError("Invalid value for `iso_country_code`, must not be `None`")

        self._iso_country_code = iso_country_code

    @property
    def rules(self):
        """Gets the rules of this PaymentChannelCountry.

        The rules for the given country

        :return: The rules of this PaymentChannelCountry.
        :rtype: List[PaymentChannelRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this PaymentChannelCountry.

        The rules for the given country

        :param rules: The rules of this PaymentChannelCountry.
        :type rules: List[PaymentChannelRule]
        """
        if rules is None:
            raise ValueError("Invalid value for `rules`, must not be `None`")

        self._rules = rules
