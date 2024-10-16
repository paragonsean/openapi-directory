# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GitHubAccount(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_type: str=None, id: int=None):
        """GitHubAccount - a model defined in OpenAPI

        :param account_type: The account_type of this GitHubAccount.
        :param id: The id of this GitHubAccount.
        """
        self.openapi_types = {
            'account_type': str,
            'id': int
        }

        self.attribute_map = {
            'account_type': 'accountType',
            'id': 'id'
        }

        self._account_type = account_type
        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GitHubAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GitHubAccount of this GitHubAccount.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_type(self):
        """Gets the account_type of this GitHubAccount.

        Type of GitHub account

        :return: The account_type of this GitHubAccount.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this GitHubAccount.

        Type of GitHub account

        :param account_type: The account_type of this GitHubAccount.
        :type account_type: str
        """
        allowed_values = ["User", "Organization"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def id(self):
        """Gets the id of this GitHubAccount.

        Id of GitHub account

        :return: The id of this GitHubAccount.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GitHubAccount.

        Id of GitHub account

        :param id: The id of this GitHubAccount.
        :type id: int
        """

        self._id = id
