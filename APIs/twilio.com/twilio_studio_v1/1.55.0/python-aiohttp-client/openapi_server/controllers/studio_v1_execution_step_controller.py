from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_execution_step_response import ListExecutionStepResponse
from openapi_server.models.studio_v1_flow_execution_execution_step import StudioV1FlowExecutionExecutionStep
from openapi_server import util


async def fetch_execution_step(request: web.Request, flow_sid, execution_sid, sid) -> web.Response:
    """fetch_execution_step

    Retrieve a Step.

    :param flow_sid: The SID of the Flow with the Step to fetch.
    :type flow_sid: str
    :param execution_sid: The SID of the Execution resource with the Step to fetch.
    :type execution_sid: str
    :param sid: The SID of the ExecutionStep resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_execution_step(request: web.Request, flow_sid, execution_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_execution_step

    Retrieve a list of all Steps for an Execution.

    :param flow_sid: The SID of the Flow with the Steps to read.
    :type flow_sid: str
    :param execution_sid: The SID of the Execution with the Steps to read.
    :type execution_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
