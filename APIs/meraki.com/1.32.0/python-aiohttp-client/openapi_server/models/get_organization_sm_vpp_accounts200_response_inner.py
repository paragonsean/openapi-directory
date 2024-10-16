# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetOrganizationSmVppAccounts200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, vpp_service_token: str=None):
        """GetOrganizationSmVppAccounts200ResponseInner - a model defined in OpenAPI

        :param id: The id of this GetOrganizationSmVppAccounts200ResponseInner.
        :param vpp_service_token: The vpp_service_token of this GetOrganizationSmVppAccounts200ResponseInner.
        """
        self.openapi_types = {
            'id': str,
            'vpp_service_token': str
        }

        self.attribute_map = {
            'id': 'id',
            'vpp_service_token': 'vppServiceToken'
        }

        self._id = id
        self._vpp_service_token = vpp_service_token

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationSmVppAccounts200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationSmVppAccounts_200_response_inner of this GetOrganizationSmVppAccounts200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GetOrganizationSmVppAccounts200ResponseInner.

        The id of the VPP Account

        :return: The id of this GetOrganizationSmVppAccounts200ResponseInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetOrganizationSmVppAccounts200ResponseInner.

        The id of the VPP Account

        :param id: The id of this GetOrganizationSmVppAccounts200ResponseInner.
        :type id: str
        """

        self._id = id

    @property
    def vpp_service_token(self):
        """Gets the vpp_service_token of this GetOrganizationSmVppAccounts200ResponseInner.

        The VPP Account's Service Token

        :return: The vpp_service_token of this GetOrganizationSmVppAccounts200ResponseInner.
        :rtype: str
        """
        return self._vpp_service_token

    @vpp_service_token.setter
    def vpp_service_token(self, vpp_service_token):
        """Sets the vpp_service_token of this GetOrganizationSmVppAccounts200ResponseInner.

        The VPP Account's Service Token

        :param vpp_service_token: The vpp_service_token of this GetOrganizationSmVppAccounts200ResponseInner.
        :type vpp_service_token: str
        """

        self._vpp_service_token = vpp_service_token
