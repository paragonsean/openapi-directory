from typing import List, Dict
from aiohttp import web

from openapi_server.models.rule_read import RuleRead
from openapi_server import util


async def agent_legacy_complex_rule_collection(request: web.Request, project_id) -> web.Response:
    """Retrieves the collection of Rule resources.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def agent_legacy_straight_rule_collection(request: web.Request, project_id) -> web.Response:
    """Retrieves the collection of Rule resources.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def agent_rule_collection(request: web.Request, project_id) -> web.Response:
    """Retrieves the collection of Rule resources.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def export_rule_collection(request: web.Request, project_id, sort_id=None, sort_view_count=None) -> web.Response:
    """Retrieves the collection of Rule resources.

    

    :param project_id: 
    :type project_id: str
    :param sort_id: 
    :type sort_id: str
    :param sort_view_count: 
    :type sort_view_count: str

    """
    return web.Response(status=200)


async def get_rule_collection(request: web.Request, project_id, sort_id=None, sort_view_count=None, page=None) -> web.Response:
    """Retrieves the collection of Rule resources.

    

    :param project_id: 
    :type project_id: str
    :param sort_id: 
    :type sort_id: str
    :param sort_view_count: 
    :type sort_view_count: str
    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_rule_item(request: web.Request, id) -> web.Response:
    """Retrieves a Rule resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
