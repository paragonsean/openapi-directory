# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.adapter import Adapter
from openapi_server.models.grafana import Grafana
from openapi_server.models.k8_s_config import K8SConfig
from openapi_server.models.load_test_preferences import LoadTestPreferences
from openapi_server.models.prometheus import Prometheus
from openapi_server import util


class Preference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, anonymous_perf_results: bool=None, anonymous_usage_stats: bool=None, grafana: Grafana=None, k8s_config: K8SConfig=None, load_test_prefs: LoadTestPreferences=None, mesh_adapters: List[Adapter]=None, prometheus: Prometheus=None, updated_at: datetime=None):
        """Preference - a model defined in OpenAPI

        :param anonymous_perf_results: The anonymous_perf_results of this Preference.
        :param anonymous_usage_stats: The anonymous_usage_stats of this Preference.
        :param grafana: The grafana of this Preference.
        :param k8s_config: The k8s_config of this Preference.
        :param load_test_prefs: The load_test_prefs of this Preference.
        :param mesh_adapters: The mesh_adapters of this Preference.
        :param prometheus: The prometheus of this Preference.
        :param updated_at: The updated_at of this Preference.
        """
        self.openapi_types = {
            'anonymous_perf_results': bool,
            'anonymous_usage_stats': bool,
            'grafana': Grafana,
            'k8s_config': K8SConfig,
            'load_test_prefs': LoadTestPreferences,
            'mesh_adapters': List[Adapter],
            'prometheus': Prometheus,
            'updated_at': datetime
        }

        self.attribute_map = {
            'anonymous_perf_results': 'anonymousPerfResults',
            'anonymous_usage_stats': 'anonymousUsageStats',
            'grafana': 'grafana',
            'k8s_config': 'k8sConfig',
            'load_test_prefs': 'loadTestPrefs',
            'mesh_adapters': 'meshAdapters',
            'prometheus': 'prometheus',
            'updated_at': 'updated_at'
        }

        self._anonymous_perf_results = anonymous_perf_results
        self._anonymous_usage_stats = anonymous_usage_stats
        self._grafana = grafana
        self._k8s_config = k8s_config
        self._load_test_prefs = load_test_prefs
        self._mesh_adapters = mesh_adapters
        self._prometheus = prometheus
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Preference':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Preference of this Preference.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def anonymous_perf_results(self):
        """Gets the anonymous_perf_results of this Preference.


        :return: The anonymous_perf_results of this Preference.
        :rtype: bool
        """
        return self._anonymous_perf_results

    @anonymous_perf_results.setter
    def anonymous_perf_results(self, anonymous_perf_results):
        """Sets the anonymous_perf_results of this Preference.


        :param anonymous_perf_results: The anonymous_perf_results of this Preference.
        :type anonymous_perf_results: bool
        """

        self._anonymous_perf_results = anonymous_perf_results

    @property
    def anonymous_usage_stats(self):
        """Gets the anonymous_usage_stats of this Preference.


        :return: The anonymous_usage_stats of this Preference.
        :rtype: bool
        """
        return self._anonymous_usage_stats

    @anonymous_usage_stats.setter
    def anonymous_usage_stats(self, anonymous_usage_stats):
        """Sets the anonymous_usage_stats of this Preference.


        :param anonymous_usage_stats: The anonymous_usage_stats of this Preference.
        :type anonymous_usage_stats: bool
        """

        self._anonymous_usage_stats = anonymous_usage_stats

    @property
    def grafana(self):
        """Gets the grafana of this Preference.


        :return: The grafana of this Preference.
        :rtype: Grafana
        """
        return self._grafana

    @grafana.setter
    def grafana(self, grafana):
        """Sets the grafana of this Preference.


        :param grafana: The grafana of this Preference.
        :type grafana: Grafana
        """

        self._grafana = grafana

    @property
    def k8s_config(self):
        """Gets the k8s_config of this Preference.


        :return: The k8s_config of this Preference.
        :rtype: K8SConfig
        """
        return self._k8s_config

    @k8s_config.setter
    def k8s_config(self, k8s_config):
        """Sets the k8s_config of this Preference.


        :param k8s_config: The k8s_config of this Preference.
        :type k8s_config: K8SConfig
        """

        self._k8s_config = k8s_config

    @property
    def load_test_prefs(self):
        """Gets the load_test_prefs of this Preference.


        :return: The load_test_prefs of this Preference.
        :rtype: LoadTestPreferences
        """
        return self._load_test_prefs

    @load_test_prefs.setter
    def load_test_prefs(self, load_test_prefs):
        """Sets the load_test_prefs of this Preference.


        :param load_test_prefs: The load_test_prefs of this Preference.
        :type load_test_prefs: LoadTestPreferences
        """

        self._load_test_prefs = load_test_prefs

    @property
    def mesh_adapters(self):
        """Gets the mesh_adapters of this Preference.


        :return: The mesh_adapters of this Preference.
        :rtype: List[Adapter]
        """
        return self._mesh_adapters

    @mesh_adapters.setter
    def mesh_adapters(self, mesh_adapters):
        """Sets the mesh_adapters of this Preference.


        :param mesh_adapters: The mesh_adapters of this Preference.
        :type mesh_adapters: List[Adapter]
        """

        self._mesh_adapters = mesh_adapters

    @property
    def prometheus(self):
        """Gets the prometheus of this Preference.


        :return: The prometheus of this Preference.
        :rtype: Prometheus
        """
        return self._prometheus

    @prometheus.setter
    def prometheus(self, prometheus):
        """Sets the prometheus of this Preference.


        :param prometheus: The prometheus of this Preference.
        :type prometheus: Prometheus
        """

        self._prometheus = prometheus

    @property
    def updated_at(self):
        """Gets the updated_at of this Preference.


        :return: The updated_at of this Preference.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Preference.


        :param updated_at: The updated_at of this Preference.
        :type updated_at: datetime
        """

        self._updated_at = updated_at
