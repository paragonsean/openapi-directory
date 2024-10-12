from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.metadata_editor_info import MetadataEditorInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_metadata_editor_info(request: web.Request, item_id) -> web.Response:
    """Gets metadata editor info for an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def update_item(request: web.Request, item_id, body) -> web.Response:
    """Updates an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param body: The new item properties.
    :type body: dict | bytes

    """
    body = BaseItemDto.from_dict(body)
    return web.Response(status=200)


async def update_item_content_type(request: web.Request, item_id, content_type=None) -> web.Response:
    """Updates an item&#39;s content type.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param content_type: The content type of the item.
    :type content_type: str

    """
    return web.Response(status=200)
