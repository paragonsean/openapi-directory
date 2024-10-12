from typing import List, Dict
from aiohttp import web

from openapi_server.models.rule_statistic import RuleStatistic
from openapi_server import util


async def get_rule_statistic_collection(request: web.Request, project_id) -> web.Response:
    """Retrieves the collection of RuleStatistic resources.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_rule_statistic_item(request: web.Request, id) -> web.Response:
    """Retrieves a RuleStatistic resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
