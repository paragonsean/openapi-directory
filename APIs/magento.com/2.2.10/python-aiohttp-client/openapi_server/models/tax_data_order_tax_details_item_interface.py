# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.tax_data_order_tax_details_applied_tax_interface import TaxDataOrderTaxDetailsAppliedTaxInterface
from openapi_server import util


class TaxDataOrderTaxDetailsItemInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, applied_taxes: List[TaxDataOrderTaxDetailsAppliedTaxInterface]=None, associated_item_id: int=None, extension_attributes: object=None, item_id: int=None, type: str=None):
        """TaxDataOrderTaxDetailsItemInterface - a model defined in OpenAPI

        :param applied_taxes: The applied_taxes of this TaxDataOrderTaxDetailsItemInterface.
        :param associated_item_id: The associated_item_id of this TaxDataOrderTaxDetailsItemInterface.
        :param extension_attributes: The extension_attributes of this TaxDataOrderTaxDetailsItemInterface.
        :param item_id: The item_id of this TaxDataOrderTaxDetailsItemInterface.
        :param type: The type of this TaxDataOrderTaxDetailsItemInterface.
        """
        self.openapi_types = {
            'applied_taxes': List[TaxDataOrderTaxDetailsAppliedTaxInterface],
            'associated_item_id': int,
            'extension_attributes': object,
            'item_id': int,
            'type': str
        }

        self.attribute_map = {
            'applied_taxes': 'applied_taxes',
            'associated_item_id': 'associated_item_id',
            'extension_attributes': 'extension_attributes',
            'item_id': 'item_id',
            'type': 'type'
        }

        self._applied_taxes = applied_taxes
        self._associated_item_id = associated_item_id
        self._extension_attributes = extension_attributes
        self._item_id = item_id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaxDataOrderTaxDetailsItemInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tax-data-order-tax-details-item-interface of this TaxDataOrderTaxDetailsItemInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def applied_taxes(self):
        """Gets the applied_taxes of this TaxDataOrderTaxDetailsItemInterface.

        Applied taxes

        :return: The applied_taxes of this TaxDataOrderTaxDetailsItemInterface.
        :rtype: List[TaxDataOrderTaxDetailsAppliedTaxInterface]
        """
        return self._applied_taxes

    @applied_taxes.setter
    def applied_taxes(self, applied_taxes):
        """Sets the applied_taxes of this TaxDataOrderTaxDetailsItemInterface.

        Applied taxes

        :param applied_taxes: The applied_taxes of this TaxDataOrderTaxDetailsItemInterface.
        :type applied_taxes: List[TaxDataOrderTaxDetailsAppliedTaxInterface]
        """

        self._applied_taxes = applied_taxes

    @property
    def associated_item_id(self):
        """Gets the associated_item_id of this TaxDataOrderTaxDetailsItemInterface.

        Associated item id if this item is associated with another item, null otherwise

        :return: The associated_item_id of this TaxDataOrderTaxDetailsItemInterface.
        :rtype: int
        """
        return self._associated_item_id

    @associated_item_id.setter
    def associated_item_id(self, associated_item_id):
        """Sets the associated_item_id of this TaxDataOrderTaxDetailsItemInterface.

        Associated item id if this item is associated with another item, null otherwise

        :param associated_item_id: The associated_item_id of this TaxDataOrderTaxDetailsItemInterface.
        :type associated_item_id: int
        """

        self._associated_item_id = associated_item_id

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this TaxDataOrderTaxDetailsItemInterface.

        ExtensionInterface class for @see \\Magento\\Tax\\Api\\Data\\OrderTaxDetailsItemInterface

        :return: The extension_attributes of this TaxDataOrderTaxDetailsItemInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this TaxDataOrderTaxDetailsItemInterface.

        ExtensionInterface class for @see \\Magento\\Tax\\Api\\Data\\OrderTaxDetailsItemInterface

        :param extension_attributes: The extension_attributes of this TaxDataOrderTaxDetailsItemInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def item_id(self):
        """Gets the item_id of this TaxDataOrderTaxDetailsItemInterface.

        Item id if this item is a product

        :return: The item_id of this TaxDataOrderTaxDetailsItemInterface.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this TaxDataOrderTaxDetailsItemInterface.

        Item id if this item is a product

        :param item_id: The item_id of this TaxDataOrderTaxDetailsItemInterface.
        :type item_id: int
        """

        self._item_id = item_id

    @property
    def type(self):
        """Gets the type of this TaxDataOrderTaxDetailsItemInterface.

        Type (shipping, product, weee, gift wrapping, etc)

        :return: The type of this TaxDataOrderTaxDetailsItemInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaxDataOrderTaxDetailsItemInterface.

        Type (shipping, product, weee, gift wrapping, etc)

        :param type: The type of this TaxDataOrderTaxDetailsItemInterface.
        :type type: str
        """

        self._type = type
