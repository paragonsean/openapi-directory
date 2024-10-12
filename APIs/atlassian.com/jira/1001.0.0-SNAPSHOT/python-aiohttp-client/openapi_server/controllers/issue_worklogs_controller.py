from typing import List, Dict
from aiohttp import web

from openapi_server.models.changed_worklogs import ChangedWorklogs
from openapi_server.models.page_of_worklogs import PageOfWorklogs
from openapi_server.models.worklog import Worklog
from openapi_server.models.worklog_ids_request_bean import WorklogIdsRequestBean
from openapi_server import util


async def add_worklog(request: web.Request, issue_id_or_key, body, notify_users=None, adjust_estimate=None, new_estimate=None, reduce_by=None, expand=None, override_editable_flag=None) -> web.Response:
    """Add worklog

    Adds a worklog to an issue.  Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Work on issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key the issue.
    :type issue_id_or_key: str
    :param body: 
    :type body: dict | bytes
    :param notify_users: Whether users watching the issue are notified by email.
    :type notify_users: bool
    :param adjust_estimate: Defines how to update the issue&#39;s time estimate, the options are:   *  &#x60;new&#x60; Sets the estimate to a specific value, defined in &#x60;newEstimate&#x60;.  *  &#x60;leave&#x60; Leaves the estimate unchanged.  *  &#x60;manual&#x60; Reduces the estimate by amount specified in &#x60;reduceBy&#x60;.  *  &#x60;auto&#x60; Reduces the estimate by the value of &#x60;timeSpent&#x60; in the worklog.
    :type adjust_estimate: str
    :param new_estimate: The value to set as the issue&#39;s remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when &#x60;adjustEstimate&#x60; is &#x60;new&#x60;.
    :type new_estimate: str
    :param reduce_by: The amount to reduce the issue&#39;s remaining estimate by, as days (\\#d), hours (\\#h), or minutes (\\#m). For example, *2d*. Required when &#x60;adjustEstimate&#x60; is &#x60;manual&#x60;.
    :type reduce_by: str
    :param expand: Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts &#x60;properties&#x60;, which returns worklog properties.
    :type expand: str
    :param override_editable_flag: Whether the worklog entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag.
    :type override_editable_flag: bool

    """
    body = Worklog.from_dict(body)
    return web.Response(status=200)


async def delete_worklog(request: web.Request, issue_id_or_key, id, notify_users=None, adjust_estimate=None, new_estimate=None, increase_by=None, override_editable_flag=None) -> web.Response:
    """Delete worklog

    Deletes a worklog from an issue.  Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete any worklog or *Delete own worklogs* to delete worklogs created by the user,  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param id: The ID of the worklog.
    :type id: str
    :param notify_users: Whether users watching the issue are notified by email.
    :type notify_users: bool
    :param adjust_estimate: Defines how to update the issue&#39;s time estimate, the options are:   *  &#x60;new&#x60; Sets the estimate to a specific value, defined in &#x60;newEstimate&#x60;.  *  &#x60;leave&#x60; Leaves the estimate unchanged.  *  &#x60;manual&#x60; Increases the estimate by amount specified in &#x60;increaseBy&#x60;.  *  &#x60;auto&#x60; Reduces the estimate by the value of &#x60;timeSpent&#x60; in the worklog.
    :type adjust_estimate: str
    :param new_estimate: The value to set as the issue&#39;s remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when &#x60;adjustEstimate&#x60; is &#x60;new&#x60;.
    :type new_estimate: str
    :param increase_by: The amount to increase the issue&#39;s remaining estimate by, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when &#x60;adjustEstimate&#x60; is &#x60;manual&#x60;.
    :type increase_by: str
    :param override_editable_flag: Whether the work log entry should be added to the issue even if the issue is not editable, because jira.issue.editable set to false or missing. For example, the issue is closed. Connect and Forge app users with admin permission can use this flag.
    :type override_editable_flag: bool

    """
    return web.Response(status=200)


async def get_ids_of_worklogs_deleted_since(request: web.Request, since=None) -> web.Response:
    """Get IDs of deleted worklogs

    Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.  This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, &#x60;until&#x60; indicates the timestamp of the youngest item on the page. Also, &#x60;nextPage&#x60; provides the URL for the next page of worklogs. The &#x60;lastPage&#x60; parameter is set to true on the last page of worklogs.  This resource does not return worklogs deleted during the minute preceding the request.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param since: The date and time, as a UNIX timestamp in milliseconds, after which deleted worklogs are returned.
    :type since: int

    """
    return web.Response(status=200)


async def get_ids_of_worklogs_modified_since(request: web.Request, since=None, expand=None) -> web.Response:
    """Get IDs of updated worklogs

    Returns a list of IDs and update timestamps for worklogs updated after a date and time.  This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, &#x60;until&#x60; indicates the timestamp of the youngest item on the page. Also, &#x60;nextPage&#x60; provides the URL for the next page of worklogs. The &#x60;lastPage&#x60; parameter is set to true on the last page of worklogs.  This resource does not return worklogs updated during the minute preceding the request.  **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:   *  the worklog is set as *Viewable by All Users*.  *  the user is a member of a project role or group with permission to view the worklog.

    :param since: The date and time, as a UNIX timestamp in milliseconds, after which updated worklogs are returned.
    :type since: int
    :param expand: Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts &#x60;properties&#x60; that returns the properties of each worklog.
    :type expand: str

    """
    return web.Response(status=200)


async def get_issue_worklog(request: web.Request, issue_id_or_key, start_at=None, max_results=None, started_after=None, started_before=None, expand=None) -> web.Response:
    """Get issue worklogs

    Returns worklogs for an issue, starting from the oldest worklog or from the worklog started on or after a date and time.  Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Workloads are only returned where the user has:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param started_after: The worklog start date and time, as a UNIX timestamp in milliseconds, after which worklogs are returned.
    :type started_after: int
    :param started_before: The worklog start date and time, as a UNIX timestamp in milliseconds, before which worklogs are returned.
    :type started_before: int
    :param expand: Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts&#x60;properties&#x60;, which returns worklog properties.
    :type expand: str

    """
    return web.Response(status=200)


async def get_worklog(request: web.Request, issue_id_or_key, id, expand=None) -> web.Response:
    """Get worklog

    Returns a worklog.  Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param id: The ID of the worklog.
    :type id: str
    :param expand: Use [expand](#expansion) to include additional information about work logs in the response. This parameter accepts  &#x60;properties&#x60;, which returns worklog properties.
    :type expand: str

    """
    return web.Response(status=200)


async def get_worklogs_for_ids(request: web.Request, body, expand=None) -> web.Response:
    """Get worklogs

    Returns worklog details for a list of worklog IDs.  The returned list of worklogs is limited to 1000 items.  **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:   *  the worklog is set as *Viewable by All Users*.  *  the user is a member of a project role or group with permission to view the worklog.

    :param body: A JSON object containing a list of worklog IDs.
    :type body: dict | bytes
    :param expand: Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts &#x60;properties&#x60; that returns the properties of each worklog.
    :type expand: str

    """
    body = WorklogIdsRequestBean.from_dict(body)
    return web.Response(status=200)


async def update_worklog(request: web.Request, issue_id_or_key, id, body, notify_users=None, adjust_estimate=None, new_estimate=None, expand=None, override_editable_flag=None) -> web.Response:
    """Update worklog

    Updates a worklog.  Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key the issue.
    :type issue_id_or_key: str
    :param id: The ID of the worklog.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param notify_users: Whether users watching the issue are notified by email.
    :type notify_users: bool
    :param adjust_estimate: Defines how to update the issue&#39;s time estimate, the options are:   *  &#x60;new&#x60; Sets the estimate to a specific value, defined in &#x60;newEstimate&#x60;.  *  &#x60;leave&#x60; Leaves the estimate unchanged.  *  &#x60;auto&#x60; Updates the estimate by the difference between the original and updated value of &#x60;timeSpent&#x60; or &#x60;timeSpentSeconds&#x60;.
    :type adjust_estimate: str
    :param new_estimate: The value to set as the issue&#39;s remaining time estimate, as days (\\#d), hours (\\#h), or minutes (\\#m or \\#). For example, *2d*. Required when &#x60;adjustEstimate&#x60; is &#x60;new&#x60;.
    :type new_estimate: str
    :param expand: Use [expand](#expansion) to include additional information about worklogs in the response. This parameter accepts &#x60;properties&#x60;, which returns worklog properties.
    :type expand: str
    :param override_editable_flag: Whether the worklog should be added to the issue even if the issue is not editable. For example, because the issue is closed. Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) can use this flag.
    :type override_editable_flag: bool

    """
    body = Worklog.from_dict(body)
    return web.Response(status=200)
