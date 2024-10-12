# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateOrganizationActionBatchRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, confirmed: bool=None, synchronous: bool=None):
        """UpdateOrganizationActionBatchRequest - a model defined in OpenAPI

        :param confirmed: The confirmed of this UpdateOrganizationActionBatchRequest.
        :param synchronous: The synchronous of this UpdateOrganizationActionBatchRequest.
        """
        self.openapi_types = {
            'confirmed': bool,
            'synchronous': bool
        }

        self.attribute_map = {
            'confirmed': 'confirmed',
            'synchronous': 'synchronous'
        }

        self._confirmed = confirmed
        self._synchronous = synchronous

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateOrganizationActionBatchRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateOrganizationActionBatch_request of this UpdateOrganizationActionBatchRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confirmed(self):
        """Gets the confirmed of this UpdateOrganizationActionBatchRequest.

        A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.

        :return: The confirmed of this UpdateOrganizationActionBatchRequest.
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this UpdateOrganizationActionBatchRequest.

        A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.

        :param confirmed: The confirmed of this UpdateOrganizationActionBatchRequest.
        :type confirmed: bool
        """

        self._confirmed = confirmed

    @property
    def synchronous(self):
        """Gets the synchronous of this UpdateOrganizationActionBatchRequest.

        Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.

        :return: The synchronous of this UpdateOrganizationActionBatchRequest.
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """Sets the synchronous of this UpdateOrganizationActionBatchRequest.

        Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.

        :param synchronous: The synchronous of this UpdateOrganizationActionBatchRequest.
        :type synchronous: bool
        """

        self._synchronous = synchronous
