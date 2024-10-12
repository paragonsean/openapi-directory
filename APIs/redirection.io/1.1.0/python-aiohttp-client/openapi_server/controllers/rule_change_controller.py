from typing import List, Dict
from aiohttp import web

from openapi_server.models.rule_change_read import RuleChangeRead
from openapi_server.models.rule_change_write import RuleChangeWrite
from openapi_server import util


async def delete_rule_change_item(request: web.Request, id) -> web.Response:
    """Removes the RuleChange resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_rule_change_collection(request: web.Request, version_id, page=None) -> web.Response:
    """Retrieves the collection of RuleChange resources.

    

    :param version_id: 
    :type version_id: str
    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_rule_change_item(request: web.Request, id) -> web.Response:
    """Retrieves a RuleChange resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_rule_change_collection(request: web.Request, rule_change=None) -> web.Response:
    """Creates a RuleChange resource.

    

    :param rule_change: The new RuleChange resource
    :type rule_change: dict | bytes

    """
    rule_change = RuleChangeWrite.from_dict(rule_change)
    return web.Response(status=200)
