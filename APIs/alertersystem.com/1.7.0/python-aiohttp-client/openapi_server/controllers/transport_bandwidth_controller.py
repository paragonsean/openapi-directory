from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_bandwidth_get_collection200_response import ApiTransportBandwidthGetCollection200Response
from openapi_server.models.transport_bandwidth_get import TransportBandwidthGet
from openapi_server.models.transport_bandwidth_jsonld_get import TransportBandwidthJsonldGet
from openapi_server.models.transport_bandwidth_jsonld_post import TransportBandwidthJsonldPost
from openapi_server.models.transport_bandwidth_jsonld_put import TransportBandwidthJsonldPut
from openapi_server.models.transport_bandwidth_patch import TransportBandwidthPatch
from openapi_server.models.transport_bandwidth_post import TransportBandwidthPost
from openapi_server.models.transport_bandwidth_put import TransportBandwidthPut
from openapi_server import util


async def api_transport_bandwidth_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportBandwidth resources.

    Retrieves the collection of TransportBandwidth resources.

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


async def api_transport_bandwidth_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportBandwidth resource.

    Removes the TransportBandwidth resource.

    :param id: TransportBandwidth identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_bandwidth_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportBandwidth resource.

    Retrieves a TransportBandwidth resource.

    :param id: TransportBandwidth identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_bandwidth_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportBandwidth resource.

    Updates the TransportBandwidth resource.

    :param id: TransportBandwidth identifier
    :type id: str
    :param body: The updated TransportBandwidth resource
    :type body: dict | bytes

    """
    body = TransportBandwidthPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_bandwidth_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportBandwidth resource.

    Replaces the TransportBandwidth resource.

    :param id: TransportBandwidth identifier
    :type id: str
    :param body: The updated TransportBandwidth resource
    :type body: dict | bytes

    """
    body = TransportBandwidthPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_bandwidth_post(request: web.Request, body) -> web.Response:
    """Creates a TransportBandwidth resource.

    Creates a TransportBandwidth resource.

    :param body: The new TransportBandwidth resource
    :type body: dict | bytes

    """
    body = TransportBandwidthPost.from_dict(body)
    return web.Response(status=200)
