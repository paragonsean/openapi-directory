from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_message_bird_get_collection200_response import ApiTransportMessageBirdGetCollection200Response
from openapi_server.models.transport_message_bird_get import TransportMessageBirdGet
from openapi_server.models.transport_message_bird_jsonld_get import TransportMessageBirdJsonldGet
from openapi_server.models.transport_message_bird_jsonld_post import TransportMessageBirdJsonldPost
from openapi_server.models.transport_message_bird_jsonld_put import TransportMessageBirdJsonldPut
from openapi_server.models.transport_message_bird_patch import TransportMessageBirdPatch
from openapi_server.models.transport_message_bird_post import TransportMessageBirdPost
from openapi_server.models.transport_message_bird_put import TransportMessageBirdPut
from openapi_server import util


async def api_transport_message_bird_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMessageBird resources.

    Retrieves the collection of TransportMessageBird resources.

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


async def api_transport_message_bird_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMessageBird resource.

    Removes the TransportMessageBird resource.

    :param id: TransportMessageBird identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_message_bird_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMessageBird resource.

    Retrieves a TransportMessageBird resource.

    :param id: TransportMessageBird identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_message_bird_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMessageBird resource.

    Updates the TransportMessageBird resource.

    :param id: TransportMessageBird identifier
    :type id: str
    :param body: The updated TransportMessageBird resource
    :type body: dict | bytes

    """
    body = TransportMessageBirdPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_message_bird_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMessageBird resource.

    Replaces the TransportMessageBird resource.

    :param id: TransportMessageBird identifier
    :type id: str
    :param body: The updated TransportMessageBird resource
    :type body: dict | bytes

    """
    body = TransportMessageBirdPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_message_bird_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMessageBird resource.

    Creates a TransportMessageBird resource.

    :param body: The new TransportMessageBird resource
    :type body: dict | bytes

    """
    body = TransportMessageBirdPost.from_dict(body)
    return web.Response(status=200)
