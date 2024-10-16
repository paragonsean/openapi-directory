# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PerformanceReportPerformanceDataStepsInnerSamplesInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cpu: float=None, elapsed_secs: float=None, mem: float=None):
        """PerformanceReportPerformanceDataStepsInnerSamplesInner - a model defined in OpenAPI

        :param cpu: The cpu of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :param elapsed_secs: The elapsed_secs of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :param mem: The mem of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        """
        self.openapi_types = {
            'cpu': float,
            'elapsed_secs': float,
            'mem': float
        }

        self.attribute_map = {
            'cpu': 'cpu',
            'elapsed_secs': 'elapsed-secs',
            'mem': 'mem'
        }

        self._cpu = cpu
        self._elapsed_secs = elapsed_secs
        self._mem = mem

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PerformanceReportPerformanceDataStepsInnerSamplesInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PerformanceReport_performance_data_steps_inner_samples_inner of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cpu(self):
        """Gets the cpu of this PerformanceReportPerformanceDataStepsInnerSamplesInner.


        :return: The cpu of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this PerformanceReportPerformanceDataStepsInnerSamplesInner.


        :param cpu: The cpu of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :type cpu: float
        """

        self._cpu = cpu

    @property
    def elapsed_secs(self):
        """Gets the elapsed_secs of this PerformanceReportPerformanceDataStepsInnerSamplesInner.


        :return: The elapsed_secs of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :rtype: float
        """
        return self._elapsed_secs

    @elapsed_secs.setter
    def elapsed_secs(self, elapsed_secs):
        """Sets the elapsed_secs of this PerformanceReportPerformanceDataStepsInnerSamplesInner.


        :param elapsed_secs: The elapsed_secs of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :type elapsed_secs: float
        """

        self._elapsed_secs = elapsed_secs

    @property
    def mem(self):
        """Gets the mem of this PerformanceReportPerformanceDataStepsInnerSamplesInner.


        :return: The mem of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :rtype: float
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this PerformanceReportPerformanceDataStepsInnerSamplesInner.


        :param mem: The mem of this PerformanceReportPerformanceDataStepsInnerSamplesInner.
        :type mem: float
        """

        self._mem = mem
