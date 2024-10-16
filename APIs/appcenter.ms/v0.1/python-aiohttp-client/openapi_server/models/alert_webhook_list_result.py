# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.webhooks_list200_response_values_inner import WebhooksList200ResponseValuesInner
from openapi_server import util


class AlertWebhookListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, values: List[WebhooksList200ResponseValuesInner]=None):
        """AlertWebhookListResult - a model defined in OpenAPI

        :param values: The values of this AlertWebhookListResult.
        """
        self.openapi_types = {
            'values': List[WebhooksList200ResponseValuesInner]
        }

        self.attribute_map = {
            'values': 'values'
        }

        self._values = values

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AlertWebhookListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AlertWebhookListResult of this AlertWebhookListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def values(self):
        """Gets the values of this AlertWebhookListResult.


        :return: The values of this AlertWebhookListResult.
        :rtype: List[WebhooksList200ResponseValuesInner]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AlertWebhookListResult.


        :param values: The values of this AlertWebhookListResult.
        :type values: List[WebhooksList200ResponseValuesInner]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")

        self._values = values
