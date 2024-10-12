from typing import List, Dict
from aiohttp import web

from openapi_server.models.votes import Votes
from openapi_server import util


async def add_vote(request: web.Request, issue_id_or_key) -> web.Response:
    """Add vote

    Adds the user&#39;s vote to an issue. This is the equivalent of the user clicking *Vote* on an issue in Jira.  This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def get_votes(request: web.Request, issue_id_or_key) -> web.Response:
    """Get votes

    Returns details about the votes on an issue.  This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  Note that users with the necessary permissions for this operation but without the *View voters and watchers* project permissions are not returned details in the &#x60;voters&#x60; field.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)


async def remove_vote(request: web.Request, issue_id_or_key) -> web.Response:
    """Delete vote

    Deletes a user&#39;s vote from an issue. This is the equivalent of the user clicking *Unvote* on an issue in Jira.  This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str

    """
    return web.Response(status=200)
