from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_termii_get_collection200_response import ApiTransportTermiiGetCollection200Response
from openapi_server.models.transport_termii_get import TransportTermiiGet
from openapi_server.models.transport_termii_jsonld_get import TransportTermiiJsonldGet
from openapi_server.models.transport_termii_jsonld_post import TransportTermiiJsonldPost
from openapi_server.models.transport_termii_jsonld_put import TransportTermiiJsonldPut
from openapi_server.models.transport_termii_patch import TransportTermiiPatch
from openapi_server.models.transport_termii_post import TransportTermiiPost
from openapi_server.models.transport_termii_put import TransportTermiiPut
from openapi_server import util


async def api_transport_termii_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportTermii resources.

    Retrieves the collection of TransportTermii resources.

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


async def api_transport_termii_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportTermii resource.

    Removes the TransportTermii resource.

    :param id: TransportTermii identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_termii_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportTermii resource.

    Retrieves a TransportTermii resource.

    :param id: TransportTermii identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_termii_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportTermii resource.

    Updates the TransportTermii resource.

    :param id: TransportTermii identifier
    :type id: str
    :param body: The updated TransportTermii resource
    :type body: dict | bytes

    """
    body = TransportTermiiPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_termii_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportTermii resource.

    Replaces the TransportTermii resource.

    :param id: TransportTermii identifier
    :type id: str
    :param body: The updated TransportTermii resource
    :type body: dict | bytes

    """
    body = TransportTermiiPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_termii_post(request: web.Request, body) -> web.Response:
    """Creates a TransportTermii resource.

    Creates a TransportTermii resource.

    :param body: The new TransportTermii resource
    :type body: dict | bytes

    """
    body = TransportTermiiPost.from_dict(body)
    return web.Response(status=200)
