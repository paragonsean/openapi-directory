from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_trigger_request import CreateTriggerRequest
from openapi_server.models.trigger import Trigger
from openapi_server import util


async def all_triggers(request: web.Request, username) -> web.Response:
    """All triggers for current user

    The Triggers endpoint returns information about the user&#39;s triggers. 

    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def create_trigger(request: web.Request, username, trigger) -> web.Response:
    """Create a new Trigger

    

    :param username: a valid username string
    :type username: str
    :param trigger: 
    :type trigger: dict | bytes

    """
    trigger = CreateTriggerRequest.from_dict(trigger)
    return web.Response(status=200)


async def destroy_trigger(request: web.Request, username, id) -> web.Response:
    """Delete an existing Trigger

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_trigger(request: web.Request, username, id) -> web.Response:
    """Returns Trigger based on ID

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def replace_trigger(request: web.Request, username, id, trigger) -> web.Response:
    """Replace an existing Trigger

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str
    :param trigger: 
    :type trigger: dict | bytes

    """
    trigger = CreateTriggerRequest.from_dict(trigger)
    return web.Response(status=200)


async def update_trigger(request: web.Request, username, id, trigger) -> web.Response:
    """Update properties of an existing Trigger

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str
    :param trigger: 
    :type trigger: dict | bytes

    """
    trigger = CreateTriggerRequest.from_dict(trigger)
    return web.Response(status=200)
