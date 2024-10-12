from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_issue_is_watching import BulkIssueIsWatching
from openapi_server.models.issue_list import IssueList
from openapi_server.models.watchers import Watchers
from openapi_server import util


async def add_watcher(request: web.Request, issue_id_or_key, body) -> web.Response:
    """Add watcher

    Adds a user as a watcher of an issue by passing the account ID of the user. For example, &#x60;\&quot;5b10ac8d82e05b22cc7d4ef5\&quot;&#x60;. If no user is specified the calling user is added.  This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  To add users other than themselves to the watchlist, *Manage watcher list* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param body: The account ID of the user. Note that username cannot be used due to privacy changes.
    :type body: str

    """
    return web.Response(status=200)


async def get_is_watching_issue_bulk(request: web.Request, body) -> web.Response:
    """Get is watching issue bulk

    Returns, for the user, details of the watched status of issues from a list. If an issue ID is invalid, the returned watched status is &#x60;false&#x60;.  This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param body: A list of issue IDs.
    :type body: dict | bytes

    """
    body = IssueList.from_dict(body)
    return web.Response(status=200)


async def get_issue_watchers(request: web.Request, issue_id_or_key) -> web.Response:
    """Get issue watchers

    Returns the watchers for an issue.  This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  To see details of users on the watchlist other than themselves, *View voters and watchers* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def remove_watcher(request: web.Request, issue_id_or_key, username=None, account_id=None) -> web.Response:
    """Delete watcher

    Deletes a user as a watcher of an issue.  This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  To remove users other than themselves from the watchlist, *Manage watcher list* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param username: This parameter is no longer available. See the [deprecation notice](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details.
    :type username: str
    :param account_id: The account ID of the user, which uniquely identifies the user across all Atlassian products. For example, *5b10ac8d82e05b22cc7d4ef5*. Required.
    :type account_id: str

    """
    return web.Response(status=200)
