from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.execute_request import ExecuteRequest
from openapi_server.models.execute_response import ExecuteResponse
from openapi_server.models.exposed_action_response_schema import ExposedActionResponseSchema
from openapi_server import util


async def check(request: web.Request, ) -> web.Response:
    """Check

    Test that the API and auth are working.


    """
    return web.Response(status=200)


async def execute_app_action_endpoint(request: web.Request, exposed_app_action_id, body) -> web.Response:
    """Execute App Action Endpoint

    Give us a plain english description of exact action you want to do. There should be dynamically generated documentation for this endpoint for each action that is exposed.

    :param exposed_app_action_id: 
    :type exposed_app_action_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExecuteRequest.from_dict(body)
    return web.Response(status=200)


async def get_configuration_link(request: web.Request, ) -> web.Response:
    """Get Configuration Link

    Provides a link to configure more actions. Alternatively, searching through apps and actions will provide more specific configuration links.


    """
    return web.Response(status=200)


async def get_execution_log_endpoint(request: web.Request, execution_log_id) -> web.Response:
    """Get Execution Log Endpoint

    Get the execution log for a given execution log id.

    :param execution_log_id: 
    :type execution_log_id: str

    """
    return web.Response(status=200)


async def list_exposed_actions(request: web.Request, ) -> web.Response:
    """List Exposed Actions

    List all the currently exposed actions for the given account.


    """
    return web.Response(status=200)
