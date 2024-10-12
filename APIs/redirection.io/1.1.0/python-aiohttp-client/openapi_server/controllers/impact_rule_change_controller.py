from typing import List, Dict
from aiohttp import web

from openapi_server.models.impact_rule_change_read import ImpactRuleChangeRead
from openapi_server.models.impact_rule_change_write import ImpactRuleChangeWrite
from openapi_server import util


async def get_impact_rule_change_item(request: web.Request, id) -> web.Response:
    """Retrieves a ImpactRuleChange resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_impact_rule_change_collection(request: web.Request, impact_rule_change=None) -> web.Response:
    """Creates a ImpactRuleChange resource.

    

    :param impact_rule_change: The new ImpactRuleChange resource
    :type impact_rule_change: dict | bytes

    """
    impact_rule_change = ImpactRuleChangeWrite.from_dict(impact_rule_change)
    return web.Response(status=200)
