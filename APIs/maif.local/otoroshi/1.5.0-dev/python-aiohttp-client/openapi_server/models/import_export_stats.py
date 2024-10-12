# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ImportExportStats(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, calls: int=None, data_in: int=None, data_out: int=None):
        """ImportExportStats - a model defined in OpenAPI

        :param calls: The calls of this ImportExportStats.
        :param data_in: The data_in of this ImportExportStats.
        :param data_out: The data_out of this ImportExportStats.
        """
        self.openapi_types = {
            'calls': int,
            'data_in': int,
            'data_out': int
        }

        self.attribute_map = {
            'calls': 'calls',
            'data_in': 'dataIn',
            'data_out': 'dataOut'
        }

        self._calls = calls
        self._data_in = data_in
        self._data_out = data_out

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImportExportStats':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImportExportStats of this ImportExportStats.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def calls(self):
        """Gets the calls of this ImportExportStats.

        Number of calls to Otoroshi globally

        :return: The calls of this ImportExportStats.
        :rtype: int
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        """Sets the calls of this ImportExportStats.

        Number of calls to Otoroshi globally

        :param calls: The calls of this ImportExportStats.
        :type calls: int
        """
        if calls is None:
            raise ValueError("Invalid value for `calls`, must not be `None`")

        self._calls = calls

    @property
    def data_in(self):
        """Gets the data_in of this ImportExportStats.

        The amount of data sent to Otoroshi globally

        :return: The data_in of this ImportExportStats.
        :rtype: int
        """
        return self._data_in

    @data_in.setter
    def data_in(self, data_in):
        """Sets the data_in of this ImportExportStats.

        The amount of data sent to Otoroshi globally

        :param data_in: The data_in of this ImportExportStats.
        :type data_in: int
        """
        if data_in is None:
            raise ValueError("Invalid value for `data_in`, must not be `None`")

        self._data_in = data_in

    @property
    def data_out(self):
        """Gets the data_out of this ImportExportStats.

        The amount of data sent from Otoroshi globally

        :return: The data_out of this ImportExportStats.
        :rtype: int
        """
        return self._data_out

    @data_out.setter
    def data_out(self, data_out):
        """Sets the data_out of this ImportExportStats.

        The amount of data sent from Otoroshi globally

        :param data_out: The data_out of this ImportExportStats.
        :type data_out: int
        """
        if data_out is None:
            raise ValueError("Invalid value for `data_out`, must not be `None`")

        self._data_out = data_out
