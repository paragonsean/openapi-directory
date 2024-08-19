from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_send_events_response import GetSendEventsResponse
from openapi_server import util


async def v3_asset_management_assets_send_events_get(request: web.Request, accept_language=None, last_offset=None, event_count=None) -> web.Response:
    """v3_asset_management_assets_send_events_get

    

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param last_offset: Specifies a date/time (with timezone information) for continuing retrieval of events.  Events occuring _after_ the &#x60;last_offset&#x60; value provided will be returned.
    :type last_offset: str
    :param event_count: Specifies the number of events to return. Default is 50, maximum value is 100.
    :type event_count: int

    """
    last_offset = util.deserialize_datetime(last_offset)
    return web.Response(status=200)
