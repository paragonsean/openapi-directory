# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.agent_properties import AgentProperties
from openapi_server.models.credentials import Credentials
from openapi_server.models.platform_properties import PlatformProperties
from openapi_server.models.run_request import RunRequest
from openapi_server.models.set_value import SetValue
from openapi_server import util


class EncodedTaskRunRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, agent_configuration: AgentProperties=None, credentials: Credentials=None, encoded_task_content: str=None, encoded_values_content: str=None, platform: PlatformProperties=None, source_location: str=None, timeout: int=3600, values: List[SetValue]=None, is_archive_enabled: bool=False, type: str=None):
        """EncodedTaskRunRequest - a model defined in OpenAPI

        :param agent_configuration: The agent_configuration of this EncodedTaskRunRequest.
        :param credentials: The credentials of this EncodedTaskRunRequest.
        :param encoded_task_content: The encoded_task_content of this EncodedTaskRunRequest.
        :param encoded_values_content: The encoded_values_content of this EncodedTaskRunRequest.
        :param platform: The platform of this EncodedTaskRunRequest.
        :param source_location: The source_location of this EncodedTaskRunRequest.
        :param timeout: The timeout of this EncodedTaskRunRequest.
        :param values: The values of this EncodedTaskRunRequest.
        :param is_archive_enabled: The is_archive_enabled of this EncodedTaskRunRequest.
        :param type: The type of this EncodedTaskRunRequest.
        """
        self.openapi_types = {
            'agent_configuration': AgentProperties,
            'credentials': Credentials,
            'encoded_task_content': str,
            'encoded_values_content': str,
            'platform': PlatformProperties,
            'source_location': str,
            'timeout': int,
            'values': List[SetValue],
            'is_archive_enabled': bool,
            'type': str
        }

        self.attribute_map = {
            'agent_configuration': 'agentConfiguration',
            'credentials': 'credentials',
            'encoded_task_content': 'encodedTaskContent',
            'encoded_values_content': 'encodedValuesContent',
            'platform': 'platform',
            'source_location': 'sourceLocation',
            'timeout': 'timeout',
            'values': 'values',
            'is_archive_enabled': 'isArchiveEnabled',
            'type': 'type'
        }

        self._agent_configuration = agent_configuration
        self._credentials = credentials
        self._encoded_task_content = encoded_task_content
        self._encoded_values_content = encoded_values_content
        self._platform = platform
        self._source_location = source_location
        self._timeout = timeout
        self._values = values
        self._is_archive_enabled = is_archive_enabled
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EncodedTaskRunRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EncodedTaskRunRequest of this EncodedTaskRunRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def agent_configuration(self):
        """Gets the agent_configuration of this EncodedTaskRunRequest.


        :return: The agent_configuration of this EncodedTaskRunRequest.
        :rtype: AgentProperties
        """
        return self._agent_configuration

    @agent_configuration.setter
    def agent_configuration(self, agent_configuration):
        """Sets the agent_configuration of this EncodedTaskRunRequest.


        :param agent_configuration: The agent_configuration of this EncodedTaskRunRequest.
        :type agent_configuration: AgentProperties
        """

        self._agent_configuration = agent_configuration

    @property
    def credentials(self):
        """Gets the credentials of this EncodedTaskRunRequest.


        :return: The credentials of this EncodedTaskRunRequest.
        :rtype: Credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this EncodedTaskRunRequest.


        :param credentials: The credentials of this EncodedTaskRunRequest.
        :type credentials: Credentials
        """

        self._credentials = credentials

    @property
    def encoded_task_content(self):
        """Gets the encoded_task_content of this EncodedTaskRunRequest.

        Base64 encoded value of the template/definition file content.

        :return: The encoded_task_content of this EncodedTaskRunRequest.
        :rtype: str
        """
        return self._encoded_task_content

    @encoded_task_content.setter
    def encoded_task_content(self, encoded_task_content):
        """Sets the encoded_task_content of this EncodedTaskRunRequest.

        Base64 encoded value of the template/definition file content.

        :param encoded_task_content: The encoded_task_content of this EncodedTaskRunRequest.
        :type encoded_task_content: str
        """
        if encoded_task_content is None:
            raise ValueError("Invalid value for `encoded_task_content`, must not be `None`")

        self._encoded_task_content = encoded_task_content

    @property
    def encoded_values_content(self):
        """Gets the encoded_values_content of this EncodedTaskRunRequest.

        Base64 encoded value of the parameters/values file content.

        :return: The encoded_values_content of this EncodedTaskRunRequest.
        :rtype: str
        """
        return self._encoded_values_content

    @encoded_values_content.setter
    def encoded_values_content(self, encoded_values_content):
        """Sets the encoded_values_content of this EncodedTaskRunRequest.

        Base64 encoded value of the parameters/values file content.

        :param encoded_values_content: The encoded_values_content of this EncodedTaskRunRequest.
        :type encoded_values_content: str
        """

        self._encoded_values_content = encoded_values_content

    @property
    def platform(self):
        """Gets the platform of this EncodedTaskRunRequest.


        :return: The platform of this EncodedTaskRunRequest.
        :rtype: PlatformProperties
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this EncodedTaskRunRequest.


        :param platform: The platform of this EncodedTaskRunRequest.
        :type platform: PlatformProperties
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")

        self._platform = platform

    @property
    def source_location(self):
        """Gets the source_location of this EncodedTaskRunRequest.

        The URL(absolute or relative) of the source context. It can be an URL to a tar or git repository.  If it is relative URL, the relative path should be obtained from calling listBuildSourceUploadUrl API.

        :return: The source_location of this EncodedTaskRunRequest.
        :rtype: str
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """Sets the source_location of this EncodedTaskRunRequest.

        The URL(absolute or relative) of the source context. It can be an URL to a tar or git repository.  If it is relative URL, the relative path should be obtained from calling listBuildSourceUploadUrl API.

        :param source_location: The source_location of this EncodedTaskRunRequest.
        :type source_location: str
        """

        self._source_location = source_location

    @property
    def timeout(self):
        """Gets the timeout of this EncodedTaskRunRequest.

        Run timeout in seconds.

        :return: The timeout of this EncodedTaskRunRequest.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this EncodedTaskRunRequest.

        Run timeout in seconds.

        :param timeout: The timeout of this EncodedTaskRunRequest.
        :type timeout: int
        """
        if timeout is not None and timeout > 28800:
            raise ValueError("Invalid value for `timeout`, must be a value less than or equal to `28800`")
        if timeout is not None and timeout < 300:
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `300`")

        self._timeout = timeout

    @property
    def values(self):
        """Gets the values of this EncodedTaskRunRequest.

        The collection of overridable values that can be passed when running a task.

        :return: The values of this EncodedTaskRunRequest.
        :rtype: List[SetValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this EncodedTaskRunRequest.

        The collection of overridable values that can be passed when running a task.

        :param values: The values of this EncodedTaskRunRequest.
        :type values: List[SetValue]
        """

        self._values = values

    @property
    def is_archive_enabled(self):
        """Gets the is_archive_enabled of this EncodedTaskRunRequest.

        The value that indicates whether archiving is enabled for the run or not.

        :return: The is_archive_enabled of this EncodedTaskRunRequest.
        :rtype: bool
        """
        return self._is_archive_enabled

    @is_archive_enabled.setter
    def is_archive_enabled(self, is_archive_enabled):
        """Sets the is_archive_enabled of this EncodedTaskRunRequest.

        The value that indicates whether archiving is enabled for the run or not.

        :param is_archive_enabled: The is_archive_enabled of this EncodedTaskRunRequest.
        :type is_archive_enabled: bool
        """

        self._is_archive_enabled = is_archive_enabled

    @property
    def type(self):
        """Gets the type of this EncodedTaskRunRequest.

        The type of the run request.

        :return: The type of this EncodedTaskRunRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EncodedTaskRunRequest.

        The type of the run request.

        :param type: The type of this EncodedTaskRunRequest.
        :type type: str
        """

        self._type = type
