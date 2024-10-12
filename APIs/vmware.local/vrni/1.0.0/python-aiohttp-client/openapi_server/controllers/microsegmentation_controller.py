from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.recommended_rules import RecommendedRules
from openapi_server.models.recommended_rules_request import RecommendedRulesRequest
from openapi_server import util


async def export_nsx_recommended_rules(request: web.Request, body=None) -> web.Response:
    """Export recommended rules for NSX-V

    Export recommended firewall rules based on the flow data gathered by vRealize Network Insight in NSX-V compatible format

    :param body: NSX Recommended Rules Request
    :type body: dict | bytes

    """
    body = RecommendedRulesRequest.from_dict(body)
    return web.Response(status=200)


async def list_recommended_rules(request: web.Request, body=None) -> web.Response:
    """Get logical recommended rules

    Get recommended firewall rules based on the flow data gathered by vRealize Network Insight. This API provides service to retrieve recommended rules based on flow traffic that is observed between two groups OR for a single group based on all the inbound and outboud traffic for that group. In case two groups are provided, both the groups should be of same type. Currently supported groups are Application, Tier, NSXSecurityGroup, EC2SecurityGroup.

    :param body: Recommended Rules Request
    :type body: dict | bytes

    """
    body = RecommendedRulesRequest.from_dict(body)
    return web.Response(status=200)
