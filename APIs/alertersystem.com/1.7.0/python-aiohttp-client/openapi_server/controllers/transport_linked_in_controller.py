from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_linked_in_get_collection200_response import ApiTransportLinkedInGetCollection200Response
from openapi_server.models.transport_linked_in_get import TransportLinkedInGet
from openapi_server.models.transport_linked_in_jsonld_get import TransportLinkedInJsonldGet
from openapi_server.models.transport_linked_in_jsonld_post import TransportLinkedInJsonldPost
from openapi_server.models.transport_linked_in_jsonld_put import TransportLinkedInJsonldPut
from openapi_server.models.transport_linked_in_patch import TransportLinkedInPatch
from openapi_server.models.transport_linked_in_post import TransportLinkedInPost
from openapi_server.models.transport_linked_in_put import TransportLinkedInPut
from openapi_server import util


async def api_transport_linked_in_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportLinkedIn resources.

    Retrieves the collection of TransportLinkedIn resources.

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


async def api_transport_linked_in_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportLinkedIn resource.

    Removes the TransportLinkedIn resource.

    :param id: TransportLinkedIn identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_linked_in_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportLinkedIn resource.

    Retrieves a TransportLinkedIn resource.

    :param id: TransportLinkedIn identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_linked_in_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportLinkedIn resource.

    Updates the TransportLinkedIn resource.

    :param id: TransportLinkedIn identifier
    :type id: str
    :param body: The updated TransportLinkedIn resource
    :type body: dict | bytes

    """
    body = TransportLinkedInPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_linked_in_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportLinkedIn resource.

    Replaces the TransportLinkedIn resource.

    :param id: TransportLinkedIn identifier
    :type id: str
    :param body: The updated TransportLinkedIn resource
    :type body: dict | bytes

    """
    body = TransportLinkedInPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_linked_in_post(request: web.Request, body) -> web.Response:
    """Creates a TransportLinkedIn resource.

    Creates a TransportLinkedIn resource.

    :param body: The new TransportLinkedIn resource
    :type body: dict | bytes

    """
    body = TransportLinkedInPost.from_dict(body)
    return web.Response(status=200)
