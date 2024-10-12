from typing import List, Dict
from aiohttp import web

from openapi_server.models.remote_issue_link import RemoteIssueLink
from openapi_server.models.remote_issue_link_identifies import RemoteIssueLinkIdentifies
from openapi_server.models.remote_issue_link_request import RemoteIssueLinkRequest
from openapi_server import util


async def create_or_update_remote_issue_link(request: web.Request, issue_id_or_key, body) -> web.Response:
    """Create or update remote issue link

    Creates or updates a remote issue link for an issue.  If a &#x60;globalId&#x60; is provided and a remote issue link with that global ID is found it is updated. Any fields without values in the request are set to null. Otherwise, the remote issue link is created.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoteIssueLinkRequest.from_dict(body)
    return web.Response(status=200)


async def delete_remote_issue_link_by_global_id(request: web.Request, issue_id_or_key, global_id) -> web.Response:
    """Delete remote issue link by global ID

    Deletes the remote issue link from the issue using the link&#39;s global ID. Where the global ID includes reserved URL characters these must be escaped in the request. For example, pass &#x60;system&#x3D;http://www.mycompany.com/support&amp;id&#x3D;1&#x60; as &#x60;system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1&#x60;.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is implemented, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param global_id: The global ID of a remote issue link.
    :type global_id: str

    """
    return web.Response(status=200)


async def delete_remote_issue_link_by_id(request: web.Request, issue_id_or_key, link_id) -> web.Response:
    """Delete remote issue link by ID

    Deletes a remote issue link from an issue.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects*, *Edit issues*, and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param link_id: The ID of a remote issue link.
    :type link_id: str

    """
    return web.Response(status=200)


async def get_remote_issue_link_by_id(request: web.Request, issue_id_or_key, link_id) -> web.Response:
    """Get remote issue link by ID

    Returns a remote issue link for an issue.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param link_id: The ID of the remote issue link.
    :type link_id: str

    """
    return web.Response(status=200)


async def get_remote_issue_links(request: web.Request, issue_id_or_key, global_id=None) -> web.Response:
    """Get remote issue links

    Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. For example, pass &#x60;system&#x3D;http://www.mycompany.com/support&amp;id&#x3D;1&#x60; as &#x60;system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1&#x60;.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param global_id: The global ID of the remote issue link.
    :type global_id: str

    """
    return web.Response(status=200)


async def update_remote_issue_link(request: web.Request, issue_id_or_key, link_id, body) -> web.Response:
    """Update remote issue link by ID

    Updates a remote issue link for an issue.  Note: Fields without values in the request are set to null.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* and *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param link_id: The ID of the remote issue link.
    :type link_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoteIssueLinkRequest.from_dict(body)
    return web.Response(status=200)
