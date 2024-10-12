from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_zulip_get_collection200_response import ApiTransportZulipGetCollection200Response
from openapi_server.models.transport_zulip_get import TransportZulipGet
from openapi_server.models.transport_zulip_jsonld_get import TransportZulipJsonldGet
from openapi_server.models.transport_zulip_jsonld_post import TransportZulipJsonldPost
from openapi_server.models.transport_zulip_jsonld_put import TransportZulipJsonldPut
from openapi_server.models.transport_zulip_patch import TransportZulipPatch
from openapi_server.models.transport_zulip_post import TransportZulipPost
from openapi_server.models.transport_zulip_put import TransportZulipPut
from openapi_server import util


async def api_transport_zulip_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportZulip resources.

    Retrieves the collection of TransportZulip resources.

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


async def api_transport_zulip_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportZulip resource.

    Removes the TransportZulip resource.

    :param id: TransportZulip identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_zulip_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportZulip resource.

    Retrieves a TransportZulip resource.

    :param id: TransportZulip identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_zulip_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportZulip resource.

    Updates the TransportZulip resource.

    :param id: TransportZulip identifier
    :type id: str
    :param body: The updated TransportZulip resource
    :type body: dict | bytes

    """
    body = TransportZulipPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_zulip_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportZulip resource.

    Replaces the TransportZulip resource.

    :param id: TransportZulip identifier
    :type id: str
    :param body: The updated TransportZulip resource
    :type body: dict | bytes

    """
    body = TransportZulipPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_zulip_post(request: web.Request, body) -> web.Response:
    """Creates a TransportZulip resource.

    Creates a TransportZulip resource.

    :param body: The new TransportZulip resource
    :type body: dict | bytes

    """
    body = TransportZulipPost.from_dict(body)
    return web.Response(status=200)
