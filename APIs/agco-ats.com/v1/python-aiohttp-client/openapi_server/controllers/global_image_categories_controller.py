from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_global_image_category import APIIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_global_image_category import GlobalResourcesSharedModelsGlobalImageCategory
from openapi_server import util


async def global_image_categories_get_file(request: web.Request, id) -> web.Response:
    """Gets a file&#39;s metadata.

    No Documentation Found.

    :param id: The file&#39;s id.
    :type id: str

    """
    return web.Response(status=200)


async def global_image_categories_get_files(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get a paged response of file metadata.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def global_image_categories_post_file(request: web.Request, body) -> web.Response:
    """Create the metadata for a file before uploading. The State should be &#39;Created&#39;.

    No Documentation Found.

    :param body: The file&#39;s metadata.
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsGlobalImageCategory.from_dict(body)
    return web.Response(status=200)
