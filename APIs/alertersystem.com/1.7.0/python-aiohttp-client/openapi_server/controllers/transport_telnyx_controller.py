from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_telnyx_get_collection200_response import ApiTransportTelnyxGetCollection200Response
from openapi_server.models.transport_telnyx_get import TransportTelnyxGet
from openapi_server.models.transport_telnyx_jsonld_get import TransportTelnyxJsonldGet
from openapi_server.models.transport_telnyx_jsonld_post import TransportTelnyxJsonldPost
from openapi_server.models.transport_telnyx_jsonld_put import TransportTelnyxJsonldPut
from openapi_server.models.transport_telnyx_patch import TransportTelnyxPatch
from openapi_server.models.transport_telnyx_post import TransportTelnyxPost
from openapi_server.models.transport_telnyx_put import TransportTelnyxPut
from openapi_server import util


async def api_transport_telnyx_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportTelnyx resources.

    Retrieves the collection of TransportTelnyx resources.

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


async def api_transport_telnyx_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportTelnyx resource.

    Removes the TransportTelnyx resource.

    :param id: TransportTelnyx identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_telnyx_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportTelnyx resource.

    Retrieves a TransportTelnyx resource.

    :param id: TransportTelnyx identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_telnyx_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportTelnyx resource.

    Updates the TransportTelnyx resource.

    :param id: TransportTelnyx identifier
    :type id: str
    :param body: The updated TransportTelnyx resource
    :type body: dict | bytes

    """
    body = TransportTelnyxPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_telnyx_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportTelnyx resource.

    Replaces the TransportTelnyx resource.

    :param id: TransportTelnyx identifier
    :type id: str
    :param body: The updated TransportTelnyx resource
    :type body: dict | bytes

    """
    body = TransportTelnyxPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_telnyx_post(request: web.Request, body) -> web.Response:
    """Creates a TransportTelnyx resource.

    Creates a TransportTelnyx resource.

    :param body: The new TransportTelnyx resource
    :type body: dict | bytes

    """
    body = TransportTelnyxPost.from_dict(body)
    return web.Response(status=200)
