# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class K8SContext(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cluster_name: str=None, context_name: str=None, current_context: bool=None):
        """K8SContext - a model defined in OpenAPI

        :param cluster_name: The cluster_name of this K8SContext.
        :param context_name: The context_name of this K8SContext.
        :param current_context: The current_context of this K8SContext.
        """
        self.openapi_types = {
            'cluster_name': str,
            'context_name': str,
            'current_context': bool
        }

        self.attribute_map = {
            'cluster_name': 'clusterName',
            'context_name': 'contextName',
            'current_context': 'currentContext'
        }

        self._cluster_name = cluster_name
        self._context_name = context_name
        self._current_context = current_context

    @classmethod
    def from_dict(cls, dikt: dict) -> 'K8SContext':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The K8SContext of this K8SContext.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cluster_name(self):
        """Gets the cluster_name of this K8SContext.


        :return: The cluster_name of this K8SContext.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this K8SContext.


        :param cluster_name: The cluster_name of this K8SContext.
        :type cluster_name: str
        """

        self._cluster_name = cluster_name

    @property
    def context_name(self):
        """Gets the context_name of this K8SContext.


        :return: The context_name of this K8SContext.
        :rtype: str
        """
        return self._context_name

    @context_name.setter
    def context_name(self, context_name):
        """Sets the context_name of this K8SContext.


        :param context_name: The context_name of this K8SContext.
        :type context_name: str
        """

        self._context_name = context_name

    @property
    def current_context(self):
        """Gets the current_context of this K8SContext.

        ContextDisplayName string `json:\"context-display-name\"`

        :return: The current_context of this K8SContext.
        :rtype: bool
        """
        return self._current_context

    @current_context.setter
    def current_context(self, current_context):
        """Sets the current_context of this K8SContext.

        ContextDisplayName string `json:\"context-display-name\"`

        :param current_context: The current_context of this K8SContext.
        :type current_context: bool
        """

        self._current_context = current_context
