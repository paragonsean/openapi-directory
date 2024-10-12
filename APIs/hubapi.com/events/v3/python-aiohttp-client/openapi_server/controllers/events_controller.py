from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_external_unified_event import CollectionResponseExternalUnifiedEvent
from openapi_server.models.error import Error
from openapi_server import util


async def get_events_v3_events_get_page(request: web.Request, object_type=None, event_type=None, occurred_after=None, occurred_before=None, object_id=None, index_table_name=None, index_specific_metadata=None, after=None, before=None, limit=None, sort=None, object_property_propname=None, property_propname=None, id=None) -> web.Response:
    """get_events_v3_events_get_page

    

    :param object_type: 
    :type object_type: str
    :param event_type: 
    :type event_type: str
    :param occurred_after: 
    :type occurred_after: str
    :param occurred_before: 
    :type occurred_before: str
    :param object_id: 
    :type object_id: int
    :param index_table_name: 
    :type index_table_name: str
    :param index_specific_metadata: 
    :type index_specific_metadata: str
    :param after: The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results.
    :type after: str
    :param before: 
    :type before: str
    :param limit: The maximum number of results to display per page.
    :type limit: int
    :param sort: 
    :type sort: List[str]
    :param object_property_propname: 
    :type object_property_propname: dict | bytes
    :param property_propname: 
    :type property_propname: dict | bytes
    :param id: 
    :type id: List[str]

    """
    occurred_after = util.deserialize_datetime(occurred_after)
    occurred_before = util.deserialize_datetime(occurred_before)
    object_property_propname = .from_dict(object_property_propname)
    property_propname = .from_dict(property_propname)
    return web.Response(status=200)
