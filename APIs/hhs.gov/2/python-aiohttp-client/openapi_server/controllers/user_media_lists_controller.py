from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server import util


async def resources_user_media_lists_id_json_get(request: web.Request, id, display_method=None) -> web.Response:
    """Get UserMediaList by ID

    Get a specific user media list.

    :param id: The id of the record to look up
    :type id: int
    :param display_method: Method used to render an html request. Accepts one: [mv, list, feed]
    :type display_method: str

    """
    return web.Response(status=200)
