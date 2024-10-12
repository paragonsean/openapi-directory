from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_sinch_get_collection200_response import ApiTransportSinchGetCollection200Response
from openapi_server.models.transport_sinch_get import TransportSinchGet
from openapi_server.models.transport_sinch_jsonld_get import TransportSinchJsonldGet
from openapi_server.models.transport_sinch_jsonld_post import TransportSinchJsonldPost
from openapi_server.models.transport_sinch_jsonld_put import TransportSinchJsonldPut
from openapi_server.models.transport_sinch_patch import TransportSinchPatch
from openapi_server.models.transport_sinch_post import TransportSinchPost
from openapi_server.models.transport_sinch_put import TransportSinchPut
from openapi_server import util


async def api_transport_sinch_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSinch resources.

    Retrieves the collection of TransportSinch resources.

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


async def api_transport_sinch_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSinch resource.

    Removes the TransportSinch resource.

    :param id: TransportSinch identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sinch_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSinch resource.

    Retrieves a TransportSinch resource.

    :param id: TransportSinch identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sinch_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSinch resource.

    Updates the TransportSinch resource.

    :param id: TransportSinch identifier
    :type id: str
    :param body: The updated TransportSinch resource
    :type body: dict | bytes

    """
    body = TransportSinchPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_sinch_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSinch resource.

    Replaces the TransportSinch resource.

    :param id: TransportSinch identifier
    :type id: str
    :param body: The updated TransportSinch resource
    :type body: dict | bytes

    """
    body = TransportSinchPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_sinch_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSinch resource.

    Creates a TransportSinch resource.

    :param body: The new TransportSinch resource
    :type body: dict | bytes

    """
    body = TransportSinchPost.from_dict(body)
    return web.Response(status=200)
