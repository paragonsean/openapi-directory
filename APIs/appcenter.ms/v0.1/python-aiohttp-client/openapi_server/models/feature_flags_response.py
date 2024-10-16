# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FeatureFlagsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, feature_flags: List[str]=None):
        """FeatureFlagsResponse - a model defined in OpenAPI

        :param feature_flags: The feature_flags of this FeatureFlagsResponse.
        """
        self.openapi_types = {
            'feature_flags': List[str]
        }

        self.attribute_map = {
            'feature_flags': 'feature_flags'
        }

        self._feature_flags = feature_flags

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FeatureFlagsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FeatureFlagsResponse of this FeatureFlagsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def feature_flags(self):
        """Gets the feature_flags of this FeatureFlagsResponse.


        :return: The feature_flags of this FeatureFlagsResponse.
        :rtype: List[str]
        """
        return self._feature_flags

    @feature_flags.setter
    def feature_flags(self, feature_flags):
        """Sets the feature_flags of this FeatureFlagsResponse.


        :param feature_flags: The feature_flags of this FeatureFlagsResponse.
        :type feature_flags: List[str]
        """
        if feature_flags is None:
            raise ValueError("Invalid value for `feature_flags`, must not be `None`")

        self._feature_flags = feature_flags
