from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_plivo_get_collection200_response import ApiTransportPlivoGetCollection200Response
from openapi_server.models.transport_plivo_get import TransportPlivoGet
from openapi_server.models.transport_plivo_jsonld_get import TransportPlivoJsonldGet
from openapi_server.models.transport_plivo_jsonld_post import TransportPlivoJsonldPost
from openapi_server.models.transport_plivo_jsonld_put import TransportPlivoJsonldPut
from openapi_server.models.transport_plivo_patch import TransportPlivoPatch
from openapi_server.models.transport_plivo_post import TransportPlivoPost
from openapi_server.models.transport_plivo_put import TransportPlivoPut
from openapi_server import util


async def api_transport_plivo_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportPlivo resources.

    Retrieves the collection of TransportPlivo resources.

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


async def api_transport_plivo_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportPlivo resource.

    Removes the TransportPlivo resource.

    :param id: TransportPlivo identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_plivo_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportPlivo resource.

    Retrieves a TransportPlivo resource.

    :param id: TransportPlivo identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_plivo_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportPlivo resource.

    Updates the TransportPlivo resource.

    :param id: TransportPlivo identifier
    :type id: str
    :param body: The updated TransportPlivo resource
    :type body: dict | bytes

    """
    body = TransportPlivoPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_plivo_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportPlivo resource.

    Replaces the TransportPlivo resource.

    :param id: TransportPlivo identifier
    :type id: str
    :param body: The updated TransportPlivo resource
    :type body: dict | bytes

    """
    body = TransportPlivoPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_plivo_post(request: web.Request, body) -> web.Response:
    """Creates a TransportPlivo resource.

    Creates a TransportPlivo resource.

    :param body: The new TransportPlivo resource
    :type body: dict | bytes

    """
    body = TransportPlivoPost.from_dict(body)
    return web.Response(status=200)
