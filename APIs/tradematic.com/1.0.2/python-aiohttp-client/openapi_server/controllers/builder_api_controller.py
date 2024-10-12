from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.rule import Rule
from openapi_server import util


async def builder_rules_get(request: web.Request, ) -> web.Response:
    """Get strategy builder rules list

    Get strategy builder rules list


    """
    return web.Response(status=200)


async def builder_rules_ruleid_get(request: web.Request, ruleid) -> web.Response:
    """Get strategy builder rules by ID

    Get strategy builder rules by ID

    :param ruleid: 
    :type ruleid: int

    """
    return web.Response(status=200)
