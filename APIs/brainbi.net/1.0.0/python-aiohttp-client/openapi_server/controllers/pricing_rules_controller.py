from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def rule_data(request: web.Request, =None) -> web.Response:
    """Rule Data

    This resource lists all data that wa saved for pricing rules.

    :param : 
    :type : str

    """
    return web.Response(status=200)


async def rule_data_latest(request: web.Request, =None) -> web.Response:
    """Rule Data Latest

    This resource lists only the latest data point that wa saved for a pricing rule.

    :param : 
    :type : str

    """
    return web.Response(status=200)


async def rules(request: web.Request, =None) -> web.Response:
    """Rules

    This resource lists all pricing rules that are currently saved in you account.

    :param : 
    :type : str

    """
    return web.Response(status=200)
