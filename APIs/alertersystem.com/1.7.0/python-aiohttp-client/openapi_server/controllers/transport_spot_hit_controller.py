from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_spot_hit_get_collection200_response import ApiTransportSpotHitGetCollection200Response
from openapi_server.models.transport_spot_hit_get import TransportSpotHitGet
from openapi_server.models.transport_spot_hit_jsonld_get import TransportSpotHitJsonldGet
from openapi_server.models.transport_spot_hit_jsonld_post import TransportSpotHitJsonldPost
from openapi_server.models.transport_spot_hit_jsonld_put import TransportSpotHitJsonldPut
from openapi_server.models.transport_spot_hit_patch import TransportSpotHitPatch
from openapi_server.models.transport_spot_hit_post import TransportSpotHitPost
from openapi_server.models.transport_spot_hit_put import TransportSpotHitPut
from openapi_server import util


async def api_transport_spot_hit_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSpotHit resources.

    Retrieves the collection of TransportSpotHit resources.

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


async def api_transport_spot_hit_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSpotHit resource.

    Removes the TransportSpotHit resource.

    :param id: TransportSpotHit identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_spot_hit_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSpotHit resource.

    Retrieves a TransportSpotHit resource.

    :param id: TransportSpotHit identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_spot_hit_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSpotHit resource.

    Updates the TransportSpotHit resource.

    :param id: TransportSpotHit identifier
    :type id: str
    :param body: The updated TransportSpotHit resource
    :type body: dict | bytes

    """
    body = TransportSpotHitPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_spot_hit_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSpotHit resource.

    Replaces the TransportSpotHit resource.

    :param id: TransportSpotHit identifier
    :type id: str
    :param body: The updated TransportSpotHit resource
    :type body: dict | bytes

    """
    body = TransportSpotHitPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_spot_hit_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSpotHit resource.

    Creates a TransportSpotHit resource.

    :param body: The new TransportSpotHit resource
    :type body: dict | bytes

    """
    body = TransportSpotHitPost.from_dict(body)
    return web.Response(status=200)
