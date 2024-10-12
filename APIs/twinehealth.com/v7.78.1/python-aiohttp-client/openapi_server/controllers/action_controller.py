from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_action_request import CreateActionRequest
from openapi_server.models.create_action_response import CreateActionResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_action_response import FetchActionResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.update_action_request import UpdateActionRequest
from openapi_server.models.update_action_response import UpdateActionResponse
from openapi_server import util


async def create_action(request: web.Request, body) -> web.Response:
    """Create action

    Create a plan action

    :param body: 
    :type body: dict | bytes

    """
    body = CreateActionRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_action(request: web.Request, id) -> web.Response:
    """Get an action

    Get a health action from a patient&#39;s plan.

    :param id: Action identifier
    :type id: str

    """
    return web.Response(status=200)


async def update_action(request: web.Request, id, body) -> web.Response:
    """Update an action

    Update a health action from a patient&#39;s plan.

    :param id: Action identifier
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateActionRequest.from_dict(body)
    return web.Response(status=200)
