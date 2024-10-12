from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_line_notify_get_collection200_response import ApiTransportLineNotifyGetCollection200Response
from openapi_server.models.transport_line_notify_get import TransportLineNotifyGet
from openapi_server.models.transport_line_notify_jsonld_get import TransportLineNotifyJsonldGet
from openapi_server.models.transport_line_notify_jsonld_post import TransportLineNotifyJsonldPost
from openapi_server.models.transport_line_notify_jsonld_put import TransportLineNotifyJsonldPut
from openapi_server.models.transport_line_notify_patch import TransportLineNotifyPatch
from openapi_server.models.transport_line_notify_post import TransportLineNotifyPost
from openapi_server.models.transport_line_notify_put import TransportLineNotifyPut
from openapi_server import util


async def api_transport_line_notify_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportLineNotify resources.

    Retrieves the collection of TransportLineNotify resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_transport_line_notify_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportLineNotify resource.

    Removes the TransportLineNotify resource.

    :param id: TransportLineNotify identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_line_notify_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportLineNotify resource.

    Retrieves a TransportLineNotify resource.

    :param id: TransportLineNotify identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_line_notify_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportLineNotify resource.

    Updates the TransportLineNotify resource.

    :param id: TransportLineNotify identifier
    :type id: str
    :param body: The updated TransportLineNotify resource
    :type body: dict | bytes

    """
    body = TransportLineNotifyPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_line_notify_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportLineNotify resource.

    Replaces the TransportLineNotify resource.

    :param id: TransportLineNotify identifier
    :type id: str
    :param body: The updated TransportLineNotify resource
    :type body: dict | bytes

    """
    body = TransportLineNotifyPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_line_notify_post(request: web.Request, body) -> web.Response:
    """Creates a TransportLineNotify resource.

    Creates a TransportLineNotify resource.

    :param body: The new TransportLineNotify resource
    :type body: dict | bytes

    """
    body = TransportLineNotifyPost.from_dict(body)
    return web.Response(status=200)
