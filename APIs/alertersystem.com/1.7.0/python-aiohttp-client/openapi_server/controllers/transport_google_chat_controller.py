from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_google_chat_get_collection200_response import ApiTransportGoogleChatGetCollection200Response
from openapi_server.models.transport_google_chat_get import TransportGoogleChatGet
from openapi_server.models.transport_google_chat_jsonld_get import TransportGoogleChatJsonldGet
from openapi_server.models.transport_google_chat_jsonld_post import TransportGoogleChatJsonldPost
from openapi_server.models.transport_google_chat_jsonld_put import TransportGoogleChatJsonldPut
from openapi_server.models.transport_google_chat_patch import TransportGoogleChatPatch
from openapi_server.models.transport_google_chat_post import TransportGoogleChatPost
from openapi_server.models.transport_google_chat_put import TransportGoogleChatPut
from openapi_server import util


async def api_transport_google_chat_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportGoogleChat resources.

    Retrieves the collection of TransportGoogleChat resources.

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


async def api_transport_google_chat_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportGoogleChat resource.

    Removes the TransportGoogleChat resource.

    :param id: TransportGoogleChat identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_google_chat_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportGoogleChat resource.

    Retrieves a TransportGoogleChat resource.

    :param id: TransportGoogleChat identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_google_chat_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportGoogleChat resource.

    Updates the TransportGoogleChat resource.

    :param id: TransportGoogleChat identifier
    :type id: str
    :param body: The updated TransportGoogleChat resource
    :type body: dict | bytes

    """
    body = TransportGoogleChatPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_google_chat_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportGoogleChat resource.

    Replaces the TransportGoogleChat resource.

    :param id: TransportGoogleChat identifier
    :type id: str
    :param body: The updated TransportGoogleChat resource
    :type body: dict | bytes

    """
    body = TransportGoogleChatPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_google_chat_post(request: web.Request, body) -> web.Response:
    """Creates a TransportGoogleChat resource.

    Creates a TransportGoogleChat resource.

    :param body: The new TransportGoogleChat resource
    :type body: dict | bytes

    """
    body = TransportGoogleChatPost.from_dict(body)
    return web.Response(status=200)
