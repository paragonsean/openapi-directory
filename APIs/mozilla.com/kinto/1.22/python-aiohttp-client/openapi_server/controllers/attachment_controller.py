from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_attachment(request: web.Request, bucket_id, collection_id, id) -> web.Response:
    """create_attachment

    

    :param bucket_id: 
    :type bucket_id: str
    :param collection_id: 
    :type collection_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_attachment(request: web.Request, bucket_id, collection_id, id) -> web.Response:
    """delete_attachment

    

    :param bucket_id: 
    :type bucket_id: str
    :param collection_id: 
    :type collection_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)
