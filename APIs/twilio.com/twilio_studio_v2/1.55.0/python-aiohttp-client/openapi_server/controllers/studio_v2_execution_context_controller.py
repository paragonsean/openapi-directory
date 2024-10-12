from typing import List, Dict
from aiohttp import web

from openapi_server.models.studio_v2_flow_execution_execution_context import StudioV2FlowExecutionExecutionContext
from openapi_server import util


async def fetch_execution_context(request: web.Request, flow_sid, execution_sid) -> web.Response:
    """fetch_execution_context

    Retrieve the most recent context for an Execution.

    :param flow_sid: The SID of the Flow with the Execution context to fetch.
    :type flow_sid: str
    :param execution_sid: The SID of the Execution context to fetch.
    :type execution_sid: str

    """
    return web.Response(status=200)
