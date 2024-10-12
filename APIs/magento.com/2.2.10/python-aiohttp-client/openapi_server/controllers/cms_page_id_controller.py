from typing import List, Dict
from aiohttp import web

from openapi_server.models.cms_data_page_interface import CmsDataPageInterface
from openapi_server.models.cms_page_repository_v1_save_post_request import CmsPageRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def cms_page_repository_v1_save_put(request: web.Request, id, body=None) -> web.Response:
    """cmsPage/{id}

    Save page.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CmsPageRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
