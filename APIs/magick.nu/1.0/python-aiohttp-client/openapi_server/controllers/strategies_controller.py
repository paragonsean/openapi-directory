from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_strategies_strategy_id_strategy_id(request: web.Request, strategy_id) -> web.Response:
    """Get Strategy by ID

    

    :param strategy_id: 
    :type strategy_id: str

    """
    return web.Response(status=200)


async def get_strategies_templates(request: web.Request, ) -> web.Response:
    """Get all Template Strategies

    


    """
    return web.Response(status=200)
