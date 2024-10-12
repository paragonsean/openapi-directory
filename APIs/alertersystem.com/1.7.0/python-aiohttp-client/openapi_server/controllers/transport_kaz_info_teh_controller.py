from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_kaz_info_teh_get_collection200_response import ApiTransportKazInfoTehGetCollection200Response
from openapi_server.models.transport_kaz_info_teh_get import TransportKazInfoTehGet
from openapi_server.models.transport_kaz_info_teh_jsonld_get import TransportKazInfoTehJsonldGet
from openapi_server.models.transport_kaz_info_teh_jsonld_post import TransportKazInfoTehJsonldPost
from openapi_server.models.transport_kaz_info_teh_jsonld_put import TransportKazInfoTehJsonldPut
from openapi_server.models.transport_kaz_info_teh_patch import TransportKazInfoTehPatch
from openapi_server.models.transport_kaz_info_teh_post import TransportKazInfoTehPost
from openapi_server.models.transport_kaz_info_teh_put import TransportKazInfoTehPut
from openapi_server import util


async def api_transport_kaz_info_teh_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportKazInfoTeh resources.

    Retrieves the collection of TransportKazInfoTeh resources.

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


async def api_transport_kaz_info_teh_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportKazInfoTeh resource.

    Removes the TransportKazInfoTeh resource.

    :param id: TransportKazInfoTeh identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_kaz_info_teh_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportKazInfoTeh resource.

    Retrieves a TransportKazInfoTeh resource.

    :param id: TransportKazInfoTeh identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_kaz_info_teh_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportKazInfoTeh resource.

    Updates the TransportKazInfoTeh resource.

    :param id: TransportKazInfoTeh identifier
    :type id: str
    :param body: The updated TransportKazInfoTeh resource
    :type body: dict | bytes

    """
    body = TransportKazInfoTehPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_kaz_info_teh_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportKazInfoTeh resource.

    Replaces the TransportKazInfoTeh resource.

    :param id: TransportKazInfoTeh identifier
    :type id: str
    :param body: The updated TransportKazInfoTeh resource
    :type body: dict | bytes

    """
    body = TransportKazInfoTehPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_kaz_info_teh_post(request: web.Request, body) -> web.Response:
    """Creates a TransportKazInfoTeh resource.

    Creates a TransportKazInfoTeh resource.

    :param body: The new TransportKazInfoTeh resource
    :type body: dict | bytes

    """
    body = TransportKazInfoTehPost.from_dict(body)
    return web.Response(status=200)
