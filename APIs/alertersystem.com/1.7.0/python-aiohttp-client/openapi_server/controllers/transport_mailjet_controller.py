from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_mailjet_get_collection200_response import ApiTransportMailjetGetCollection200Response
from openapi_server.models.transport_mailjet_get import TransportMailjetGet
from openapi_server.models.transport_mailjet_jsonld_get import TransportMailjetJsonldGet
from openapi_server.models.transport_mailjet_jsonld_post import TransportMailjetJsonldPost
from openapi_server.models.transport_mailjet_jsonld_put import TransportMailjetJsonldPut
from openapi_server.models.transport_mailjet_patch import TransportMailjetPatch
from openapi_server.models.transport_mailjet_post import TransportMailjetPost
from openapi_server.models.transport_mailjet_put import TransportMailjetPut
from openapi_server import util


async def api_transport_mailjet_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMailjet resources.

    Retrieves the collection of TransportMailjet resources.

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


async def api_transport_mailjet_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMailjet resource.

    Removes the TransportMailjet resource.

    :param id: TransportMailjet identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mailjet_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMailjet resource.

    Retrieves a TransportMailjet resource.

    :param id: TransportMailjet identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_mailjet_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMailjet resource.

    Updates the TransportMailjet resource.

    :param id: TransportMailjet identifier
    :type id: str
    :param body: The updated TransportMailjet resource
    :type body: dict | bytes

    """
    body = TransportMailjetPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_mailjet_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMailjet resource.

    Replaces the TransportMailjet resource.

    :param id: TransportMailjet identifier
    :type id: str
    :param body: The updated TransportMailjet resource
    :type body: dict | bytes

    """
    body = TransportMailjetPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_mailjet_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMailjet resource.

    Creates a TransportMailjet resource.

    :param body: The new TransportMailjet resource
    :type body: dict | bytes

    """
    body = TransportMailjetPost.from_dict(body)
    return web.Response(status=200)
