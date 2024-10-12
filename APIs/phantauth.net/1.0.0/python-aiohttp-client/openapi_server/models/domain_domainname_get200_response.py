# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DomainDomainnameGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, logo: str=None, members: List[object]=None, name: str=None, profile: str=None, sub: str=None):
        """DomainDomainnameGet200Response - a model defined in OpenAPI

        :param id: The id of this DomainDomainnameGet200Response.
        :param logo: The logo of this DomainDomainnameGet200Response.
        :param members: The members of this DomainDomainnameGet200Response.
        :param name: The name of this DomainDomainnameGet200Response.
        :param profile: The profile of this DomainDomainnameGet200Response.
        :param sub: The sub of this DomainDomainnameGet200Response.
        """
        self.openapi_types = {
            'id': str,
            'logo': str,
            'members': List[object],
            'name': str,
            'profile': str,
            'sub': str
        }

        self.attribute_map = {
            'id': '@id',
            'logo': 'logo',
            'members': 'members',
            'name': 'name',
            'profile': 'profile',
            'sub': 'sub'
        }

        self._id = id
        self._logo = logo
        self._members = members
        self._name = name
        self._profile = profile
        self._sub = sub

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DomainDomainnameGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _domain__domainname__get_200_response of this DomainDomainnameGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this DomainDomainnameGet200Response.

        The URL of the domain's JSON representation.

        :return: The id of this DomainDomainnameGet200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainDomainnameGet200Response.

        The URL of the domain's JSON representation.

        :param id: The id of this DomainDomainnameGet200Response.
        :type id: str
        """

        self._id = id

    @property
    def logo(self):
        """Gets the logo of this DomainDomainnameGet200Response.

        The URL of the domain logo. The image from this address is displayed on the webpage of the domain.

        :return: The logo of this DomainDomainnameGet200Response.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this DomainDomainnameGet200Response.

        The URL of the domain logo. The image from this address is displayed on the webpage of the domain.

        :param logo: The logo of this DomainDomainnameGet200Response.
        :type logo: str
        """

        self._logo = logo

    @property
    def members(self):
        """Gets the members of this DomainDomainnameGet200Response.

        The tenants included in a domain.

        :return: The members of this DomainDomainnameGet200Response.
        :rtype: List[object]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this DomainDomainnameGet200Response.

        The tenants included in a domain.

        :param members: The members of this DomainDomainnameGet200Response.
        :type members: List[object]
        """

        self._members = members

    @property
    def name(self):
        """Gets the name of this DomainDomainnameGet200Response.

        The displayed domain name.

        :return: The name of this DomainDomainnameGet200Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainDomainnameGet200Response.

        The displayed domain name.

        :param name: The name of this DomainDomainnameGet200Response.
        :type name: str
        """

        self._name = name

    @property
    def profile(self):
        """Gets the profile of this DomainDomainnameGet200Response.

        The URL of the domain's webpage.

        :return: The profile of this DomainDomainnameGet200Response.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this DomainDomainnameGet200Response.

        The URL of the domain's webpage.

        :param profile: The profile of this DomainDomainnameGet200Response.
        :type profile: str
        """

        self._profile = profile

    @property
    def sub(self):
        """Gets the sub of this DomainDomainnameGet200Response.

        The fully qualified DNS name of the domain (e.g. phantauth.net).

        :return: The sub of this DomainDomainnameGet200Response.
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        """Sets the sub of this DomainDomainnameGet200Response.

        The fully qualified DNS name of the domain (e.g. phantauth.net).

        :param sub: The sub of this DomainDomainnameGet200Response.
        :type sub: str
        """

        self._sub = sub
