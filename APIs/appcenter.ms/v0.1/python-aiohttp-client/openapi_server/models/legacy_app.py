# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.legacy_app_collaborators_value import LegacyAppCollaboratorsValue
from openapi_server import util


class LegacyApp(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, collaborators: Dict[str, LegacyAppCollaboratorsValue]=None, deployments: List[str]=None, name: str=None):
        """LegacyApp - a model defined in OpenAPI

        :param collaborators: The collaborators of this LegacyApp.
        :param deployments: The deployments of this LegacyApp.
        :param name: The name of this LegacyApp.
        """
        self.openapi_types = {
            'collaborators': Dict[str, LegacyAppCollaboratorsValue],
            'deployments': List[str],
            'name': str
        }

        self.attribute_map = {
            'collaborators': 'collaborators',
            'deployments': 'deployments',
            'name': 'name'
        }

        self._collaborators = collaborators
        self._deployments = deployments
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LegacyApp':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LegacyApp of this LegacyApp.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def collaborators(self):
        """Gets the collaborators of this LegacyApp.


        :return: The collaborators of this LegacyApp.
        :rtype: Dict[str, LegacyAppCollaboratorsValue]
        """
        return self._collaborators

    @collaborators.setter
    def collaborators(self, collaborators):
        """Sets the collaborators of this LegacyApp.


        :param collaborators: The collaborators of this LegacyApp.
        :type collaborators: Dict[str, LegacyAppCollaboratorsValue]
        """

        self._collaborators = collaborators

    @property
    def deployments(self):
        """Gets the deployments of this LegacyApp.


        :return: The deployments of this LegacyApp.
        :rtype: List[str]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this LegacyApp.


        :param deployments: The deployments of this LegacyApp.
        :type deployments: List[str]
        """

        self._deployments = deployments

    @property
    def name(self):
        """Gets the name of this LegacyApp.

        The app name.

        :return: The name of this LegacyApp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LegacyApp.

        The app name.

        :param name: The name of this LegacyApp.
        :type name: str
        """

        self._name = name
