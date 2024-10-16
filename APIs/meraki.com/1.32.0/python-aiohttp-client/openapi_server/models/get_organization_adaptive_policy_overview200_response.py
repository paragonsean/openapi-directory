# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_organization_adaptive_policy_overview200_response_counts import GetOrganizationAdaptivePolicyOverview200ResponseCounts
from openapi_server.models.get_organization_adaptive_policy_overview200_response_limits import GetOrganizationAdaptivePolicyOverview200ResponseLimits
from openapi_server import util


class GetOrganizationAdaptivePolicyOverview200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, counts: GetOrganizationAdaptivePolicyOverview200ResponseCounts=None, limits: GetOrganizationAdaptivePolicyOverview200ResponseLimits=None):
        """GetOrganizationAdaptivePolicyOverview200Response - a model defined in OpenAPI

        :param counts: The counts of this GetOrganizationAdaptivePolicyOverview200Response.
        :param limits: The limits of this GetOrganizationAdaptivePolicyOverview200Response.
        """
        self.openapi_types = {
            'counts': GetOrganizationAdaptivePolicyOverview200ResponseCounts,
            'limits': GetOrganizationAdaptivePolicyOverview200ResponseLimits
        }

        self.attribute_map = {
            'counts': 'counts',
            'limits': 'limits'
        }

        self._counts = counts
        self._limits = limits

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationAdaptivePolicyOverview200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationAdaptivePolicyOverview_200_response of this GetOrganizationAdaptivePolicyOverview200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def counts(self):
        """Gets the counts of this GetOrganizationAdaptivePolicyOverview200Response.


        :return: The counts of this GetOrganizationAdaptivePolicyOverview200Response.
        :rtype: GetOrganizationAdaptivePolicyOverview200ResponseCounts
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this GetOrganizationAdaptivePolicyOverview200Response.


        :param counts: The counts of this GetOrganizationAdaptivePolicyOverview200Response.
        :type counts: GetOrganizationAdaptivePolicyOverview200ResponseCounts
        """

        self._counts = counts

    @property
    def limits(self):
        """Gets the limits of this GetOrganizationAdaptivePolicyOverview200Response.


        :return: The limits of this GetOrganizationAdaptivePolicyOverview200Response.
        :rtype: GetOrganizationAdaptivePolicyOverview200ResponseLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this GetOrganizationAdaptivePolicyOverview200Response.


        :param limits: The limits of this GetOrganizationAdaptivePolicyOverview200Response.
        :type limits: GetOrganizationAdaptivePolicyOverview200ResponseLimits
        """

        self._limits = limits
