from typing import List, Dict
from aiohttp import web

from openapi_server.models.done import Done
from openapi_server.models.group import Group
from openapi_server.models.outage import Outage
from openapi_server.models.snow_monkey_config import SnowMonkeyConfig
from openapi_server import util


async def get_snow_monkey_config(request: web.Request, ) -> web.Response:
    """Get current Snow Monkey config

    Get current Snow Monkey config


    """
    return web.Response(status=200)


async def get_snow_monkey_outages(request: web.Request, ) -> web.Response:
    """Get all current Snow Monkey ourages

    Get all current Snow Monkey ourages


    """
    return web.Response(status=200)


async def patch_snow_monkey(request: web.Request, body=None) -> web.Response:
    """Update current Snow Monkey config

    Update current Snow Monkey config

    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def reset_snow_monkey(request: web.Request, ) -> web.Response:
    """Reset Snow Monkey Outages for the day

    Reset Snow Monkey Outages for the day


    """
    return web.Response(status=200)


async def start_snow_monkey(request: web.Request, ) -> web.Response:
    """Start the Snow Monkey

    Start the Snow Monkey


    """
    return web.Response(status=200)


async def stop_snow_monkey(request: web.Request, ) -> web.Response:
    """Stop the Snow Monkey

    Stop the Snow Monkey


    """
    return web.Response(status=200)


async def update_snow_monkey(request: web.Request, body=None) -> web.Response:
    """Update current Snow Monkey config

    Update current Snow Monkey config

    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)
