from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_owner_parameters import AddOwnerParameters
from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.graph_error import GraphError
from openapi_server import util


async def applications_add_owner(request: web.Request, application_object_id, api_version, tenant_id, body) -> web.Response:
    """applications_add_owner

    Add an owner to an application.

    :param application_object_id: The object ID of the application to which to add the owner.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: The URL of the owner object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
    :type body: dict | bytes

    """
    body = AddOwnerParameters.from_dict(body)
    return web.Response(status=200)


async def applications_list_owners(request: web.Request, application_object_id, api_version, tenant_id) -> web.Response:
    """Directory objects that are owners of the application.

    The owners are a set of non-admin users who are allowed to modify this object.

    :param application_object_id: The object ID of the application for which to get owners.
    :type application_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def applications_remove_owner(request: web.Request, application_object_id, owner_object_id, api_version, tenant_id) -> web.Response:
    """applications_remove_owner

    Remove a member from owners.

    :param application_object_id: The object ID of the application from which to remove the owner.
    :type application_object_id: str
    :param owner_object_id: Owner object id
    :type owner_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
