from typing import List, Dict
from aiohttp import web

from openapi_server.models.cms_data_page_interface import CmsDataPageInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def cms_page_repository_v1_delete_by_id_delete(request: web.Request, page_id) -> web.Response:
    """cmsPage/{pageId}

    Delete page by ID.

    :param page_id: 
    :type page_id: int

    """
    return web.Response(status=200)


async def cms_page_repository_v1_get_by_id_get(request: web.Request, page_id) -> web.Response:
    """cmsPage/{pageId}

    Retrieve page.

    :param page_id: 
    :type page_id: int

    """
    return web.Response(status=200)
