from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.object_schema import ObjectSchema
from openapi_server.models.schema3 import Schema3
from openapi_server import util


async def get_record(request: web.Request, bucket_id, collection_id, id, fields=None, if_match=None, if_none_match=None) -> web.Response:
    """get_record

    

    :param bucket_id: 
    :type bucket_id: str
    :param collection_id: 
    :type collection_id: str
    :param id: 
    :type id: str
    :param fields: 
    :type fields: List[str]
    :param if_match: 
    :type if_match: str
    :param if_none_match: 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_records(request: web.Request, bucket_id, collection_id, limit=None, sort=None, token=None, since=None, to=None, before=None, id=None, last_modified=None, fields=None, if_match=None, if_none_match=None) -> web.Response:
    """get_records

    

    :param bucket_id: 
    :type bucket_id: str
    :param collection_id: 
    :type collection_id: str
    :param limit: 
    :type limit: int
    :param sort: 
    :type sort: List[str]
    :param token: 
    :type token: str
    :param since: 
    :type since: int
    :param to: 
    :type to: int
    :param before: 
    :type before: int
    :param id: 
    :type id: str
    :param last_modified: 
    :type last_modified: int
    :param fields: 
    :type fields: List[str]
    :param if_match: 
    :type if_match: str
    :param if_none_match: 
    :type if_none_match: str

    """
    return web.Response(status=200)
