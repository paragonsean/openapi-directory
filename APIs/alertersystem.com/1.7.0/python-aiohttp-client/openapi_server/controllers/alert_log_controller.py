from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_log_get import AlertLogGet
from openapi_server.models.alert_log_jsonld_get import AlertLogJsonldGet
from openapi_server.models.api_alert_log_get_collection200_response import ApiAlertLogGetCollection200Response
from openapi_server import util


async def api_alert_log_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, monitor=None, monitor2=None, alert_service=None, alert_service2=None, alert_log_status_code=None, alert_log_status_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of AlertLog resources.

    Retrieves the collection of AlertLog resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param monitor: 
    :type monitor: str
    :param monitor2: 
    :type monitor2: List[str]
    :param alert_service: 
    :type alert_service: str
    :param alert_service2: 
    :type alert_service2: List[str]
    :param alert_log_status_code: 
    :type alert_log_status_code: str
    :param alert_log_status_code2: 
    :type alert_log_status_code2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_alert_log_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a AlertLog resource.

    Retrieves a AlertLog resource.

    :param id: AlertLog identifier
    :type id: str

    """
    return web.Response(status=200)
