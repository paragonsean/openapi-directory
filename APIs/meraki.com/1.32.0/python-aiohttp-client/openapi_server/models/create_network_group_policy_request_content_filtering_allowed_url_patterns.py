# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, patterns: List[str]=None, settings: str=None):
        """CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns - a model defined in OpenAPI

        :param patterns: The patterns of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.
        :param settings: The settings of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.
        """
        self.openapi_types = {
            'patterns': List[str],
            'settings': str
        }

        self.attribute_map = {
            'patterns': 'patterns',
            'settings': 'settings'
        }

        self._patterns = patterns
        self._settings = settings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def patterns(self):
        """Gets the patterns of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.

        A list of URL patterns that are allowed

        :return: The patterns of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.
        :rtype: List[str]
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        """Sets the patterns of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.

        A list of URL patterns that are allowed

        :param patterns: The patterns of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.
        :type patterns: List[str]
        """

        self._patterns = patterns

    @property
    def settings(self):
        """Gets the settings of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.

        How URL patterns are applied. Can be 'network default', 'append' or 'override'.

        :return: The settings of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.
        :rtype: str
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.

        How URL patterns are applied. Can be 'network default', 'append' or 'override'.

        :param settings: The settings of this CreateNetworkGroupPolicyRequestContentFilteringAllowedUrlPatterns.
        :type settings: str
        """
        allowed_values = ["append", "network default", "override"]  # noqa: E501
        if settings not in allowed_values:
            raise ValueError(
                "Invalid value for `settings` ({0}), must be one of {1}"
                .format(settings, allowed_values)
            )

        self._settings = settings
