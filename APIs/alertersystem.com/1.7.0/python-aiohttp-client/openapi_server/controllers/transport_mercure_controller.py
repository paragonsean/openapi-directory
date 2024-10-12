from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_mercure_get_collection200_response import ApiTransportMercureGetCollection200Response
from openapi_server.models.transport_mercure_get import TransportMercureGet
from openapi_server.models.transport_mercure_jsonld_get import TransportMercureJsonldGet
from openapi_server.models.transport_mercure_jsonld_post import TransportMercureJsonldPost
from openapi_server.models.transport_mercure_jsonld_put import TransportMercureJsonldPut
from openapi_server.models.transport_mercure_patch import TransportMercurePatch
from openapi_server.models.transport_mercure_post import TransportMercurePost
from openapi_server.models.transport_mercure_put import TransportMercurePut
from openapi_server import util


async def api_transport_mercure_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMercure resources.

    Retrieves the collection of TransportMercure resources.

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


async def api_transport_mercure_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMercure resource.

    Removes the TransportMercure resource.

    :param id: TransportMercure identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mercure_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMercure resource.

    Retrieves a TransportMercure resource.

    :param id: TransportMercure identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mercure_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMercure resource.

    Updates the TransportMercure resource.

    :param id: TransportMercure identifier
    :type id: str
    :param body: The updated TransportMercure resource
    :type body: dict | bytes

    """
    body = TransportMercurePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_mercure_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMercure resource.

    Replaces the TransportMercure resource.

    :param id: TransportMercure identifier
    :type id: str
    :param body: The updated TransportMercure resource
    :type body: dict | bytes

    """
    body = TransportMercurePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_mercure_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMercure resource.

    Creates a TransportMercure resource.

    :param body: The new TransportMercure resource
    :type body: dict | bytes

    """
    body = TransportMercurePost.from_dict(body)
    return web.Response(status=200)
