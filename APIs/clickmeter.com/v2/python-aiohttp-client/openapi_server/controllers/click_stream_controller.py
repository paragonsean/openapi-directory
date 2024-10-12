from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_responses_entities_response_api_core_dto_click_stream_hit import ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit
from openapi_server import util


async def click_stream_get(request: web.Request, group=None, datapoint=None, conversion=None, page_size=None, filter=None) -> web.Response:
    """Retrieve the latest list of events of this account. Limited to last 100.

    

    :param group: Filter by this group id (mutually exclusive with \&quot;datapoint\&quot; and \&quot;conversion\&quot;)
    :type group: int
    :param datapoint: Filter by this datapoint id (mutually exclusive with \&quot;group\&quot; and \&quot;conversion\&quot;)
    :type datapoint: int
    :param conversion: Filter by this conversion id (mutually exclusive with \&quot;datapoint\&quot; and \&quot;group\&quot;)
    :type conversion: int
    :param page_size: Limit results to this number
    :type page_size: int
    :param filter: Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;)
    :type filter: str

    """
    return web.Response(status=200)
