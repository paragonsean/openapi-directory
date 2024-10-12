from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_zendesk_get_collection200_response import ApiTransportZendeskGetCollection200Response
from openapi_server.models.transport_zendesk_get import TransportZendeskGet
from openapi_server.models.transport_zendesk_jsonld_get import TransportZendeskJsonldGet
from openapi_server.models.transport_zendesk_jsonld_post import TransportZendeskJsonldPost
from openapi_server.models.transport_zendesk_jsonld_put import TransportZendeskJsonldPut
from openapi_server.models.transport_zendesk_patch import TransportZendeskPatch
from openapi_server.models.transport_zendesk_post import TransportZendeskPost
from openapi_server.models.transport_zendesk_put import TransportZendeskPut
from openapi_server import util


async def api_transport_zendesk_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportZendesk resources.

    Retrieves the collection of TransportZendesk resources.

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


async def api_transport_zendesk_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportZendesk resource.

    Removes the TransportZendesk resource.

    :param id: TransportZendesk identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_zendesk_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportZendesk resource.

    Retrieves a TransportZendesk resource.

    :param id: TransportZendesk identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_zendesk_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportZendesk resource.

    Updates the TransportZendesk resource.

    :param id: TransportZendesk identifier
    :type id: str
    :param body: The updated TransportZendesk resource
    :type body: dict | bytes

    """
    body = TransportZendeskPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_zendesk_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportZendesk resource.

    Replaces the TransportZendesk resource.

    :param id: TransportZendesk identifier
    :type id: str
    :param body: The updated TransportZendesk resource
    :type body: dict | bytes

    """
    body = TransportZendeskPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_zendesk_post(request: web.Request, body) -> web.Response:
    """Creates a TransportZendesk resource.

    Creates a TransportZendesk resource.

    :param body: The new TransportZendesk resource
    :type body: dict | bytes

    """
    body = TransportZendeskPost.from_dict(body)
    return web.Response(status=200)
