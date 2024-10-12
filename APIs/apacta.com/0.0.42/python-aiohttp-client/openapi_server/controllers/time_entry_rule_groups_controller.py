from typing import List, Dict
from aiohttp import web

from openapi_server.models.time_entry_rule_groups_get200_response import TimeEntryRuleGroupsGet200Response
from openapi_server import util


async def time_entry_rule_groups_get(request: web.Request, q=None) -> web.Response:
    """List time entry rule groups

    

    :param q: 
    :type q: str

    """
    return web.Response(status=200)
