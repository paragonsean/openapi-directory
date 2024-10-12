from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_rocket_chat_get_collection200_response import ApiTransportRocketChatGetCollection200Response
from openapi_server.models.transport_rocket_chat_get import TransportRocketChatGet
from openapi_server.models.transport_rocket_chat_jsonld_get import TransportRocketChatJsonldGet
from openapi_server.models.transport_rocket_chat_jsonld_post import TransportRocketChatJsonldPost
from openapi_server.models.transport_rocket_chat_jsonld_put import TransportRocketChatJsonldPut
from openapi_server.models.transport_rocket_chat_patch import TransportRocketChatPatch
from openapi_server.models.transport_rocket_chat_post import TransportRocketChatPost
from openapi_server.models.transport_rocket_chat_put import TransportRocketChatPut
from openapi_server import util


async def api_transport_rocket_chat_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportRocketChat resources.

    Retrieves the collection of TransportRocketChat resources.

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


async def api_transport_rocket_chat_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportRocketChat resource.

    Removes the TransportRocketChat resource.

    :param id: TransportRocketChat identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_rocket_chat_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportRocketChat resource.

    Retrieves a TransportRocketChat resource.

    :param id: TransportRocketChat identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_rocket_chat_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportRocketChat resource.

    Updates the TransportRocketChat resource.

    :param id: TransportRocketChat identifier
    :type id: str
    :param body: The updated TransportRocketChat resource
    :type body: dict | bytes

    """
    body = TransportRocketChatPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_rocket_chat_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportRocketChat resource.

    Replaces the TransportRocketChat resource.

    :param id: TransportRocketChat identifier
    :type id: str
    :param body: The updated TransportRocketChat resource
    :type body: dict | bytes

    """
    body = TransportRocketChatPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_rocket_chat_post(request: web.Request, body) -> web.Response:
    """Creates a TransportRocketChat resource.

    Creates a TransportRocketChat resource.

    :param body: The new TransportRocketChat resource
    :type body: dict | bytes

    """
    body = TransportRocketChatPost.from_dict(body)
    return web.Response(status=200)
