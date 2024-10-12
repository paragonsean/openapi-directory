from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.property_keys import PropertyKeys
from openapi_server import util


async def delete_issue_type_property(request: web.Request, issue_type_id, property_key) -> web.Response:
    """Delete issue type property

    Deletes the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_id: The ID of the issue type.
    :type issue_type_id: str
    :param property_key: The key of the property. Use [Get issue type property keys](#api-rest-api-3-issuetype-issueTypeId-properties-get) to get a list of all issue type property keys.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_issue_type_property(request: web.Request, issue_type_id, property_key) -> web.Response:
    """Get issue type property

    Returns the key and value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the details of any issue type.  *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the details of any issue types associated with the projects the user has permission to browse.

    :param issue_type_id: The ID of the issue type.
    :type issue_type_id: str
    :param property_key: The key of the property. Use [Get issue type property keys](#api-rest-api-3-issuetype-issueTypeId-properties-get) to get a list of all issue type property keys.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_issue_type_property_keys(request: web.Request, issue_type_id) -> web.Response:
    """Get issue type property keys

    Returns all the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys of the issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the property keys of any issue type.  *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the property keys of any issue types associated with the projects the user has permission to browse.

    :param issue_type_id: The ID of the issue type.
    :type issue_type_id: str

    """
    return web.Response(status=200)


async def set_issue_type_property(request: web.Request, issue_type_id, property_key, body) -> web.Response:
    """Set issue type property

    Creates or updates the value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). Use this resource to store and update data against an issue type.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_type_id: The ID of the issue type.
    :type issue_type_id: str
    :param property_key: The key of the issue type property. The maximum length is 255 characters.
    :type property_key: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
