# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.error import Error
from openapi_server import util


class Errors(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, errors: List[Error]=None):
        """Errors - a model defined in OpenAPI

        :param errors: The errors of this Errors.
        """
        self.openapi_types = {
            'errors': List[Error]
        }

        self.attribute_map = {
            'errors': 'errors'
        }

        self._errors = errors

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Errors':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Errors of this Errors.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def errors(self):
        """Gets the errors of this Errors.


        :return: The errors of this Errors.
        :rtype: List[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Errors.


        :param errors: The errors of this Errors.
        :type errors: List[Error]
        """

        self._errors = errors
