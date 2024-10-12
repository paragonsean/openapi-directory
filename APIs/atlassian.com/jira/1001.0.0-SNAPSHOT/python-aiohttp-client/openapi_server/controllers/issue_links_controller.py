from typing import List, Dict
from aiohttp import web

from openapi_server.models.issue_link import IssueLink
from openapi_server.models.link_issue_request_json_bean import LinkIssueRequestJsonBean
from openapi_server import util


async def delete_issue_link(request: web.Request, link_id) -> web.Response:
    """Delete issue link

    Deletes an issue link.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  Browse project [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues in the link.  *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one of the projects containing issues in the link.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.

    :param link_id: The ID of the issue link.
    :type link_id: str

    """
    return web.Response(status=200)


async def get_issue_link(request: web.Request, link_id) -> web.Response:
    """Get issue link

    Returns an issue link.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the linked issues.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.

    :param link_id: The ID of the issue link.
    :type link_id: str

    """
    return web.Response(status=200)


async def link_issues(request: web.Request, body) -> web.Response:
    """Create issue link

    Creates a link between two issues. Use this operation to indicate a relationship between two issues and optionally add a comment to the from (outward) issue. To use this resource the site must have [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled.  This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link, use &#x60;https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields&#x3D;issuelinks&#x60;.  If the link request duplicates a link, the response indicates that the issue link was created. If the request included a comment, the comment is added.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues to be linked,  *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) on the project containing the from (outward) issue,  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param body: The issue link request.
    :type body: dict | bytes

    """
    body = LinkIssueRequestJsonBean.from_dict(body)
    return web.Response(status=200)
