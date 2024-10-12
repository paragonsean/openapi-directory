# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.catalog_inventory_data_stock_item_interface import CatalogInventoryDataStockItemInterface
from openapi_server import util


class CatalogInventoryDataStockStatusInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extension_attributes: object=None, product_id: int=None, qty: int=None, stock_id: int=None, stock_item: CatalogInventoryDataStockItemInterface=None, stock_status: int=None):
        """CatalogInventoryDataStockStatusInterface - a model defined in OpenAPI

        :param extension_attributes: The extension_attributes of this CatalogInventoryDataStockStatusInterface.
        :param product_id: The product_id of this CatalogInventoryDataStockStatusInterface.
        :param qty: The qty of this CatalogInventoryDataStockStatusInterface.
        :param stock_id: The stock_id of this CatalogInventoryDataStockStatusInterface.
        :param stock_item: The stock_item of this CatalogInventoryDataStockStatusInterface.
        :param stock_status: The stock_status of this CatalogInventoryDataStockStatusInterface.
        """
        self.openapi_types = {
            'extension_attributes': object,
            'product_id': int,
            'qty': int,
            'stock_id': int,
            'stock_item': CatalogInventoryDataStockItemInterface,
            'stock_status': int
        }

        self.attribute_map = {
            'extension_attributes': 'extension_attributes',
            'product_id': 'product_id',
            'qty': 'qty',
            'stock_id': 'stock_id',
            'stock_item': 'stock_item',
            'stock_status': 'stock_status'
        }

        self._extension_attributes = extension_attributes
        self._product_id = product_id
        self._qty = qty
        self._stock_id = stock_id
        self._stock_item = stock_item
        self._stock_status = stock_status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CatalogInventoryDataStockStatusInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The catalog-inventory-data-stock-status-interface of this CatalogInventoryDataStockStatusInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this CatalogInventoryDataStockStatusInterface.

        ExtensionInterface class for @see \\Magento\\CatalogInventory\\Api\\Data\\StockStatusInterface

        :return: The extension_attributes of this CatalogInventoryDataStockStatusInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this CatalogInventoryDataStockStatusInterface.

        ExtensionInterface class for @see \\Magento\\CatalogInventory\\Api\\Data\\StockStatusInterface

        :param extension_attributes: The extension_attributes of this CatalogInventoryDataStockStatusInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def product_id(self):
        """Gets the product_id of this CatalogInventoryDataStockStatusInterface.


        :return: The product_id of this CatalogInventoryDataStockStatusInterface.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CatalogInventoryDataStockStatusInterface.


        :param product_id: The product_id of this CatalogInventoryDataStockStatusInterface.
        :type product_id: int
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")

        self._product_id = product_id

    @property
    def qty(self):
        """Gets the qty of this CatalogInventoryDataStockStatusInterface.


        :return: The qty of this CatalogInventoryDataStockStatusInterface.
        :rtype: int
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this CatalogInventoryDataStockStatusInterface.


        :param qty: The qty of this CatalogInventoryDataStockStatusInterface.
        :type qty: int
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")

        self._qty = qty

    @property
    def stock_id(self):
        """Gets the stock_id of this CatalogInventoryDataStockStatusInterface.


        :return: The stock_id of this CatalogInventoryDataStockStatusInterface.
        :rtype: int
        """
        return self._stock_id

    @stock_id.setter
    def stock_id(self, stock_id):
        """Sets the stock_id of this CatalogInventoryDataStockStatusInterface.


        :param stock_id: The stock_id of this CatalogInventoryDataStockStatusInterface.
        :type stock_id: int
        """
        if stock_id is None:
            raise ValueError("Invalid value for `stock_id`, must not be `None`")

        self._stock_id = stock_id

    @property
    def stock_item(self):
        """Gets the stock_item of this CatalogInventoryDataStockStatusInterface.


        :return: The stock_item of this CatalogInventoryDataStockStatusInterface.
        :rtype: CatalogInventoryDataStockItemInterface
        """
        return self._stock_item

    @stock_item.setter
    def stock_item(self, stock_item):
        """Sets the stock_item of this CatalogInventoryDataStockStatusInterface.


        :param stock_item: The stock_item of this CatalogInventoryDataStockStatusInterface.
        :type stock_item: CatalogInventoryDataStockItemInterface
        """
        if stock_item is None:
            raise ValueError("Invalid value for `stock_item`, must not be `None`")

        self._stock_item = stock_item

    @property
    def stock_status(self):
        """Gets the stock_status of this CatalogInventoryDataStockStatusInterface.


        :return: The stock_status of this CatalogInventoryDataStockStatusInterface.
        :rtype: int
        """
        return self._stock_status

    @stock_status.setter
    def stock_status(self, stock_status):
        """Sets the stock_status of this CatalogInventoryDataStockStatusInterface.


        :param stock_status: The stock_status of this CatalogInventoryDataStockStatusInterface.
        :type stock_status: int
        """
        if stock_status is None:
            raise ValueError("Invalid value for `stock_status`, must not be `None`")

        self._stock_status = stock_status
