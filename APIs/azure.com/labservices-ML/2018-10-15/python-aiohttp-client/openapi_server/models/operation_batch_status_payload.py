# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OperationBatchStatusPayload(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, urls: List[str]=None):
        """OperationBatchStatusPayload - a model defined in OpenAPI

        :param urls: The urls of this OperationBatchStatusPayload.
        """
        self.openapi_types = {
            'urls': List[str]
        }

        self.attribute_map = {
            'urls': 'urls'
        }

        self._urls = urls

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OperationBatchStatusPayload':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OperationBatchStatusPayload of this OperationBatchStatusPayload.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def urls(self):
        """Gets the urls of this OperationBatchStatusPayload.

        The operation url of long running operation

        :return: The urls of this OperationBatchStatusPayload.
        :rtype: List[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this OperationBatchStatusPayload.

        The operation url of long running operation

        :param urls: The urls of this OperationBatchStatusPayload.
        :type urls: List[str]
        """
        if urls is None:
            raise ValueError("Invalid value for `urls`, must not be `None`")

        self._urls = urls
