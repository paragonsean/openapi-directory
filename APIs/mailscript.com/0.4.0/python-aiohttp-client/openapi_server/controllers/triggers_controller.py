from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_trigger_request import AddTriggerRequest
from openapi_server.models.add_trigger_response import AddTriggerResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_triggers_response import GetAllTriggersResponse
from openapi_server import util


async def add_trigger(request: web.Request, body) -> web.Response:
    """Setup a trigger

    

    :param body: Trigger body
    :type body: dict | bytes

    """
    body = AddTriggerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_trigger(request: web.Request, trigger) -> web.Response:
    """Delete a trigger

    

    :param trigger: ID of the trigger
    :type trigger: str

    """
    return web.Response(status=200)


async def get_all_triggers(request: web.Request, ) -> web.Response:
    """Get all triggers you have access to

    


    """
    return web.Response(status=200)


async def update_trigger(request: web.Request, trigger, body) -> web.Response:
    """Update a trigger

    

    :param trigger: ID of the trigger
    :type trigger: str
    :param body: Trigger body
    :type body: dict | bytes

    """
    body = AddTriggerRequest.from_dict(body)
    return web.Response(status=200)
