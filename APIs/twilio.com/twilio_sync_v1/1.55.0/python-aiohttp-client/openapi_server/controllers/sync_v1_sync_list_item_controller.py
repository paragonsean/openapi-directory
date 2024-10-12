from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_list_item_response import ListSyncListItemResponse
from openapi_server.models.sync_list_item_enum_query_from_bound_type import SyncListItemEnumQueryFromBoundType
from openapi_server.models.sync_list_item_enum_query_result_order import SyncListItemEnumQueryResultOrder
from openapi_server.models.sync_v1_service_sync_list_sync_list_item import SyncV1ServiceSyncListSyncListItem
from openapi_server import util


async def create_sync_list_item(request: web.Request, service_sid, list_sid, data, collection_ttl=None, item_ttl=None, ttl=None) -> web.Response:
    """create_sync_list_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new List Item in.
    :type service_sid: str
    :param list_sid: The SID of the Sync List to add the new List Item to. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length.
    :type data: dict | bytes
    :param collection_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item&#39;s parent Sync List expires (time-to-live) and is deleted.
    :type collection_ttl: int
    :param item_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted.
    :type item_ttl: int
    :param ttl: An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored.
    :type ttl: int

    """
    data = object.from_dict(data)
    return web.Response(status=200)


async def delete_sync_list_item(request: web.Request, service_sid, list_sid, index, if_match=None) -> web.Response:
    """delete_sync_list_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to delete.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param index: The index of the Sync List Item resource to delete.
    :type index: int
    :param if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    :type if_match: str

    """
    return web.Response(status=200)


async def fetch_sync_list_item(request: web.Request, service_sid, list_sid, index) -> web.Response:
    """fetch_sync_list_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to fetch.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param index: The index of the Sync List Item resource to fetch.
    :type index: int

    """
    return web.Response(status=200)


async def list_sync_list_item(request: web.Request, service_sid, list_sid, order=None, _from=None, bounds=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_list_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the List Item resources to read.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the List Items to read. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param order: How to order the List Items returned by their &#x60;index&#x60; value. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) and the default is ascending.
    :type order: str
    :param _from: The &#x60;index&#x60; of the first Sync List Item resource to read. See also &#x60;bounds&#x60;.
    :type _from: str
    :param bounds: Whether to include the List Item referenced by the &#x60;from&#x60; parameter. Can be: &#x60;inclusive&#x60; to include the List Item referenced by the &#x60;from&#x60; parameter or &#x60;exclusive&#x60; to start with the next List Item. The default value is &#x60;inclusive&#x60;.
    :type bounds: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_list_item(request: web.Request, service_sid, list_sid, index, if_match=None, collection_ttl=None, data=None, item_ttl=None, ttl=None) -> web.Response:
    """update_sync_list_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to update.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param index: The index of the Sync List Item resource to update.
    :type index: int
    :param if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    :type if_match: str
    :param collection_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item&#39;s parent Sync List expires (time-to-live) and is deleted. This parameter can only be used when the List Item&#39;s &#x60;data&#x60; or &#x60;ttl&#x60; is updated in the same request.
    :type collection_ttl: int
    :param data: A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length.
    :type data: dict | bytes
    :param item_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted.
    :type item_ttl: int
    :param ttl: An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored.
    :type ttl: int

    """
    data = object.from_dict(data)
    return web.Response(status=200)
