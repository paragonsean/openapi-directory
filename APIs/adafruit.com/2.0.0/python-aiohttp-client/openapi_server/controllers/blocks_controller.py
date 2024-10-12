from typing import List, Dict
from aiohttp import web

from openapi_server.models.block import Block
from openapi_server.models.create_block_request import CreateBlockRequest
from openapi_server import util


async def all_blocks(request: web.Request, username, dashboard_id) -> web.Response:
    """All blocks for current user

    The Blocks endpoint returns information about the user&#39;s blocks. 

    :param username: a valid username string
    :type username: str
    :param dashboard_id: 
    :type dashboard_id: str

    """
    return web.Response(status=200)


async def create_block(request: web.Request, username, dashboard_id, block) -> web.Response:
    """Create a new Block

    

    :param username: a valid username string
    :type username: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param block: 
    :type block: dict | bytes

    """
    block = CreateBlockRequest.from_dict(block)
    return web.Response(status=200)


async def destroy_block(request: web.Request, username, dashboard_id, id) -> web.Response:
    """Delete an existing Block

    

    :param username: a valid username string
    :type username: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_block(request: web.Request, username, dashboard_id, id) -> web.Response:
    """Returns Block based on ID

    

    :param username: a valid username string
    :type username: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def replace_block(request: web.Request, username, dashboard_id, id, block) -> web.Response:
    """Replace an existing Block

    

    :param username: a valid username string
    :type username: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param id: 
    :type id: str
    :param block: 
    :type block: dict | bytes

    """
    block = CreateBlockRequest.from_dict(block)
    return web.Response(status=200)


async def update_block(request: web.Request, username, dashboard_id, id, block) -> web.Response:
    """Update properties of an existing Block

    

    :param username: a valid username string
    :type username: str
    :param dashboard_id: 
    :type dashboard_id: str
    :param id: 
    :type id: str
    :param block: 
    :type block: dict | bytes

    """
    block = CreateBlockRequest.from_dict(block)
    return web.Response(status=200)
