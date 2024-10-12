# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.base_image_dependency import BaseImageDependency
from openapi_server import util


class TaskStepProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, base_image_dependencies: List[BaseImageDependency]=None, context_access_token: str=None, context_path: str=None, type: str=None):
        """TaskStepProperties - a model defined in OpenAPI

        :param base_image_dependencies: The base_image_dependencies of this TaskStepProperties.
        :param context_access_token: The context_access_token of this TaskStepProperties.
        :param context_path: The context_path of this TaskStepProperties.
        :param type: The type of this TaskStepProperties.
        """
        self.openapi_types = {
            'base_image_dependencies': List[BaseImageDependency],
            'context_access_token': str,
            'context_path': str,
            'type': str
        }

        self.attribute_map = {
            'base_image_dependencies': 'baseImageDependencies',
            'context_access_token': 'contextAccessToken',
            'context_path': 'contextPath',
            'type': 'type'
        }

        self._base_image_dependencies = base_image_dependencies
        self._context_access_token = context_access_token
        self._context_path = context_path
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaskStepProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TaskStepProperties of this TaskStepProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def base_image_dependencies(self):
        """Gets the base_image_dependencies of this TaskStepProperties.

        List of base image dependencies for a step.

        :return: The base_image_dependencies of this TaskStepProperties.
        :rtype: List[BaseImageDependency]
        """
        return self._base_image_dependencies

    @base_image_dependencies.setter
    def base_image_dependencies(self, base_image_dependencies):
        """Sets the base_image_dependencies of this TaskStepProperties.

        List of base image dependencies for a step.

        :param base_image_dependencies: The base_image_dependencies of this TaskStepProperties.
        :type base_image_dependencies: List[BaseImageDependency]
        """

        self._base_image_dependencies = base_image_dependencies

    @property
    def context_access_token(self):
        """Gets the context_access_token of this TaskStepProperties.

        The token (git PAT or SAS token of storage account blob) associated with the context for a step.

        :return: The context_access_token of this TaskStepProperties.
        :rtype: str
        """
        return self._context_access_token

    @context_access_token.setter
    def context_access_token(self, context_access_token):
        """Sets the context_access_token of this TaskStepProperties.

        The token (git PAT or SAS token of storage account blob) associated with the context for a step.

        :param context_access_token: The context_access_token of this TaskStepProperties.
        :type context_access_token: str
        """

        self._context_access_token = context_access_token

    @property
    def context_path(self):
        """Gets the context_path of this TaskStepProperties.

        The URL(absolute or relative) of the source context for the task step.

        :return: The context_path of this TaskStepProperties.
        :rtype: str
        """
        return self._context_path

    @context_path.setter
    def context_path(self, context_path):
        """Sets the context_path of this TaskStepProperties.

        The URL(absolute or relative) of the source context for the task step.

        :param context_path: The context_path of this TaskStepProperties.
        :type context_path: str
        """

        self._context_path = context_path

    @property
    def type(self):
        """Gets the type of this TaskStepProperties.

        The type of the step.

        :return: The type of this TaskStepProperties.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskStepProperties.

        The type of the step.

        :param type: The type of this TaskStepProperties.
        :type type: str
        """
        allowed_values = ["Docker", "FileTask", "EncodedTask"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
