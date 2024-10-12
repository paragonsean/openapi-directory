from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_engagespot_get_collection200_response import ApiTransportEngagespotGetCollection200Response
from openapi_server.models.transport_engagespot_get import TransportEngagespotGet
from openapi_server.models.transport_engagespot_jsonld_get import TransportEngagespotJsonldGet
from openapi_server.models.transport_engagespot_jsonld_post import TransportEngagespotJsonldPost
from openapi_server.models.transport_engagespot_jsonld_put import TransportEngagespotJsonldPut
from openapi_server.models.transport_engagespot_patch import TransportEngagespotPatch
from openapi_server.models.transport_engagespot_post import TransportEngagespotPost
from openapi_server.models.transport_engagespot_put import TransportEngagespotPut
from openapi_server import util


async def api_transport_engagespot_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportEngagespot resources.

    Retrieves the collection of TransportEngagespot resources.

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


async def api_transport_engagespot_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportEngagespot resource.

    Removes the TransportEngagespot resource.

    :param id: TransportEngagespot identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_engagespot_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportEngagespot resource.

    Retrieves a TransportEngagespot resource.

    :param id: TransportEngagespot identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_engagespot_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportEngagespot resource.

    Updates the TransportEngagespot resource.

    :param id: TransportEngagespot identifier
    :type id: str
    :param body: The updated TransportEngagespot resource
    :type body: dict | bytes

    """
    body = TransportEngagespotPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_engagespot_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportEngagespot resource.

    Replaces the TransportEngagespot resource.

    :param id: TransportEngagespot identifier
    :type id: str
    :param body: The updated TransportEngagespot resource
    :type body: dict | bytes

    """
    body = TransportEngagespotPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_engagespot_post(request: web.Request, body) -> web.Response:
    """Creates a TransportEngagespot resource.

    Creates a TransportEngagespot resource.

    :param body: The new TransportEngagespot resource
    :type body: dict | bytes

    """
    body = TransportEngagespotPost.from_dict(body)
    return web.Response(status=200)
