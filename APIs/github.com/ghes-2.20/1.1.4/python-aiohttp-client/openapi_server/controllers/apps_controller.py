from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_check_token_request import AppsCheckTokenRequest
from openapi_server.models.apps_create_content_attachment_request import AppsCreateContentAttachmentRequest
from openapi_server.models.apps_create_from_manifest201_response import AppsCreateFromManifest201Response
from openapi_server.models.apps_create_installation_access_token_request import AppsCreateInstallationAccessTokenRequest
from openapi_server.models.apps_delete_authorization_request import AppsDeleteAuthorizationRequest
from openapi_server.models.apps_delete_token_request import AppsDeleteTokenRequest
from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.apps_list_installation_repos_for_authenticated_user200_response import AppsListInstallationReposForAuthenticatedUser200Response
from openapi_server.models.apps_list_repos_accessible_to_installation200_response import AppsListReposAccessibleToInstallation200Response
from openapi_server.models.authorization import Authorization
from openapi_server.models.basic_error import BasicError
from openapi_server.models.content_reference_attachment import ContentReferenceAttachment
from openapi_server.models.installation_ghes2 import InstallationGhes2
from openapi_server.models.installation_token import InstallationToken
from openapi_server.models.integration import Integration
from openapi_server.models.nullable_authorization import NullableAuthorization
from openapi_server.models.orgs_list_app_installations200_response import OrgsListAppInstallations200Response
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.validation_error_simple import ValidationErrorSimple
from openapi_server import util


async def apps_add_repo_to_installation(request: web.Request, installation_id, repository_id) -> web.Response:
    """Add a repository to an app installation

    Add a single repository to an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@2.20/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

    :param installation_id: installation_id parameter
    :type installation_id: int
    :param repository_id: 
    :type repository_id: int

    """
    return web.Response(status=200)


async def apps_check_authorization(request: web.Request, client_id, access_token) -> web.Response:
    """Check an authorization

    **Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain &#x60;access_token&#x60; in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving &#x60;access_token&#x60; to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).  OAuth applications can use a special API method for checking OAuth token validity without exceeding the normal rate limits for failed login attempts. Authentication works differently with this particular endpoint. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password. Invalid tokens will return &#x60;404 NOT FOUND&#x60;.

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param access_token: 
    :type access_token: str

    """
    return web.Response(status=200)


async def apps_check_token(request: web.Request, client_id, body) -> web.Response:
    """Check a token

    OAuth applications can use a special API method for checking OAuth token validity without exceeding the normal rate limits for failed login attempts. Authentication works differently with this particular endpoint. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) to use this endpoint, where the username is the OAuth application &#x60;client_id&#x60; and the password is its &#x60;client_secret&#x60;. Invalid tokens will return &#x60;404 NOT FOUND&#x60;.

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppsCheckTokenRequest.from_dict(body)
    return web.Response(status=200)


async def apps_create_content_attachment(request: web.Request, owner, repo, content_reference_id, body) -> web.Response:
    """Create a content attachment

    Creates an attachment under a content reference URL in the body or comment of an issue or pull request. Use the &#x60;id&#x60; and &#x60;repository&#x60; &#x60;full_name&#x60; of the content reference from the [&#x60;content_reference&#x60; event](https://docs.github.com/enterprise-server@2.20/webhooks/event-payloads/#content_reference) to create an attachment.  The app must create a content attachment within six hours of the content reference URL being posted. See \&quot;[Using content attachments](https://docs.github.com/enterprise-server@2.20/apps/using-content-attachments/)\&quot; for details about content attachments.  You must use an [installation access token](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

    :param owner: The owner of the repository. Determined from the &#x60;repository&#x60; &#x60;full_name&#x60; of the &#x60;content_reference&#x60; event.
    :type owner: str
    :param repo: The name of the repository. Determined from the &#x60;repository&#x60; &#x60;full_name&#x60; of the &#x60;content_reference&#x60; event.
    :type repo: str
    :param content_reference_id: The &#x60;id&#x60; of the &#x60;content_reference&#x60; event.
    :type content_reference_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AppsCreateContentAttachmentRequest.from_dict(body)
    return web.Response(status=200)


async def apps_create_from_manifest(request: web.Request, code, body=None) -> web.Response:
    """Create a GitHub App from a manifest

    Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary &#x60;code&#x60; used to retrieve the GitHub App&#39;s &#x60;id&#x60;, &#x60;pem&#x60; (private key), and &#x60;webhook_secret&#x60;.

    :param code: 
    :type code: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def apps_create_installation_access_token(request: web.Request, accept, installation_id, body=None) -> web.Response:
    """Create an installation access token for an app

    Creates an installation access token that enables a GitHub App to make authenticated API requests for the app&#39;s installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of &#x60;401 - Unauthorized&#x60;, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the &#x60;repository_ids&#x60; when creating the token. When you omit &#x60;repository_ids&#x60;, the response does not contain the &#x60;repositories&#x60; key.  You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param installation_id: installation_id parameter
    :type installation_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AppsCreateInstallationAccessTokenRequest.from_dict(body)
    return web.Response(status=200)


async def apps_delete_authorization(request: web.Request, client_id, body=None) -> web.Response:
    """Delete an app authorization

    OAuth application owners can revoke a grant for their OAuth application and a specific user. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password. You must also provide a valid OAuth &#x60;access_token&#x60; as an input parameter and the grant for the token&#39;s owner will be deleted. Deleting an OAuth application&#39;s grant will also delete all OAuth tokens associated with the application for the user. Once deleted, the application will have no access to the user&#39;s account and will no longer be listed on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized).

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppsDeleteAuthorizationRequest.from_dict(body)
    return web.Response(status=200)


async def apps_delete_installation(request: web.Request, accept, installation_id) -> web.Response:
    """Delete an installation for the authenticated app

    Uninstalls a GitHub App on a user, organization, or business account. You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param installation_id: installation_id parameter
    :type installation_id: int

    """
    return web.Response(status=200)


async def apps_delete_token(request: web.Request, client_id, body) -> web.Response:
    """Delete an app token

    OAuth application owners can revoke a single token for an OAuth application. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password.

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppsDeleteTokenRequest.from_dict(body)
    return web.Response(status=200)


async def apps_get_authenticated(request: web.Request, ) -> web.Response:
    """Get the authenticated app

    Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the &#x60;installations_count&#x60; in the response. For more details about your app&#39;s installations, see the \&quot;[List installations for the authenticated app](https://docs.github.com/enterprise-server@2.20/rest/reference/apps#list-installations-for-the-authenticated-app)\&quot; endpoint.  You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.


    """
    return web.Response(status=200)


async def apps_get_by_slug(request: web.Request, app_slug) -> web.Response:
    """Get an app

    **Note**: The &#x60;:app_slug&#x60; is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., &#x60;https://github.com/settings/apps/:app_slug&#x60;).  If the GitHub App you specify is public, you can access this endpoint without authenticating. If the GitHub App you specify is private, you must authenticate with a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) or an [installation access token](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

    :param app_slug: 
    :type app_slug: str

    """
    return web.Response(status=200)


async def apps_get_installation(request: web.Request, accept, installation_id) -> web.Response:
    """Get an installation for the authenticated app

    Enables an authenticated GitHub App to find an installation&#39;s information using the installation id. The installation&#39;s account type (&#x60;target_type&#x60;) will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param installation_id: installation_id parameter
    :type installation_id: int

    """
    return web.Response(status=200)


async def apps_get_org_installation(request: web.Request, accept, org) -> web.Response:
    """Get an organization installation for the authenticated app

    Enables an authenticated GitHub App to find the organization&#39;s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param org: 
    :type org: str

    """
    return web.Response(status=200)


async def apps_get_repo_installation(request: web.Request, accept, owner, repo) -> web.Response:
    """Get a repository installation for the authenticated app

    Enables an authenticated GitHub App to find the repository&#39;s installation information. The installation&#39;s account type will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def apps_get_user_installation(request: web.Request, accept, username) -> web.Response:
    """Get a user installation for the authenticated app

    Enables an authenticated GitHub App to find the user’s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def apps_list_installation_repos_for_authenticated_user(request: web.Request, accept, installation_id, per_page=None, page=None) -> web.Response:
    """List repositories accessible to the user access token

    List repositories that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access for an installation.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The access the user has to each repository is included in the hash under the &#x60;permissions&#x60; key.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param installation_id: installation_id parameter
    :type installation_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def apps_list_installations(request: web.Request, accept, per_page=None, page=None) -> web.Response:
    """List installations for the authenticated app

    You must use a [JWT](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.  The permissions the installation has are included under the &#x60;permissions&#x60; key.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def apps_list_installations_for_authenticated_user(request: web.Request, accept, per_page=None, page=None) -> web.Response:
    """List app installations accessible to the user access token

    Lists installations of your GitHub App that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You can find the permissions for the installation under the &#x60;permissions&#x60; key.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def apps_list_repos_accessible_to_installation(request: web.Request, accept, per_page=None, page=None) -> web.Response:
    """List repositories accessible to the app installation

    List repositories that an app installation can access.  You must use an [installation access token](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

    :param accept: This API is under preview and subject to change.
    :type accept: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def apps_remove_repo_from_installation(request: web.Request, installation_id, repository_id) -> web.Response:
    """Remove a repository from an app installation

    Remove a single repository from an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@2.20/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

    :param installation_id: installation_id parameter
    :type installation_id: int
    :param repository_id: 
    :type repository_id: int

    """
    return web.Response(status=200)


async def apps_reset_authorization(request: web.Request, client_id, access_token) -> web.Response:
    """Reset an authorization

    **Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain &#x60;access_token&#x60; in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving &#x60;access_token&#x60; to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).  OAuth applications can use this API method to reset a valid OAuth token without end-user involvement. Applications must save the \&quot;token\&quot; property in the response because changes take effect immediately. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password. Invalid tokens will return &#x60;404 NOT FOUND&#x60;.

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param access_token: 
    :type access_token: str

    """
    return web.Response(status=200)


async def apps_reset_token(request: web.Request, client_id, body) -> web.Response:
    """Reset a token

    OAuth applications can use this API method to reset a valid OAuth token without end-user involvement. Applications must save the \&quot;token\&quot; property in the response because changes take effect immediately. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password. Invalid tokens will return &#x60;404 NOT FOUND&#x60;.

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppsCheckTokenRequest.from_dict(body)
    return web.Response(status=200)


async def apps_revoke_authorization_for_application(request: web.Request, client_id, access_token) -> web.Response:
    """Revoke an authorization for an application

    **Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain &#x60;access_token&#x60; in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving &#x60;access_token&#x60; to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).  OAuth application owners can revoke a single token for an OAuth application. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password.

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param access_token: 
    :type access_token: str

    """
    return web.Response(status=200)


async def apps_revoke_grant_for_application(request: web.Request, client_id, access_token) -> web.Response:
    """Revoke a grant for an application

    **Deprecation Notice:** GitHub Enterprise Server will discontinue OAuth endpoints that contain &#x60;access_token&#x60; in the path parameter. We have introduced new endpoints that allow you to securely manage tokens for OAuth Apps by moving &#x60;access_token&#x60; to the request body. For more information, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-app-endpoint/).  OAuth application owners can revoke a grant for their OAuth application and a specific user. You must use [Basic Authentication](https://docs.github.com/enterprise-server@2.20/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password. You must also provide a valid token as &#x60;:access_token&#x60; and the grant for the token&#39;s owner will be deleted.  Deleting an OAuth application&#39;s grant will also delete all OAuth tokens associated with the application for the user. Once deleted, the application will have no access to the user&#39;s account and will no longer be listed on [the Applications settings page under \&quot;Authorized OAuth Apps\&quot; on GitHub Enterprise Server](https://github.com/settings/applications#authorized).

    :param client_id: The client ID of your GitHub app.
    :type client_id: str
    :param access_token: 
    :type access_token: str

    """
    return web.Response(status=200)


async def apps_revoke_installation_access_token(request: web.Request, ) -> web.Response:
    """Revoke an installation access token

    Revokes the installation token you&#39;re using to authenticate as an installation and access this endpoint.  Once an installation token is revoked, the token is invalidated and cannot be used. Other endpoints that require the revoked installation token must have a new installation token to work. You can create a new token using the \&quot;[Create an installation access token for an app](https://docs.github.com/enterprise-server@2.20/rest/reference/apps#create-an-installation-access-token-for-an-app)\&quot; endpoint.  You must use an [installation access token](https://docs.github.com/enterprise-server@2.20/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.


    """
    return web.Response(status=200)
