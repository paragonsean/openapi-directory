# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.latencies_ms import LatenciesMs
from openapi_server import util


class PerformanceSpec(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, actual_qps: float=None, details_uri: str=None, end_time: datetime=None, env_id: str=None, latencies: LatenciesMs=None, mesh_config_id: str=None, smp_version: str=None, start_time: datetime=None, test_id: str=None):
        """PerformanceSpec - a model defined in OpenAPI

        :param actual_qps: The actual_qps of this PerformanceSpec.
        :param details_uri: The details_uri of this PerformanceSpec.
        :param end_time: The end_time of this PerformanceSpec.
        :param env_id: The env_id of this PerformanceSpec.
        :param latencies: The latencies of this PerformanceSpec.
        :param mesh_config_id: The mesh_config_id of this PerformanceSpec.
        :param smp_version: The smp_version of this PerformanceSpec.
        :param start_time: The start_time of this PerformanceSpec.
        :param test_id: The test_id of this PerformanceSpec.
        """
        self.openapi_types = {
            'actual_qps': float,
            'details_uri': str,
            'end_time': datetime,
            'env_id': str,
            'latencies': LatenciesMs,
            'mesh_config_id': str,
            'smp_version': str,
            'start_time': datetime,
            'test_id': str
        }

        self.attribute_map = {
            'actual_qps': 'ActualQPS',
            'details_uri': 'DetailsURI',
            'end_time': 'EndTime',
            'env_id': 'EnvID',
            'latencies': 'Latencies',
            'mesh_config_id': 'MeshConfigID',
            'smp_version': 'SMPVersion',
            'start_time': 'StartTime',
            'test_id': 'TestID'
        }

        self._actual_qps = actual_qps
        self._details_uri = details_uri
        self._end_time = end_time
        self._env_id = env_id
        self._latencies = latencies
        self._mesh_config_id = mesh_config_id
        self._smp_version = smp_version
        self._start_time = start_time
        self._test_id = test_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PerformanceSpec':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PerformanceSpec of this PerformanceSpec.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def actual_qps(self):
        """Gets the actual_qps of this PerformanceSpec.


        :return: The actual_qps of this PerformanceSpec.
        :rtype: float
        """
        return self._actual_qps

    @actual_qps.setter
    def actual_qps(self, actual_qps):
        """Sets the actual_qps of this PerformanceSpec.


        :param actual_qps: The actual_qps of this PerformanceSpec.
        :type actual_qps: float
        """

        self._actual_qps = actual_qps

    @property
    def details_uri(self):
        """Gets the details_uri of this PerformanceSpec.


        :return: The details_uri of this PerformanceSpec.
        :rtype: str
        """
        return self._details_uri

    @details_uri.setter
    def details_uri(self, details_uri):
        """Sets the details_uri of this PerformanceSpec.


        :param details_uri: The details_uri of this PerformanceSpec.
        :type details_uri: str
        """

        self._details_uri = details_uri

    @property
    def end_time(self):
        """Gets the end_time of this PerformanceSpec.


        :return: The end_time of this PerformanceSpec.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PerformanceSpec.


        :param end_time: The end_time of this PerformanceSpec.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def env_id(self):
        """Gets the env_id of this PerformanceSpec.


        :return: The env_id of this PerformanceSpec.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this PerformanceSpec.


        :param env_id: The env_id of this PerformanceSpec.
        :type env_id: str
        """

        self._env_id = env_id

    @property
    def latencies(self):
        """Gets the latencies of this PerformanceSpec.


        :return: The latencies of this PerformanceSpec.
        :rtype: LatenciesMs
        """
        return self._latencies

    @latencies.setter
    def latencies(self, latencies):
        """Sets the latencies of this PerformanceSpec.


        :param latencies: The latencies of this PerformanceSpec.
        :type latencies: LatenciesMs
        """

        self._latencies = latencies

    @property
    def mesh_config_id(self):
        """Gets the mesh_config_id of this PerformanceSpec.


        :return: The mesh_config_id of this PerformanceSpec.
        :rtype: str
        """
        return self._mesh_config_id

    @mesh_config_id.setter
    def mesh_config_id(self, mesh_config_id):
        """Sets the mesh_config_id of this PerformanceSpec.


        :param mesh_config_id: The mesh_config_id of this PerformanceSpec.
        :type mesh_config_id: str
        """

        self._mesh_config_id = mesh_config_id

    @property
    def smp_version(self):
        """Gets the smp_version of this PerformanceSpec.


        :return: The smp_version of this PerformanceSpec.
        :rtype: str
        """
        return self._smp_version

    @smp_version.setter
    def smp_version(self, smp_version):
        """Sets the smp_version of this PerformanceSpec.


        :param smp_version: The smp_version of this PerformanceSpec.
        :type smp_version: str
        """

        self._smp_version = smp_version

    @property
    def start_time(self):
        """Gets the start_time of this PerformanceSpec.


        :return: The start_time of this PerformanceSpec.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PerformanceSpec.


        :param start_time: The start_time of this PerformanceSpec.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def test_id(self):
        """Gets the test_id of this PerformanceSpec.


        :return: The test_id of this PerformanceSpec.
        :rtype: str
        """
        return self._test_id

    @test_id.setter
    def test_id(self, test_id):
        """Sets the test_id of this PerformanceSpec.


        :param test_id: The test_id of this PerformanceSpec.
        :type test_id: str
        """

        self._test_id = test_id
