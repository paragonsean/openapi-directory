from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_chatwork_get_collection200_response import ApiTransportChatworkGetCollection200Response
from openapi_server.models.transport_chatwork_get import TransportChatworkGet
from openapi_server.models.transport_chatwork_jsonld_get import TransportChatworkJsonldGet
from openapi_server.models.transport_chatwork_jsonld_post import TransportChatworkJsonldPost
from openapi_server.models.transport_chatwork_jsonld_put import TransportChatworkJsonldPut
from openapi_server.models.transport_chatwork_patch import TransportChatworkPatch
from openapi_server.models.transport_chatwork_post import TransportChatworkPost
from openapi_server.models.transport_chatwork_put import TransportChatworkPut
from openapi_server import util


async def api_transport_chatwork_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportChatwork resources.

    Retrieves the collection of TransportChatwork resources.

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


async def api_transport_chatwork_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportChatwork resource.

    Removes the TransportChatwork resource.

    :param id: TransportChatwork identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_chatwork_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportChatwork resource.

    Retrieves a TransportChatwork resource.

    :param id: TransportChatwork identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_chatwork_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportChatwork resource.

    Updates the TransportChatwork resource.

    :param id: TransportChatwork identifier
    :type id: str
    :param body: The updated TransportChatwork resource
    :type body: dict | bytes

    """
    body = TransportChatworkPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_chatwork_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportChatwork resource.

    Replaces the TransportChatwork resource.

    :param id: TransportChatwork identifier
    :type id: str
    :param body: The updated TransportChatwork resource
    :type body: dict | bytes

    """
    body = TransportChatworkPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_chatwork_post(request: web.Request, body) -> web.Response:
    """Creates a TransportChatwork resource.

    Creates a TransportChatwork resource.

    :param body: The new TransportChatwork resource
    :type body: dict | bytes

    """
    body = TransportChatworkPost.from_dict(body)
    return web.Response(status=200)
