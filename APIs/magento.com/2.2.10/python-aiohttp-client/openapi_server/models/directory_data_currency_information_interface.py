# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.directory_data_exchange_rate_interface import DirectoryDataExchangeRateInterface
from openapi_server import util


class DirectoryDataCurrencyInformationInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, available_currency_codes: List[str]=None, base_currency_code: str=None, base_currency_symbol: str=None, default_display_currency_code: str=None, default_display_currency_symbol: str=None, exchange_rates: List[DirectoryDataExchangeRateInterface]=None, extension_attributes: object=None):
        """DirectoryDataCurrencyInformationInterface - a model defined in OpenAPI

        :param available_currency_codes: The available_currency_codes of this DirectoryDataCurrencyInformationInterface.
        :param base_currency_code: The base_currency_code of this DirectoryDataCurrencyInformationInterface.
        :param base_currency_symbol: The base_currency_symbol of this DirectoryDataCurrencyInformationInterface.
        :param default_display_currency_code: The default_display_currency_code of this DirectoryDataCurrencyInformationInterface.
        :param default_display_currency_symbol: The default_display_currency_symbol of this DirectoryDataCurrencyInformationInterface.
        :param exchange_rates: The exchange_rates of this DirectoryDataCurrencyInformationInterface.
        :param extension_attributes: The extension_attributes of this DirectoryDataCurrencyInformationInterface.
        """
        self.openapi_types = {
            'available_currency_codes': List[str],
            'base_currency_code': str,
            'base_currency_symbol': str,
            'default_display_currency_code': str,
            'default_display_currency_symbol': str,
            'exchange_rates': List[DirectoryDataExchangeRateInterface],
            'extension_attributes': object
        }

        self.attribute_map = {
            'available_currency_codes': 'available_currency_codes',
            'base_currency_code': 'base_currency_code',
            'base_currency_symbol': 'base_currency_symbol',
            'default_display_currency_code': 'default_display_currency_code',
            'default_display_currency_symbol': 'default_display_currency_symbol',
            'exchange_rates': 'exchange_rates',
            'extension_attributes': 'extension_attributes'
        }

        self._available_currency_codes = available_currency_codes
        self._base_currency_code = base_currency_code
        self._base_currency_symbol = base_currency_symbol
        self._default_display_currency_code = default_display_currency_code
        self._default_display_currency_symbol = default_display_currency_symbol
        self._exchange_rates = exchange_rates
        self._extension_attributes = extension_attributes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DirectoryDataCurrencyInformationInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The directory-data-currency-information-interface of this DirectoryDataCurrencyInformationInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def available_currency_codes(self):
        """Gets the available_currency_codes of this DirectoryDataCurrencyInformationInterface.

        The list of allowed currency codes for the store.

        :return: The available_currency_codes of this DirectoryDataCurrencyInformationInterface.
        :rtype: List[str]
        """
        return self._available_currency_codes

    @available_currency_codes.setter
    def available_currency_codes(self, available_currency_codes):
        """Sets the available_currency_codes of this DirectoryDataCurrencyInformationInterface.

        The list of allowed currency codes for the store.

        :param available_currency_codes: The available_currency_codes of this DirectoryDataCurrencyInformationInterface.
        :type available_currency_codes: List[str]
        """
        if available_currency_codes is None:
            raise ValueError("Invalid value for `available_currency_codes`, must not be `None`")

        self._available_currency_codes = available_currency_codes

    @property
    def base_currency_code(self):
        """Gets the base_currency_code of this DirectoryDataCurrencyInformationInterface.

        The base currency code for the store.

        :return: The base_currency_code of this DirectoryDataCurrencyInformationInterface.
        :rtype: str
        """
        return self._base_currency_code

    @base_currency_code.setter
    def base_currency_code(self, base_currency_code):
        """Sets the base_currency_code of this DirectoryDataCurrencyInformationInterface.

        The base currency code for the store.

        :param base_currency_code: The base_currency_code of this DirectoryDataCurrencyInformationInterface.
        :type base_currency_code: str
        """
        if base_currency_code is None:
            raise ValueError("Invalid value for `base_currency_code`, must not be `None`")

        self._base_currency_code = base_currency_code

    @property
    def base_currency_symbol(self):
        """Gets the base_currency_symbol of this DirectoryDataCurrencyInformationInterface.

        The currency symbol of the base currency for the store.

        :return: The base_currency_symbol of this DirectoryDataCurrencyInformationInterface.
        :rtype: str
        """
        return self._base_currency_symbol

    @base_currency_symbol.setter
    def base_currency_symbol(self, base_currency_symbol):
        """Sets the base_currency_symbol of this DirectoryDataCurrencyInformationInterface.

        The currency symbol of the base currency for the store.

        :param base_currency_symbol: The base_currency_symbol of this DirectoryDataCurrencyInformationInterface.
        :type base_currency_symbol: str
        """
        if base_currency_symbol is None:
            raise ValueError("Invalid value for `base_currency_symbol`, must not be `None`")

        self._base_currency_symbol = base_currency_symbol

    @property
    def default_display_currency_code(self):
        """Gets the default_display_currency_code of this DirectoryDataCurrencyInformationInterface.

        The default display currency code for the store.

        :return: The default_display_currency_code of this DirectoryDataCurrencyInformationInterface.
        :rtype: str
        """
        return self._default_display_currency_code

    @default_display_currency_code.setter
    def default_display_currency_code(self, default_display_currency_code):
        """Sets the default_display_currency_code of this DirectoryDataCurrencyInformationInterface.

        The default display currency code for the store.

        :param default_display_currency_code: The default_display_currency_code of this DirectoryDataCurrencyInformationInterface.
        :type default_display_currency_code: str
        """
        if default_display_currency_code is None:
            raise ValueError("Invalid value for `default_display_currency_code`, must not be `None`")

        self._default_display_currency_code = default_display_currency_code

    @property
    def default_display_currency_symbol(self):
        """Gets the default_display_currency_symbol of this DirectoryDataCurrencyInformationInterface.

        The currency symbol of the default display currency for the store.

        :return: The default_display_currency_symbol of this DirectoryDataCurrencyInformationInterface.
        :rtype: str
        """
        return self._default_display_currency_symbol

    @default_display_currency_symbol.setter
    def default_display_currency_symbol(self, default_display_currency_symbol):
        """Sets the default_display_currency_symbol of this DirectoryDataCurrencyInformationInterface.

        The currency symbol of the default display currency for the store.

        :param default_display_currency_symbol: The default_display_currency_symbol of this DirectoryDataCurrencyInformationInterface.
        :type default_display_currency_symbol: str
        """
        if default_display_currency_symbol is None:
            raise ValueError("Invalid value for `default_display_currency_symbol`, must not be `None`")

        self._default_display_currency_symbol = default_display_currency_symbol

    @property
    def exchange_rates(self):
        """Gets the exchange_rates of this DirectoryDataCurrencyInformationInterface.

        The list of exchange rate information for the store.

        :return: The exchange_rates of this DirectoryDataCurrencyInformationInterface.
        :rtype: List[DirectoryDataExchangeRateInterface]
        """
        return self._exchange_rates

    @exchange_rates.setter
    def exchange_rates(self, exchange_rates):
        """Sets the exchange_rates of this DirectoryDataCurrencyInformationInterface.

        The list of exchange rate information for the store.

        :param exchange_rates: The exchange_rates of this DirectoryDataCurrencyInformationInterface.
        :type exchange_rates: List[DirectoryDataExchangeRateInterface]
        """
        if exchange_rates is None:
            raise ValueError("Invalid value for `exchange_rates`, must not be `None`")

        self._exchange_rates = exchange_rates

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this DirectoryDataCurrencyInformationInterface.

        ExtensionInterface class for @see \\Magento\\Directory\\Api\\Data\\CurrencyInformationInterface

        :return: The extension_attributes of this DirectoryDataCurrencyInformationInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this DirectoryDataCurrencyInformationInterface.

        ExtensionInterface class for @see \\Magento\\Directory\\Api\\Data\\CurrencyInformationInterface

        :param extension_attributes: The extension_attributes of this DirectoryDataCurrencyInformationInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes
