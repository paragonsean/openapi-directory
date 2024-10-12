from typing import List, Dict
from aiohttp import web

from openapi_server.models.image_provider_info import ImageProviderInfo
from openapi_server.models.image_type import ImageType
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.remote_image_result import RemoteImageResult
from openapi_server import util


async def download_remote_image(request: web.Request, item_id, type, image_url=None) -> web.Response:
    """Downloads a remote image for an item.

    

    :param item_id: Item Id.
    :type item_id: str
    :type item_id: str
    :param type: The image type.
    :type type: dict | bytes
    :param image_url: The image url.
    :type image_url: str

    """
    type = .from_dict(type)
    return web.Response(status=200)


async def get_remote_image(request: web.Request, image_url) -> web.Response:
    """Gets a remote image.

    

    :param image_url: The image url.
    :type image_url: str

    """
    return web.Response(status=200)


async def get_remote_image_providers(request: web.Request, item_id) -> web.Response:
    """Gets available remote image providers for an item.

    

    :param item_id: Item Id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_remote_images(request: web.Request, item_id, type=None, start_index=None, limit=None, provider_name=None, include_all_languages=None) -> web.Response:
    """Gets available remote images for an item.

    

    :param item_id: Item Id.
    :type item_id: str
    :type item_id: str
    :param type: The image type.
    :type type: dict | bytes
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param provider_name: Optional. The image provider to use.
    :type provider_name: str
    :param include_all_languages: Optional. Include all languages.
    :type include_all_languages: bool

    """
    type = .from_dict(type)
    return web.Response(status=200)
