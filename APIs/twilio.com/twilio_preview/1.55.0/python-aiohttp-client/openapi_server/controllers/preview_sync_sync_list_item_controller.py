from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_sync_list_item_response import ListSyncSyncListItemResponse
from openapi_server.models.preview_sync_service_sync_list_sync_list_item import PreviewSyncServiceSyncListSyncListItem
from openapi_server.models.sync_list_item_enum_query_from_bound_type import SyncListItemEnumQueryFromBoundType
from openapi_server.models.sync_list_item_enum_query_result_order import SyncListItemEnumQueryResultOrder
from openapi_server import util


async def create_sync_sync_list_item(request: web.Request, service_sid, list_sid, data) -> web.Response:
    """create_sync_sync_list_item

    

    :param service_sid: 
    :type service_sid: str
    :param list_sid: 
    :type list_sid: str
    :param data: 
    :type data: dict | bytes

    """
    data = object.from_dict(data)
    return web.Response(status=200)


async def delete_sync_sync_list_item(request: web.Request, service_sid, list_sid, index, if_match=None) -> web.Response:
    """delete_sync_sync_list_item

    

    :param service_sid: 
    :type service_sid: str
    :param list_sid: 
    :type list_sid: str
    :param index: 
    :type index: int
    :param if_match: The If-Match HTTP request header
    :type if_match: str

    """
    return web.Response(status=200)


async def fetch_sync_sync_list_item(request: web.Request, service_sid, list_sid, index) -> web.Response:
    """fetch_sync_sync_list_item

    

    :param service_sid: 
    :type service_sid: str
    :param list_sid: 
    :type list_sid: str
    :param index: 
    :type index: int

    """
    return web.Response(status=200)


async def list_sync_sync_list_item(request: web.Request, service_sid, list_sid, order=None, _from=None, bounds=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_sync_list_item

    

    :param service_sid: 
    :type service_sid: str
    :param list_sid: 
    :type list_sid: str
    :param order: 
    :type order: str
    :param _from: 
    :type _from: str
    :param bounds: 
    :type bounds: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_sync_list_item(request: web.Request, service_sid, list_sid, index, data, if_match=None) -> web.Response:
    """update_sync_sync_list_item

    

    :param service_sid: 
    :type service_sid: str
    :param list_sid: 
    :type list_sid: str
    :param index: 
    :type index: int
    :param data: 
    :type data: dict | bytes
    :param if_match: The If-Match HTTP request header
    :type if_match: str

    """
    data = object.from_dict(data)
    return web.Response(status=200)
