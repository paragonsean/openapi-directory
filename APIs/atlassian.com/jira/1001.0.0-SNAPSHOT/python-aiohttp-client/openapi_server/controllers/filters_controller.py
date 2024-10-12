from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_filter_owner import ChangeFilterOwner
from openapi_server.models.column_item import ColumnItem
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.filter import Filter
from openapi_server.models.page_bean_filter_details import PageBeanFilterDetails
from openapi_server import util


async def change_filter_owner(request: web.Request, id, body) -> web.Response:
    """Change filter owner

    Changes the owner of the filter.  **[Permissions](#permissions) required:** Permission to access Jira. However, the user must own the filter or have the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the filter to update.
    :type id: int
    :param body: The account ID of the new owner of the filter.
    :type body: dict | bytes

    """
    body = ChangeFilterOwner.from_dict(body)
    return web.Response(status=200)


async def create_filter(request: web.Request, body, expand=None, override_share_permissions=None) -> web.Response:
    """Create filter

    Creates a filter. The filter is shared according to the [default share scope](#api-rest-api-3-filter-post). The filter is not selected as a favorite.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param body: The filter to create.
    :type body: dict | bytes
    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;sharedUsers&#x60; Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don&#39;t specify &#x60;sharedUsers&#x60;, then the &#x60;sharedUsers&#x60; object is returned but it doesn&#39;t list any users. The list of users returned is limited to 1000, to access additional users append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 users, use &#x60;?expand&#x3D;sharedUsers[1001:2000]&#x60;.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter. If you don&#39;t specify &#x60;subscriptions&#x60;, the &#x60;subscriptions&#x60; object is returned but it doesn&#39;t list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 subscriptions, use &#x60;?expand&#x3D;subscriptions[1001:2000]&#x60;.
    :type expand: str
    :param override_share_permissions: EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be created. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
    :type override_share_permissions: bool

    """
    body = Filter.from_dict(body)
    return web.Response(status=200)


async def delete_favourite_for_filter(request: web.Request, id, expand=None) -> web.Response:
    """Remove filter as favorite

    Removes a filter as a favorite for the user. Note that this operation only removes filters visible to the user from the user&#39;s favorites list. For example, if the user favorites a public filter that is subsequently made private (and is therefore no longer visible on their favorites list) they cannot remove it from their favorites list.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param id: The ID of the filter.
    :type id: int
    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;sharedUsers&#x60; Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don&#39;t specify &#x60;sharedUsers&#x60;, then the &#x60;sharedUsers&#x60; object is returned but it doesn&#39;t list any users. The list of users returned is limited to 1000, to access additional users append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 users, use &#x60;?expand&#x3D;sharedUsers[1001:2000]&#x60;.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter. If you don&#39;t specify &#x60;subscriptions&#x60;, the &#x60;subscriptions&#x60; object is returned but it doesn&#39;t list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 subscriptions, use &#x60;?expand&#x3D;subscriptions[1001:2000]&#x60;.
    :type expand: str

    """
    return web.Response(status=200)


async def delete_filter(request: web.Request, id) -> web.Response:
    """Delete filter

    Delete a filter.  **[Permissions](#permissions) required:** Permission to access Jira, however filters can only be deleted by the creator of the filter or a user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the filter to delete.
    :type id: int

    """
    return web.Response(status=200)


async def get_columns(request: web.Request, id) -> web.Response:
    """Get columns

    Returns the columns configured for a filter. The column configuration is used when the filter&#39;s results are viewed in *List View* with the *Columns* set to *Filter*.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, column details are only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

    :param id: The ID of the filter.
    :type id: int

    """
    return web.Response(status=200)


async def get_favourite_filters(request: web.Request, expand=None) -> web.Response:
    """Get favorite filters

    Returns the visible favorite filters of the user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the filter is:   *  owned by the user.  *  shared with a group that the user is a member of.  *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  shared with a public project.  *  shared with the public.  For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.

    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;sharedUsers&#x60; Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don&#39;t specify &#x60;sharedUsers&#x60;, then the &#x60;sharedUsers&#x60; object is returned but it doesn&#39;t list any users. The list of users returned is limited to 1000, to access additional users append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 users, use &#x60;?expand&#x3D;sharedUsers[1001:2000]&#x60;.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter. If you don&#39;t specify &#x60;subscriptions&#x60;, the &#x60;subscriptions&#x60; object is returned but it doesn&#39;t list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 subscriptions, use &#x60;?expand&#x3D;subscriptions[1001:2000]&#x60;.
    :type expand: str

    """
    return web.Response(status=200)


async def get_filter(request: web.Request, id, expand=None, override_share_permissions=None) -> web.Response:
    """Get filter

    Returns a filter.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, the filter is only returned where it is:   *  owned by the user.  *  shared with a group that the user is a member of.  *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  shared with a public project.  *  shared with the public.

    :param id: The ID of the filter to return.
    :type id: int
    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;sharedUsers&#x60; Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don&#39;t specify &#x60;sharedUsers&#x60;, then the &#x60;sharedUsers&#x60; object is returned but it doesn&#39;t list any users. The list of users returned is limited to 1000, to access additional users append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 users, use &#x60;?expand&#x3D;sharedUsers[1001:2000]&#x60;.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter. If you don&#39;t specify &#x60;subscriptions&#x60;, the &#x60;subscriptions&#x60; object is returned but it doesn&#39;t list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 subscriptions, use &#x60;?expand&#x3D;subscriptions[1001:2000]&#x60;.
    :type expand: str
    :param override_share_permissions: EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
    :type override_share_permissions: bool

    """
    return web.Response(status=200)


async def get_filters_paginated(request: web.Request, filter_name=None, account_id=None, owner=None, groupname=None, group_id=None, project_id=None, id=None, order_by=None, start_at=None, max_results=None, expand=None, override_share_permissions=None) -> web.Response:
    """Search for filters

    Returns a [paginated](#pagination) list of filters. Use this operation to get:   *  specific filters, by defining &#x60;id&#x60; only.  *  filters that match all of the specified attributes. For example, all filters for a user with a particular word in their name. When multiple attributes are specified only filters matching all attributes are returned.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, only the following filters that match the query parameters are returned:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

    :param filter_name: String used to perform a case-insensitive partial match with &#x60;name&#x60;.
    :type filter_name: str
    :param account_id: User account ID used to return filters with the matching &#x60;owner.accountId&#x60;. This parameter cannot be used with &#x60;owner&#x60;.
    :type account_id: str
    :param owner: This parameter is deprecated because of privacy changes. Use &#x60;accountId&#x60; instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. User name used to return filters with the matching &#x60;owner.name&#x60;. This parameter cannot be used with &#x60;accountId&#x60;.
    :type owner: str
    :param groupname: As a group&#39;s name can change, use of &#x60;groupId&#x60; is recommended to identify a group. Group name used to returns filters that are shared with a group that matches &#x60;sharePermissions.group.groupname&#x60;. This parameter cannot be used with the &#x60;groupId&#x60; parameter.
    :type groupname: str
    :param group_id: Group ID used to returns filters that are shared with a group that matches &#x60;sharePermissions.group.groupId&#x60;. This parameter cannot be used with the &#x60;groupname&#x60; parameter.
    :type group_id: str
    :param project_id: Project ID used to returns filters that are shared with a project that matches &#x60;sharePermissions.project.id&#x60;.
    :type project_id: int
    :param id: The list of filter IDs. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;. Do not exceed 200 filter IDs.
    :type id: List[int]
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;description&#x60; Sorts by filter description. Note that this sorting works independently of whether the expand to display the description field is in use.  *  &#x60;favourite_count&#x60; Sorts by the count of how many users have this filter as a favorite.  *  &#x60;is_favourite&#x60; Sorts by whether the filter is marked as a favorite.  *  &#x60;id&#x60; Sorts by filter ID.  *  &#x60;name&#x60; Sorts by filter name.  *  &#x60;owner&#x60; Sorts by the ID of the filter owner.  *  &#x60;is_shared&#x60; Sorts by whether the filter is shared.
    :type order_by: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;description&#x60; Returns the description of the filter.  *  &#x60;favourite&#x60; Returns an indicator of whether the user has set the filter as a favorite.  *  &#x60;favouritedCount&#x60; Returns a count of how many users have set this filter as a favorite.  *  &#x60;jql&#x60; Returns the JQL query that the filter uses.  *  &#x60;owner&#x60; Returns the owner of the filter.  *  &#x60;searchUrl&#x60; Returns a URL to perform the filter&#39;s JQL query.  *  &#x60;sharePermissions&#x60; Returns the share permissions defined for the filter.  *  &#x60;editPermissions&#x60; Returns the edit permissions defined for the filter.  *  &#x60;isWritable&#x60; Returns whether the current user has permission to edit the filter.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter.  *  &#x60;viewUrl&#x60; Returns a URL to view the filter.
    :type expand: str
    :param override_share_permissions: EXPERIMENTAL: Whether share permissions are overridden to enable filters with any share permissions to be returned. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
    :type override_share_permissions: bool

    """
    return web.Response(status=200)


async def get_my_filters(request: web.Request, expand=None, include_favourites=None) -> web.Response:
    """Get my filters

    Returns the filters owned by the user. If &#x60;includeFavourites&#x60; is &#x60;true&#x60;, the user&#39;s visible favorite filters are also returned.  **[Permissions](#permissions) required:** Permission to access Jira, however, a favorite filters is only visible to the user where the filter is:   *  owned by the user.  *  shared with a group that the user is a member of.  *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  shared with a public project.  *  shared with the public.  For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.

    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;sharedUsers&#x60; Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don&#39;t specify &#x60;sharedUsers&#x60;, then the &#x60;sharedUsers&#x60; object is returned but it doesn&#39;t list any users. The list of users returned is limited to 1000, to access additional users append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 users, use &#x60;?expand&#x3D;sharedUsers[1001:2000]&#x60;.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter. If you don&#39;t specify &#x60;subscriptions&#x60;, the &#x60;subscriptions&#x60; object is returned but it doesn&#39;t list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 subscriptions, use &#x60;?expand&#x3D;subscriptions[1001:2000]&#x60;.
    :type expand: str
    :param include_favourites: Include the user&#39;s favorite filters in the response.
    :type include_favourites: bool

    """
    return web.Response(status=200)


async def reset_columns(request: web.Request, id) -> web.Response:
    """Reset columns

    Reset the user&#39;s column configuration for the filter to the default.  **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only reset for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

    :param id: The ID of the filter.
    :type id: int

    """
    return web.Response(status=200)


async def set_columns(request: web.Request, id, body=None) -> web.Response:
    """Set columns

    Sets the columns for a filter. Only navigable fields can be set as columns. Use [Get fields](#api-rest-api-3-field-get) to get the list fields in Jira. A navigable field has &#x60;navigable&#x60; set to &#x60;true&#x60;.  The parameters for this resource are expressed as HTML form data. For example, in curl:  &#x60;curl -X PUT -d columns&#x3D;summary -d columns&#x3D;description https://your-domain.atlassian.net/rest/api/3/filter/10000/columns&#x60;  **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only set for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

    :param id: The ID of the filter.
    :type id: int
    :param body: The IDs of the fields to set as columns. In the form data, specify each field as &#x60;columns&#x3D;id&#x60;, where &#x60;id&#x60; is the *id* of a field (as seen in the response for [Get fields](#api-rest-api-&lt;ver&gt;-field-get)). For example, &#x60;columns&#x3D;summary&#x60;.
    :type body: List[str]

    """
    return web.Response(status=200)


async def set_favourite_for_filter(request: web.Request, id, expand=None) -> web.Response:
    """Add filter as favorite

    Add a filter as a favorite for the user.  **[Permissions](#permissions) required:** Permission to access Jira, however, the user can only favorite:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

    :param id: The ID of the filter.
    :type id: int
    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;sharedUsers&#x60; Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don&#39;t specify &#x60;sharedUsers&#x60;, then the &#x60;sharedUsers&#x60; object is returned but it doesn&#39;t list any users. The list of users returned is limited to 1000, to access additional users append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 users, use &#x60;?expand&#x3D;sharedUsers[1001:2000]&#x60;.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter. If you don&#39;t specify &#x60;subscriptions&#x60;, the &#x60;subscriptions&#x60; object is returned but it doesn&#39;t list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 subscriptions, use &#x60;?expand&#x3D;subscriptions[1001:2000]&#x60;.
    :type expand: str

    """
    return web.Response(status=200)


async def update_filter(request: web.Request, id, body, expand=None, override_share_permissions=None) -> web.Response:
    """Update filter

    Updates a filter. Use this operation to update a filter&#39;s name, description, JQL, or sharing.  **[Permissions](#permissions) required:** Permission to access Jira, however the user must own the filter.

    :param id: The ID of the filter to update.
    :type id: int
    :param body: The filter to update.
    :type body: dict | bytes
    :param expand: Use [expand](#expansion) to include additional information about filter in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;sharedUsers&#x60; Returns the users that the filter is shared with. This includes users that can browse projects that the filter is shared with. If you don&#39;t specify &#x60;sharedUsers&#x60;, then the &#x60;sharedUsers&#x60; object is returned but it doesn&#39;t list any users. The list of users returned is limited to 1000, to access additional users append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 users, use &#x60;?expand&#x3D;sharedUsers[1001:2000]&#x60;.  *  &#x60;subscriptions&#x60; Returns the users that are subscribed to the filter. If you don&#39;t specify &#x60;subscriptions&#x60;, the &#x60;subscriptions&#x60; object is returned but it doesn&#39;t list any subscriptions. The list of subscriptions returned is limited to 1000, to access additional subscriptions append &#x60;[start-index:end-index]&#x60; to the expand request. For example, to access the next 1000 subscriptions, use &#x60;?expand&#x3D;subscriptions[1001:2000]&#x60;.
    :type expand: str
    :param override_share_permissions: EXPERIMENTAL: Whether share permissions are overridden to enable the addition of any share permissions to filters. Available to users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
    :type override_share_permissions: bool

    """
    body = Filter.from_dict(body)
    return web.Response(status=200)
