# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.cluster_configuration_clustering import ClusterConfigurationClustering
from openapi_server.models.cluster_configuration_routing import ClusterConfigurationRouting
from openapi_server import util


class ClusterConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, clustering: ClusterConfigurationClustering=None, response_type: str='json', routing: ClusterConfigurationRouting=None):
        """ClusterConfiguration - a model defined in OpenAPI

        :param clustering: The clustering of this ClusterConfiguration.
        :param response_type: The response_type of this ClusterConfiguration.
        :param routing: The routing of this ClusterConfiguration.
        """
        self.openapi_types = {
            'clustering': ClusterConfigurationClustering,
            'response_type': str,
            'routing': ClusterConfigurationRouting
        }

        self.attribute_map = {
            'clustering': 'clustering',
            'response_type': 'response_type',
            'routing': 'routing'
        }

        self._clustering = clustering
        self._response_type = response_type
        self._routing = routing

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ClusterConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ClusterConfiguration of this ClusterConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def clustering(self):
        """Gets the clustering of this ClusterConfiguration.


        :return: The clustering of this ClusterConfiguration.
        :rtype: ClusterConfigurationClustering
        """
        return self._clustering

    @clustering.setter
    def clustering(self, clustering):
        """Sets the clustering of this ClusterConfiguration.


        :param clustering: The clustering of this ClusterConfiguration.
        :type clustering: ClusterConfigurationClustering
        """

        self._clustering = clustering

    @property
    def response_type(self):
        """Gets the response_type of this ClusterConfiguration.

        Specifies the response format. You can either choose `geojson` or `json`.

        :return: The response_type of this ClusterConfiguration.
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this ClusterConfiguration.

        Specifies the response format. You can either choose `geojson` or `json`.

        :param response_type: The response_type of this ClusterConfiguration.
        :type response_type: str
        """

        self._response_type = response_type

    @property
    def routing(self):
        """Gets the routing of this ClusterConfiguration.


        :return: The routing of this ClusterConfiguration.
        :rtype: ClusterConfigurationRouting
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """Sets the routing of this ClusterConfiguration.


        :param routing: The routing of this ClusterConfiguration.
        :type routing: ClusterConfigurationRouting
        """

        self._routing = routing
