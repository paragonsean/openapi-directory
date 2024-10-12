from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_monitor_status_log_get_collection200_response import ApiMonitorStatusLogGetCollection200Response
from openapi_server.models.monitor_status_log_get import MonitorStatusLogGet
from openapi_server.models.monitor_status_log_jsonld_get import MonitorStatusLogJsonldGet
from openapi_server import util


async def api_monitor_status_log_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, monitor=None, monitor2=None, monitor_status_code=None, monitor_status_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of MonitorStatusLog resources.

    Retrieves the collection of MonitorStatusLog resources.

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
    :param monitor_status_code: 
    :type monitor_status_code: str
    :param monitor_status_code2: 
    :type monitor_status_code2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_monitor_status_log_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a MonitorStatusLog resource.

    Retrieves a MonitorStatusLog resource.

    :param id: MonitorStatusLog identifier
    :type id: str

    """
    return web.Response(status=200)
