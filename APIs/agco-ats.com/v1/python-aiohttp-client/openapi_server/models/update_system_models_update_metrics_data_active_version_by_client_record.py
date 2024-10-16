# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bundle_number: int=None, client_count: int=None, release_name: str=None):
        """UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord - a model defined in OpenAPI

        :param bundle_number: The bundle_number of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :param client_count: The client_count of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :param release_name: The release_name of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        """
        self.openapi_types = {
            'bundle_number': int,
            'client_count': int,
            'release_name': str
        }

        self.attribute_map = {
            'bundle_number': 'BundleNumber',
            'client_count': 'ClientCount',
            'release_name': 'ReleaseName'
        }

        self._bundle_number = bundle_number
        self._client_count = client_count
        self._release_name = release_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateSystem.Models.UpdateMetricsData.ActiveVersionByClientRecord of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bundle_number(self):
        """Gets the bundle_number of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.


        :return: The bundle_number of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :rtype: int
        """
        return self._bundle_number

    @bundle_number.setter
    def bundle_number(self, bundle_number):
        """Sets the bundle_number of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.


        :param bundle_number: The bundle_number of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :type bundle_number: int
        """

        self._bundle_number = bundle_number

    @property
    def client_count(self):
        """Gets the client_count of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.


        :return: The client_count of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :rtype: int
        """
        return self._client_count

    @client_count.setter
    def client_count(self, client_count):
        """Sets the client_count of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.


        :param client_count: The client_count of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :type client_count: int
        """

        self._client_count = client_count

    @property
    def release_name(self):
        """Gets the release_name of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.


        :return: The release_name of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """Sets the release_name of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.


        :param release_name: The release_name of this UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.
        :type release_name: str
        """

        self._release_name = release_name
