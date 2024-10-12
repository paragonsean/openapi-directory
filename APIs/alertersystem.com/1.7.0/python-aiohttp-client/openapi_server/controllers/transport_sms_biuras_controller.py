from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_sms_biuras_get_collection200_response import ApiTransportSmsBiurasGetCollection200Response
from openapi_server.models.transport_sms_biuras_get import TransportSmsBiurasGet
from openapi_server.models.transport_sms_biuras_jsonld_get import TransportSmsBiurasJsonldGet
from openapi_server.models.transport_sms_biuras_jsonld_post import TransportSmsBiurasJsonldPost
from openapi_server.models.transport_sms_biuras_jsonld_put import TransportSmsBiurasJsonldPut
from openapi_server.models.transport_sms_biuras_patch import TransportSmsBiurasPatch
from openapi_server.models.transport_sms_biuras_post import TransportSmsBiurasPost
from openapi_server.models.transport_sms_biuras_put import TransportSmsBiurasPut
from openapi_server import util


async def api_transport_sms_biuras_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportSmsBiuras resources.

    Retrieves the collection of TransportSmsBiuras resources.

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


async def api_transport_sms_biuras_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportSmsBiuras resource.

    Removes the TransportSmsBiuras resource.

    :param id: TransportSmsBiuras identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sms_biuras_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportSmsBiuras resource.

    Retrieves a TransportSmsBiuras resource.

    :param id: TransportSmsBiuras identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_sms_biuras_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportSmsBiuras resource.

    Updates the TransportSmsBiuras resource.

    :param id: TransportSmsBiuras identifier
    :type id: str
    :param body: The updated TransportSmsBiuras resource
    :type body: dict | bytes

    """
    body = TransportSmsBiurasPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_sms_biuras_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportSmsBiuras resource.

    Replaces the TransportSmsBiuras resource.

    :param id: TransportSmsBiuras identifier
    :type id: str
    :param body: The updated TransportSmsBiuras resource
    :type body: dict | bytes

    """
    body = TransportSmsBiurasPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_sms_biuras_post(request: web.Request, body) -> web.Response:
    """Creates a TransportSmsBiuras resource.

    Creates a TransportSmsBiuras resource.

    :param body: The new TransportSmsBiuras resource
    :type body: dict | bytes

    """
    body = TransportSmsBiurasPost.from_dict(body)
    return web.Response(status=200)
