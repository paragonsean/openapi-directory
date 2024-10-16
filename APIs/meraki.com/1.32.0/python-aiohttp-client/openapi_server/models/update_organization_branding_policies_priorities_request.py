# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateOrganizationBrandingPoliciesPrioritiesRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, branding_policy_ids: List[str]=None):
        """UpdateOrganizationBrandingPoliciesPrioritiesRequest - a model defined in OpenAPI

        :param branding_policy_ids: The branding_policy_ids of this UpdateOrganizationBrandingPoliciesPrioritiesRequest.
        """
        self.openapi_types = {
            'branding_policy_ids': List[str]
        }

        self.attribute_map = {
            'branding_policy_ids': 'brandingPolicyIds'
        }

        self._branding_policy_ids = branding_policy_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateOrganizationBrandingPoliciesPrioritiesRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The updateOrganizationBrandingPoliciesPriorities_request of this UpdateOrganizationBrandingPoliciesPrioritiesRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def branding_policy_ids(self):
        """Gets the branding_policy_ids of this UpdateOrganizationBrandingPoliciesPrioritiesRequest.

              An ordered list of branding policy IDs that determines the priority order of how to apply the policies 

        :return: The branding_policy_ids of this UpdateOrganizationBrandingPoliciesPrioritiesRequest.
        :rtype: List[str]
        """
        return self._branding_policy_ids

    @branding_policy_ids.setter
    def branding_policy_ids(self, branding_policy_ids):
        """Sets the branding_policy_ids of this UpdateOrganizationBrandingPoliciesPrioritiesRequest.

              An ordered list of branding policy IDs that determines the priority order of how to apply the policies 

        :param branding_policy_ids: The branding_policy_ids of this UpdateOrganizationBrandingPoliciesPrioritiesRequest.
        :type branding_policy_ids: List[str]
        """

        self._branding_policy_ids = branding_policy_ids
