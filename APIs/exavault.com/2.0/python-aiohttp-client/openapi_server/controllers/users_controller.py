from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user_request_body import AddUserRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.update_user_request_body import UpdateUserRequestBody
from openapi_server.models.user_collection_response import UserCollectionResponse
from openapi_server.models.user_response import UserResponse
from openapi_server import util


async def add_user(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Create a user

    Adds a new user to the account. The user may be configured as an admin or standard user, and (if a standard user) may be assigned a restricted [home directory](/docs/account/04-users/00-introduction#setting-the-user-s-home-directory) and restricted [permissions](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions).   **Notes:**  - You must be an [admin-level user](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this.

    :param ev_api_key: API key required to make the API call
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddUserRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_user(request: web.Request, id, ev_api_key, ev_access_token) -> web.Response:
    """Delete a user

    Delete a user from the account. Deleting a user does **NOT** delete any files from the account; it merely removes a user&#39;s access. Aternatively, locking a user via the [PATCH /users/{id}](#operation/updateUser) will keep the user in your account, but make it unable to log in.   Resources and shares owned by the deleted user will be owned by the master user after the deletion.  **Notes:**   - You must have [admin-level access](/docs/account/04-users/01-admin-users) to delete a user. - The primary owner of the account cannot be deleted. 

    :param id: The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
    :type id: int
    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def get_user_by_id(request: web.Request, id, ev_api_key, ev_access_token, include=None) -> web.Response:
    """Get info for a user

    Get the details for a specific user. You can use the &#x60;include&#x60; parameter to also get the details of related records, such as the account or the home directory.  **Notes:**  - You must have [admin or master](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) access to use this.

    :param id: The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
    :type id: int
    :param ev_api_key: API Key
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param include: Comma-separated list of relationships to include in response. Possible values include **homeResource** and **ownerAccount**.
    :type include: str

    """
    return web.Response(status=200)


async def list_users(request: web.Request, ev_api_key, ev_access_token, username=None, home_resource=None, nickname=None, email=None, role=None, status=None, search=None, offset=None, sort=None, limit=None, include=None) -> web.Response:
    """Get a list of users

    Get a list of the users in your account. There are three main types of searches you can do with this method:  1. Search for a user by username. If you provide the &#x60;username&#x60; parameter in your call, then only the user who exactly matches that username will be in the list of matches. Any other parameters are ignored. 1. Search for a user by individual filter fields (&#x60;nickname&#x60;,&#x60;email&#x60;,&#x60;role&#x60;,&#x60;status&#x60;,&#x60;homeDir&#x60;). Users in the list will be ones who match all of the filters you choose to search by. For example, you could look for users with the \&quot;admin\&quot; &#x60;role&#x60; AND &#x60;email&#x60; addresses ending in \&quot;*@acme.com\&quot;.  1. Search for a user by search string. If you provide the &#x60;search&#x60; parameter, users whose nickname OR email OR role OR homeDir match value your provide.  **Notes:**  - You must be an [admin-level user](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to use this. - The homeDir is the full path to the user&#39;s home directory, not a resource ID or hash.

    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param username: The username of the user you are looking for. Only entries with the same username as this will be in the list of results. Does not support wildcard searches.
    :type username: str
    :param home_resource: Resource identifier for user&#39;s home directory. Does not support wildcard searches.
    :type home_resource: str
    :param nickname: Nickname to search for. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches.
    :type nickname: str
    :param email: Email to search for. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches
    :type email: str
    :param role: Types of users to include the list. Ignored if &#x60;username&#x60; is provided. Valid options are **admin**, **master** and **user**
    :type role: str
    :param status: Whether a user is locked. Ignored if &#x60;username&#x60; is provided. **0** means user is locked, **1** means user is not locked. 
    :type status: int
    :param search: Searches the nickname, email, role and homeDir fields for the provided value. Ignored if &#x60;username&#x60; is provided. Supports wildcard searches.
    :type search: str
    :param offset: Starting user record in the result set. Can be used for pagination.
    :type offset: int
    :param sort: Sort order or matching users. You can sort by multiple columns by separating sort options with a comma; the sort will be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  Valid sort fields are: **nickname**, **username**, **email**, **homeDir** and **modified**
    :type sort: str
    :param limit: Number of users to return. Can be used for pagination.
    :type limit: int
    :param include: Comma separated list of relationships to include in response. Valid options are **homeResource** and **ownerAccount**.
    :type include: str

    """
    return web.Response(status=200)


async def update_user(request: web.Request, id, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Update a user

    Updates the settings for the user. Note that the unique key for this API call is our internal ID, and _not_ the username, as the username can be changed.  In the request body, you should only send the parameters for values that you wish to change for the user.  **Notes:**  - You must have [admin or master](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) access to edit other users. If you have user-level access, you can only update your own user settings. - You cannot edit a master user with this method.

    :param id: The user&#39;s ID. Note that this is our internal ID, and _not the username_. You can obtain it by calling the [GET /users](#operation/listUsers) method.
    :type id: int
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateUserRequestBody.from_dict(body)
    return web.Response(status=200)
