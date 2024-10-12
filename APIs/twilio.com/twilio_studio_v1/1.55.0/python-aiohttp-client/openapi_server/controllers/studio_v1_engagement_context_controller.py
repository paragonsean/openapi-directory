from typing import List, Dict
from aiohttp import web

from openapi_server.models.studio_v1_flow_engagement_engagement_context import StudioV1FlowEngagementEngagementContext
from openapi_server import util


async def fetch_engagement_context(request: web.Request, flow_sid, engagement_sid) -> web.Response:
    """fetch_engagement_context

    Retrieve the most recent context for an Engagement.

    :param flow_sid: The SID of the Flow.
    :type flow_sid: str
    :param engagement_sid: The SID of the Engagement.
    :type engagement_sid: str

    """
    return web.Response(status=200)
