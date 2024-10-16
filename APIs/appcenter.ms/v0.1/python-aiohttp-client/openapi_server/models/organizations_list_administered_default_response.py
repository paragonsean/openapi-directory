# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.organizations_list_administered_default_response_error import OrganizationsListAdministeredDefaultResponseError
from openapi_server import util


class OrganizationsListAdministeredDefaultResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error: OrganizationsListAdministeredDefaultResponseError=None):
        """OrganizationsListAdministeredDefaultResponse - a model defined in OpenAPI

        :param error: The error of this OrganizationsListAdministeredDefaultResponse.
        """
        self.openapi_types = {
            'error': OrganizationsListAdministeredDefaultResponseError
        }

        self.attribute_map = {
            'error': 'error'
        }

        self._error = error

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrganizationsListAdministeredDefaultResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The organizations_listAdministered_default_response of this OrganizationsListAdministeredDefaultResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self):
        """Gets the error of this OrganizationsListAdministeredDefaultResponse.


        :return: The error of this OrganizationsListAdministeredDefaultResponse.
        :rtype: OrganizationsListAdministeredDefaultResponseError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OrganizationsListAdministeredDefaultResponse.


        :param error: The error of this OrganizationsListAdministeredDefaultResponse.
        :type error: OrganizationsListAdministeredDefaultResponseError
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")

        self._error = error
