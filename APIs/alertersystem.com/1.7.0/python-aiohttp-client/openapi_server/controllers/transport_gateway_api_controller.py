from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_gateway_api_get_collection200_response import ApiTransportGatewayApiGetCollection200Response
from openapi_server.models.transport_gateway_api_get import TransportGatewayApiGet
from openapi_server.models.transport_gateway_api_jsonld_get import TransportGatewayApiJsonldGet
from openapi_server.models.transport_gateway_api_jsonld_post import TransportGatewayApiJsonldPost
from openapi_server.models.transport_gateway_api_jsonld_put import TransportGatewayApiJsonldPut
from openapi_server.models.transport_gateway_api_patch import TransportGatewayApiPatch
from openapi_server.models.transport_gateway_api_post import TransportGatewayApiPost
from openapi_server.models.transport_gateway_api_put import TransportGatewayApiPut
from openapi_server import util


async def api_transport_gateway_api_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportGatewayApi resources.

    Retrieves the collection of TransportGatewayApi resources.

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


async def api_transport_gateway_api_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportGatewayApi resource.

    Removes the TransportGatewayApi resource.

    :param id: TransportGatewayApi identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_gateway_api_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportGatewayApi resource.

    Retrieves a TransportGatewayApi resource.

    :param id: TransportGatewayApi identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_gateway_api_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportGatewayApi resource.

    Updates the TransportGatewayApi resource.

    :param id: TransportGatewayApi identifier
    :type id: str
    :param body: The updated TransportGatewayApi resource
    :type body: dict | bytes

    """
    body = TransportGatewayApiPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_gateway_api_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportGatewayApi resource.

    Replaces the TransportGatewayApi resource.

    :param id: TransportGatewayApi identifier
    :type id: str
    :param body: The updated TransportGatewayApi resource
    :type body: dict | bytes

    """
    body = TransportGatewayApiPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_gateway_api_post(request: web.Request, body) -> web.Response:
    """Creates a TransportGatewayApi resource.

    Creates a TransportGatewayApi resource.

    :param body: The new TransportGatewayApi resource
    :type body: dict | bytes

    """
    body = TransportGatewayApiPost.from_dict(body)
    return web.Response(status=200)
