# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.branch_configurations_get200_response_all_of_artifact_versioning import BranchConfigurationsGet200ResponseAllOfArtifactVersioning
from openapi_server.models.branch_configurations_get200_response_all_of_toolsets import BranchConfigurationsGet200ResponseAllOfToolsets
from openapi_server.models.builds_list_branches200_response_inner_value import BuildsListBranches200ResponseInnerValue
from openapi_server import util


class BranchConfigurationsGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, artifact_versioning: BranchConfigurationsGet200ResponseAllOfArtifactVersioning=None, badge_is_enabled: bool=None, clone_from_branch: str=None, signed: bool=None, tests_enabled: bool=None, toolsets: BranchConfigurationsGet200ResponseAllOfToolsets=None, trigger: str=None, id: int=None):
        """BranchConfigurationsGet200Response - a model defined in OpenAPI

        :param artifact_versioning: The artifact_versioning of this BranchConfigurationsGet200Response.
        :param badge_is_enabled: The badge_is_enabled of this BranchConfigurationsGet200Response.
        :param clone_from_branch: The clone_from_branch of this BranchConfigurationsGet200Response.
        :param signed: The signed of this BranchConfigurationsGet200Response.
        :param tests_enabled: The tests_enabled of this BranchConfigurationsGet200Response.
        :param toolsets: The toolsets of this BranchConfigurationsGet200Response.
        :param trigger: The trigger of this BranchConfigurationsGet200Response.
        :param id: The id of this BranchConfigurationsGet200Response.
        """
        self.openapi_types = {
            'artifact_versioning': BranchConfigurationsGet200ResponseAllOfArtifactVersioning,
            'badge_is_enabled': bool,
            'clone_from_branch': str,
            'signed': bool,
            'tests_enabled': bool,
            'toolsets': BranchConfigurationsGet200ResponseAllOfToolsets,
            'trigger': str,
            'id': int
        }

        self.attribute_map = {
            'artifact_versioning': 'artifactVersioning',
            'badge_is_enabled': 'badgeIsEnabled',
            'clone_from_branch': 'cloneFromBranch',
            'signed': 'signed',
            'tests_enabled': 'testsEnabled',
            'toolsets': 'toolsets',
            'trigger': 'trigger',
            'id': 'id'
        }

        self._artifact_versioning = artifact_versioning
        self._badge_is_enabled = badge_is_enabled
        self._clone_from_branch = clone_from_branch
        self._signed = signed
        self._tests_enabled = tests_enabled
        self._toolsets = toolsets
        self._trigger = trigger
        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BranchConfigurationsGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The branchConfigurations_get_200_response of this BranchConfigurationsGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def artifact_versioning(self):
        """Gets the artifact_versioning of this BranchConfigurationsGet200Response.


        :return: The artifact_versioning of this BranchConfigurationsGet200Response.
        :rtype: BranchConfigurationsGet200ResponseAllOfArtifactVersioning
        """
        return self._artifact_versioning

    @artifact_versioning.setter
    def artifact_versioning(self, artifact_versioning):
        """Sets the artifact_versioning of this BranchConfigurationsGet200Response.


        :param artifact_versioning: The artifact_versioning of this BranchConfigurationsGet200Response.
        :type artifact_versioning: BranchConfigurationsGet200ResponseAllOfArtifactVersioning
        """

        self._artifact_versioning = artifact_versioning

    @property
    def badge_is_enabled(self):
        """Gets the badge_is_enabled of this BranchConfigurationsGet200Response.


        :return: The badge_is_enabled of this BranchConfigurationsGet200Response.
        :rtype: bool
        """
        return self._badge_is_enabled

    @badge_is_enabled.setter
    def badge_is_enabled(self, badge_is_enabled):
        """Sets the badge_is_enabled of this BranchConfigurationsGet200Response.


        :param badge_is_enabled: The badge_is_enabled of this BranchConfigurationsGet200Response.
        :type badge_is_enabled: bool
        """

        self._badge_is_enabled = badge_is_enabled

    @property
    def clone_from_branch(self):
        """Gets the clone_from_branch of this BranchConfigurationsGet200Response.

        A configured branch name to clone from. If provided, all other parameters will be ignored. Only supported in POST requests.

        :return: The clone_from_branch of this BranchConfigurationsGet200Response.
        :rtype: str
        """
        return self._clone_from_branch

    @clone_from_branch.setter
    def clone_from_branch(self, clone_from_branch):
        """Sets the clone_from_branch of this BranchConfigurationsGet200Response.

        A configured branch name to clone from. If provided, all other parameters will be ignored. Only supported in POST requests.

        :param clone_from_branch: The clone_from_branch of this BranchConfigurationsGet200Response.
        :type clone_from_branch: str
        """

        self._clone_from_branch = clone_from_branch

    @property
    def signed(self):
        """Gets the signed of this BranchConfigurationsGet200Response.


        :return: The signed of this BranchConfigurationsGet200Response.
        :rtype: bool
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        """Sets the signed of this BranchConfigurationsGet200Response.


        :param signed: The signed of this BranchConfigurationsGet200Response.
        :type signed: bool
        """

        self._signed = signed

    @property
    def tests_enabled(self):
        """Gets the tests_enabled of this BranchConfigurationsGet200Response.


        :return: The tests_enabled of this BranchConfigurationsGet200Response.
        :rtype: bool
        """
        return self._tests_enabled

    @tests_enabled.setter
    def tests_enabled(self, tests_enabled):
        """Sets the tests_enabled of this BranchConfigurationsGet200Response.


        :param tests_enabled: The tests_enabled of this BranchConfigurationsGet200Response.
        :type tests_enabled: bool
        """

        self._tests_enabled = tests_enabled

    @property
    def toolsets(self):
        """Gets the toolsets of this BranchConfigurationsGet200Response.


        :return: The toolsets of this BranchConfigurationsGet200Response.
        :rtype: BranchConfigurationsGet200ResponseAllOfToolsets
        """
        return self._toolsets

    @toolsets.setter
    def toolsets(self, toolsets):
        """Sets the toolsets of this BranchConfigurationsGet200Response.


        :param toolsets: The toolsets of this BranchConfigurationsGet200Response.
        :type toolsets: BranchConfigurationsGet200ResponseAllOfToolsets
        """

        self._toolsets = toolsets

    @property
    def trigger(self):
        """Gets the trigger of this BranchConfigurationsGet200Response.


        :return: The trigger of this BranchConfigurationsGet200Response.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this BranchConfigurationsGet200Response.


        :param trigger: The trigger of this BranchConfigurationsGet200Response.
        :type trigger: str
        """
        allowed_values = ["continous", "continuous", "manual"]  # noqa: E501
        if trigger not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger` ({0}), must be one of {1}"
                .format(trigger, allowed_values)
            )

        self._trigger = trigger

    @property
    def id(self):
        """Gets the id of this BranchConfigurationsGet200Response.


        :return: The id of this BranchConfigurationsGet200Response.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BranchConfigurationsGet200Response.


        :param id: The id of this BranchConfigurationsGet200Response.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
