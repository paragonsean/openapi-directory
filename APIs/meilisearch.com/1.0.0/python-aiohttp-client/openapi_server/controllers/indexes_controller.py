from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_index_with_primary_key_request import CreateIndexWithPrimaryKeyRequest
from openapi_server.models.swap_indexes_request_inner import SwapIndexesRequestInner
from openapi_server.models.update_index_request import UpdateIndexRequest
from openapi_server import util


async def create_index_with_primary_key(request: web.Request, body=None) -> web.Response:
    """Create index with primary key

    Create index with primary key

    :param body: 
    :type body: dict | bytes

    """
    body = CreateIndexWithPrimaryKeyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_an_index(request: web.Request, ) -> web.Response:
    """Delete an index

    Delete an index


    """
    return web.Response(status=200)


async def get_indexes(request: web.Request, offset=None, limit=None) -> web.Response:
    """Get indexes

    Get indexes

    :param offset: 
    :type offset: str
    :param limit: 
    :type limit: str

    """
    return web.Response(status=200)


async def show_index(request: web.Request, ) -> web.Response:
    """Show index

    Show index


    """
    return web.Response(status=200)


async def swap_indexes(request: web.Request, body=None) -> web.Response:
    """Swap indexes

    Swap indexes

    :param body: 
    :type body: list | bytes

    """
    body = [SwapIndexesRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_index(request: web.Request, body=None) -> web.Response:
    """Update index

    Can only change the document identifier if it has not already been added before.

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateIndexRequest.from_dict(body)
    return web.Response(status=200)
