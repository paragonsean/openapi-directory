from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_traffic_shaping_dscp_tagging_options_2(request: web.Request, network_id) -> web.Response:
    """Returns the available DSCP tagging options for your traffic shaping rules.

    Returns the available DSCP tagging options for your traffic shaping rules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
