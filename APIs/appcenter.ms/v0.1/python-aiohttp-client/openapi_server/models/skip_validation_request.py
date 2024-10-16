# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SkipValidationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, skip_validation: bool=None):
        """SkipValidationRequest - a model defined in OpenAPI

        :param skip_validation: The skip_validation of this SkipValidationRequest.
        """
        self.openapi_types = {
            'skip_validation': bool
        }

        self.attribute_map = {
            'skip_validation': 'skip_validation'
        }

        self._skip_validation = skip_validation

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SkipValidationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SkipValidationRequest of this SkipValidationRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def skip_validation(self):
        """Gets the skip_validation of this SkipValidationRequest.

        true if we want to skip the validation, false otherwise

        :return: The skip_validation of this SkipValidationRequest.
        :rtype: bool
        """
        return self._skip_validation

    @skip_validation.setter
    def skip_validation(self, skip_validation):
        """Sets the skip_validation of this SkipValidationRequest.

        true if we want to skip the validation, false otherwise

        :param skip_validation: The skip_validation of this SkipValidationRequest.
        :type skip_validation: bool
        """

        self._skip_validation = skip_validation
