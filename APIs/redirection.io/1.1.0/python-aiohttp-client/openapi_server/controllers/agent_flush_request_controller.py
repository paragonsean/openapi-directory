from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_flush_request import AgentFlushRequest
from openapi_server import util


async def agent_flush_requests_post(request: web.Request, agent_flush_request=None) -> web.Response:
    """Creates a AgentFlushRequest resource.

    

    :param agent_flush_request: The new AgentFlushRequest resource
    :type agent_flush_request: dict | bytes

    """
    agent_flush_request = AgentFlushRequest.from_dict(agent_flush_request)
    return web.Response(status=200)


async def post_logs_post(request: web.Request, agent_flush_request=None) -> web.Response:
    """Creates a AgentFlushRequest resource.

    

    :param agent_flush_request: The new AgentFlushRequest resource
    :type agent_flush_request: dict | bytes

    """
    agent_flush_request = AgentFlushRequest.from_dict(agent_flush_request)
    return web.Response(status=200)
