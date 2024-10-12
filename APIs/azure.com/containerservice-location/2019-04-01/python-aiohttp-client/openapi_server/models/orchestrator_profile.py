# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OrchestratorProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_preview: bool=None, orchestrator_type: str=None, orchestrator_version: str=None):
        """OrchestratorProfile - a model defined in OpenAPI

        :param is_preview: The is_preview of this OrchestratorProfile.
        :param orchestrator_type: The orchestrator_type of this OrchestratorProfile.
        :param orchestrator_version: The orchestrator_version of this OrchestratorProfile.
        """
        self.openapi_types = {
            'is_preview': bool,
            'orchestrator_type': str,
            'orchestrator_version': str
        }

        self.attribute_map = {
            'is_preview': 'isPreview',
            'orchestrator_type': 'orchestratorType',
            'orchestrator_version': 'orchestratorVersion'
        }

        self._is_preview = is_preview
        self._orchestrator_type = orchestrator_type
        self._orchestrator_version = orchestrator_version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrchestratorProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrchestratorProfile of this OrchestratorProfile.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_preview(self):
        """Gets the is_preview of this OrchestratorProfile.

        Whether Kubernetes version is currently in preview.

        :return: The is_preview of this OrchestratorProfile.
        :rtype: bool
        """
        return self._is_preview

    @is_preview.setter
    def is_preview(self, is_preview):
        """Sets the is_preview of this OrchestratorProfile.

        Whether Kubernetes version is currently in preview.

        :param is_preview: The is_preview of this OrchestratorProfile.
        :type is_preview: bool
        """

        self._is_preview = is_preview

    @property
    def orchestrator_type(self):
        """Gets the orchestrator_type of this OrchestratorProfile.

        Orchestrator type.

        :return: The orchestrator_type of this OrchestratorProfile.
        :rtype: str
        """
        return self._orchestrator_type

    @orchestrator_type.setter
    def orchestrator_type(self, orchestrator_type):
        """Sets the orchestrator_type of this OrchestratorProfile.

        Orchestrator type.

        :param orchestrator_type: The orchestrator_type of this OrchestratorProfile.
        :type orchestrator_type: str
        """

        self._orchestrator_type = orchestrator_type

    @property
    def orchestrator_version(self):
        """Gets the orchestrator_version of this OrchestratorProfile.

        Orchestrator version (major, minor, patch).

        :return: The orchestrator_version of this OrchestratorProfile.
        :rtype: str
        """
        return self._orchestrator_version

    @orchestrator_version.setter
    def orchestrator_version(self, orchestrator_version):
        """Sets the orchestrator_version of this OrchestratorProfile.

        Orchestrator version (major, minor, patch).

        :param orchestrator_version: The orchestrator_version of this OrchestratorProfile.
        :type orchestrator_version: str
        """
        if orchestrator_version is None:
            raise ValueError("Invalid value for `orchestrator_version`, must not be `None`")

        self._orchestrator_version = orchestrator_version
