# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.anonymization_profile import AnonymizationProfile
from openapi_server.models.tag_value import TagValue
from openapi_server import util


class AnonymizationData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, profile: AnonymizationProfile=None, tag_values: List[TagValue]=None):
        """AnonymizationData - a model defined in OpenAPI

        :param profile: The profile of this AnonymizationData.
        :param tag_values: The tag_values of this AnonymizationData.
        """
        self.openapi_types = {
            'profile': AnonymizationProfile,
            'tag_values': List[TagValue]
        }

        self.attribute_map = {
            'profile': 'profile',
            'tag_values': 'tagValues'
        }

        self._profile = profile
        self._tag_values = tag_values

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AnonymizationData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The anonymizationData of this AnonymizationData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def profile(self):
        """Gets the profile of this AnonymizationData.


        :return: The profile of this AnonymizationData.
        :rtype: AnonymizationProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this AnonymizationData.


        :param profile: The profile of this AnonymizationData.
        :type profile: AnonymizationProfile
        """

        self._profile = profile

    @property
    def tag_values(self):
        """Gets the tag_values of this AnonymizationData.


        :return: The tag_values of this AnonymizationData.
        :rtype: List[TagValue]
        """
        return self._tag_values

    @tag_values.setter
    def tag_values(self, tag_values):
        """Sets the tag_values of this AnonymizationData.


        :param tag_values: The tag_values of this AnonymizationData.
        :type tag_values: List[TagValue]
        """

        self._tag_values = tag_values
