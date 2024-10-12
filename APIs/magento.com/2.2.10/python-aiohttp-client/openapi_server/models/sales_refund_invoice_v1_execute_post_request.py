# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sales_data_creditmemo_comment_creation_interface import SalesDataCreditmemoCommentCreationInterface
from openapi_server.models.sales_data_creditmemo_creation_arguments_interface import SalesDataCreditmemoCreationArgumentsInterface
from openapi_server.models.sales_data_creditmemo_item_creation_interface import SalesDataCreditmemoItemCreationInterface
from openapi_server import util


class SalesRefundInvoiceV1ExecutePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, append_comment: bool=None, arguments: SalesDataCreditmemoCreationArgumentsInterface=None, comment: SalesDataCreditmemoCommentCreationInterface=None, is_online: bool=None, items: List[SalesDataCreditmemoItemCreationInterface]=None, notify: bool=None):
        """SalesRefundInvoiceV1ExecutePostRequest - a model defined in OpenAPI

        :param append_comment: The append_comment of this SalesRefundInvoiceV1ExecutePostRequest.
        :param arguments: The arguments of this SalesRefundInvoiceV1ExecutePostRequest.
        :param comment: The comment of this SalesRefundInvoiceV1ExecutePostRequest.
        :param is_online: The is_online of this SalesRefundInvoiceV1ExecutePostRequest.
        :param items: The items of this SalesRefundInvoiceV1ExecutePostRequest.
        :param notify: The notify of this SalesRefundInvoiceV1ExecutePostRequest.
        """
        self.openapi_types = {
            'append_comment': bool,
            'arguments': SalesDataCreditmemoCreationArgumentsInterface,
            'comment': SalesDataCreditmemoCommentCreationInterface,
            'is_online': bool,
            'items': List[SalesDataCreditmemoItemCreationInterface],
            'notify': bool
        }

        self.attribute_map = {
            'append_comment': 'appendComment',
            'arguments': 'arguments',
            'comment': 'comment',
            'is_online': 'isOnline',
            'items': 'items',
            'notify': 'notify'
        }

        self._append_comment = append_comment
        self._arguments = arguments
        self._comment = comment
        self._is_online = is_online
        self._items = items
        self._notify = notify

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SalesRefundInvoiceV1ExecutePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The salesRefundInvoiceV1ExecutePost_request of this SalesRefundInvoiceV1ExecutePostRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def append_comment(self):
        """Gets the append_comment of this SalesRefundInvoiceV1ExecutePostRequest.


        :return: The append_comment of this SalesRefundInvoiceV1ExecutePostRequest.
        :rtype: bool
        """
        return self._append_comment

    @append_comment.setter
    def append_comment(self, append_comment):
        """Sets the append_comment of this SalesRefundInvoiceV1ExecutePostRequest.


        :param append_comment: The append_comment of this SalesRefundInvoiceV1ExecutePostRequest.
        :type append_comment: bool
        """

        self._append_comment = append_comment

    @property
    def arguments(self):
        """Gets the arguments of this SalesRefundInvoiceV1ExecutePostRequest.


        :return: The arguments of this SalesRefundInvoiceV1ExecutePostRequest.
        :rtype: SalesDataCreditmemoCreationArgumentsInterface
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this SalesRefundInvoiceV1ExecutePostRequest.


        :param arguments: The arguments of this SalesRefundInvoiceV1ExecutePostRequest.
        :type arguments: SalesDataCreditmemoCreationArgumentsInterface
        """

        self._arguments = arguments

    @property
    def comment(self):
        """Gets the comment of this SalesRefundInvoiceV1ExecutePostRequest.


        :return: The comment of this SalesRefundInvoiceV1ExecutePostRequest.
        :rtype: SalesDataCreditmemoCommentCreationInterface
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SalesRefundInvoiceV1ExecutePostRequest.


        :param comment: The comment of this SalesRefundInvoiceV1ExecutePostRequest.
        :type comment: SalesDataCreditmemoCommentCreationInterface
        """

        self._comment = comment

    @property
    def is_online(self):
        """Gets the is_online of this SalesRefundInvoiceV1ExecutePostRequest.


        :return: The is_online of this SalesRefundInvoiceV1ExecutePostRequest.
        :rtype: bool
        """
        return self._is_online

    @is_online.setter
    def is_online(self, is_online):
        """Sets the is_online of this SalesRefundInvoiceV1ExecutePostRequest.


        :param is_online: The is_online of this SalesRefundInvoiceV1ExecutePostRequest.
        :type is_online: bool
        """

        self._is_online = is_online

    @property
    def items(self):
        """Gets the items of this SalesRefundInvoiceV1ExecutePostRequest.


        :return: The items of this SalesRefundInvoiceV1ExecutePostRequest.
        :rtype: List[SalesDataCreditmemoItemCreationInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SalesRefundInvoiceV1ExecutePostRequest.


        :param items: The items of this SalesRefundInvoiceV1ExecutePostRequest.
        :type items: List[SalesDataCreditmemoItemCreationInterface]
        """

        self._items = items

    @property
    def notify(self):
        """Gets the notify of this SalesRefundInvoiceV1ExecutePostRequest.


        :return: The notify of this SalesRefundInvoiceV1ExecutePostRequest.
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this SalesRefundInvoiceV1ExecutePostRequest.


        :param notify: The notify of this SalesRefundInvoiceV1ExecutePostRequest.
        :type notify: bool
        """

        self._notify = notify
