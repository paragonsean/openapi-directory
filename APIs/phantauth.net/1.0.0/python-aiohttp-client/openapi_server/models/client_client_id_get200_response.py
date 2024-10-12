# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ClientClientIdGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, client_id: str=None, client_name: str=None, client_secret: str=None, client_uri: str=None, contacts: List[object]=None, grant_types: List[object]=None, jwks: List[object]=None, jwks_uri: str=None, logo_email: str=None, logo_uri: str=None, policy_uri: str=None, redirect_uris: List[object]=None, response_types: List[object]=None, scope: str=None, software_id: str=None, software_version: str=None, token_endpoint_auth_method: str=None, tos_uri: str=None):
        """ClientClientIdGet200Response - a model defined in OpenAPI

        :param id: The id of this ClientClientIdGet200Response.
        :param client_id: The client_id of this ClientClientIdGet200Response.
        :param client_name: The client_name of this ClientClientIdGet200Response.
        :param client_secret: The client_secret of this ClientClientIdGet200Response.
        :param client_uri: The client_uri of this ClientClientIdGet200Response.
        :param contacts: The contacts of this ClientClientIdGet200Response.
        :param grant_types: The grant_types of this ClientClientIdGet200Response.
        :param jwks: The jwks of this ClientClientIdGet200Response.
        :param jwks_uri: The jwks_uri of this ClientClientIdGet200Response.
        :param logo_email: The logo_email of this ClientClientIdGet200Response.
        :param logo_uri: The logo_uri of this ClientClientIdGet200Response.
        :param policy_uri: The policy_uri of this ClientClientIdGet200Response.
        :param redirect_uris: The redirect_uris of this ClientClientIdGet200Response.
        :param response_types: The response_types of this ClientClientIdGet200Response.
        :param scope: The scope of this ClientClientIdGet200Response.
        :param software_id: The software_id of this ClientClientIdGet200Response.
        :param software_version: The software_version of this ClientClientIdGet200Response.
        :param token_endpoint_auth_method: The token_endpoint_auth_method of this ClientClientIdGet200Response.
        :param tos_uri: The tos_uri of this ClientClientIdGet200Response.
        """
        self.openapi_types = {
            'id': str,
            'client_id': str,
            'client_name': str,
            'client_secret': str,
            'client_uri': str,
            'contacts': List[object],
            'grant_types': List[object],
            'jwks': List[object],
            'jwks_uri': str,
            'logo_email': str,
            'logo_uri': str,
            'policy_uri': str,
            'redirect_uris': List[object],
            'response_types': List[object],
            'scope': str,
            'software_id': str,
            'software_version': str,
            'token_endpoint_auth_method': str,
            'tos_uri': str
        }

        self.attribute_map = {
            'id': '@id',
            'client_id': 'client_id',
            'client_name': 'client_name',
            'client_secret': 'client_secret',
            'client_uri': 'client_uri',
            'contacts': 'contacts',
            'grant_types': 'grant_types',
            'jwks': 'jwks',
            'jwks_uri': 'jwks_uri',
            'logo_email': 'logo_email',
            'logo_uri': 'logo_uri',
            'policy_uri': 'policy_uri',
            'redirect_uris': 'redirect_uris',
            'response_types': 'response_types',
            'scope': 'scope',
            'software_id': 'software_id',
            'software_version': 'software_version',
            'token_endpoint_auth_method': 'token_endpoint_auth_method',
            'tos_uri': 'tos_uri'
        }

        self._id = id
        self._client_id = client_id
        self._client_name = client_name
        self._client_secret = client_secret
        self._client_uri = client_uri
        self._contacts = contacts
        self._grant_types = grant_types
        self._jwks = jwks
        self._jwks_uri = jwks_uri
        self._logo_email = logo_email
        self._logo_uri = logo_uri
        self._policy_uri = policy_uri
        self._redirect_uris = redirect_uris
        self._response_types = response_types
        self._scope = scope
        self._software_id = software_id
        self._software_version = software_version
        self._token_endpoint_auth_method = token_endpoint_auth_method
        self._tos_uri = tos_uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ClientClientIdGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _client__client_id__get_200_response of this ClientClientIdGet200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ClientClientIdGet200Response.

        URL of the Client's JSON representation.

        :return: The id of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientClientIdGet200Response.

        URL of the Client's JSON representation.

        :param id: The id of this ClientClientIdGet200Response.
        :type id: str
        """

        self._id = id

    @property
    def client_id(self):
        """Gets the client_id of this ClientClientIdGet200Response.

        OAuth 2.0 client identifier string.

        :return: The client_id of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ClientClientIdGet200Response.

        OAuth 2.0 client identifier string.

        :param client_id: The client_id of this ClientClientIdGet200Response.
        :type client_id: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this ClientClientIdGet200Response.

        Human-readable string name of the client to be presented to the end-user during authorization.

        :return: The client_name of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this ClientClientIdGet200Response.

        Human-readable string name of the client to be presented to the end-user during authorization.

        :param client_name: The client_name of this ClientClientIdGet200Response.
        :type client_name: str
        """

        self._client_name = client_name

    @property
    def client_secret(self):
        """Gets the client_secret of this ClientClientIdGet200Response.

        OAuth 2.0 client secret string. 

        :return: The client_secret of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this ClientClientIdGet200Response.

        OAuth 2.0 client secret string. 

        :param client_secret: The client_secret of this ClientClientIdGet200Response.
        :type client_secret: str
        """

        self._client_secret = client_secret

    @property
    def client_uri(self):
        """Gets the client_uri of this ClientClientIdGet200Response.

        URL string of a web page providing information about the client.

        :return: The client_uri of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._client_uri

    @client_uri.setter
    def client_uri(self, client_uri):
        """Sets the client_uri of this ClientClientIdGet200Response.

        URL string of a web page providing information about the client.

        :param client_uri: The client_uri of this ClientClientIdGet200Response.
        :type client_uri: str
        """

        self._client_uri = client_uri

    @property
    def contacts(self):
        """Gets the contacts of this ClientClientIdGet200Response.

        Array of strings representing ways to contact people responsible for this client, typically email addresses.

        :return: The contacts of this ClientClientIdGet200Response.
        :rtype: List[object]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this ClientClientIdGet200Response.

        Array of strings representing ways to contact people responsible for this client, typically email addresses.

        :param contacts: The contacts of this ClientClientIdGet200Response.
        :type contacts: List[object]
        """

        self._contacts = contacts

    @property
    def grant_types(self):
        """Gets the grant_types of this ClientClientIdGet200Response.

        Array of OAuth 2.0 grant type strings that the client can use at the token endpoint.

        :return: The grant_types of this ClientClientIdGet200Response.
        :rtype: List[object]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this ClientClientIdGet200Response.

        Array of OAuth 2.0 grant type strings that the client can use at the token endpoint.

        :param grant_types: The grant_types of this ClientClientIdGet200Response.
        :type grant_types: List[object]
        """

        self._grant_types = grant_types

    @property
    def jwks(self):
        """Gets the jwks of this ClientClientIdGet200Response.

        Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys.  The value of this field MUST be a JSON object containing a valid JWK Set.

        :return: The jwks of this ClientClientIdGet200Response.
        :rtype: List[object]
        """
        return self._jwks

    @jwks.setter
    def jwks(self, jwks):
        """Sets the jwks of this ClientClientIdGet200Response.

        Client's JSON Web Key Set [RFC7517] document value, which contains the client's public keys.  The value of this field MUST be a JSON object containing a valid JWK Set.

        :param jwks: The jwks of this ClientClientIdGet200Response.
        :type jwks: List[object]
        """

        self._jwks = jwks

    @property
    def jwks_uri(self):
        """Gets the jwks_uri of this ClientClientIdGet200Response.

        URL string referencing the client's JSON Web Key (JWK) Set [RFC7517] document, which contains the client's public keys.

        :return: The jwks_uri of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """Sets the jwks_uri of this ClientClientIdGet200Response.

        URL string referencing the client's JSON Web Key (JWK) Set [RFC7517] document, which contains the client's public keys.

        :param jwks_uri: The jwks_uri of this ClientClientIdGet200Response.
        :type jwks_uri: str
        """

        self._jwks_uri = jwks_uri

    @property
    def logo_email(self):
        """Gets the logo_email of this ClientClientIdGet200Response.

        An email address used to generate a gravatar.com logo_uri.

        :return: The logo_email of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._logo_email

    @logo_email.setter
    def logo_email(self, logo_email):
        """Sets the logo_email of this ClientClientIdGet200Response.

        An email address used to generate a gravatar.com logo_uri.

        :param logo_email: The logo_email of this ClientClientIdGet200Response.
        :type logo_email: str
        """

        self._logo_email = logo_email

    @property
    def logo_uri(self):
        """Gets the logo_uri of this ClientClientIdGet200Response.

        URL string that references a logo for the client.

        :return: The logo_uri of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._logo_uri

    @logo_uri.setter
    def logo_uri(self, logo_uri):
        """Sets the logo_uri of this ClientClientIdGet200Response.

        URL string that references a logo for the client.

        :param logo_uri: The logo_uri of this ClientClientIdGet200Response.
        :type logo_uri: str
        """

        self._logo_uri = logo_uri

    @property
    def policy_uri(self):
        """Gets the policy_uri of this ClientClientIdGet200Response.

        URL string that points to a human-readable privacy policy document that describes how the deployment organization collects, uses, retains, and discloses personal data.

        :return: The policy_uri of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._policy_uri

    @policy_uri.setter
    def policy_uri(self, policy_uri):
        """Sets the policy_uri of this ClientClientIdGet200Response.

        URL string that points to a human-readable privacy policy document that describes how the deployment organization collects, uses, retains, and discloses personal data.

        :param policy_uri: The policy_uri of this ClientClientIdGet200Response.
        :type policy_uri: str
        """

        self._policy_uri = policy_uri

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this ClientClientIdGet200Response.

        Array of redirection URI strings for use in redirect-based flows such as the authorization code and implicit flows.

        :return: The redirect_uris of this ClientClientIdGet200Response.
        :rtype: List[object]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this ClientClientIdGet200Response.

        Array of redirection URI strings for use in redirect-based flows such as the authorization code and implicit flows.

        :param redirect_uris: The redirect_uris of this ClientClientIdGet200Response.
        :type redirect_uris: List[object]
        """

        self._redirect_uris = redirect_uris

    @property
    def response_types(self):
        """Gets the response_types of this ClientClientIdGet200Response.

        Array of the OAuth 2.0 response type strings that the client can use at the authorization endpoint.

        :return: The response_types of this ClientClientIdGet200Response.
        :rtype: List[object]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        """Sets the response_types of this ClientClientIdGet200Response.

        Array of the OAuth 2.0 response type strings that the client can use at the authorization endpoint.

        :param response_types: The response_types of this ClientClientIdGet200Response.
        :type response_types: List[object]
        """

        self._response_types = response_types

    @property
    def scope(self):
        """Gets the scope of this ClientClientIdGet200Response.

        String containing a space-separated list of scope values (as described in Section 3.3 of OAuth 2.0 [RFC6749]) that the client can use when requesting access tokens.

        :return: The scope of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ClientClientIdGet200Response.

        String containing a space-separated list of scope values (as described in Section 3.3 of OAuth 2.0 [RFC6749]) that the client can use when requesting access tokens.

        :param scope: The scope of this ClientClientIdGet200Response.
        :type scope: str
        """

        self._scope = scope

    @property
    def software_id(self):
        """Gets the software_id of this ClientClientIdGet200Response.

        A unique identifier string (e.g., a Universally Unique Identifier (UUID)) assigned by the client developer or software publisher used by registration endpoints to identify the client software to be dynamically registered.

        :return: The software_id of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._software_id

    @software_id.setter
    def software_id(self, software_id):
        """Sets the software_id of this ClientClientIdGet200Response.

        A unique identifier string (e.g., a Universally Unique Identifier (UUID)) assigned by the client developer or software publisher used by registration endpoints to identify the client software to be dynamically registered.

        :param software_id: The software_id of this ClientClientIdGet200Response.
        :type software_id: str
        """

        self._software_id = software_id

    @property
    def software_version(self):
        """Gets the software_version of this ClientClientIdGet200Response.

        A version identifier string for the client software identified by software_id.

        :return: The software_version of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this ClientClientIdGet200Response.

        A version identifier string for the client software identified by software_id.

        :param software_version: The software_version of this ClientClientIdGet200Response.
        :type software_version: str
        """

        self._software_version = software_version

    @property
    def token_endpoint_auth_method(self):
        """Gets the token_endpoint_auth_method of this ClientClientIdGet200Response.

        String indicator of the requested authentication method for the token endpoint.

        :return: The token_endpoint_auth_method of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._token_endpoint_auth_method

    @token_endpoint_auth_method.setter
    def token_endpoint_auth_method(self, token_endpoint_auth_method):
        """Sets the token_endpoint_auth_method of this ClientClientIdGet200Response.

        String indicator of the requested authentication method for the token endpoint.

        :param token_endpoint_auth_method: The token_endpoint_auth_method of this ClientClientIdGet200Response.
        :type token_endpoint_auth_method: str
        """

        self._token_endpoint_auth_method = token_endpoint_auth_method

    @property
    def tos_uri(self):
        """Gets the tos_uri of this ClientClientIdGet200Response.

        URL string that points to a human-readable terms of service document for the client that describes a contractual relationship between the end-user and the client that the end-user accepts when authorizing the client.

        :return: The tos_uri of this ClientClientIdGet200Response.
        :rtype: str
        """
        return self._tos_uri

    @tos_uri.setter
    def tos_uri(self, tos_uri):
        """Sets the tos_uri of this ClientClientIdGet200Response.

        URL string that points to a human-readable terms of service document for the client that describes a contractual relationship between the end-user and the client that the end-user accepts when authorizing the client.

        :param tos_uri: The tos_uri of this ClientClientIdGet200Response.
        :type tos_uri: str
        """

        self._tos_uri = tos_uri
