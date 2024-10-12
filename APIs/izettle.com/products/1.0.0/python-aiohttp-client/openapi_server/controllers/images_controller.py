from typing import List, Dict
from aiohttp import web

from openapi_server.models.library_images_response import LibraryImagesResponse
from openapi_server import util


async def get_all_image_urls(request: web.Request, organization_uuid) -> web.Response:
    """Retrieve all library item images

    Retrieves all library items images used by the organization, sorted by updated date

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str

    """
    return web.Response(status=200)
