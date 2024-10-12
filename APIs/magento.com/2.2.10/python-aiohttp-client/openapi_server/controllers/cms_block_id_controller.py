from typing import List, Dict
from aiohttp import web

from openapi_server.models.cms_block_repository_v1_save_post_request import CmsBlockRepositoryV1SavePostRequest
from openapi_server.models.cms_data_block_interface import CmsDataBlockInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def cms_block_repository_v1_save_put(request: web.Request, id, body=None) -> web.Response:
    """cmsBlock/{id}

    Save block.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CmsBlockRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
