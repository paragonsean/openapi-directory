from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_forty_six_elks_get_collection200_response import ApiTransportFortySixElksGetCollection200Response
from openapi_server.models.transport_forty_six_elks_get import TransportFortySixElksGet
from openapi_server.models.transport_forty_six_elks_jsonld_get import TransportFortySixElksJsonldGet
from openapi_server.models.transport_forty_six_elks_jsonld_post import TransportFortySixElksJsonldPost
from openapi_server.models.transport_forty_six_elks_jsonld_put import TransportFortySixElksJsonldPut
from openapi_server.models.transport_forty_six_elks_patch import TransportFortySixElksPatch
from openapi_server.models.transport_forty_six_elks_post import TransportFortySixElksPost
from openapi_server.models.transport_forty_six_elks_put import TransportFortySixElksPut
from openapi_server import util


async def api_transport_forty_six_elks_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportFortySixElks resources.

    Retrieves the collection of TransportFortySixElks resources.

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


async def api_transport_forty_six_elks_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportFortySixElks resource.

    Removes the TransportFortySixElks resource.

    :param id: TransportFortySixElks identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_forty_six_elks_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportFortySixElks resource.

    Retrieves a TransportFortySixElks resource.

    :param id: TransportFortySixElks identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_forty_six_elks_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportFortySixElks resource.

    Updates the TransportFortySixElks resource.

    :param id: TransportFortySixElks identifier
    :type id: str
    :param body: The updated TransportFortySixElks resource
    :type body: dict | bytes

    """
    body = TransportFortySixElksPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_forty_six_elks_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportFortySixElks resource.

    Replaces the TransportFortySixElks resource.

    :param id: TransportFortySixElks identifier
    :type id: str
    :param body: The updated TransportFortySixElks resource
    :type body: dict | bytes

    """
    body = TransportFortySixElksPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_forty_six_elks_post(request: web.Request, body) -> web.Response:
    """Creates a TransportFortySixElks resource.

    Creates a TransportFortySixElks resource.

    :param body: The new TransportFortySixElks resource
    :type body: dict | bytes

    """
    body = TransportFortySixElksPost.from_dict(body)
    return web.Response(status=200)
