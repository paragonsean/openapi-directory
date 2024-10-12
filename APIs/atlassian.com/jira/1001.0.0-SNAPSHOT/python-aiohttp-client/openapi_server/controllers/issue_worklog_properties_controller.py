from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.property_keys import PropertyKeys
from openapi_server import util


async def delete_worklog_property(request: web.Request, issue_id_or_key, worklog_id, property_key) -> web.Response:
    """Delete worklog property

    Deletes a worklog property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param worklog_id: The ID of the worklog.
    :type worklog_id: str
    :param property_key: The key of the property.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_worklog_property(request: web.Request, issue_id_or_key, worklog_id, property_key) -> web.Response:
    """Get worklog property

    Returns the value of a worklog property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param worklog_id: The ID of the worklog.
    :type worklog_id: str
    :param property_key: The key of the property.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_worklog_property_keys(request: web.Request, issue_id_or_key, worklog_id) -> web.Response:
    """Get worklog property keys

    Returns the keys of all properties for a worklog.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param worklog_id: The ID of the worklog.
    :type worklog_id: str

    """
    return web.Response(status=200)


async def set_worklog_property(request: web.Request, issue_id_or_key, worklog_id, property_key, body) -> web.Response:
    """Set worklog property

    Sets the value of a worklog property. Use this operation to store custom data against the worklog.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

    :param issue_id_or_key: The ID or key of the issue.
    :type issue_id_or_key: str
    :param worklog_id: The ID of the worklog.
    :type worklog_id: str
    :param property_key: The key of the issue property. The maximum length is 255 characters.
    :type property_key: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
