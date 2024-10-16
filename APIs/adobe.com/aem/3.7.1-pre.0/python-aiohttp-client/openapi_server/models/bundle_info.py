# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.bundle_data import BundleData
from openapi_server import util


class BundleInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: List[BundleData]=None, s: List[int]=None, status: str=None):
        """BundleInfo - a model defined in OpenAPI

        :param data: The data of this BundleInfo.
        :param s: The s of this BundleInfo.
        :param status: The status of this BundleInfo.
        """
        self.openapi_types = {
            'data': List[BundleData],
            's': List[int],
            'status': str
        }

        self.attribute_map = {
            'data': 'data',
            's': 's',
            'status': 'status'
        }

        self._data = data
        self._s = s
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BundleInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BundleInfo of this BundleInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this BundleInfo.


        :return: The data of this BundleInfo.
        :rtype: List[BundleData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BundleInfo.


        :param data: The data of this BundleInfo.
        :type data: List[BundleData]
        """

        self._data = data

    @property
    def s(self):
        """Gets the s of this BundleInfo.


        :return: The s of this BundleInfo.
        :rtype: List[int]
        """
        return self._s

    @s.setter
    def s(self, s):
        """Sets the s of this BundleInfo.


        :param s: The s of this BundleInfo.
        :type s: List[int]
        """

        self._s = s

    @property
    def status(self):
        """Gets the status of this BundleInfo.

        Status description of all bundles

        :return: The status of this BundleInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BundleInfo.

        Status description of all bundles

        :param status: The status of this BundleInfo.
        :type status: str
        """

        self._status = status
