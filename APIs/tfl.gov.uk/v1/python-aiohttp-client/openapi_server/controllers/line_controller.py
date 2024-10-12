from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_disruption import TflApiPresentationEntitiesDisruption
from openapi_server.models.tfl_api_presentation_entities_line import TflApiPresentationEntitiesLine
from openapi_server.models.tfl_api_presentation_entities_mode import TflApiPresentationEntitiesMode
from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction
from openapi_server.models.tfl_api_presentation_entities_route_search_response import TflApiPresentationEntitiesRouteSearchResponse
from openapi_server.models.tfl_api_presentation_entities_route_sequence import TflApiPresentationEntitiesRouteSequence
from openapi_server.models.tfl_api_presentation_entities_status_severity import TflApiPresentationEntitiesStatusSeverity
from openapi_server.models.tfl_api_presentation_entities_stop_point import TflApiPresentationEntitiesStopPoint
from openapi_server.models.tfl_api_presentation_entities_timetable_response import TflApiPresentationEntitiesTimetableResponse
from openapi_server import util


async def line_arrivals(request: web.Request, ids, stop_point_id, direction=None, destination_station_id=None) -> web.Response:
    """Get the list of arrival predictions for given line ids based at the given stop

    

    :param ids: A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    :type ids: List[str]
    :param stop_point_id: Optional. Id of stop to get arrival predictions for (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type stop_point_id: str
    :param direction: Optional. The direction of travel. Can be inbound or outbound or all. If left blank, and destinationStopId is set, will default to all
    :type direction: str
    :param destination_station_id: Optional. Id of destination stop
    :type destination_station_id: str

    """
    return web.Response(status=200)


async def line_disruption(request: web.Request, ids) -> web.Response:
    """Get disruptions for the given line ids

    

    :param ids: A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    :type ids: List[str]

    """
    return web.Response(status=200)


async def line_disruption_by_mode(request: web.Request, modes) -> web.Response:
    """Get disruptions for all lines of the given modes.

    

    :param modes: A comma-separated list of modes e.g. tube,dlr
    :type modes: List[str]

    """
    return web.Response(status=200)


async def line_get(request: web.Request, ids) -> web.Response:
    """Gets lines that match the specified line ids.

    

    :param ids: A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    :type ids: List[str]

    """
    return web.Response(status=200)


async def line_get_by_mode(request: web.Request, modes) -> web.Response:
    """Gets lines that serve the given modes.

    

    :param modes: A comma-separated list of modes e.g. tube,dlr
    :type modes: List[str]

    """
    return web.Response(status=200)


async def line_line_routes_by_ids(request: web.Request, ids, service_types=None) -> web.Response:
    """Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route.

    

    :param ids: A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    :type ids: List[str]
    :param service_types: A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified
    :type service_types: List[str]

    """
    return web.Response(status=200)


async def line_meta_disruption_categories(request: web.Request, ) -> web.Response:
    """Gets a list of valid disruption categories

    


    """
    return web.Response(status=200)


async def line_meta_modes(request: web.Request, ) -> web.Response:
    """Gets a list of valid modes

    


    """
    return web.Response(status=200)


async def line_meta_service_types(request: web.Request, ) -> web.Response:
    """Gets a list of valid ServiceTypes to filter on

    


    """
    return web.Response(status=200)


async def line_meta_severity(request: web.Request, ) -> web.Response:
    """Gets a list of valid severity codes

    


    """
    return web.Response(status=200)


async def line_route(request: web.Request, service_types=None) -> web.Response:
    """Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.

    

    :param service_types: A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified
    :type service_types: List[str]

    """
    return web.Response(status=200)


async def line_route_by_mode(request: web.Request, modes, service_types=None) -> web.Response:
    """Gets all lines and their valid routes for given modes, including the name and id of the originating and terminating stops for each route

    

    :param modes: A comma-separated list of modes e.g. tube,dlr
    :type modes: List[str]
    :param service_types: A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified
    :type service_types: List[str]

    """
    return web.Response(status=200)


async def line_route_sequence(request: web.Request, id, direction, service_types=None, exclude_crowding=None) -> web.Response:
    """Gets all valid routes for given line id, including the sequence of stops on each route.

    

    :param id: A single line id e.g. victoria
    :type id: str
    :param direction: The direction of travel. Can be inbound or outbound.
    :type direction: str
    :param service_types: A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified
    :type service_types: List[str]
    :param exclude_crowding: That excludes crowding from line disruptions. Can be true or false.
    :type exclude_crowding: bool

    """
    return web.Response(status=200)


async def line_search(request: web.Request, query, modes=None, service_types=None) -> web.Response:
    """Search for lines or routes matching the query string

    

    :param query: Search term e.g victoria
    :type query: str
    :param modes: Optionally filter by the specified modes
    :type modes: List[str]
    :param service_types: A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified
    :type service_types: List[str]

    """
    return web.Response(status=200)


async def line_status(request: web.Request, ids, start_date, end_date, start_date2, end_date2, detail=None, date_range_start_date=None, date_range_end_date=None) -> web.Response:
    """Gets the line status for given line ids during the provided dates e.g Minor Delays

    

    :param ids: A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    :type ids: List[str]
    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str
    :param start_date2: Automatically added
    :type start_date2: str
    :param end_date2: Automatically added
    :type end_date2: str
    :param detail: Include details of the disruptions that are causing the line status including the affected stops and routes
    :type detail: bool
    :param date_range_start_date: 
    :type date_range_start_date: str
    :param date_range_end_date: 
    :type date_range_end_date: str

    """
    date_range_start_date = util.deserialize_datetime(date_range_start_date)
    date_range_end_date = util.deserialize_datetime(date_range_end_date)
    return web.Response(status=200)


async def line_status_by_ids(request: web.Request, ids, detail=None) -> web.Response:
    """Gets the line status of for given line ids e.g Minor Delays

    

    :param ids: A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    :type ids: List[str]
    :param detail: Include details of the disruptions that are causing the line status including the affected stops and routes
    :type detail: bool

    """
    return web.Response(status=200)


async def line_status_by_mode(request: web.Request, modes, detail=None, severity_level=None) -> web.Response:
    """Gets the line status of for all lines for the given modes

    

    :param modes: A comma-separated list of modes to filter by. e.g. tube,dlr
    :type modes: List[str]
    :param detail: Include details of the disruptions that are causing the line status including the affected stops and routes
    :type detail: bool
    :param severity_level: If specified, ensures that only those line status(es) are returned within the lines that have disruptions with the matching severity level.
    :type severity_level: str

    """
    return web.Response(status=200)


async def line_status_by_severity(request: web.Request, severity) -> web.Response:
    """Gets the line status for all lines with a given severity              A list of valid severity codes can be obtained from a call to Line/Meta/Severity

    

    :param severity: The level of severity (eg: a number from 0 to 14)
    :type severity: int

    """
    return web.Response(status=200)


async def line_stop_points(request: web.Request, id, tfl_operated_national_rail_stations_only=None) -> web.Response:
    """Gets a list of the stations that serve the given line id

    

    :param id: A single line id e.g. victoria
    :type id: str
    :param tfl_operated_national_rail_stations_only: If the national-rail line is requested, this flag will filter the national rail stations so that only those operated by TfL are returned
    :type tfl_operated_national_rail_stations_only: bool

    """
    return web.Response(status=200)


async def line_timetable(request: web.Request, from_stop_point_id, id) -> web.Response:
    """Gets the timetable for a specified station on the give line

    

    :param from_stop_point_id: The originating station&#39;s stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type from_stop_point_id: str
    :param id: A single line id e.g. victoria
    :type id: str

    """
    return web.Response(status=200)


async def line_timetable_to(request: web.Request, from_stop_point_id, id, to_stop_point_id) -> web.Response:
    """Gets the timetable for a specified station on the give line with specified destination

    

    :param from_stop_point_id: The originating station&#39;s stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type from_stop_point_id: str
    :param id: A single line id e.g. victoria
    :type id: str
    :param to_stop_point_id: The destination stations&#39;s Naptan code
    :type to_stop_point_id: str

    """
    return web.Response(status=200)
