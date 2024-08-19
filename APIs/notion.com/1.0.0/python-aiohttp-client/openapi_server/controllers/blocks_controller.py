from typing import List, Dict
from aiohttp import web

from openapi_server.models.append_block_children200_response import AppendBlockChildren200Response
from openapi_server.models.append_block_children_request import AppendBlockChildrenRequest
from openapi_server.models.delete_a_block200_response import DeleteABlock200Response
from openapi_server.models.retrieve_a_block200_response import RetrieveABlock200Response
from openapi_server.models.retrieve_block_children200_response import RetrieveBlockChildren200Response
from openapi_server.models.update_a_block_request import UpdateABlockRequest
from openapi_server import util


async def append_block_children(request: web.Request, id, notion_version=None, body=None) -> web.Response:
    """Append block children

    Append block children

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = AppendBlockChildrenRequest.from_dict(body)
    return web.Response(status=200)


async def delete_a_block(request: web.Request, id, notion_version=None) -> web.Response:
    """Delete a block

    Delete a block

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str

    """
    return web.Response(status=200)


async def retrieve_a_block(request: web.Request, id, notion_version=None) -> web.Response:
    """Retrieve a block

    Retrieve a block

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str

    """
    return web.Response(status=200)


async def retrieve_block_children(request: web.Request, id, page_size=None, notion_version=None) -> web.Response:
    """Retrieve block children

    Retrieve block children

    :param id: 
    :type id: str
    :param page_size: 
    :type page_size: str
    :param notion_version: 
    :type notion_version: str

    """
    return web.Response(status=200)


async def update_a_block(request: web.Request, id, notion_version=None, body=None) -> web.Response:
    """Update a block

    This endpoint allows you to update block content. [See Full Documentation](https://developers.notion.com/reference/update-a-block)

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateABlockRequest.from_dict(body)
    return web.Response(status=200)
