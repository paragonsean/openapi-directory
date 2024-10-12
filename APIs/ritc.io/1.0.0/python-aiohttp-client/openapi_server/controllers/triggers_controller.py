from typing import List, Dict
from aiohttp import web

from openapi_server.models.trigger54 import Trigger54
from openapi_server.models.trigger_full_response import TriggerFullResponse
from openapi_server.models.trigger_short_response import TriggerShortResponse
from openapi_server import util


async def add_trigger(request: web.Request, trigger_object) -> web.Response:
    """add_trigger

    Create a new trigger in an app

    :param trigger_object: Trigger parameters and configuration
    :type trigger_object: dict | bytes

    """
    trigger_object = Trigger54.from_dict(trigger_object)
    return web.Response(status=200)


async def get_trigger(request: web.Request, trigger_id) -> web.Response:
    """get_trigger

    Get a trigger

    :param trigger_id: Id of Trigger
    :type trigger_id: str

    """
    return web.Response(status=200)


async def list_triggers(request: web.Request, ) -> web.Response:
    """list_triggers

    Triggers in an app


    """
    return web.Response(status=200)


async def remove_trigger(request: web.Request, trigger_id) -> web.Response:
    """remove_trigger

    Delete a trigger

    :param trigger_id: Id of Trigger
    :type trigger_id: str

    """
    return web.Response(status=200)


async def update_trigger(request: web.Request, trigger_id, trigger_object) -> web.Response:
    """update_trigger

    Update a trigger

    :param trigger_id: Id of user
    :type trigger_id: str
    :param trigger_object: Trigger information
    :type trigger_object: dict | bytes

    """
    trigger_object = Trigger54.from_dict(trigger_object)
    return web.Response(status=200)
