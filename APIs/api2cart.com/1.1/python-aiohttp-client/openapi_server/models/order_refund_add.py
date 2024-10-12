# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.order_refund_add_items_inner import OrderRefundAddItemsInner
from openapi_server import util


class OrderRefundAdd(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _date: str=None, fee_price: float=None, is_online: bool=False, item_restock: bool=False, items: List[OrderRefundAddItemsInner]=None, message: str=None, order_id: str=None, send_notifications: bool=False, shipping_price: float=None, total_price: float=None):
        """OrderRefundAdd - a model defined in OpenAPI

        :param _date: The _date of this OrderRefundAdd.
        :param fee_price: The fee_price of this OrderRefundAdd.
        :param is_online: The is_online of this OrderRefundAdd.
        :param item_restock: The item_restock of this OrderRefundAdd.
        :param items: The items of this OrderRefundAdd.
        :param message: The message of this OrderRefundAdd.
        :param order_id: The order_id of this OrderRefundAdd.
        :param send_notifications: The send_notifications of this OrderRefundAdd.
        :param shipping_price: The shipping_price of this OrderRefundAdd.
        :param total_price: The total_price of this OrderRefundAdd.
        """
        self.openapi_types = {
            '_date': str,
            'fee_price': float,
            'is_online': bool,
            'item_restock': bool,
            'items': List[OrderRefundAddItemsInner],
            'message': str,
            'order_id': str,
            'send_notifications': bool,
            'shipping_price': float,
            'total_price': float
        }

        self.attribute_map = {
            '_date': 'date',
            'fee_price': 'fee_price',
            'is_online': 'is_online',
            'item_restock': 'item_restock',
            'items': 'items',
            'message': 'message',
            'order_id': 'order_id',
            'send_notifications': 'send_notifications',
            'shipping_price': 'shipping_price',
            'total_price': 'total_price'
        }

        self.__date = _date
        self._fee_price = fee_price
        self._is_online = is_online
        self._item_restock = item_restock
        self._items = items
        self._message = message
        self._order_id = order_id
        self._send_notifications = send_notifications
        self._shipping_price = shipping_price
        self._total_price = total_price

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderRefundAdd':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrderRefundAdd of this OrderRefundAdd.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _date(self):
        """Gets the _date of this OrderRefundAdd.

        Specifies an order creation date in format Y-m-d H:i:s

        :return: The _date of this OrderRefundAdd.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this OrderRefundAdd.

        Specifies an order creation date in format Y-m-d H:i:s

        :param _date: The _date of this OrderRefundAdd.
        :type _date: str
        """

        self.__date = _date

    @property
    def fee_price(self):
        """Gets the fee_price of this OrderRefundAdd.

        Specifies refund's fee price

        :return: The fee_price of this OrderRefundAdd.
        :rtype: float
        """
        return self._fee_price

    @fee_price.setter
    def fee_price(self, fee_price):
        """Sets the fee_price of this OrderRefundAdd.

        Specifies refund's fee price

        :param fee_price: The fee_price of this OrderRefundAdd.
        :type fee_price: float
        """

        self._fee_price = fee_price

    @property
    def is_online(self):
        """Gets the is_online of this OrderRefundAdd.

        Indicates whether refund type is online

        :return: The is_online of this OrderRefundAdd.
        :rtype: bool
        """
        return self._is_online

    @is_online.setter
    def is_online(self, is_online):
        """Sets the is_online of this OrderRefundAdd.

        Indicates whether refund type is online

        :param is_online: The is_online of this OrderRefundAdd.
        :type is_online: bool
        """

        self._is_online = is_online

    @property
    def item_restock(self):
        """Gets the item_restock of this OrderRefundAdd.

        Boolean, whether or not to add the line items back to the store inventory.

        :return: The item_restock of this OrderRefundAdd.
        :rtype: bool
        """
        return self._item_restock

    @item_restock.setter
    def item_restock(self, item_restock):
        """Sets the item_restock of this OrderRefundAdd.

        Boolean, whether or not to add the line items back to the store inventory.

        :param item_restock: The item_restock of this OrderRefundAdd.
        :type item_restock: bool
        """

        self._item_restock = item_restock

    @property
    def items(self):
        """Gets the items of this OrderRefundAdd.

        Defines items in the order that will be refunded

        :return: The items of this OrderRefundAdd.
        :rtype: List[OrderRefundAddItemsInner]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this OrderRefundAdd.

        Defines items in the order that will be refunded

        :param items: The items of this OrderRefundAdd.
        :type items: List[OrderRefundAddItemsInner]
        """

        self._items = items

    @property
    def message(self):
        """Gets the message of this OrderRefundAdd.

        Refund reason, or some else message which assigned to refund.

        :return: The message of this OrderRefundAdd.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OrderRefundAdd.

        Refund reason, or some else message which assigned to refund.

        :param message: The message of this OrderRefundAdd.
        :type message: str
        """

        self._message = message

    @property
    def order_id(self):
        """Gets the order_id of this OrderRefundAdd.

        Defines the order for which the refund will be created.

        :return: The order_id of this OrderRefundAdd.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderRefundAdd.

        Defines the order for which the refund will be created.

        :param order_id: The order_id of this OrderRefundAdd.
        :type order_id: str
        """

        self._order_id = order_id

    @property
    def send_notifications(self):
        """Gets the send_notifications of this OrderRefundAdd.

        Send notifications to customer after refund was created

        :return: The send_notifications of this OrderRefundAdd.
        :rtype: bool
        """
        return self._send_notifications

    @send_notifications.setter
    def send_notifications(self, send_notifications):
        """Sets the send_notifications of this OrderRefundAdd.

        Send notifications to customer after refund was created

        :param send_notifications: The send_notifications of this OrderRefundAdd.
        :type send_notifications: bool
        """

        self._send_notifications = send_notifications

    @property
    def shipping_price(self):
        """Gets the shipping_price of this OrderRefundAdd.

        Defines refund shipping amount.

        :return: The shipping_price of this OrderRefundAdd.
        :rtype: float
        """
        return self._shipping_price

    @shipping_price.setter
    def shipping_price(self, shipping_price):
        """Sets the shipping_price of this OrderRefundAdd.

        Defines refund shipping amount.

        :param shipping_price: The shipping_price of this OrderRefundAdd.
        :type shipping_price: float
        """

        self._shipping_price = shipping_price

    @property
    def total_price(self):
        """Gets the total_price of this OrderRefundAdd.

        Defines order refund amount.

        :return: The total_price of this OrderRefundAdd.
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this OrderRefundAdd.

        Defines order refund amount.

        :param total_price: The total_price of this OrderRefundAdd.
        :type total_price: float
        """

        self._total_price = total_price
