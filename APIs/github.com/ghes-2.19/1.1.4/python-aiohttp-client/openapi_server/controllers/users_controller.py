from typing import List, Dict
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.email import Email
from openapi_server.models.gpg_key import GpgKey
from openapi_server.models.hovercard import Hovercard
from openapi_server.models.key import Key
from openapi_server.models.key_simple import KeySimple
from openapi_server.models.private_user import PrivateUser
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.users_add_email_for_authenticated_request import UsersAddEmailForAuthenticatedRequest
from openapi_server.models.users_create_gpg_key_for_authenticated_request import UsersCreateGpgKeyForAuthenticatedRequest
from openapi_server.models.users_create_public_ssh_key_for_authenticated_request import UsersCreatePublicSshKeyForAuthenticatedRequest
from openapi_server.models.users_delete_email_for_authenticated_request import UsersDeleteEmailForAuthenticatedRequest
from openapi_server.models.users_get_authenticated200_response import UsersGetAuthenticated200Response
from openapi_server.models.users_update_authenticated_request import UsersUpdateAuthenticatedRequest
from openapi_server.models.validation_error import ValidationError
from openapi_server import util


async def users_add_email_for_authenticated(request: web.Request, body=None) -> web.Response:
    """Add an email address for the authenticated user

    This endpoint is accessible with the &#x60;user&#x60; scope.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersAddEmailForAuthenticatedRequest.from_dict(body)
    return web.Response(status=200)


async def users_check_following_for_user(request: web.Request, username, target_user) -> web.Response:
    """Check if a user follows another user

    

    :param username: 
    :type username: str
    :param target_user: 
    :type target_user: str

    """
    return web.Response(status=200)


async def users_check_person_is_followed_by_authenticated(request: web.Request, username) -> web.Response:
    """Check if a person is followed by the authenticated user

    

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def users_create_gpg_key_for_authenticated(request: web.Request, body) -> web.Response:
    """Create a GPG key for the authenticated user

    Adds a GPG key to the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least &#x60;write:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param body: 
    :type body: dict | bytes

    """
    body = UsersCreateGpgKeyForAuthenticatedRequest.from_dict(body)
    return web.Response(status=200)


async def users_create_public_ssh_key_for_authenticated(request: web.Request, body) -> web.Response:
    """Create a public SSH key for the authenticated user

    Adds a public SSH key to the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least &#x60;write:public_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param body: 
    :type body: dict | bytes

    """
    body = UsersCreatePublicSshKeyForAuthenticatedRequest.from_dict(body)
    return web.Response(status=200)


async def users_delete_email_for_authenticated(request: web.Request, body=None) -> web.Response:
    """Delete an email address for the authenticated user

    This endpoint is accessible with the &#x60;user&#x60; scope.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersDeleteEmailForAuthenticatedRequest.from_dict(body)
    return web.Response(status=200)


async def users_delete_gpg_key_for_authenticated(request: web.Request, gpg_key_id) -> web.Response:
    """Delete a GPG key for the authenticated user

    Removes a GPG key from the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;admin:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param gpg_key_id: gpg_key_id parameter
    :type gpg_key_id: int

    """
    return web.Response(status=200)


async def users_delete_public_ssh_key_for_authenticated(request: web.Request, key_id) -> web.Response:
    """Delete a public SSH key for the authenticated user

    Removes a public SSH key from the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;admin:public_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param key_id: key_id parameter
    :type key_id: int

    """
    return web.Response(status=200)


async def users_follow(request: web.Request, username) -> web.Response:
    """Follow a user

    Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;  Following a user requires the user to be logged in and authenticated with basic auth or OAuth with the &#x60;user:follow&#x60; scope.

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def users_get_authenticated(request: web.Request, ) -> web.Response:
    """Get the authenticated user

    If the authenticated user is authenticated through basic authentication or OAuth with the &#x60;user&#x60; scope, then the response lists public and private profile information.  If the authenticated user is authenticated through OAuth without the &#x60;user&#x60; scope, then the response lists only public profile information.


    """
    return web.Response(status=200)


async def users_get_by_username(request: web.Request, username) -> web.Response:
    """Get a user

    Provides publicly available information about someone with a GitHub account.  GitHub Apps with the &#x60;Plan&#x60; user permission can use this endpoint to retrieve information about a user&#39;s GitHub Enterprise Server plan. The GitHub App must be authenticated as a user. See \&quot;[Identifying and authorizing users for GitHub Apps](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/)\&quot; for details about authentication. For an example response, see &#39;Response with GitHub Enterprise Server plan information&#39; below\&quot;  The &#x60;email&#x60; key in the following response is the publicly visible email address from your GitHub Enterprise Server [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for &#x60;email&#x60;, then it will have a value of &#x60;null&#x60;. You only see publicly visible email addresses when authenticated with GitHub Enterprise Server. For more information, see [Authentication](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#authentication).  The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see \&quot;[Emails API](https://docs.github.com/enterprise-server@2.19/rest/reference/users#emails)\&quot;.

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def users_get_context_for_user(request: web.Request, username, subject_type=None, subject_id=None) -> web.Response:
    """Get contextual information for a user

    Provides hovercard information when authenticated through basic auth or OAuth with the &#x60;repo&#x60; scope. You can find out more about someone in relation to their pull requests, issues, repositories, and organizations.  The &#x60;subject_type&#x60; and &#x60;subject_id&#x60; parameters provide context for the person&#39;s hovercard, which returns more information than without the parameters. For example, if you wanted to find out more about &#x60;octocat&#x60; who owns the &#x60;Spoon-Knife&#x60; repository via cURL, it would look like this:  &#x60;&#x60;&#x60;shell  curl -u username:token   https://api.github.com/users/octocat/hovercard?subject_type&#x3D;repository&amp;subject_id&#x3D;1300192 &#x60;&#x60;&#x60;

    :param username: 
    :type username: str
    :param subject_type: Identifies which additional information you&#39;d like to receive about the person&#39;s hovercard. Can be &#x60;organization&#x60;, &#x60;repository&#x60;, &#x60;issue&#x60;, &#x60;pull_request&#x60;. **Required** when using &#x60;subject_id&#x60;.
    :type subject_type: str
    :param subject_id: Uses the ID for the &#x60;subject_type&#x60; you specified. **Required** when using &#x60;subject_type&#x60;.
    :type subject_id: str

    """
    return web.Response(status=200)


async def users_get_gpg_key_for_authenticated(request: web.Request, gpg_key_id) -> web.Response:
    """Get a GPG key for the authenticated user

    View extended details for a single GPG key. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param gpg_key_id: gpg_key_id parameter
    :type gpg_key_id: int

    """
    return web.Response(status=200)


async def users_get_public_ssh_key_for_authenticated(request: web.Request, key_id) -> web.Response:
    """Get a public SSH key for the authenticated user

    View extended details for a single public SSH key. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:public_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param key_id: key_id parameter
    :type key_id: int

    """
    return web.Response(status=200)


async def users_list(request: web.Request, since=None, per_page=None) -> web.Response:
    """List users

    Lists all users, in the order that they signed up on GitHub Enterprise Server. This list includes personal user accounts and organization accounts.  Note: Pagination is powered exclusively by the &#x60;since&#x60; parameter. Use the [Link header](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of users.

    :param since: A user ID. Only return users with an ID greater than this ID.
    :type since: int
    :param per_page: Results per page (max 100)
    :type per_page: int

    """
    return web.Response(status=200)


async def users_list_emails_for_authenticated(request: web.Request, per_page=None, page=None) -> web.Response:
    """List email addresses for the authenticated user

    Lists all of your email addresses, and specifies which one is visible to the public. This endpoint is accessible with the &#x60;user:email&#x60; scope.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_followed_by_authenticated(request: web.Request, per_page=None, page=None) -> web.Response:
    """List the people the authenticated user follows

    Lists the people who the authenticated user follows.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_followers_for_authenticated_user(request: web.Request, per_page=None, page=None) -> web.Response:
    """List followers of the authenticated user

    Lists the people following the authenticated user.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_followers_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List followers of a user

    Lists the people following the specified user.

    :param username: 
    :type username: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_following_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List the people a user follows

    Lists the people who the specified user follows.

    :param username: 
    :type username: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_gpg_keys_for_authenticated(request: web.Request, per_page=None, page=None) -> web.Response:
    """List GPG keys for the authenticated user

    Lists the current user&#39;s GPG keys. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_gpg_keys_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List GPG keys for a user

    Lists the GPG keys for a user. This information is accessible by anyone.

    :param username: 
    :type username: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_public_emails_for_authenticated(request: web.Request, per_page=None, page=None) -> web.Response:
    """List public email addresses for the authenticated user

    Lists your publicly visible email address, which you can set with the [Set primary email visibility for the authenticated user](https://docs.github.com/enterprise-server@2.19/rest/reference/users#set-primary-email-visibility-for-the-authenticated-user) endpoint. This endpoint is accessible with the &#x60;user:email&#x60; scope.

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_public_keys_for_user(request: web.Request, username, per_page=None, page=None) -> web.Response:
    """List public keys for a user

    Lists the _verified_ public SSH keys for a user. This is accessible by anyone.

    :param username: 
    :type username: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_list_public_ssh_keys_for_authenticated(request: web.Request, per_page=None, page=None) -> web.Response:
    """List public SSH keys for the authenticated user

    Lists the public SSH keys for the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:public_key&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def users_unfollow(request: web.Request, username) -> web.Response:
    """Unfollow a user

    Unfollowing a user requires the user to be logged in and authenticated with basic auth or OAuth with the &#x60;user:follow&#x60; scope.

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def users_update_authenticated(request: web.Request, body=None) -> web.Response:
    """Update the authenticated user

    **Note:** If your email is set to private and you send an &#x60;email&#x60; parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersUpdateAuthenticatedRequest.from_dict(body)
    return web.Response(status=200)
