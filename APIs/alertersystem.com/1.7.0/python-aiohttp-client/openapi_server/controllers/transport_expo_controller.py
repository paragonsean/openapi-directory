from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_expo_get_collection200_response import ApiTransportExpoGetCollection200Response
from openapi_server.models.transport_expo_get import TransportExpoGet
from openapi_server.models.transport_expo_jsonld_get import TransportExpoJsonldGet
from openapi_server.models.transport_expo_jsonld_post import TransportExpoJsonldPost
from openapi_server.models.transport_expo_jsonld_put import TransportExpoJsonldPut
from openapi_server.models.transport_expo_patch import TransportExpoPatch
from openapi_server.models.transport_expo_post import TransportExpoPost
from openapi_server.models.transport_expo_put import TransportExpoPut
from openapi_server import util


async def api_transport_expo_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportExpo resources.

    Retrieves the collection of TransportExpo resources.

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


async def api_transport_expo_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportExpo resource.

    Removes the TransportExpo resource.

    :param id: TransportExpo identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_expo_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportExpo resource.

    Retrieves a TransportExpo resource.

    :param id: TransportExpo identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_expo_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportExpo resource.

    Updates the TransportExpo resource.

    :param id: TransportExpo identifier
    :type id: str
    :param body: The updated TransportExpo resource
    :type body: dict | bytes

    """
    body = TransportExpoPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_expo_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportExpo resource.

    Replaces the TransportExpo resource.

    :param id: TransportExpo identifier
    :type id: str
    :param body: The updated TransportExpo resource
    :type body: dict | bytes

    """
    body = TransportExpoPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_expo_post(request: web.Request, body) -> web.Response:
    """Creates a TransportExpo resource.

    Creates a TransportExpo resource.

    :param body: The new TransportExpo resource
    :type body: dict | bytes

    """
    body = TransportExpoPost.from_dict(body)
    return web.Response(status=200)
