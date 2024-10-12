from typing import List, Dict
from aiohttp import web

from openapi_server.models.studio_v1_flow_engagement_step_step_context import StudioV1FlowEngagementStepStepContext
from openapi_server import util


async def fetch_step_context(request: web.Request, flow_sid, engagement_sid, step_sid) -> web.Response:
    """fetch_step_context

    Retrieve the context for an Engagement Step.

    :param flow_sid: The SID of the Flow with the Step to fetch.
    :type flow_sid: str
    :param engagement_sid: The SID of the Engagement with the Step to fetch.
    :type engagement_sid: str
    :param step_sid: The SID of the Step to fetch
    :type step_sid: str

    """
    return web.Response(status=200)
