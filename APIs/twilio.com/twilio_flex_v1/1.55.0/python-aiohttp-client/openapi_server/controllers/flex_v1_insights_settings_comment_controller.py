from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_settings_comment import FlexV1InsightsSettingsComment
from openapi_server import util


async def fetch_insights_settings_comment(request: web.Request, authorization=None) -> web.Response:
    """fetch_insights_settings_comment

    To get the Comment Settings for an Account

    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)
