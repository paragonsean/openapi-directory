# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class IdentityProviderRepresentation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, add_read_token_role_on_create: bool=None, alias: str=None, config: Dict[str, object]=None, display_name: str=None, enabled: bool=None, first_broker_login_flow_alias: str=None, internal_id: str=None, link_only: bool=None, post_broker_login_flow_alias: str=None, provider_id: str=None, store_token: bool=None, trust_email: bool=None):
        """IdentityProviderRepresentation - a model defined in OpenAPI

        :param add_read_token_role_on_create: The add_read_token_role_on_create of this IdentityProviderRepresentation.
        :param alias: The alias of this IdentityProviderRepresentation.
        :param config: The config of this IdentityProviderRepresentation.
        :param display_name: The display_name of this IdentityProviderRepresentation.
        :param enabled: The enabled of this IdentityProviderRepresentation.
        :param first_broker_login_flow_alias: The first_broker_login_flow_alias of this IdentityProviderRepresentation.
        :param internal_id: The internal_id of this IdentityProviderRepresentation.
        :param link_only: The link_only of this IdentityProviderRepresentation.
        :param post_broker_login_flow_alias: The post_broker_login_flow_alias of this IdentityProviderRepresentation.
        :param provider_id: The provider_id of this IdentityProviderRepresentation.
        :param store_token: The store_token of this IdentityProviderRepresentation.
        :param trust_email: The trust_email of this IdentityProviderRepresentation.
        """
        self.openapi_types = {
            'add_read_token_role_on_create': bool,
            'alias': str,
            'config': Dict[str, object],
            'display_name': str,
            'enabled': bool,
            'first_broker_login_flow_alias': str,
            'internal_id': str,
            'link_only': bool,
            'post_broker_login_flow_alias': str,
            'provider_id': str,
            'store_token': bool,
            'trust_email': bool
        }

        self.attribute_map = {
            'add_read_token_role_on_create': 'addReadTokenRoleOnCreate',
            'alias': 'alias',
            'config': 'config',
            'display_name': 'displayName',
            'enabled': 'enabled',
            'first_broker_login_flow_alias': 'firstBrokerLoginFlowAlias',
            'internal_id': 'internalId',
            'link_only': 'linkOnly',
            'post_broker_login_flow_alias': 'postBrokerLoginFlowAlias',
            'provider_id': 'providerId',
            'store_token': 'storeToken',
            'trust_email': 'trustEmail'
        }

        self._add_read_token_role_on_create = add_read_token_role_on_create
        self._alias = alias
        self._config = config
        self._display_name = display_name
        self._enabled = enabled
        self._first_broker_login_flow_alias = first_broker_login_flow_alias
        self._internal_id = internal_id
        self._link_only = link_only
        self._post_broker_login_flow_alias = post_broker_login_flow_alias
        self._provider_id = provider_id
        self._store_token = store_token
        self._trust_email = trust_email

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IdentityProviderRepresentation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IdentityProviderRepresentation of this IdentityProviderRepresentation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def add_read_token_role_on_create(self):
        """Gets the add_read_token_role_on_create of this IdentityProviderRepresentation.


        :return: The add_read_token_role_on_create of this IdentityProviderRepresentation.
        :rtype: bool
        """
        return self._add_read_token_role_on_create

    @add_read_token_role_on_create.setter
    def add_read_token_role_on_create(self, add_read_token_role_on_create):
        """Sets the add_read_token_role_on_create of this IdentityProviderRepresentation.


        :param add_read_token_role_on_create: The add_read_token_role_on_create of this IdentityProviderRepresentation.
        :type add_read_token_role_on_create: bool
        """

        self._add_read_token_role_on_create = add_read_token_role_on_create

    @property
    def alias(self):
        """Gets the alias of this IdentityProviderRepresentation.


        :return: The alias of this IdentityProviderRepresentation.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this IdentityProviderRepresentation.


        :param alias: The alias of this IdentityProviderRepresentation.
        :type alias: str
        """

        self._alias = alias

    @property
    def config(self):
        """Gets the config of this IdentityProviderRepresentation.


        :return: The config of this IdentityProviderRepresentation.
        :rtype: Dict[str, object]
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this IdentityProviderRepresentation.


        :param config: The config of this IdentityProviderRepresentation.
        :type config: Dict[str, object]
        """

        self._config = config

    @property
    def display_name(self):
        """Gets the display_name of this IdentityProviderRepresentation.


        :return: The display_name of this IdentityProviderRepresentation.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IdentityProviderRepresentation.


        :param display_name: The display_name of this IdentityProviderRepresentation.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def enabled(self):
        """Gets the enabled of this IdentityProviderRepresentation.


        :return: The enabled of this IdentityProviderRepresentation.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IdentityProviderRepresentation.


        :param enabled: The enabled of this IdentityProviderRepresentation.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def first_broker_login_flow_alias(self):
        """Gets the first_broker_login_flow_alias of this IdentityProviderRepresentation.


        :return: The first_broker_login_flow_alias of this IdentityProviderRepresentation.
        :rtype: str
        """
        return self._first_broker_login_flow_alias

    @first_broker_login_flow_alias.setter
    def first_broker_login_flow_alias(self, first_broker_login_flow_alias):
        """Sets the first_broker_login_flow_alias of this IdentityProviderRepresentation.


        :param first_broker_login_flow_alias: The first_broker_login_flow_alias of this IdentityProviderRepresentation.
        :type first_broker_login_flow_alias: str
        """

        self._first_broker_login_flow_alias = first_broker_login_flow_alias

    @property
    def internal_id(self):
        """Gets the internal_id of this IdentityProviderRepresentation.


        :return: The internal_id of this IdentityProviderRepresentation.
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this IdentityProviderRepresentation.


        :param internal_id: The internal_id of this IdentityProviderRepresentation.
        :type internal_id: str
        """

        self._internal_id = internal_id

    @property
    def link_only(self):
        """Gets the link_only of this IdentityProviderRepresentation.


        :return: The link_only of this IdentityProviderRepresentation.
        :rtype: bool
        """
        return self._link_only

    @link_only.setter
    def link_only(self, link_only):
        """Sets the link_only of this IdentityProviderRepresentation.


        :param link_only: The link_only of this IdentityProviderRepresentation.
        :type link_only: bool
        """

        self._link_only = link_only

    @property
    def post_broker_login_flow_alias(self):
        """Gets the post_broker_login_flow_alias of this IdentityProviderRepresentation.


        :return: The post_broker_login_flow_alias of this IdentityProviderRepresentation.
        :rtype: str
        """
        return self._post_broker_login_flow_alias

    @post_broker_login_flow_alias.setter
    def post_broker_login_flow_alias(self, post_broker_login_flow_alias):
        """Sets the post_broker_login_flow_alias of this IdentityProviderRepresentation.


        :param post_broker_login_flow_alias: The post_broker_login_flow_alias of this IdentityProviderRepresentation.
        :type post_broker_login_flow_alias: str
        """

        self._post_broker_login_flow_alias = post_broker_login_flow_alias

    @property
    def provider_id(self):
        """Gets the provider_id of this IdentityProviderRepresentation.


        :return: The provider_id of this IdentityProviderRepresentation.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this IdentityProviderRepresentation.


        :param provider_id: The provider_id of this IdentityProviderRepresentation.
        :type provider_id: str
        """

        self._provider_id = provider_id

    @property
    def store_token(self):
        """Gets the store_token of this IdentityProviderRepresentation.


        :return: The store_token of this IdentityProviderRepresentation.
        :rtype: bool
        """
        return self._store_token

    @store_token.setter
    def store_token(self, store_token):
        """Sets the store_token of this IdentityProviderRepresentation.


        :param store_token: The store_token of this IdentityProviderRepresentation.
        :type store_token: bool
        """

        self._store_token = store_token

    @property
    def trust_email(self):
        """Gets the trust_email of this IdentityProviderRepresentation.


        :return: The trust_email of this IdentityProviderRepresentation.
        :rtype: bool
        """
        return self._trust_email

    @trust_email.setter
    def trust_email(self, trust_email):
        """Sets the trust_email of this IdentityProviderRepresentation.


        :param trust_email: The trust_email of this IdentityProviderRepresentation.
        :type trust_email: bool
        """

        self._trust_email = trust_email
