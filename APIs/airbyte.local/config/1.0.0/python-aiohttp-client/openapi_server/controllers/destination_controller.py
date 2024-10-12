from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_connection_read import CheckConnectionRead
from openapi_server.models.destination_clone_request_body import DestinationCloneRequestBody
from openapi_server.models.destination_create import DestinationCreate
from openapi_server.models.destination_id_request_body import DestinationIdRequestBody
from openapi_server.models.destination_read import DestinationRead
from openapi_server.models.destination_read_list import DestinationReadList
from openapi_server.models.destination_search import DestinationSearch
from openapi_server.models.destination_update import DestinationUpdate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_server import util


async def check_connection_to_destination(request: web.Request, body) -> web.Response:
    """Check connection to the destination

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def check_connection_to_destination_for_update(request: web.Request, body) -> web.Response:
    """Check connection for a proposed update to a destination

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationUpdate.from_dict(body)
    return web.Response(status=200)


async def clone_destination(request: web.Request, body) -> web.Response:
    """Clone destination

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationCloneRequestBody.from_dict(body)
    return web.Response(status=200)


async def create_destination(request: web.Request, body) -> web.Response:
    """Create a destination

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationCreate.from_dict(body)
    return web.Response(status=200)


async def delete_destination(request: web.Request, body) -> web.Response:
    """Delete the destination

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_destination(request: web.Request, body) -> web.Response:
    """Get configured destination

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def list_destinations_for_workspace(request: web.Request, body) -> web.Response:
    """List configured destinations for a workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def search_destinations(request: web.Request, body) -> web.Response:
    """Search destinations

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationSearch.from_dict(body)
    return web.Response(status=200)


async def update_destination(request: web.Request, body) -> web.Response:
    """Update a destination

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationUpdate.from_dict(body)
    return web.Response(status=200)
