# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.anonymization_profile import AnonymizationProfile
from openapi_server.models.image_tag_values import ImageTagValues
from openapi_server import util


class BulkAnonymizationData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image_tag_values_set: List[ImageTagValues]=None, profile: AnonymizationProfile=None):
        """BulkAnonymizationData - a model defined in OpenAPI

        :param image_tag_values_set: The image_tag_values_set of this BulkAnonymizationData.
        :param profile: The profile of this BulkAnonymizationData.
        """
        self.openapi_types = {
            'image_tag_values_set': List[ImageTagValues],
            'profile': AnonymizationProfile
        }

        self.attribute_map = {
            'image_tag_values_set': 'imageTagValuesSet',
            'profile': 'profile'
        }

        self._image_tag_values_set = image_tag_values_set
        self._profile = profile

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BulkAnonymizationData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The bulkAnonymizationData of this BulkAnonymizationData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_tag_values_set(self):
        """Gets the image_tag_values_set of this BulkAnonymizationData.


        :return: The image_tag_values_set of this BulkAnonymizationData.
        :rtype: List[ImageTagValues]
        """
        return self._image_tag_values_set

    @image_tag_values_set.setter
    def image_tag_values_set(self, image_tag_values_set):
        """Sets the image_tag_values_set of this BulkAnonymizationData.


        :param image_tag_values_set: The image_tag_values_set of this BulkAnonymizationData.
        :type image_tag_values_set: List[ImageTagValues]
        """

        self._image_tag_values_set = image_tag_values_set

    @property
    def profile(self):
        """Gets the profile of this BulkAnonymizationData.


        :return: The profile of this BulkAnonymizationData.
        :rtype: AnonymizationProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this BulkAnonymizationData.


        :param profile: The profile of this BulkAnonymizationData.
        :type profile: AnonymizationProfile
        """

        self._profile = profile
