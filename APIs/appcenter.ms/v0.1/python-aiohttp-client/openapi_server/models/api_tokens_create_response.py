# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiTokensCreateResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, api_token: str=None, created_at: str=None, description: str=None, id: str=None, scope: List[str]=None):
        """ApiTokensCreateResponse - a model defined in OpenAPI

        :param api_token: The api_token of this ApiTokensCreateResponse.
        :param created_at: The created_at of this ApiTokensCreateResponse.
        :param description: The description of this ApiTokensCreateResponse.
        :param id: The id of this ApiTokensCreateResponse.
        :param scope: The scope of this ApiTokensCreateResponse.
        """
        self.openapi_types = {
            'api_token': str,
            'created_at': str,
            'description': str,
            'id': str,
            'scope': List[str]
        }

        self.attribute_map = {
            'api_token': 'api_token',
            'created_at': 'created_at',
            'description': 'description',
            'id': 'id',
            'scope': 'scope'
        }

        self._api_token = api_token
        self._created_at = created_at
        self._description = description
        self._id = id
        self._scope = scope

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiTokensCreateResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ApiTokensCreateResponse of this ApiTokensCreateResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_token(self):
        """Gets the api_token of this ApiTokensCreateResponse.

        The api token generated will not be accessible again

        :return: The api_token of this ApiTokensCreateResponse.
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this ApiTokensCreateResponse.

        The api token generated will not be accessible again

        :param api_token: The api_token of this ApiTokensCreateResponse.
        :type api_token: str
        """
        if api_token is None:
            raise ValueError("Invalid value for `api_token`, must not be `None`")

        self._api_token = api_token

    @property
    def created_at(self):
        """Gets the created_at of this ApiTokensCreateResponse.

        The creation time

        :return: The created_at of this ApiTokensCreateResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiTokensCreateResponse.

        The creation time

        :param created_at: The created_at of this ApiTokensCreateResponse.
        :type created_at: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ApiTokensCreateResponse.

        The description of the token

        :return: The description of this ApiTokensCreateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiTokensCreateResponse.

        The description of the token

        :param description: The description of this ApiTokensCreateResponse.
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ApiTokensCreateResponse.

        The unique id (UUID) of the api token

        :return: The id of this ApiTokensCreateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTokensCreateResponse.

        The unique id (UUID) of the api token

        :param id: The id of this ApiTokensCreateResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def scope(self):
        """Gets the scope of this ApiTokensCreateResponse.

        The scope for this token.

        :return: The scope of this ApiTokensCreateResponse.
        :rtype: List[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ApiTokensCreateResponse.

        The scope for this token.

        :param scope: The scope of this ApiTokensCreateResponse.
        :type scope: List[str]
        """
        allowed_values = ["all", "viewer"]  # noqa: E501
        if not set(scope).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `scope` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(scope) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._scope = scope
