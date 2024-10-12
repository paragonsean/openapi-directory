from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_clickatell_get_collection200_response import ApiTransportClickatellGetCollection200Response
from openapi_server.models.transport_clickatell_get import TransportClickatellGet
from openapi_server.models.transport_clickatell_jsonld_get import TransportClickatellJsonldGet
from openapi_server.models.transport_clickatell_jsonld_post import TransportClickatellJsonldPost
from openapi_server.models.transport_clickatell_jsonld_put import TransportClickatellJsonldPut
from openapi_server.models.transport_clickatell_patch import TransportClickatellPatch
from openapi_server.models.transport_clickatell_post import TransportClickatellPost
from openapi_server.models.transport_clickatell_put import TransportClickatellPut
from openapi_server import util


async def api_transport_clickatell_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportClickatell resources.

    Retrieves the collection of TransportClickatell resources.

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


async def api_transport_clickatell_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportClickatell resource.

    Removes the TransportClickatell resource.

    :param id: TransportClickatell identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_clickatell_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportClickatell resource.

    Retrieves a TransportClickatell resource.

    :param id: TransportClickatell identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_clickatell_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportClickatell resource.

    Updates the TransportClickatell resource.

    :param id: TransportClickatell identifier
    :type id: str
    :param body: The updated TransportClickatell resource
    :type body: dict | bytes

    """
    body = TransportClickatellPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_clickatell_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportClickatell resource.

    Replaces the TransportClickatell resource.

    :param id: TransportClickatell identifier
    :type id: str
    :param body: The updated TransportClickatell resource
    :type body: dict | bytes

    """
    body = TransportClickatellPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_clickatell_post(request: web.Request, body) -> web.Response:
    """Creates a TransportClickatell resource.

    Creates a TransportClickatell resource.

    :param body: The new TransportClickatell resource
    :type body: dict | bytes

    """
    body = TransportClickatellPost.from_dict(body)
    return web.Response(status=200)
