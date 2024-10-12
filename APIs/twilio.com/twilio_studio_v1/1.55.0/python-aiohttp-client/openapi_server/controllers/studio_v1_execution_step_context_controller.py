from typing import List, Dict
from aiohttp import web

from openapi_server.models.studio_v1_flow_execution_execution_step_execution_step_context import StudioV1FlowExecutionExecutionStepExecutionStepContext
from openapi_server import util


async def fetch_execution_step_context(request: web.Request, flow_sid, execution_sid, step_sid) -> web.Response:
    """fetch_execution_step_context

    Retrieve the context for an Execution Step.

    :param flow_sid: The SID of the Flow with the Step to fetch.
    :type flow_sid: str
    :param execution_sid: The SID of the Execution resource with the Step to fetch.
    :type execution_sid: str
    :param step_sid: The SID of the Step to fetch.
    :type step_sid: str

    """
    return web.Response(status=200)
