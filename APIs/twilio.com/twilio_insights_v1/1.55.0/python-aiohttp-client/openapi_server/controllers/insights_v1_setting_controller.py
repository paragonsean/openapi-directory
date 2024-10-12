from typing import List, Dict
from aiohttp import web

from openapi_server.models.insights_v1_account_settings import InsightsV1AccountSettings
from openapi_server import util


async def fetch_account_settings(request: web.Request, subaccount_sid=None) -> web.Response:
    """fetch_account_settings

    Get the Voice Insights Settings.

    :param subaccount_sid: The unique SID identifier of the Subaccount.
    :type subaccount_sid: str

    """
    return web.Response(status=200)


async def update_account_settings(request: web.Request, advanced_features=None, subaccount_sid=None, voice_trace=None) -> web.Response:
    """update_account_settings

    Update a specific Voice Insights Setting.

    :param advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
    :type advanced_features: bool
    :param subaccount_sid: The unique SID identifier of the Subaccount.
    :type subaccount_sid: str
    :param voice_trace: A boolean flag to enable Voice Trace.
    :type voice_trace: bool

    """
    return web.Response(status=200)
