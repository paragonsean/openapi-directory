# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.deployment_parameters import DeploymentParameters
from openapi_server.models.template_link import TemplateLink
from openapi_server import util


class DeploymentProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mode: str=None, parameters: DeploymentParameters=None, template_link: TemplateLink=None):
        """DeploymentProperties - a model defined in OpenAPI

        :param mode: The mode of this DeploymentProperties.
        :param parameters: The parameters of this DeploymentProperties.
        :param template_link: The template_link of this DeploymentProperties.
        """
        self.openapi_types = {
            'mode': str,
            'parameters': DeploymentParameters,
            'template_link': TemplateLink
        }

        self.attribute_map = {
            'mode': 'mode',
            'parameters': 'parameters',
            'template_link': 'templateLink'
        }

        self._mode = mode
        self._parameters = parameters
        self._template_link = template_link

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DeploymentProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DeploymentProperties of this DeploymentProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mode(self):
        """Gets the mode of this DeploymentProperties.

        Gets or sets the deployment mode.

        :return: The mode of this DeploymentProperties.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DeploymentProperties.

        Gets or sets the deployment mode.

        :param mode: The mode of this DeploymentProperties.
        :type mode: str
        """
        allowed_values = ["Incremental"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def parameters(self):
        """Gets the parameters of this DeploymentProperties.


        :return: The parameters of this DeploymentProperties.
        :rtype: DeploymentParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this DeploymentProperties.


        :param parameters: The parameters of this DeploymentProperties.
        :type parameters: DeploymentParameters
        """

        self._parameters = parameters

    @property
    def template_link(self):
        """Gets the template_link of this DeploymentProperties.


        :return: The template_link of this DeploymentProperties.
        :rtype: TemplateLink
        """
        return self._template_link

    @template_link.setter
    def template_link(self, template_link):
        """Sets the template_link of this DeploymentProperties.


        :param template_link: The template_link of this DeploymentProperties.
        :type template_link: TemplateLink
        """
        if template_link is None:
            raise ValueError("Invalid value for `template_link`, must not be `None`")

        self._template_link = template_link
