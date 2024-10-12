from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_flush_aggregate_request import AgentFlushAggregateRequest
from openapi_server import util


async def post_agent_flush_aggregate_request_collection(request: web.Request, agent_flush_aggregate_request=None) -> web.Response:
    """Creates a AgentFlushAggregateRequest resource.

    

    :param agent_flush_aggregate_request: The new AgentFlushAggregateRequest resource
    :type agent_flush_aggregate_request: dict | bytes

    """
    agent_flush_aggregate_request = AgentFlushAggregateRequest.from_dict(agent_flush_aggregate_request)
    return web.Response(status=200)
