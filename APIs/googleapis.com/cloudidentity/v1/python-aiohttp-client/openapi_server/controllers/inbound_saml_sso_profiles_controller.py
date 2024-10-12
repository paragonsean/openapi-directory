from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_idp_credential_request import AddIdpCredentialRequest
from openapi_server.models.inbound_saml_sso_profile import InboundSamlSsoProfile
from openapi_server.models.list_idp_credentials_response import ListIdpCredentialsResponse
from openapi_server.models.list_inbound_saml_sso_profiles_response import ListInboundSamlSsoProfilesResponse
from openapi_server.models.operation import Operation
from openapi_server import util


async def cloudidentity_inbound_saml_sso_profiles_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_inbound_saml_sso_profiles_create

    Creates an InboundSamlSsoProfile for a customer.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = InboundSamlSsoProfile.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_inbound_saml_sso_profiles_idp_credentials_add(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudidentity_inbound_saml_sso_profiles_idp_credentials_add

    Adds an IdpCredential. Up to 2 credentials are allowed.

    :param parent: Required. The InboundSamlSsoProfile that owns the IdpCredential. Format: &#x60;inboundSamlSsoProfiles/{sso_profile_id}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddIdpCredentialRequest.from_dict(body)
    return web.Response(status=200)


async def cloudidentity_inbound_saml_sso_profiles_idp_credentials_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """cloudidentity_inbound_saml_sso_profiles_idp_credentials_list

    Returns a list of IdpCredentials in an InboundSamlSsoProfile.

    :param parent: Required. The parent, which owns this collection of &#x60;IdpCredential&#x60;s. Format: &#x60;inboundSamlSsoProfiles/{sso_profile_id}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of &#x60;IdpCredential&#x60;s to return. The service may return fewer than this value.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListIdpCredentials&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListIdpCredentials&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudidentity_inbound_saml_sso_profiles_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudidentity_inbound_saml_sso_profiles_list

    Lists InboundSamlSsoProfiles for a customer.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: A [Common Expression Language](https://github.com/google/cel-spec) expression to filter the results. The only supported filter is filtering by customer. For example: &#x60;customer&#x3D;&#x3D;\&quot;customers/C0123abc\&quot;&#x60;. Omitting the filter or specifying a filter of &#x60;customer&#x3D;&#x3D;\&quot;customers/my_customer\&quot;&#x60; will return the profiles for the customer that the caller (authenticated user) belongs to.
    :type filter: str
    :param page_size: The maximum number of InboundSamlSsoProfiles to return. The service may return fewer than this value. If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time. The maximum allowed value is 100. Requests with page_size greater than that will be silently interpreted as having this maximum value.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListInboundSamlSsoProfiles&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListInboundSamlSsoProfiles&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)
