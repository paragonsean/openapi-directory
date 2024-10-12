from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_map_item_response import ListSyncMapItemResponse
from openapi_server.models.sync_map_item_enum_query_from_bound_type import SyncMapItemEnumQueryFromBoundType
from openapi_server.models.sync_map_item_enum_query_result_order import SyncMapItemEnumQueryResultOrder
from openapi_server.models.sync_v1_service_sync_map_sync_map_item import SyncV1ServiceSyncMapSyncMapItem
from openapi_server import util


async def create_sync_map_item(request: web.Request, service_sid, map_sid, data, key, collection_ttl=None, item_ttl=None, ttl=None) -> web.Response:
    """create_sync_map_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Map Item in.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length.
    :type data: dict | bytes
    :param key: The unique, user-defined key for the Map Item. Can be up to 320 characters long.
    :type key: str
    :param collection_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item&#39;s parent Sync Map expires (time-to-live) and is deleted.
    :type collection_ttl: int
    :param item_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted.
    :type item_ttl: int
    :param ttl: An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored.
    :type ttl: int

    """
    data = object.from_dict(data)
    return web.Response(status=200)


async def delete_sync_map_item(request: web.Request, service_sid, map_sid, key, if_match=None) -> web.Response:
    """delete_sync_map_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to delete.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param key: The &#x60;key&#x60; value of the Sync Map Item resource to delete.
    :type key: str
    :param if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    :type if_match: str

    """
    return web.Response(status=200)


async def fetch_sync_map_item(request: web.Request, service_sid, map_sid, key) -> web.Response:
    """fetch_sync_map_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to fetch.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param key: The &#x60;key&#x60; value of the Sync Map Item resource to fetch.
    :type key: str

    """
    return web.Response(status=200)


async def list_sync_map_item(request: web.Request, service_sid, map_sid, order=None, _from=None, bounds=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_map_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Map Item resources to read.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param order: How to order the Map Items returned by their &#x60;key&#x60; value. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) and the default is ascending. Map Items are [ordered lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) by Item key.
    :type order: str
    :param _from: The &#x60;key&#x60; of the first Sync Map Item resource to read. See also &#x60;bounds&#x60;.
    :type _from: str
    :param bounds: Whether to include the Map Item referenced by the &#x60;from&#x60; parameter. Can be: &#x60;inclusive&#x60; to include the Map Item referenced by the &#x60;from&#x60; parameter or &#x60;exclusive&#x60; to start with the next Map Item. The default value is &#x60;inclusive&#x60;.
    :type bounds: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_map_item(request: web.Request, service_sid, map_sid, key, if_match=None, collection_ttl=None, data=None, item_ttl=None, ttl=None) -> web.Response:
    """update_sync_map_item

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to update.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param key: The &#x60;key&#x60; value of the Sync Map Item resource to update. 
    :type key: str
    :param if_match: If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    :type if_match: str
    :param collection_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item&#39;s parent Sync Map expires (time-to-live) and is deleted. This parameter can only be used when the Map Item&#39;s &#x60;data&#x60; or &#x60;ttl&#x60; is updated in the same request.
    :type collection_ttl: int
    :param data: A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length.
    :type data: dict | bytes
    :param item_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted.
    :type item_ttl: int
    :param ttl: An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored.
    :type ttl: int

    """
    data = object.from_dict(data)
    return web.Response(status=200)
