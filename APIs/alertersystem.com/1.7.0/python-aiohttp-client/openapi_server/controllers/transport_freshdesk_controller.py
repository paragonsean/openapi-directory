from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_freshdesk_get_collection200_response import ApiTransportFreshdeskGetCollection200Response
from openapi_server.models.transport_freshdesk_get import TransportFreshdeskGet
from openapi_server.models.transport_freshdesk_jsonld_get import TransportFreshdeskJsonldGet
from openapi_server.models.transport_freshdesk_jsonld_post import TransportFreshdeskJsonldPost
from openapi_server.models.transport_freshdesk_jsonld_put import TransportFreshdeskJsonldPut
from openapi_server.models.transport_freshdesk_patch import TransportFreshdeskPatch
from openapi_server.models.transport_freshdesk_post import TransportFreshdeskPost
from openapi_server.models.transport_freshdesk_put import TransportFreshdeskPut
from openapi_server import util


async def api_transport_freshdesk_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportFreshdesk resources.

    Retrieves the collection of TransportFreshdesk resources.

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


async def api_transport_freshdesk_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportFreshdesk resource.

    Removes the TransportFreshdesk resource.

    :param id: TransportFreshdesk identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_freshdesk_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportFreshdesk resource.

    Retrieves a TransportFreshdesk resource.

    :param id: TransportFreshdesk identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_freshdesk_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportFreshdesk resource.

    Updates the TransportFreshdesk resource.

    :param id: TransportFreshdesk identifier
    :type id: str
    :param body: The updated TransportFreshdesk resource
    :type body: dict | bytes

    """
    body = TransportFreshdeskPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_freshdesk_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportFreshdesk resource.

    Replaces the TransportFreshdesk resource.

    :param id: TransportFreshdesk identifier
    :type id: str
    :param body: The updated TransportFreshdesk resource
    :type body: dict | bytes

    """
    body = TransportFreshdeskPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_freshdesk_post(request: web.Request, body) -> web.Response:
    """Creates a TransportFreshdesk resource.

    Creates a TransportFreshdesk resource.

    :param body: The new TransportFreshdesk resource
    :type body: dict | bytes

    """
    body = TransportFreshdeskPost.from_dict(body)
    return web.Response(status=200)
