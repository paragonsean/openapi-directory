from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_insights_settings_answersets import FlexV1InsightsSettingsAnswersets
from openapi_server import util


async def fetch_insights_settings_answersets(request: web.Request, authorization=None) -> web.Response:
    """fetch_insights_settings_answersets

    To get the Answer Set Settings for an Account

    :param authorization: The Authorization HTTP request header
    :type authorization: str

    """
    return web.Response(status=200)
