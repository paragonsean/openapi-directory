from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_opsgenie_get_collection200_response import ApiTransportOpsgenieGetCollection200Response
from openapi_server.models.transport_opsgenie_get import TransportOpsgenieGet
from openapi_server.models.transport_opsgenie_jsonld_get import TransportOpsgenieJsonldGet
from openapi_server.models.transport_opsgenie_jsonld_post import TransportOpsgenieJsonldPost
from openapi_server.models.transport_opsgenie_jsonld_put import TransportOpsgenieJsonldPut
from openapi_server.models.transport_opsgenie_patch import TransportOpsgeniePatch
from openapi_server.models.transport_opsgenie_post import TransportOpsgeniePost
from openapi_server.models.transport_opsgenie_put import TransportOpsgeniePut
from openapi_server import util


async def api_transport_opsgenie_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportOpsgenie resources.

    Retrieves the collection of TransportOpsgenie resources.

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


async def api_transport_opsgenie_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportOpsgenie resource.

    Removes the TransportOpsgenie resource.

    :param id: TransportOpsgenie identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_opsgenie_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportOpsgenie resource.

    Retrieves a TransportOpsgenie resource.

    :param id: TransportOpsgenie identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_opsgenie_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportOpsgenie resource.

    Updates the TransportOpsgenie resource.

    :param id: TransportOpsgenie identifier
    :type id: str
    :param body: The updated TransportOpsgenie resource
    :type body: dict | bytes

    """
    body = TransportOpsgeniePatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_opsgenie_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportOpsgenie resource.

    Replaces the TransportOpsgenie resource.

    :param id: TransportOpsgenie identifier
    :type id: str
    :param body: The updated TransportOpsgenie resource
    :type body: dict | bytes

    """
    body = TransportOpsgeniePut.from_dict(body)
    return web.Response(status=200)


async def api_transport_opsgenie_post(request: web.Request, body) -> web.Response:
    """Creates a TransportOpsgenie resource.

    Creates a TransportOpsgenie resource.

    :param body: The new TransportOpsgenie resource
    :type body: dict | bytes

    """
    body = TransportOpsgeniePost.from_dict(body)
    return web.Response(status=200)
