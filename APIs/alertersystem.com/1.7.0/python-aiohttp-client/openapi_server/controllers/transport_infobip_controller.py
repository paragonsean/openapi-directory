from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_infobip_get_collection200_response import ApiTransportInfobipGetCollection200Response
from openapi_server.models.transport_infobip_get import TransportInfobipGet
from openapi_server.models.transport_infobip_jsonld_get import TransportInfobipJsonldGet
from openapi_server.models.transport_infobip_jsonld_post import TransportInfobipJsonldPost
from openapi_server.models.transport_infobip_jsonld_put import TransportInfobipJsonldPut
from openapi_server.models.transport_infobip_patch import TransportInfobipPatch
from openapi_server.models.transport_infobip_post import TransportInfobipPost
from openapi_server.models.transport_infobip_put import TransportInfobipPut
from openapi_server import util


async def api_transport_infobip_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportInfobip resources.

    Retrieves the collection of TransportInfobip resources.

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


async def api_transport_infobip_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportInfobip resource.

    Removes the TransportInfobip resource.

    :param id: TransportInfobip identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_infobip_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportInfobip resource.

    Retrieves a TransportInfobip resource.

    :param id: TransportInfobip identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_infobip_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportInfobip resource.

    Updates the TransportInfobip resource.

    :param id: TransportInfobip identifier
    :type id: str
    :param body: The updated TransportInfobip resource
    :type body: dict | bytes

    """
    body = TransportInfobipPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_infobip_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportInfobip resource.

    Replaces the TransportInfobip resource.

    :param id: TransportInfobip identifier
    :type id: str
    :param body: The updated TransportInfobip resource
    :type body: dict | bytes

    """
    body = TransportInfobipPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_infobip_post(request: web.Request, body) -> web.Response:
    """Creates a TransportInfobip resource.

    Creates a TransportInfobip resource.

    :param body: The new TransportInfobip resource
    :type body: dict | bytes

    """
    body = TransportInfobipPost.from_dict(body)
    return web.Response(status=200)
