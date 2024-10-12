# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.issue import Issue
from openapi_server import util


class Error400(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, errors: List[Issue]=None):
        """Error400 - a model defined in OpenAPI

        :param errors: The errors of this Error400.
        """
        self.openapi_types = {
            'errors': List[Issue]
        }

        self.attribute_map = {
            'errors': 'errors'
        }

        self._errors = errors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Error400':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The error_400 of this Error400.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def errors(self):
        """Gets the errors of this Error400.


        :return: The errors of this Error400.
        :rtype: List[Issue]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Error400.


        :param errors: The errors of this Error400.
        :type errors: List[Issue]
        """

        self._errors = errors
