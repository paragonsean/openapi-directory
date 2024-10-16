# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_count: int=None, error_code: str=None, long_description: str=None, short_description: str=None):
        """UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord - a model defined in OpenAPI

        :param client_count: The client_count of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :param error_code: The error_code of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :param long_description: The long_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :param short_description: The short_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        """
        self.openapi_types = {
            'client_count': int,
            'error_code': str,
            'long_description': str,
            'short_description': str
        }

        self.attribute_map = {
            'client_count': 'ClientCount',
            'error_code': 'ErrorCode',
            'long_description': 'LongDescription',
            'short_description': 'ShortDescription'
        }

        self._client_count = client_count
        self._error_code = error_code
        self._long_description = long_description
        self._short_description = short_description

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateSystem.Models.UpdateMetricsData.PackageErrorsRecord of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_count(self):
        """Gets the client_count of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :return: The client_count of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :rtype: int
        """
        return self._client_count

    @client_count.setter
    def client_count(self, client_count):
        """Sets the client_count of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :param client_count: The client_count of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :type client_count: int
        """

        self._client_count = client_count

    @property
    def error_code(self):
        """Gets the error_code of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :return: The error_code of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :param error_code: The error_code of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def long_description(self):
        """Gets the long_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :return: The long_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :param long_description: The long_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :type long_description: str
        """

        self._long_description = long_description

    @property
    def short_description(self):
        """Gets the short_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :return: The short_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.


        :param short_description: The short_description of this UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.
        :type short_description: str
        """

        self._short_description = short_description
