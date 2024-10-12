from typing import List, Dict
from aiohttp import web

from openapi_server.models.cms_data_block_interface import CmsDataBlockInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def cms_block_repository_v1_delete_by_id_delete(request: web.Request, block_id) -> web.Response:
    """cmsBlock/{blockId}

    Delete block by ID.

    :param block_id: 
    :type block_id: int

    """
    return web.Response(status=200)


async def cms_block_repository_v1_get_by_id_get(request: web.Request, block_id) -> web.Response:
    """cmsBlock/{blockId}

    Retrieve block.

    :param block_id: 
    :type block_id: int

    """
    return web.Response(status=200)
