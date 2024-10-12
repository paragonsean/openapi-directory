from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server.models.associations_list import AssociationsList
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def associations_create_or_update(request: web.Request, scope, association_name, api_version, association) -> web.Response:
    """associations_create_or_update

    Create or update an association.

    :param scope: The scope of the association. The scope can be any valid REST resource instance. For example, use &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}&#39; for a virtual machine resource.
    :type scope: str
    :param association_name: The name of the association.
    :type association_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param association: The parameters required to create or update an association.
    :type association: dict | bytes

    """
    association = Association.from_dict(association)
    return web.Response(status=200)


async def associations_delete(request: web.Request, scope, association_name, api_version) -> web.Response:
    """associations_delete

    Delete an association.

    :param scope: The scope of the association.
    :type scope: str
    :param association_name: The name of the association.
    :type association_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def associations_get(request: web.Request, scope, association_name, api_version) -> web.Response:
    """associations_get

    Get an association.

    :param scope: The scope of the association.
    :type scope: str
    :param association_name: The name of the association.
    :type association_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def associations_list_all(request: web.Request, scope, api_version) -> web.Response:
    """associations_list_all

    Gets all association for the given scope.

    :param scope: The scope of the association.
    :type scope: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)
