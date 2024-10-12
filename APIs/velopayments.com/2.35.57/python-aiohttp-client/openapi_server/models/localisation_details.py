# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LocalisationDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, parameters: Dict[str, str]=None, template: str=None):
        """LocalisationDetails - a model defined in OpenAPI

        :param parameters: The parameters of this LocalisationDetails.
        :param template: The template of this LocalisationDetails.
        """
        self.openapi_types = {
            'parameters': Dict[str, str],
            'template': str
        }

        self.attribute_map = {
            'parameters': 'parameters',
            'template': 'template'
        }

        self._parameters = parameters
        self._template = template

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LocalisationDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LocalisationDetails of this LocalisationDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parameters(self):
        """Gets the parameters of this LocalisationDetails.

        name to value map containing any named parameters that appear in the message template

        :return: The parameters of this LocalisationDetails.
        :rtype: Dict[str, str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this LocalisationDetails.

        name to value map containing any named parameters that appear in the message template

        :param parameters: The parameters of this LocalisationDetails.
        :type parameters: Dict[str, str]
        """

        self._parameters = parameters

    @property
    def template(self):
        """Gets the template of this LocalisationDetails.

        the English language message template used to construct the error message

        :return: The template of this LocalisationDetails.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this LocalisationDetails.

        the English language message template used to construct the error message

        :param template: The template of this LocalisationDetails.
        :type template: str
        """

        self._template = template
