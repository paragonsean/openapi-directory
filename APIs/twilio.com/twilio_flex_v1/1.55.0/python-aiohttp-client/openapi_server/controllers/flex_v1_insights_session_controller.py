from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_session import FlexV1InsightsSession
from openapi_server import util


async def create_insights_session(request: web.Request, authorization=None) -> web.Response:
    """create_insights_session

    To obtain session details for fetching reports and dashboards

    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)
