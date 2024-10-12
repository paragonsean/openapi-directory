# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.framework_attribute_interface import FrameworkAttributeInterface
from openapi_server.models.rma_data_comment_interface import RmaDataCommentInterface
from openapi_server.models.rma_data_item_interface import RmaDataItemInterface
from openapi_server.models.rma_data_track_interface import RmaDataTrackInterface
from openapi_server import util


class RmaDataRmaInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, comments: List[RmaDataCommentInterface]=None, custom_attributes: List[FrameworkAttributeInterface]=None, customer_custom_email: str=None, customer_id: int=None, date_requested: str=None, entity_id: int=None, extension_attributes: object=None, increment_id: str=None, items: List[RmaDataItemInterface]=None, order_id: int=None, order_increment_id: str=None, status: str=None, store_id: int=None, tracks: List[RmaDataTrackInterface]=None):
        """RmaDataRmaInterface - a model defined in OpenAPI

        :param comments: The comments of this RmaDataRmaInterface.
        :param custom_attributes: The custom_attributes of this RmaDataRmaInterface.
        :param customer_custom_email: The customer_custom_email of this RmaDataRmaInterface.
        :param customer_id: The customer_id of this RmaDataRmaInterface.
        :param date_requested: The date_requested of this RmaDataRmaInterface.
        :param entity_id: The entity_id of this RmaDataRmaInterface.
        :param extension_attributes: The extension_attributes of this RmaDataRmaInterface.
        :param increment_id: The increment_id of this RmaDataRmaInterface.
        :param items: The items of this RmaDataRmaInterface.
        :param order_id: The order_id of this RmaDataRmaInterface.
        :param order_increment_id: The order_increment_id of this RmaDataRmaInterface.
        :param status: The status of this RmaDataRmaInterface.
        :param store_id: The store_id of this RmaDataRmaInterface.
        :param tracks: The tracks of this RmaDataRmaInterface.
        """
        self.openapi_types = {
            'comments': List[RmaDataCommentInterface],
            'custom_attributes': List[FrameworkAttributeInterface],
            'customer_custom_email': str,
            'customer_id': int,
            'date_requested': str,
            'entity_id': int,
            'extension_attributes': object,
            'increment_id': str,
            'items': List[RmaDataItemInterface],
            'order_id': int,
            'order_increment_id': str,
            'status': str,
            'store_id': int,
            'tracks': List[RmaDataTrackInterface]
        }

        self.attribute_map = {
            'comments': 'comments',
            'custom_attributes': 'custom_attributes',
            'customer_custom_email': 'customer_custom_email',
            'customer_id': 'customer_id',
            'date_requested': 'date_requested',
            'entity_id': 'entity_id',
            'extension_attributes': 'extension_attributes',
            'increment_id': 'increment_id',
            'items': 'items',
            'order_id': 'order_id',
            'order_increment_id': 'order_increment_id',
            'status': 'status',
            'store_id': 'store_id',
            'tracks': 'tracks'
        }

        self._comments = comments
        self._custom_attributes = custom_attributes
        self._customer_custom_email = customer_custom_email
        self._customer_id = customer_id
        self._date_requested = date_requested
        self._entity_id = entity_id
        self._extension_attributes = extension_attributes
        self._increment_id = increment_id
        self._items = items
        self._order_id = order_id
        self._order_increment_id = order_increment_id
        self._status = status
        self._store_id = store_id
        self._tracks = tracks

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RmaDataRmaInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The rma-data-rma-interface of this RmaDataRmaInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comments(self):
        """Gets the comments of this RmaDataRmaInterface.

        Comments list

        :return: The comments of this RmaDataRmaInterface.
        :rtype: List[RmaDataCommentInterface]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RmaDataRmaInterface.

        Comments list

        :param comments: The comments of this RmaDataRmaInterface.
        :type comments: List[RmaDataCommentInterface]
        """
        if comments is None:
            raise ValueError("Invalid value for `comments`, must not be `None`")

        self._comments = comments

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this RmaDataRmaInterface.

        Custom attributes values.

        :return: The custom_attributes of this RmaDataRmaInterface.
        :rtype: List[FrameworkAttributeInterface]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this RmaDataRmaInterface.

        Custom attributes values.

        :param custom_attributes: The custom_attributes of this RmaDataRmaInterface.
        :type custom_attributes: List[FrameworkAttributeInterface]
        """

        self._custom_attributes = custom_attributes

    @property
    def customer_custom_email(self):
        """Gets the customer_custom_email of this RmaDataRmaInterface.

        Customer_custom_email

        :return: The customer_custom_email of this RmaDataRmaInterface.
        :rtype: str
        """
        return self._customer_custom_email

    @customer_custom_email.setter
    def customer_custom_email(self, customer_custom_email):
        """Sets the customer_custom_email of this RmaDataRmaInterface.

        Customer_custom_email

        :param customer_custom_email: The customer_custom_email of this RmaDataRmaInterface.
        :type customer_custom_email: str
        """
        if customer_custom_email is None:
            raise ValueError("Invalid value for `customer_custom_email`, must not be `None`")

        self._customer_custom_email = customer_custom_email

    @property
    def customer_id(self):
        """Gets the customer_id of this RmaDataRmaInterface.

        Customer_id

        :return: The customer_id of this RmaDataRmaInterface.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this RmaDataRmaInterface.

        Customer_id

        :param customer_id: The customer_id of this RmaDataRmaInterface.
        :type customer_id: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")

        self._customer_id = customer_id

    @property
    def date_requested(self):
        """Gets the date_requested of this RmaDataRmaInterface.

        Date_requested

        :return: The date_requested of this RmaDataRmaInterface.
        :rtype: str
        """
        return self._date_requested

    @date_requested.setter
    def date_requested(self, date_requested):
        """Sets the date_requested of this RmaDataRmaInterface.

        Date_requested

        :param date_requested: The date_requested of this RmaDataRmaInterface.
        :type date_requested: str
        """
        if date_requested is None:
            raise ValueError("Invalid value for `date_requested`, must not be `None`")

        self._date_requested = date_requested

    @property
    def entity_id(self):
        """Gets the entity_id of this RmaDataRmaInterface.

        Entity_id

        :return: The entity_id of this RmaDataRmaInterface.
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this RmaDataRmaInterface.

        Entity_id

        :param entity_id: The entity_id of this RmaDataRmaInterface.
        :type entity_id: int
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")

        self._entity_id = entity_id

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this RmaDataRmaInterface.

        ExtensionInterface class for @see \\Magento\\Rma\\Api\\Data\\RmaInterface

        :return: The extension_attributes of this RmaDataRmaInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this RmaDataRmaInterface.

        ExtensionInterface class for @see \\Magento\\Rma\\Api\\Data\\RmaInterface

        :param extension_attributes: The extension_attributes of this RmaDataRmaInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def increment_id(self):
        """Gets the increment_id of this RmaDataRmaInterface.

        Entity_id

        :return: The increment_id of this RmaDataRmaInterface.
        :rtype: str
        """
        return self._increment_id

    @increment_id.setter
    def increment_id(self, increment_id):
        """Sets the increment_id of this RmaDataRmaInterface.

        Entity_id

        :param increment_id: The increment_id of this RmaDataRmaInterface.
        :type increment_id: str
        """
        if increment_id is None:
            raise ValueError("Invalid value for `increment_id`, must not be `None`")

        self._increment_id = increment_id

    @property
    def items(self):
        """Gets the items of this RmaDataRmaInterface.

        Items

        :return: The items of this RmaDataRmaInterface.
        :rtype: List[RmaDataItemInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this RmaDataRmaInterface.

        Items

        :param items: The items of this RmaDataRmaInterface.
        :type items: List[RmaDataItemInterface]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def order_id(self):
        """Gets the order_id of this RmaDataRmaInterface.

        Order_id

        :return: The order_id of this RmaDataRmaInterface.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this RmaDataRmaInterface.

        Order_id

        :param order_id: The order_id of this RmaDataRmaInterface.
        :type order_id: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")

        self._order_id = order_id

    @property
    def order_increment_id(self):
        """Gets the order_increment_id of this RmaDataRmaInterface.

        Order_increment_id

        :return: The order_increment_id of this RmaDataRmaInterface.
        :rtype: str
        """
        return self._order_increment_id

    @order_increment_id.setter
    def order_increment_id(self, order_increment_id):
        """Sets the order_increment_id of this RmaDataRmaInterface.

        Order_increment_id

        :param order_increment_id: The order_increment_id of this RmaDataRmaInterface.
        :type order_increment_id: str
        """
        if order_increment_id is None:
            raise ValueError("Invalid value for `order_increment_id`, must not be `None`")

        self._order_increment_id = order_increment_id

    @property
    def status(self):
        """Gets the status of this RmaDataRmaInterface.

        Status

        :return: The status of this RmaDataRmaInterface.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RmaDataRmaInterface.

        Status

        :param status: The status of this RmaDataRmaInterface.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def store_id(self):
        """Gets the store_id of this RmaDataRmaInterface.

        Store_id

        :return: The store_id of this RmaDataRmaInterface.
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this RmaDataRmaInterface.

        Store_id

        :param store_id: The store_id of this RmaDataRmaInterface.
        :type store_id: int
        """
        if store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")

        self._store_id = store_id

    @property
    def tracks(self):
        """Gets the tracks of this RmaDataRmaInterface.

        Tracks list

        :return: The tracks of this RmaDataRmaInterface.
        :rtype: List[RmaDataTrackInterface]
        """
        return self._tracks

    @tracks.setter
    def tracks(self, tracks):
        """Sets the tracks of this RmaDataRmaInterface.

        Tracks list

        :param tracks: The tracks of this RmaDataRmaInterface.
        :type tracks: List[RmaDataTrackInterface]
        """
        if tracks is None:
            raise ValueError("Invalid value for `tracks`, must not be `None`")

        self._tracks = tracks
