from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_grant import ApplicationGrant
from openapi_server.models.authorization import Authorization
from openapi_server.models.basic_error import BasicError
from openapi_server.models.oauth_authorizations_create_authorization_request import OauthAuthorizationsCreateAuthorizationRequest
from openapi_server.models.oauth_authorizations_get_or_create_authorization_for_app_and_fingerprint_request import OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest
from openapi_server.models.oauth_authorizations_get_or_create_authorization_for_app_request import OauthAuthorizationsGetOrCreateAuthorizationForAppRequest
from openapi_server.models.oauth_authorizations_update_authorization_request import OauthAuthorizationsUpdateAuthorizationRequest
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def oauth_authorizations_create_authorization(request: web.Request, body=None) -> web.Response:
    """Create a new authorization

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  **Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).  Creates OAuth tokens using [Basic Authentication](https://docs.github.com/enterprise-server@2.22/rest/overview/other-authentication-methods#basic-authentication). If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@2.22/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;  To create tokens for a particular OAuth application using this endpoint, you must authenticate as the user you want to create an authorization for and provide the app&#39;s client ID and secret, found on your OAuth application&#39;s settings page. If your OAuth application intends to create multiple tokens for one user, use &#x60;fingerprint&#x60; to differentiate between them.  You can also create tokens on GitHub Enterprise Server from the [personal access tokens settings](https://github.com/settings/tokens) page. Read more about these tokens in [the GitHub Help documentation](https://help.github.com/articles/creating-an-access-token-for-command-line-use).  Organizations that enforce SAML SSO require personal access tokens to be allowed. Read more about allowing tokens in [the GitHub Help documentation](https://help.github.com/articles/about-identity-and-access-management-with-saml-single-sign-on).

    :param body: 
    :type body: dict | bytes

    """
    body = OauthAuthorizationsCreateAuthorizationRequest.from_dict(body)
    return web.Response(status=200)


async def oauth_authorizations_delete_authorization(request: web.Request, authorization_id) -> web.Response:
    """Delete an authorization

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    :param authorization_id: authorization_id parameter
    :type authorization_id: int

    """
    return web.Response(status=200)


async def oauth_authorizations_delete_grant(request: web.Request, grant_id) -> web.Response:
    """Delete a grant

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  Deleting an OAuth application&#39;s grant will also delete all OAuth tokens associated with the application for your user. Once deleted, the application has no access to your account and is no longer listed on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized).

    :param grant_id: grant_id parameter
    :type grant_id: int

    """
    return web.Response(status=200)


async def oauth_authorizations_get_authorization(request: web.Request, authorization_id) -> web.Response:
    """Get a single authorization

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    :param authorization_id: authorization_id parameter
    :type authorization_id: int

    """
    return web.Response(status=200)


async def oauth_authorizations_get_grant(request: web.Request, grant_id) -> web.Response:
    """Get a single grant

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    :param grant_id: grant_id parameter
    :type grant_id: int

    """
    return web.Response(status=200)


async def oauth_authorizations_get_or_create_authorization_for_app(request: web.Request, client_id, body) -> web.Response:
    """Get-or-create an authorization for a specific app

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  **Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).  Creates a new authorization for the specified OAuth application, only if an authorization for that application doesn&#39;t already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. It returns the user&#39;s existing authorization for the application if one is present. Otherwise, it creates and returns a new one.  If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@2.22/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;  **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OauthAuthorizationsGetOrCreateAuthorizationForAppRequest.from_dict(body)
    return web.Response(status=200)


async def oauth_authorizations_get_or_create_authorization_for_app_and_fingerprint(request: web.Request, client_id, fingerprint, body) -> web.Response:
    """Get-or-create an authorization for a specific app and fingerprint

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  **Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).  This method will create a new authorization for the specified OAuth application, only if an authorization for that application and fingerprint do not already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. &#x60;fingerprint&#x60; is a unique string to distinguish an authorization from others created for the same client ID and user. It returns the user&#39;s existing authorization for the application if one is present. Otherwise, it creates and returns a new one.  If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@2.22/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param fingerprint: 
    :type fingerprint: str
    :param body: 
    :type body: dict | bytes

    """
    body = OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest.from_dict(body)
    return web.Response(status=200)


async def oauth_authorizations_list_authorizations(request: web.Request, per_page=None, page=None, client_id=None) -> web.Response:
    """List your authorizations

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param client_id: The client ID of your GitHub app.
    :type client_id: str

    """
    return web.Response(status=200)


async def oauth_authorizations_list_grants(request: web.Request, per_page=None, page=None, client_id=None) -> web.Response:
    """List your grants

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  You can use this API to list the set of OAuth applications that have been granted access to your account. Unlike the [list your authorizations](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations#list-your-authorizations) API, this API does not manage individual tokens. This API will return one entry for each OAuth application that has been granted access to your account, regardless of the number of tokens an application has generated for your user. The list of OAuth applications returned matches what is shown on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized). The &#x60;scopes&#x60; returned are the union of scopes authorized for the application. For example, if an application has one token with &#x60;repo&#x60; scope and another token with &#x60;user&#x60; scope, the grant will return &#x60;[\&quot;repo\&quot;, \&quot;user\&quot;]&#x60;.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param client_id: The client ID of your GitHub app.
    :type client_id: str

    """
    return web.Response(status=200)


async def oauth_authorizations_update_authorization(request: web.Request, authorization_id, body=None) -> web.Response:
    """Update an existing authorization

    **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@2.22/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@2.22/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@2.22/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;  You can only send one of these scope keys at a time.

    :param authorization_id: authorization_id parameter
    :type authorization_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = OauthAuthorizationsUpdateAuthorizationRequest.from_dict(body)
    return web.Response(status=200)
