# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.code_push_deployments_list200_response_inner_latest_release import CodePushDeploymentsList200ResponseInnerLatestRelease
from openapi_server import util


class CodePushDeploymentsList200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, latest_release: CodePushDeploymentsList200ResponseInnerLatestRelease=None, name: str=None):
        """CodePushDeploymentsList200ResponseInner - a model defined in OpenAPI

        :param key: The key of this CodePushDeploymentsList200ResponseInner.
        :param latest_release: The latest_release of this CodePushDeploymentsList200ResponseInner.
        :param name: The name of this CodePushDeploymentsList200ResponseInner.
        """
        self.openapi_types = {
            'key': str,
            'latest_release': CodePushDeploymentsList200ResponseInnerLatestRelease,
            'name': str
        }

        self.attribute_map = {
            'key': 'key',
            'latest_release': 'latest_release',
            'name': 'name'
        }

        self._key = key
        self._latest_release = latest_release
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CodePushDeploymentsList200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The codePushDeployments_list_200_response_inner of this CodePushDeploymentsList200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this CodePushDeploymentsList200ResponseInner.


        :return: The key of this CodePushDeploymentsList200ResponseInner.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CodePushDeploymentsList200ResponseInner.


        :param key: The key of this CodePushDeploymentsList200ResponseInner.
        :type key: str
        """

        self._key = key

    @property
    def latest_release(self):
        """Gets the latest_release of this CodePushDeploymentsList200ResponseInner.


        :return: The latest_release of this CodePushDeploymentsList200ResponseInner.
        :rtype: CodePushDeploymentsList200ResponseInnerLatestRelease
        """
        return self._latest_release

    @latest_release.setter
    def latest_release(self, latest_release):
        """Sets the latest_release of this CodePushDeploymentsList200ResponseInner.


        :param latest_release: The latest_release of this CodePushDeploymentsList200ResponseInner.
        :type latest_release: CodePushDeploymentsList200ResponseInnerLatestRelease
        """

        self._latest_release = latest_release

    @property
    def name(self):
        """Gets the name of this CodePushDeploymentsList200ResponseInner.


        :return: The name of this CodePushDeploymentsList200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodePushDeploymentsList200ResponseInner.


        :param name: The name of this CodePushDeploymentsList200ResponseInner.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
