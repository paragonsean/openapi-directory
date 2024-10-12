from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_gotify_get_collection200_response import ApiTransportGotifyGetCollection200Response
from openapi_server.models.transport_gotify_get import TransportGotifyGet
from openapi_server.models.transport_gotify_jsonld_get import TransportGotifyJsonldGet
from openapi_server.models.transport_gotify_jsonld_post import TransportGotifyJsonldPost
from openapi_server.models.transport_gotify_jsonld_put import TransportGotifyJsonldPut
from openapi_server.models.transport_gotify_patch import TransportGotifyPatch
from openapi_server.models.transport_gotify_post import TransportGotifyPost
from openapi_server.models.transport_gotify_put import TransportGotifyPut
from openapi_server import util


async def api_transport_gotify_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportGotify resources.

    Retrieves the collection of TransportGotify resources.

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


async def api_transport_gotify_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportGotify resource.

    Removes the TransportGotify resource.

    :param id: TransportGotify identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_gotify_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportGotify resource.

    Retrieves a TransportGotify resource.

    :param id: TransportGotify identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_gotify_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportGotify resource.

    Updates the TransportGotify resource.

    :param id: TransportGotify identifier
    :type id: str
    :param body: The updated TransportGotify resource
    :type body: dict | bytes

    """
    body = TransportGotifyPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_gotify_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportGotify resource.

    Replaces the TransportGotify resource.

    :param id: TransportGotify identifier
    :type id: str
    :param body: The updated TransportGotify resource
    :type body: dict | bytes

    """
    body = TransportGotifyPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_gotify_post(request: web.Request, body) -> web.Response:
    """Creates a TransportGotify resource.

    Creates a TransportGotify resource.

    :param body: The new TransportGotify resource
    :type body: dict | bytes

    """
    body = TransportGotifyPost.from_dict(body)
    return web.Response(status=200)
