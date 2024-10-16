# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.clocking_records_post201_response_data import ClockingRecordsPost201ResponseData
from openapi_server import util


class CreateSuccessResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: ClockingRecordsPost201ResponseData=None, success: bool=True):
        """CreateSuccessResponse - a model defined in OpenAPI

        :param data: The data of this CreateSuccessResponse.
        :param success: The success of this CreateSuccessResponse.
        """
        self.openapi_types = {
            'data': ClockingRecordsPost201ResponseData,
            'success': bool
        }

        self.attribute_map = {
            'data': 'data',
            'success': 'success'
        }

        self._data = data
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateSuccessResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateSuccessResponse of this CreateSuccessResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this CreateSuccessResponse.


        :return: The data of this CreateSuccessResponse.
        :rtype: ClockingRecordsPost201ResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateSuccessResponse.


        :param data: The data of this CreateSuccessResponse.
        :type data: ClockingRecordsPost201ResponseData
        """

        self._data = data

    @property
    def success(self):
        """Gets the success of this CreateSuccessResponse.


        :return: The success of this CreateSuccessResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CreateSuccessResponse.


        :param success: The success of this CreateSuccessResponse.
        :type success: bool
        """

        self._success = success
