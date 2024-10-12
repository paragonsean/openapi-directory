# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SalesDataCreditmemoItemCreationInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, extension_attributes: object=None, order_item_id: int=None, qty: float=None):
        """SalesDataCreditmemoItemCreationInterface - a model defined in OpenAPI

        :param extension_attributes: The extension_attributes of this SalesDataCreditmemoItemCreationInterface.
        :param order_item_id: The order_item_id of this SalesDataCreditmemoItemCreationInterface.
        :param qty: The qty of this SalesDataCreditmemoItemCreationInterface.
        """
        self.openapi_types = {
            'extension_attributes': object,
            'order_item_id': int,
            'qty': float
        }

        self.attribute_map = {
            'extension_attributes': 'extension_attributes',
            'order_item_id': 'order_item_id',
            'qty': 'qty'
        }

        self._extension_attributes = extension_attributes
        self._order_item_id = order_item_id
        self._qty = qty

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesDataCreditmemoItemCreationInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The sales-data-creditmemo-item-creation-interface of this SalesDataCreditmemoItemCreationInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this SalesDataCreditmemoItemCreationInterface.

        ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\CreditmemoItemCreationInterface

        :return: The extension_attributes of this SalesDataCreditmemoItemCreationInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this SalesDataCreditmemoItemCreationInterface.

        ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\CreditmemoItemCreationInterface

        :param extension_attributes: The extension_attributes of this SalesDataCreditmemoItemCreationInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def order_item_id(self):
        """Gets the order_item_id of this SalesDataCreditmemoItemCreationInterface.

        Order item ID.

        :return: The order_item_id of this SalesDataCreditmemoItemCreationInterface.
        :rtype: int
        """
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, order_item_id):
        """Sets the order_item_id of this SalesDataCreditmemoItemCreationInterface.

        Order item ID.

        :param order_item_id: The order_item_id of this SalesDataCreditmemoItemCreationInterface.
        :type order_item_id: int
        """
        if order_item_id is None:
            raise ValueError("Invalid value for `order_item_id`, must not be `None`")

        self._order_item_id = order_item_id

    @property
    def qty(self):
        """Gets the qty of this SalesDataCreditmemoItemCreationInterface.

        Quantity.

        :return: The qty of this SalesDataCreditmemoItemCreationInterface.
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this SalesDataCreditmemoItemCreationInterface.

        Quantity.

        :param qty: The qty of this SalesDataCreditmemoItemCreationInterface.
        :type qty: float
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")

        self._qty = qty
