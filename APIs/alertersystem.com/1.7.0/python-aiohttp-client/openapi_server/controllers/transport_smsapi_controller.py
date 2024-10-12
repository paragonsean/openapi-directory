from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_smsapi_get_collection200_response import ApiTransportSmsapiGetCollection200Response
from openapi_server.models.transport_smsapi_get import TransportSmsapiGet
from openapi_server.models.transport_smsapi_jsonld_get import TransportSmsapiJsonldGet
from openapi_server.models.transport_smsapi_jsonld_post import TransportSmsapiJsonldPost
from openapi_server.models.transport_smsapi_jsonld_put import TransportSmsapiJsonldPut
from openapi_server.models.transport_smsapi_patch import TransportSmsapiPatch
from openapi_server.models.transport_smsapi_post import TransportSmsapiPost
from openapi_server.models.transport_smsapi_put import TransportSmsapiPut
from openapi_server import util


async def api_transport_smsapi_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSmsapi resources.

    Retrieves the collection of TransportSmsapi resources.

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


async def api_transport_smsapi_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSmsapi resource.

    Removes the TransportSmsapi resource.

    :param id: TransportSmsapi identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_smsapi_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSmsapi resource.

    Retrieves a TransportSmsapi resource.

    :param id: TransportSmsapi identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_smsapi_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSmsapi resource.

    Updates the TransportSmsapi resource.

    :param id: TransportSmsapi identifier
    :type id: str
    :param body: The updated TransportSmsapi resource
    :type body: dict | bytes

    """
    body = TransportSmsapiPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_smsapi_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSmsapi resource.

    Replaces the TransportSmsapi resource.

    :param id: TransportSmsapi identifier
    :type id: str
    :param body: The updated TransportSmsapi resource
    :type body: dict | bytes

    """
    body = TransportSmsapiPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_smsapi_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSmsapi resource.

    Creates a TransportSmsapi resource.

    :param body: The new TransportSmsapi resource
    :type body: dict | bytes

    """
    body = TransportSmsapiPost.from_dict(body)
    return web.Response(status=200)
