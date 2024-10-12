# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.webhook_resource import WebhookResource
from openapi_server import util


class GetWebhookResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: WebhookResource=None):
        """GetWebhookResponse - a model defined in OpenAPI

        :param data: The data of this GetWebhookResponse.
        """
        self.openapi_types = {
            'data': WebhookResource
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetWebhookResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GetWebhookResponse of this GetWebhookResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this GetWebhookResponse.

        The webhook returned in this response. 

        :return: The data of this GetWebhookResponse.
        :rtype: WebhookResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetWebhookResponse.

        The webhook returned in this response. 

        :param data: The data of this GetWebhookResponse.
        :type data: WebhookResource
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data
