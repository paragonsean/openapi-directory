# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.framework_attribute_interface import FrameworkAttributeInterface
from openapi_server.models.quote_data_address_interface import QuoteDataAddressInterface
from openapi_server import util


class CheckoutDataTotalsInformationInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: QuoteDataAddressInterface=None, custom_attributes: List[FrameworkAttributeInterface]=None, extension_attributes: object=None, shipping_carrier_code: str=None, shipping_method_code: str=None):
        """CheckoutDataTotalsInformationInterface - a model defined in OpenAPI

        :param address: The address of this CheckoutDataTotalsInformationInterface.
        :param custom_attributes: The custom_attributes of this CheckoutDataTotalsInformationInterface.
        :param extension_attributes: The extension_attributes of this CheckoutDataTotalsInformationInterface.
        :param shipping_carrier_code: The shipping_carrier_code of this CheckoutDataTotalsInformationInterface.
        :param shipping_method_code: The shipping_method_code of this CheckoutDataTotalsInformationInterface.
        """
        self.openapi_types = {
            'address': QuoteDataAddressInterface,
            'custom_attributes': List[FrameworkAttributeInterface],
            'extension_attributes': object,
            'shipping_carrier_code': str,
            'shipping_method_code': str
        }

        self.attribute_map = {
            'address': 'address',
            'custom_attributes': 'custom_attributes',
            'extension_attributes': 'extension_attributes',
            'shipping_carrier_code': 'shipping_carrier_code',
            'shipping_method_code': 'shipping_method_code'
        }

        self._address = address
        self._custom_attributes = custom_attributes
        self._extension_attributes = extension_attributes
        self._shipping_carrier_code = shipping_carrier_code
        self._shipping_method_code = shipping_method_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CheckoutDataTotalsInformationInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The checkout-data-totals-information-interface of this CheckoutDataTotalsInformationInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this CheckoutDataTotalsInformationInterface.


        :return: The address of this CheckoutDataTotalsInformationInterface.
        :rtype: QuoteDataAddressInterface
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CheckoutDataTotalsInformationInterface.


        :param address: The address of this CheckoutDataTotalsInformationInterface.
        :type address: QuoteDataAddressInterface
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")

        self._address = address

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this CheckoutDataTotalsInformationInterface.

        Custom attributes values.

        :return: The custom_attributes of this CheckoutDataTotalsInformationInterface.
        :rtype: List[FrameworkAttributeInterface]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this CheckoutDataTotalsInformationInterface.

        Custom attributes values.

        :param custom_attributes: The custom_attributes of this CheckoutDataTotalsInformationInterface.
        :type custom_attributes: List[FrameworkAttributeInterface]
        """

        self._custom_attributes = custom_attributes

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this CheckoutDataTotalsInformationInterface.

        ExtensionInterface class for @see \\Magento\\Checkout\\Api\\Data\\TotalsInformationInterface

        :return: The extension_attributes of this CheckoutDataTotalsInformationInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this CheckoutDataTotalsInformationInterface.

        ExtensionInterface class for @see \\Magento\\Checkout\\Api\\Data\\TotalsInformationInterface

        :param extension_attributes: The extension_attributes of this CheckoutDataTotalsInformationInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def shipping_carrier_code(self):
        """Gets the shipping_carrier_code of this CheckoutDataTotalsInformationInterface.

        Carrier code

        :return: The shipping_carrier_code of this CheckoutDataTotalsInformationInterface.
        :rtype: str
        """
        return self._shipping_carrier_code

    @shipping_carrier_code.setter
    def shipping_carrier_code(self, shipping_carrier_code):
        """Sets the shipping_carrier_code of this CheckoutDataTotalsInformationInterface.

        Carrier code

        :param shipping_carrier_code: The shipping_carrier_code of this CheckoutDataTotalsInformationInterface.
        :type shipping_carrier_code: str
        """

        self._shipping_carrier_code = shipping_carrier_code

    @property
    def shipping_method_code(self):
        """Gets the shipping_method_code of this CheckoutDataTotalsInformationInterface.

        Shipping method code

        :return: The shipping_method_code of this CheckoutDataTotalsInformationInterface.
        :rtype: str
        """
        return self._shipping_method_code

    @shipping_method_code.setter
    def shipping_method_code(self, shipping_method_code):
        """Sets the shipping_method_code of this CheckoutDataTotalsInformationInterface.

        Shipping method code

        :param shipping_method_code: The shipping_method_code of this CheckoutDataTotalsInformationInterface.
        :type shipping_method_code: str
        """

        self._shipping_method_code = shipping_method_code
