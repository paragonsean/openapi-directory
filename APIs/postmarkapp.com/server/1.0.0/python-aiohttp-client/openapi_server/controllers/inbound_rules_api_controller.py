from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_inbound_rule200_response import CreateInboundRule200Response
from openapi_server.models.create_inbound_rule_request import CreateInboundRuleRequest
from openapi_server.models.list_inbound_rules200_response import ListInboundRules200Response
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def create_inbound_rule(request: web.Request, x_postmark_server_token, body=None) -> web.Response:
    """Create an inbound rule trigger

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateInboundRuleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_inbound_rule(request: web.Request, x_postmark_server_token, triggerid) -> web.Response:
    """Delete a single trigger

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param triggerid: The ID of the Inbound Rule that should be deleted.
    :type triggerid: int

    """
    return web.Response(status=200)


async def list_inbound_rules(request: web.Request, x_postmark_server_token, count, offset) -> web.Response:
    """List inbound rule triggers

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param count: Number of records to return per request.
    :type count: int
    :param offset: Number of records to skip.
    :type offset: int

    """
    return web.Response(status=200)
