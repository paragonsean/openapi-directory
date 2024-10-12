from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.position import Position
from openapi_server.models.report_stops import ReportStops
from openapi_server.models.report_summary import ReportSummary
from openapi_server.models.report_trips import ReportTrips
from openapi_server import util


async def reports_events_get(request: web.Request, _from, to, device_id=None, group_id=None, type=None) -> web.Response:
    """Fetch a list of Events within the time period for the Devices or Groups

    At least one _deviceId_ or one _groupId_ must be passed

    :param _from: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type _from: str
    :param to: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type to: str
    :param device_id: 
    :type device_id: List[int]
    :param group_id: 
    :type group_id: List[int]
    :param type: % can be used to return events of all types
    :type type: List[str]

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def reports_route_get(request: web.Request, _from, to, device_id=None, group_id=None) -> web.Response:
    """Fetch a list of Positions within the time period for the Devices or Groups

    At least one _deviceId_ or one _groupId_ must be passed

    :param _from: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type _from: str
    :param to: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type to: str
    :param device_id: 
    :type device_id: List[int]
    :param group_id: 
    :type group_id: List[int]

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def reports_stops_get(request: web.Request, _from, to, device_id=None, group_id=None) -> web.Response:
    """Fetch a list of ReportStops within the time period for the Devices or Groups

    At least one _deviceId_ or one _groupId_ must be passed

    :param _from: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type _from: str
    :param to: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type to: str
    :param device_id: 
    :type device_id: List[int]
    :param group_id: 
    :type group_id: List[int]

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def reports_summary_get(request: web.Request, _from, to, device_id=None, group_id=None) -> web.Response:
    """Fetch a list of ReportSummary within the time period for the Devices or Groups

    At least one _deviceId_ or one _groupId_ must be passed

    :param _from: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type _from: str
    :param to: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type to: str
    :param device_id: 
    :type device_id: List[int]
    :param group_id: 
    :type group_id: List[int]

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def reports_trips_get(request: web.Request, _from, to, device_id=None, group_id=None) -> web.Response:
    """Fetch a list of ReportTrips within the time period for the Devices or Groups

    At least one _deviceId_ or one _groupId_ must be passed

    :param _from: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type _from: str
    :param to: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type to: str
    :param device_id: 
    :type device_id: List[int]
    :param group_id: 
    :type group_id: List[int]

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
