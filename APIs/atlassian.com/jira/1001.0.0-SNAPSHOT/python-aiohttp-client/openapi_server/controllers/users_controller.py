from typing import List, Dict
from aiohttp import web

from openapi_server.models.column_item import ColumnItem
from openapi_server.models.group_name import GroupName
from openapi_server.models.new_user_details import NewUserDetails
from openapi_server.models.page_bean_user import PageBeanUser
from openapi_server.models.unrestricted_user_email import UnrestrictedUserEmail
from openapi_server.models.user import User
from openapi_server.models.user_migration_bean import UserMigrationBean
from openapi_server import util


async def bulk_get_users(request: web.Request, account_id, start_at=None, max_results=None, username=None, key=None) -> web.Response:
    """Bulk get users

    Returns a [paginated](#pagination) list of the users specified by one or more account IDs.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param account_id: The account ID of a user. To specify multiple users, pass multiple &#x60;accountId&#x60; parameters. For example, &#x60;accountId&#x3D;5b10a2844c20165700ede21g&amp;accountId&#x3D;5b10ac8d82e05b22cc7d4ef5&#x60;.
    :type account_id: List[str]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param username: This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: List[str]
    :param key: This parameter is no longer available and will be removed from the documentation soon. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type key: List[str]

    """
    return web.Response(status=200)


async def bulk_get_users_migration(request: web.Request, start_at=None, max_results=None, username=None, key=None) -> web.Response:
    """Get account IDs for users

    Returns the account IDs for the users specified in the &#x60;key&#x60; or &#x60;username&#x60; parameters. Note that multiple &#x60;key&#x60; or &#x60;username&#x60; parameters can be specified.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param username: Username of a user. To specify multiple users, pass multiple copies of this parameter. For example, &#x60;username&#x3D;fred&amp;username&#x3D;barney&#x60;. Required if &#x60;key&#x60; isn&#39;t provided. Cannot be provided if &#x60;key&#x60; is present.
    :type username: List[str]
    :param key: Key of a user. To specify multiple users, pass multiple copies of this parameter. For example, &#x60;key&#x3D;fred&amp;key&#x3D;barney&#x60;. Required if &#x60;username&#x60; isn&#39;t provided. Cannot be provided if &#x60;username&#x60; is present.
    :type key: List[str]

    """
    return web.Response(status=200)


async def create_user(request: web.Request, body) -> web.Response:
    """Create user

    Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable alternative is available this resource will be deprecated.  If the user exists and has access to Jira, the operation returns a 201 status. If the user exists but does not have access to Jira, the operation returns a 400 status.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: Details about the user to be created.
    :type body: dict | bytes

    """
    body = NewUserDetails.from_dict(body)
    return web.Response(status=200)


async def get_all_users(request: web.Request, start_at=None, max_results=None) -> web.Response:
    """Get all users

    Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return.
    :type start_at: int
    :param max_results: The maximum number of items to return.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_all_users_default(request: web.Request, start_at=None, max_results=None) -> web.Response:
    """Get all users default

    Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.  Privacy controls are applied to the response based on the users&#39; preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return.
    :type start_at: int
    :param max_results: The maximum number of items to return.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_user(request: web.Request, account_id=None, username=None, key=None, expand=None) -> web.Response:
    """Get user

    Returns a user.  Privacy controls are applied to the response based on the user&#39;s preferences. This could mean, for example, that the user&#39;s email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required.
    :type account_id: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide) for details.
    :type username: str
    :param key: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide) for details.
    :type key: str
    :param expand: Use [expand](#expansion) to include additional information about users in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;groups&#x60; includes all groups and nested groups to which the user belongs.  *  &#x60;applicationRoles&#x60; includes details of all the applications to which the user has access.
    :type expand: str

    """
    return web.Response(status=200)


async def get_user_default_columns(request: web.Request, account_id=None, username=None) -> web.Response:
    """Get user default columns

    Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If &#x60;accountId&#x60; is not passed in the request, the calling user&#39;s details are returned.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the column details for any user.  *  Permission to access Jira, to get the calling user&#39;s column details.

    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
    :type account_id: str
    :param username: This parameter is no longer available See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str

    """
    return web.Response(status=200)


async def get_user_email(request: web.Request, account_id) -> web.Response:
    """Get user email

    Returns a user&#39;s email address. This API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603).

    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, &#x60;5b10ac8d82e05b22cc7d4ef5&#x60;.
    :type account_id: str

    """
    return web.Response(status=200)


async def get_user_email_bulk(request: web.Request, account_id) -> web.Response:
    """Get user email bulk

    Returns a user&#39;s email address. This API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603).

    :param account_id: The account IDs of the users for which emails are required. An &#x60;accountId&#x60; is an identifier that uniquely identifies the user across all Atlassian products. For example, &#x60;5b10ac8d82e05b22cc7d4ef5&#x60;. Note, this should be treated as an opaque identifier (that is, do not assume any structure in the value).
    :type account_id: List[str]

    """
    return web.Response(status=200)


async def get_user_groups(request: web.Request, account_id, username=None, key=None) -> web.Response:
    """Get user groups

    Returns the groups to which a user belongs.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
    :type account_id: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str
    :param key: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type key: str

    """
    return web.Response(status=200)


async def remove_user(request: web.Request, account_id, username=None, key=None) -> web.Response:
    """Delete user

    Deletes a user. If the operation completes successfully then the user is removed from Jira&#39;s user base. This operation does not delete the user&#39;s Atlassian account.  **[Permissions](#permissions) required:** Site administration (that is, membership of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).

    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
    :type account_id: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str
    :param key: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type key: str

    """
    return web.Response(status=200)


async def reset_user_columns(request: web.Request, account_id=None, username=None) -> web.Response:
    """Reset user default columns

    Resets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user to the system default. If &#x60;accountId&#x60; is not passed, the calling user&#39;s default columns are reset.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.  *  Permission to access Jira, to set the calling user&#39;s columns.

    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
    :type account_id: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str

    """
    return web.Response(status=200)


async def set_user_columns(request: web.Request, account_id=None, body=None) -> web.Response:
    """Set user default columns

    Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If an account ID is not passed, the calling user&#39;s default columns are set. If no column details are sent, then all default columns are removed.  The parameters for this resource are expressed as HTML form data. For example, in curl:  &#x60;curl -X PUT -d columns&#x3D;summary -d columns&#x3D;description https://your-domain.atlassian.net/rest/api/3/user/columns?accountId&#x3D;5b10ac8d82e05b22cc7d4ef5&#39;&#x60;  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the columns on any user.  *  Permission to access Jira, to set the calling user&#39;s columns.

    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*.
    :type account_id: str
    :param body: The ID of a column to set. To set multiple columns, send multiple &#x60;columns&#x60; parameters.
    :type body: List[str]

    """
    return web.Response(status=200)
