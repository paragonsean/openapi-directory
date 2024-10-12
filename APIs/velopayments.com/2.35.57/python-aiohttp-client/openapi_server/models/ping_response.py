# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PingResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, webhook_id: str=None):
        """PingResponse - a model defined in OpenAPI

        :param id: The id of this PingResponse.
        :param webhook_id: The webhook_id of this PingResponse.
        """
        self.openapi_types = {
            'id': str,
            'webhook_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'webhook_id': 'webhookId'
        }

        self._id = id
        self._webhook_id = webhook_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PingResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PingResponse of this PingResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PingResponse.


        :return: The id of this PingResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PingResponse.


        :param id: The id of this PingResponse.
        :type id: str
        """

        self._id = id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this PingResponse.


        :return: The webhook_id of this PingResponse.
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this PingResponse.


        :param webhook_id: The webhook_id of this PingResponse.
        :type webhook_id: str
        """

        self._webhook_id = webhook_id
