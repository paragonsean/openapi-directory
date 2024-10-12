from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_collection_changeset(request: web.Request, bid, cid, expected, since=None, limit=None, bucket=None, collection=None) -> web.Response:
    """get_collection_changeset

    

    :param bid: 
    :type bid: str
    :param cid: 
    :type cid: str
    :param expected: 
    :type expected: str
    :param since: 
    :type since: str
    :param limit: 
    :type limit: int
    :param bucket: 
    :type bucket: str
    :param collection: 
    :type collection: str

    """
    return web.Response(status=200)
