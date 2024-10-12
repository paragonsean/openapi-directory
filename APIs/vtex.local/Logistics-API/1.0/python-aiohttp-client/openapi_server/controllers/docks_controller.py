from typing import List, Dict
from aiohttp import web

from openapi_server.models.all_docks200_response_inner import AllDocks200ResponseInner
from openapi_server.models.create_update_dock_request import CreateUpdateDockRequest
from openapi_server.models.dock_by_id200_response import DockById200Response
from openapi_server import util


async def activate_dock(request: web.Request, content_type, accept, dock_id) -> web.Response:
    """Activate dock

    Activates dock through dock ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param dock_id: 
    :type dock_id: str

    """
    return web.Response(status=200)


async def all_docks(request: web.Request, content_type, accept) -> web.Response:
    """List all  docks

    Informs a list of all docks.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def create_update_dock(request: web.Request, content_type, accept, body) -> web.Response:
    """Create/update dock

    Creates or updates docks to be used in your logistic operation.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateUpdateDockRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_dock(request: web.Request, content_type, accept, dock_id) -> web.Response:
    """Deactivate dock

    Deactivate dock by dock ID

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param dock_id: 
    :type dock_id: str

    """
    return web.Response(status=200)


async def dock(request: web.Request, content_type, accept, dock_id) -> web.Response:
    """Delete dock

    Deletes dock by dock ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param dock_id: 
    :type dock_id: str

    """
    return web.Response(status=200)


async def dock_by_id(request: web.Request, content_type, accept, dock_id) -> web.Response:
    """List dock by ID

    Informs a given dock&#39;s information, searching by dock ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param dock_id: 
    :type dock_id: str

    """
    return web.Response(status=200)
