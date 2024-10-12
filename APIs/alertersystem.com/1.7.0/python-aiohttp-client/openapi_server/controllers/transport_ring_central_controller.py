from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_ring_central_get_collection200_response import ApiTransportRingCentralGetCollection200Response
from openapi_server.models.transport_ring_central_get import TransportRingCentralGet
from openapi_server.models.transport_ring_central_jsonld_get import TransportRingCentralJsonldGet
from openapi_server.models.transport_ring_central_jsonld_post import TransportRingCentralJsonldPost
from openapi_server.models.transport_ring_central_jsonld_put import TransportRingCentralJsonldPut
from openapi_server.models.transport_ring_central_patch import TransportRingCentralPatch
from openapi_server.models.transport_ring_central_post import TransportRingCentralPost
from openapi_server.models.transport_ring_central_put import TransportRingCentralPut
from openapi_server import util


async def api_transport_ring_central_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportRingCentral resources.

    Retrieves the collection of TransportRingCentral resources.

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


async def api_transport_ring_central_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportRingCentral resource.

    Removes the TransportRingCentral resource.

    :param id: TransportRingCentral identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_ring_central_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportRingCentral resource.

    Retrieves a TransportRingCentral resource.

    :param id: TransportRingCentral identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_ring_central_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportRingCentral resource.

    Updates the TransportRingCentral resource.

    :param id: TransportRingCentral identifier
    :type id: str
    :param body: The updated TransportRingCentral resource
    :type body: dict | bytes

    """
    body = TransportRingCentralPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_ring_central_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportRingCentral resource.

    Replaces the TransportRingCentral resource.

    :param id: TransportRingCentral identifier
    :type id: str
    :param body: The updated TransportRingCentral resource
    :type body: dict | bytes

    """
    body = TransportRingCentralPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_ring_central_post(request: web.Request, body) -> web.Response:
    """Creates a TransportRingCentral resource.

    Creates a TransportRingCentral resource.

    :param body: The new TransportRingCentral resource
    :type body: dict | bytes

    """
    body = TransportRingCentralPost.from_dict(body)
    return web.Response(status=200)
