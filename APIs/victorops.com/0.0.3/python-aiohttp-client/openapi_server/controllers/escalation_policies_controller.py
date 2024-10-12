from typing import List, Dict
from aiohttp import web

from openapi_server.models.escalation_policy_info_list import EscalationPolicyInfoList
from openapi_server.models.escalation_policy_list import EscalationPolicyList
from openapi_server import util


async def api_public_v1_policies_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """Get escalation policy info

    Retrieves a list of escalation policy information. This API may be called a maximum of once a minute.

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_team_team_policies_get(request: web.Request, x_vo_api_id, x_vo_api_key, team) -> web.Response:
    """Retrieve a list of escalation policies for a team

    Get the escalation policies for the specified team.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to fetch
    :type team: str

    """
    return web.Response(status=200)
