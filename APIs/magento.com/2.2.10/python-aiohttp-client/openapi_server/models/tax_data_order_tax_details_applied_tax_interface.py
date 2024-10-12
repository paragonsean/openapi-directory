# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tax_data_order_tax_details_applied_tax_extension_interface import TaxDataOrderTaxDetailsAppliedTaxExtensionInterface
from openapi_server import util


class TaxDataOrderTaxDetailsAppliedTaxInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount: float=None, base_amount: float=None, code: str=None, extension_attributes: TaxDataOrderTaxDetailsAppliedTaxExtensionInterface=None, percent: float=None, title: str=None):
        """TaxDataOrderTaxDetailsAppliedTaxInterface - a model defined in OpenAPI

        :param amount: The amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :param base_amount: The base_amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :param code: The code of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :param extension_attributes: The extension_attributes of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :param percent: The percent of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :param title: The title of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        """
        self.openapi_types = {
            'amount': float,
            'base_amount': float,
            'code': str,
            'extension_attributes': TaxDataOrderTaxDetailsAppliedTaxExtensionInterface,
            'percent': float,
            'title': str
        }

        self.attribute_map = {
            'amount': 'amount',
            'base_amount': 'base_amount',
            'code': 'code',
            'extension_attributes': 'extension_attributes',
            'percent': 'percent',
            'title': 'title'
        }

        self._amount = amount
        self._base_amount = base_amount
        self._code = code
        self._extension_attributes = extension_attributes
        self._percent = percent
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaxDataOrderTaxDetailsAppliedTaxInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tax-data-order-tax-details-applied-tax-interface of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self):
        """Gets the amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Tax amount

        :return: The amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Tax amount

        :param amount: The amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :type amount: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")

        self._amount = amount

    @property
    def base_amount(self):
        """Gets the base_amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Tax amount in base currency

        :return: The base_amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :rtype: float
        """
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount):
        """Sets the base_amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Tax amount in base currency

        :param base_amount: The base_amount of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :type base_amount: float
        """
        if base_amount is None:
            raise ValueError("Invalid value for `base_amount`, must not be `None`")

        self._base_amount = base_amount

    @property
    def code(self):
        """Gets the code of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Code

        :return: The code of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Code

        :param code: The code of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :type code: str
        """

        self._code = code

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this TaxDataOrderTaxDetailsAppliedTaxInterface.


        :return: The extension_attributes of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :rtype: TaxDataOrderTaxDetailsAppliedTaxExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this TaxDataOrderTaxDetailsAppliedTaxInterface.


        :param extension_attributes: The extension_attributes of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :type extension_attributes: TaxDataOrderTaxDetailsAppliedTaxExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def percent(self):
        """Gets the percent of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Tax Percent

        :return: The percent of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Tax Percent

        :param percent: The percent of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :type percent: float
        """

        self._percent = percent

    @property
    def title(self):
        """Gets the title of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Title

        :return: The title of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaxDataOrderTaxDetailsAppliedTaxInterface.

        Title

        :param title: The title of this TaxDataOrderTaxDetailsAppliedTaxInterface.
        :type title: str
        """

        self._title = title
