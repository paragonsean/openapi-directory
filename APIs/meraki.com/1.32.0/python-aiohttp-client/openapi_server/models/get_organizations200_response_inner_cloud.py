# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_organizations200_response_inner_cloud_region import GetOrganizations200ResponseInnerCloudRegion
from openapi_server import util


class GetOrganizations200ResponseInnerCloud(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, region: GetOrganizations200ResponseInnerCloudRegion=None):
        """GetOrganizations200ResponseInnerCloud - a model defined in OpenAPI

        :param region: The region of this GetOrganizations200ResponseInnerCloud.
        """
        self.openapi_types = {
            'region': GetOrganizations200ResponseInnerCloudRegion
        }

        self.attribute_map = {
            'region': 'region'
        }

        self._region = region

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizations200ResponseInnerCloud':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizations_200_response_inner_cloud of this GetOrganizations200ResponseInnerCloud.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def region(self):
        """Gets the region of this GetOrganizations200ResponseInnerCloud.


        :return: The region of this GetOrganizations200ResponseInnerCloud.
        :rtype: GetOrganizations200ResponseInnerCloudRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this GetOrganizations200ResponseInnerCloud.


        :param region: The region of this GetOrganizations200ResponseInnerCloud.
        :type region: GetOrganizations200ResponseInnerCloudRegion
        """

        self._region = region
