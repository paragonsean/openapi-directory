from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_vonage_get_collection200_response import ApiTransportVonageGetCollection200Response
from openapi_server.models.transport_vonage_get import TransportVonageGet
from openapi_server.models.transport_vonage_jsonld_get import TransportVonageJsonldGet
from openapi_server.models.transport_vonage_jsonld_post import TransportVonageJsonldPost
from openapi_server.models.transport_vonage_jsonld_put import TransportVonageJsonldPut
from openapi_server.models.transport_vonage_patch import TransportVonagePatch
from openapi_server.models.transport_vonage_post import TransportVonagePost
from openapi_server.models.transport_vonage_put import TransportVonagePut
from openapi_server import util


async def api_transport_vonage_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportVonage resources.

    Retrieves the collection of TransportVonage resources.

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


async def api_transport_vonage_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportVonage resource.

    Removes the TransportVonage resource.

    :param id: TransportVonage identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_vonage_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportVonage resource.

    Retrieves a TransportVonage resource.

    :param id: TransportVonage identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_vonage_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportVonage resource.

    Updates the TransportVonage resource.

    :param id: TransportVonage identifier
    :type id: str
    :param body: The updated TransportVonage resource
    :type body: dict | bytes

    """
    body = TransportVonagePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_vonage_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportVonage resource.

    Replaces the TransportVonage resource.

    :param id: TransportVonage identifier
    :type id: str
    :param body: The updated TransportVonage resource
    :type body: dict | bytes

    """
    body = TransportVonagePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_vonage_post(request: web.Request, body) -> web.Response:
    """Creates a TransportVonage resource.

    Creates a TransportVonage resource.

    :param body: The new TransportVonage resource
    :type body: dict | bytes

    """
    body = TransportVonagePost.from_dict(body)
    return web.Response(status=200)
