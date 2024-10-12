from typing import List, Dict
from aiohttp import web

from openapi_server.models.metadata_refresh_mode import MetadataRefreshMode
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def post(request: web.Request, item_id, metadata_refresh_mode=None, image_refresh_mode=None, replace_all_metadata=None, replace_all_images=None) -> web.Response:
    """Refreshes metadata for an item.

    

    :param item_id: Item id.
    :type item_id: str
    :type item_id: str
    :param metadata_refresh_mode: (Optional) Specifies the metadata refresh mode.
    :type metadata_refresh_mode: dict | bytes
    :param image_refresh_mode: (Optional) Specifies the image refresh mode.
    :type image_refresh_mode: dict | bytes
    :param replace_all_metadata: (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.
    :type replace_all_metadata: bool
    :param replace_all_images: (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.
    :type replace_all_images: bool

    """
    metadata_refresh_mode = .from_dict(metadata_refresh_mode)
    image_refresh_mode = .from_dict(image_refresh_mode)
    return web.Response(status=200)
