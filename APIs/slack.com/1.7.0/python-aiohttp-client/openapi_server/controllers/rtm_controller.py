from typing import List, Dict
from aiohttp import web

from openapi_server.models.rtm_connect_error_schema import RtmConnectErrorSchema
from openapi_server.models.rtm_connect_schema import RtmConnectSchema
from openapi_server import util


async def rtm_connect(request: web.Request, token, batch_presence_aware=None, presence_sub=None) -> web.Response:
    """rtm_connect

    Starts a Real Time Messaging session.

    :param token: Authentication token. Requires scope: &#x60;rtm:stream&#x60;
    :type token: str
    :param batch_presence_aware: Batch presence deliveries via subscription. Enabling changes the shape of &#x60;presence_change&#x60; events. See [batch presence](/docs/presence-and-status#batching).
    :type batch_presence_aware: bool
    :param presence_sub: Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).
    :type presence_sub: bool

    """
    return web.Response(status=200)
