# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.update_network_wireless_billing_request_plans_inner_bandwidth_limits import UpdateNetworkWirelessBillingRequestPlansInnerBandwidthLimits
from openapi_server import util


class UpdateNetworkWirelessBillingRequestPlansInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bandwidth_limits: UpdateNetworkWirelessBillingRequestPlansInnerBandwidthLimits=None, id: str=None, price: float=None, time_limit: str=None):
        """UpdateNetworkWirelessBillingRequestPlansInner - a model defined in OpenAPI

        :param bandwidth_limits: The bandwidth_limits of this UpdateNetworkWirelessBillingRequestPlansInner.
        :param id: The id of this UpdateNetworkWirelessBillingRequestPlansInner.
        :param price: The price of this UpdateNetworkWirelessBillingRequestPlansInner.
        :param time_limit: The time_limit of this UpdateNetworkWirelessBillingRequestPlansInner.
        """
        self.openapi_types = {
            'bandwidth_limits': UpdateNetworkWirelessBillingRequestPlansInnerBandwidthLimits,
            'id': str,
            'price': float,
            'time_limit': str
        }

        self.attribute_map = {
            'bandwidth_limits': 'bandwidthLimits',
            'id': 'id',
            'price': 'price',
            'time_limit': 'timeLimit'
        }

        self._bandwidth_limits = bandwidth_limits
        self._id = id
        self._price = price
        self._time_limit = time_limit

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateNetworkWirelessBillingRequestPlansInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateNetworkWirelessBilling_request_plans_inner of this UpdateNetworkWirelessBillingRequestPlansInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bandwidth_limits(self):
        """Gets the bandwidth_limits of this UpdateNetworkWirelessBillingRequestPlansInner.


        :return: The bandwidth_limits of this UpdateNetworkWirelessBillingRequestPlansInner.
        :rtype: UpdateNetworkWirelessBillingRequestPlansInnerBandwidthLimits
        """
        return self._bandwidth_limits

    @bandwidth_limits.setter
    def bandwidth_limits(self, bandwidth_limits):
        """Sets the bandwidth_limits of this UpdateNetworkWirelessBillingRequestPlansInner.


        :param bandwidth_limits: The bandwidth_limits of this UpdateNetworkWirelessBillingRequestPlansInner.
        :type bandwidth_limits: UpdateNetworkWirelessBillingRequestPlansInnerBandwidthLimits
        """
        if bandwidth_limits is None:
            raise ValueError("Invalid value for `bandwidth_limits`, must not be `None`")

        self._bandwidth_limits = bandwidth_limits

    @property
    def id(self):
        """Gets the id of this UpdateNetworkWirelessBillingRequestPlansInner.

        The id of the pricing plan to update.

        :return: The id of this UpdateNetworkWirelessBillingRequestPlansInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateNetworkWirelessBillingRequestPlansInner.

        The id of the pricing plan to update.

        :param id: The id of this UpdateNetworkWirelessBillingRequestPlansInner.
        :type id: str
        """

        self._id = id

    @property
    def price(self):
        """Gets the price of this UpdateNetworkWirelessBillingRequestPlansInner.

        The price of the billing plan.

        :return: The price of this UpdateNetworkWirelessBillingRequestPlansInner.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this UpdateNetworkWirelessBillingRequestPlansInner.

        The price of the billing plan.

        :param price: The price of this UpdateNetworkWirelessBillingRequestPlansInner.
        :type price: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def time_limit(self):
        """Gets the time_limit of this UpdateNetworkWirelessBillingRequestPlansInner.

        The time limit of the pricing plan in minutes. Can be '1 hour', '1 day', '1 week', or '30 days'.

        :return: The time_limit of this UpdateNetworkWirelessBillingRequestPlansInner.
        :rtype: str
        """
        return self._time_limit

    @time_limit.setter
    def time_limit(self, time_limit):
        """Sets the time_limit of this UpdateNetworkWirelessBillingRequestPlansInner.

        The time limit of the pricing plan in minutes. Can be '1 hour', '1 day', '1 week', or '30 days'.

        :param time_limit: The time_limit of this UpdateNetworkWirelessBillingRequestPlansInner.
        :type time_limit: str
        """
        allowed_values = ["1 day", "1 hour", "1 week", "30 days"]  # noqa: E501
        if time_limit not in allowed_values:
            raise ValueError(
                "Invalid value for `time_limit` ({0}), must be one of {1}"
                .format(time_limit, allowed_values)
            )

        self._time_limit = time_limit
