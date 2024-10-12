from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_user_roles import FlexV1InsightsUserRoles
from openapi_server import util


async def fetch_insights_user_roles(request: web.Request, authorization=None) -> web.Response:
    """fetch_insights_user_roles

    This is used by Flex UI and Quality Management to fetch the Flex Insights roles for the user

    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)
