# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.raw_record_xml import RawRecordXml
from openapi_server import util


class ArticleHistoryResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[RawRecordXml]=None, status: str=None):
        """ArticleHistoryResponse - a model defined in OpenAPI

        :param data: The data of this ArticleHistoryResponse.
        :param status: The status of this ArticleHistoryResponse.
        """
        self.openapi_types = {
            'data': List[RawRecordXml],
            'status': str
        }

        self.attribute_map = {
            'data': 'data',
            'status': 'status'
        }

        self._data = data
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ArticleHistoryResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ArticleHistoryResponse of this ArticleHistoryResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ArticleHistoryResponse.

        List of article versions

        :return: The data of this ArticleHistoryResponse.
        :rtype: List[RawRecordXml]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ArticleHistoryResponse.

        List of article versions

        :param data: The data of this ArticleHistoryResponse.
        :type data: List[RawRecordXml]
        """

        self._data = data

    @property
    def status(self):
        """Gets the status of this ArticleHistoryResponse.

        Operation status

        :return: The status of this ArticleHistoryResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ArticleHistoryResponse.

        Operation status

        :param status: The status of this ArticleHistoryResponse.
        :type status: str
        """
        allowed_values = ["OK", "Not found", "Too many queries", "Missing parameter", "Invalid parameter", "Parameter out of bounds"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
