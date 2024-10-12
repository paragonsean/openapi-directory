from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_service_get import AlertServiceGet
from openapi_server.models.alert_service_jsonld_get import AlertServiceJsonldGet
from openapi_server.models.alert_service_jsonld_post import AlertServiceJsonldPost
from openapi_server.models.alert_service_jsonld_put import AlertServiceJsonldPut
from openapi_server.models.alert_service_patch import AlertServicePatch
from openapi_server.models.alert_service_post import AlertServicePost
from openapi_server.models.alert_service_put import AlertServicePut
from openapi_server.models.api_alert_service_get_collection200_response import ApiAlertServiceGetCollection200Response
from openapi_server import util


async def api_alert_service_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of AlertService resources.

    Retrieves the collection of AlertService resources.

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


async def api_alert_service_id_delete(request: web.Request, id) -> web.Response:
    """Removes the AlertService resource.

    Removes the AlertService resource.

    :param id: AlertService identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_alert_service_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a AlertService resource.

    Retrieves a AlertService resource.

    :param id: AlertService identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_alert_service_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the AlertService resource.

    Updates the AlertService resource.

    :param id: AlertService identifier
    :type id: str
    :param body: The updated AlertService resource
    :type body: dict | bytes

    """
    body = AlertServicePatch.from_dict(body)
    return web.Response(status=200)


async def api_alert_service_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the AlertService resource.

    Replaces the AlertService resource.

    :param id: AlertService identifier
    :type id: str
    :param body: The updated AlertService resource
    :type body: dict | bytes

    """
    body = AlertServicePut.from_dict(body)
    return web.Response(status=200)


async def api_alert_service_post(request: web.Request, body) -> web.Response:
    """Creates a AlertService resource.

    Creates a AlertService resource.

    :param body: The new AlertService resource
    :type body: dict | bytes

    """
    body = AlertServicePost.from_dict(body)
    return web.Response(status=200)
