# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OrderStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, comments: str=None, status: str=None, update_date_time: datetime=None):
        """OrderStatus - a model defined in OpenAPI

        :param comments: The comments of this OrderStatus.
        :param status: The status of this OrderStatus.
        :param update_date_time: The update_date_time of this OrderStatus.
        """
        self.openapi_types = {
            'comments': str,
            'status': str,
            'update_date_time': datetime
        }

        self.attribute_map = {
            'comments': 'comments',
            'status': 'status',
            'update_date_time': 'updateDateTime'
        }

        self._comments = comments
        self._status = status
        self._update_date_time = update_date_time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrderStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrderStatus of this OrderStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comments(self):
        """Gets the comments of this OrderStatus.

        Comments related to this status change.

        :return: The comments of this OrderStatus.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this OrderStatus.

        Comments related to this status change.

        :param comments: The comments of this OrderStatus.
        :type comments: str
        """

        self._comments = comments

    @property
    def status(self):
        """Gets the status of this OrderStatus.

        Status of the order as per the allowed status types.

        :return: The status of this OrderStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderStatus.

        Status of the order as per the allowed status types.

        :param status: The status of this OrderStatus.
        :type status: str
        """
        allowed_values = ["Untracked", "AwaitingFulfilment", "AwaitingPreparation", "AwaitingShipment", "Shipped", "Arriving", "Delivered", "ReplacementRequested", "LostDevice", "Declined", "ReturnInitiated", "AwaitingReturnShipment", "ShippedBack", "CollectedAtMicrosoft"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def update_date_time(self):
        """Gets the update_date_time of this OrderStatus.

        Time of status update.

        :return: The update_date_time of this OrderStatus.
        :rtype: datetime
        """
        return self._update_date_time

    @update_date_time.setter
    def update_date_time(self, update_date_time):
        """Sets the update_date_time of this OrderStatus.

        Time of status update.

        :param update_date_time: The update_date_time of this OrderStatus.
        :type update_date_time: datetime
        """

        self._update_date_time = update_date_time
