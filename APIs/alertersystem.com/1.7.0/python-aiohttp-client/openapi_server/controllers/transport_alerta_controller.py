from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_alerta_get_collection200_response import ApiTransportAlertaGetCollection200Response
from openapi_server.models.transport_alerta_get import TransportAlertaGet
from openapi_server.models.transport_alerta_jsonld_get import TransportAlertaJsonldGet
from openapi_server.models.transport_alerta_jsonld_post import TransportAlertaJsonldPost
from openapi_server.models.transport_alerta_jsonld_put import TransportAlertaJsonldPut
from openapi_server.models.transport_alerta_patch import TransportAlertaPatch
from openapi_server.models.transport_alerta_post import TransportAlertaPost
from openapi_server.models.transport_alerta_put import TransportAlertaPut
from openapi_server import util


async def api_transport_alerta_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportAlerta resources.

    Retrieves the collection of TransportAlerta resources.

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


async def api_transport_alerta_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportAlerta resource.

    Removes the TransportAlerta resource.

    :param id: TransportAlerta identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_alerta_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportAlerta resource.

    Retrieves a TransportAlerta resource.

    :param id: TransportAlerta identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_alerta_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportAlerta resource.

    Updates the TransportAlerta resource.

    :param id: TransportAlerta identifier
    :type id: str
    :param body: The updated TransportAlerta resource
    :type body: dict | bytes

    """
    body = TransportAlertaPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_alerta_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportAlerta resource.

    Replaces the TransportAlerta resource.

    :param id: TransportAlerta identifier
    :type id: str
    :param body: The updated TransportAlerta resource
    :type body: dict | bytes

    """
    body = TransportAlertaPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_alerta_post(request: web.Request, body) -> web.Response:
    """Creates a TransportAlerta resource.

    Creates a TransportAlerta resource.

    :param body: The new TransportAlerta resource
    :type body: dict | bytes

    """
    body = TransportAlertaPost.from_dict(body)
    return web.Response(status=200)
