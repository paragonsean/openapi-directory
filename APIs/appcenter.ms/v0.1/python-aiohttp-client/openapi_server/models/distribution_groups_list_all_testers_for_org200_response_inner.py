# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DistributionGroupsListAllTestersForOrg200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name: str=None, email: str=None, name: str=None):
        """DistributionGroupsListAllTestersForOrg200ResponseInner - a model defined in OpenAPI

        :param display_name: The display_name of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :param email: The email of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :param name: The name of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        """
        self.openapi_types = {
            'display_name': str,
            'email': str,
            'name': str
        }

        self.attribute_map = {
            'display_name': 'display_name',
            'email': 'email',
            'name': 'name'
        }

        self._display_name = display_name
        self._email = email
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DistributionGroupsListAllTestersForOrg200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The distributionGroups_listAllTestersForOrg_200_response_inner of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self):
        """Gets the display_name of this DistributionGroupsListAllTestersForOrg200ResponseInner.

        The full name of the tester. Might for example be first and last name

        :return: The display_name of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DistributionGroupsListAllTestersForOrg200ResponseInner.

        The full name of the tester. Might for example be first and last name

        :param display_name: The display_name of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this DistributionGroupsListAllTestersForOrg200ResponseInner.

        The email address of the tester

        :return: The email of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DistributionGroupsListAllTestersForOrg200ResponseInner.

        The email address of the tester

        :param email: The email of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def name(self):
        """Gets the name of this DistributionGroupsListAllTestersForOrg200ResponseInner.

        The unique name that is used to identify the tester.

        :return: The name of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DistributionGroupsListAllTestersForOrg200ResponseInner.

        The unique name that is used to identify the tester.

        :param name: The name of this DistributionGroupsListAllTestersForOrg200ResponseInner.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
