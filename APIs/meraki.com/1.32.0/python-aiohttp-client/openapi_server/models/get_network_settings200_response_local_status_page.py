# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.get_network_settings200_response_local_status_page_authentication import GetNetworkSettings200ResponseLocalStatusPageAuthentication
from openapi_server import util


class GetNetworkSettings200ResponseLocalStatusPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, authentication: GetNetworkSettings200ResponseLocalStatusPageAuthentication=None):
        """GetNetworkSettings200ResponseLocalStatusPage - a model defined in OpenAPI

        :param authentication: The authentication of this GetNetworkSettings200ResponseLocalStatusPage.
        """
        self.openapi_types = {
            'authentication': GetNetworkSettings200ResponseLocalStatusPageAuthentication
        }

        self.attribute_map = {
            'authentication': 'authentication'
        }

        self._authentication = authentication

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSettings200ResponseLocalStatusPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSettings_200_response_localStatusPage of this GetNetworkSettings200ResponseLocalStatusPage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def authentication(self):
        """Gets the authentication of this GetNetworkSettings200ResponseLocalStatusPage.


        :return: The authentication of this GetNetworkSettings200ResponseLocalStatusPage.
        :rtype: GetNetworkSettings200ResponseLocalStatusPageAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this GetNetworkSettings200ResponseLocalStatusPage.


        :param authentication: The authentication of this GetNetworkSettings200ResponseLocalStatusPage.
        :type authentication: GetNetworkSettings200ResponseLocalStatusPageAuthentication
        """

        self._authentication = authentication
