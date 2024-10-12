from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_block_hash_v2200_response import GetBlockHashV2200Response
from openapi_server.models.get_block_v2200_response import GetBlockV2200Response
from openapi_server.models.get_raw_block_v2200_response import GetRawBlockV2200Response
from openapi_server import util


async def get_block_hash_v2(request: web.Request, blockchain, block_height) -> web.Response:
    """Get block hash V2

    Get block hash by its height  Note: Blockbook always follows the main chain of the backend it is attached to.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param block_height: Block height/index
    :type block_height: int

    """
    return web.Response(status=200)


async def get_block_v2(request: web.Request, blockchain, block_hash_or_height, page=None, page_size=None) -> web.Response:
    """Get Block V2

    Returns information about block with transactions, subject to paging.  Note: Blockbook always follows the main chain of the backend it is attached to. If there is a rollback-reorg in the backend, Blockbook will also do rollback. When you ask for block by height, you will always get the main chain block. If you ask for block by hash, you may get the block from another fork but it is not guaranteed (backend may not keep it)

    :param blockchain: Blockchain name
    :type blockchain: str
    :param block_hash_or_height: Block hash or height
    :type block_hash_or_height: str
    :param page: specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
    :type page: int
    :param page_size: number of transactions returned by call (default and maximum 1000)
    :type page_size: int

    """
    return web.Response(status=200)


async def get_raw_block_v2(request: web.Request, blockchain, block_hash_or_height) -> web.Response:
    """Get raw block data V2

    Returns the raw hex-encoded block data for a given block hash or height

    :param blockchain: Blockchain name
    :type blockchain: str
    :param block_hash_or_height: Block hash or height
    :type block_hash_or_height: str

    """
    return web.Response(status=200)
