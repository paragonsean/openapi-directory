from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server import util


async def get_suggestions(request: web.Request, user_id, media_type=None, type=None, start_index=None, limit=None, enable_total_record_count=None) -> web.Response:
    """Gets suggestions.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param media_type: The media types.
    :type media_type: List[str]
    :param type: The type.
    :type type: List[str]
    :param start_index: Optional. The start index.
    :type start_index: int
    :param limit: Optional. The limit.
    :type limit: int
    :param enable_total_record_count: Whether to enable the total record count.
    :type enable_total_record_count: bool

    """
    return web.Response(status=200)
