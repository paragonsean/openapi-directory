from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_pager_duty_get_collection200_response import ApiTransportPagerDutyGetCollection200Response
from openapi_server.models.transport_pager_duty_get import TransportPagerDutyGet
from openapi_server.models.transport_pager_duty_jsonld_get import TransportPagerDutyJsonldGet
from openapi_server.models.transport_pager_duty_jsonld_post import TransportPagerDutyJsonldPost
from openapi_server.models.transport_pager_duty_jsonld_put import TransportPagerDutyJsonldPut
from openapi_server.models.transport_pager_duty_patch import TransportPagerDutyPatch
from openapi_server.models.transport_pager_duty_post import TransportPagerDutyPost
from openapi_server.models.transport_pager_duty_put import TransportPagerDutyPut
from openapi_server import util


async def api_transport_pager_duty_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportPagerDuty resources.

    Retrieves the collection of TransportPagerDuty resources.

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


async def api_transport_pager_duty_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportPagerDuty resource.

    Removes the TransportPagerDuty resource.

    :param id: TransportPagerDuty identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pager_duty_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportPagerDuty resource.

    Retrieves a TransportPagerDuty resource.

    :param id: TransportPagerDuty identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_pager_duty_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportPagerDuty resource.

    Updates the TransportPagerDuty resource.

    :param id: TransportPagerDuty identifier
    :type id: str
    :param body: The updated TransportPagerDuty resource
    :type body: dict | bytes

    """
    body = TransportPagerDutyPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_pager_duty_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportPagerDuty resource.

    Replaces the TransportPagerDuty resource.

    :param id: TransportPagerDuty identifier
    :type id: str
    :param body: The updated TransportPagerDuty resource
    :type body: dict | bytes

    """
    body = TransportPagerDutyPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_pager_duty_post(request: web.Request, body) -> web.Response:
    """Creates a TransportPagerDuty resource.

    Creates a TransportPagerDuty resource.

    :param body: The new TransportPagerDuty resource
    :type body: dict | bytes

    """
    body = TransportPagerDutyPost.from_dict(body)
    return web.Response(status=200)
