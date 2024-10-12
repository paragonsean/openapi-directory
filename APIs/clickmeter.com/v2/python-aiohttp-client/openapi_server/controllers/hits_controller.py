from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage
from openapi_server import util


async def hits_get_hits(request: web.Request, timeframe, limit=None, offset=None, from_day=None, to_day=None, filter=None) -> web.Response:
    """Retrieve the list of events related to this account.

    

    :param timeframe: Timeframe of the request. See list at $timeframeList
    :type timeframe: str
    :param limit: Limit results to this number
    :type limit: int
    :param offset: Offset where to start from (it&#39;s the lastKey field in the response object)
    :type offset: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param filter: Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;)
    :type filter: str

    """
    return web.Response(status=200)
