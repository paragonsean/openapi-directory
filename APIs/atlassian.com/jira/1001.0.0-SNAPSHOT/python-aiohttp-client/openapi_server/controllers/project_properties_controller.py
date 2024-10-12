from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.property_keys import PropertyKeys
from openapi_server import util


async def delete_project_property(request: web.Request, project_id_or_key, property_key) -> web.Response:
    """Delete project property

    Deletes the [property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) from a project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param property_key: The project property key. Use [Get project property keys](#api-rest-api-3-project-projectIdOrKey-properties-get) to get a list of all project property keys.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_project_property(request: web.Request, project_id_or_key, property_key) -> web.Response:
    """Get project property

    Returns the value of a [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param property_key: The project property key. Use [Get project property keys](#api-rest-api-3-project-projectIdOrKey-properties-get) to get a list of all project property keys.
    :type property_key: str

    """
    return web.Response(status=200)


async def get_project_property_keys(request: web.Request, project_id_or_key) -> web.Response:
    """Get project property keys

    Returns all [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys for the project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def set_project_property(request: web.Request, project_id_or_key, property_key, body) -> web.Response:
    """Set project property

    Sets the value of the [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). You can use project properties to store custom data against the project.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the property is created.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param property_key: The key of the project property. The maximum length is 255 characters.
    :type property_key: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
