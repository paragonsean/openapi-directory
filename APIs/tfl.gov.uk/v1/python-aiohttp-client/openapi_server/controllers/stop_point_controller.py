from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_arrival_departure import TflApiPresentationEntitiesArrivalDeparture
from openapi_server.models.tfl_api_presentation_entities_disrupted_point import TflApiPresentationEntitiesDisruptedPoint
from openapi_server.models.tfl_api_presentation_entities_line_service_type import TflApiPresentationEntitiesLineServiceType
from openapi_server.models.tfl_api_presentation_entities_mode import TflApiPresentationEntitiesMode
from openapi_server.models.tfl_api_presentation_entities_place import TflApiPresentationEntitiesPlace
from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction
from openapi_server.models.tfl_api_presentation_entities_search_response import TflApiPresentationEntitiesSearchResponse
from openapi_server.models.tfl_api_presentation_entities_stop_point import TflApiPresentationEntitiesStopPoint
from openapi_server.models.tfl_api_presentation_entities_stop_point_category import TflApiPresentationEntitiesStopPointCategory
from openapi_server.models.tfl_api_presentation_entities_stop_point_route_section import TflApiPresentationEntitiesStopPointRouteSection
from openapi_server.models.tfl_api_presentation_entities_stop_points_response import TflApiPresentationEntitiesStopPointsResponse
from openapi_server import util


async def stop_point_arrival_departures(request: web.Request, id, line_ids) -> web.Response:
    """Gets the list of arrival and departure predictions for the given stop point id (overground, Elizabeth line and thameslink only)

    

    :param id: A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type id: str
    :param line_ids: A comma-separated list of line ids e.g. elizabeth, london-overground, thameslink
    :type line_ids: List[str]

    """
    return web.Response(status=200)


async def stop_point_arrivals(request: web.Request, id) -> web.Response:
    """Gets the list of arrival predictions for the given stop point id

    

    :param id: A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type id: str

    """
    return web.Response(status=200)


async def stop_point_crowding(request: web.Request, id, line, direction) -> web.Response:
    """Gets all the Crowding data (static) for the StopPointId, plus crowding data for a given line and optionally a particular direction.

    

    :param id: The Naptan id of the stop
    :type id: str
    :param line: A particular line e.g. victoria, circle, northern etc.
    :type line: str
    :param direction: The direction of travel. Can be inbound or outbound.
    :type direction: str

    """
    return web.Response(status=200)


async def stop_point_direction(request: web.Request, id, to_stop_point_id, line_id=None) -> web.Response:
    """Returns the canonical direction, \&quot;inbound\&quot; or \&quot;outbound\&quot;, for a given pair of stop point Ids in the direction from -&amp;gt; to.

    

    :param id: Originating stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type id: str
    :param to_stop_point_id: Destination stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type to_stop_point_id: str
    :param line_id: Optional line id filter e.g. victoria
    :type line_id: str

    """
    return web.Response(status=200)


async def stop_point_disruption(request: web.Request, ids, get_family=None, include_route_blocked_stops=None, flatten_response=None) -> web.Response:
    """Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.

    

    :param ids: A comma-seperated list of stop point ids. Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
    :type ids: List[str]
    :param get_family: Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false.
    :type get_family: bool
    :param include_route_blocked_stops: 
    :type include_route_blocked_stops: bool
    :param flatten_response: Specify true to associate all disruptions with parent stop point. (Only applicable when getFamily is true).
    :type flatten_response: bool

    """
    return web.Response(status=200)


async def stop_point_disruption_by_mode(request: web.Request, modes, include_route_blocked_stops=None) -> web.Response:
    """Gets a distinct list of disrupted stop points for the given modes

    

    :param modes: A comma-seperated list of modes e.g. tube,dlr
    :type modes: List[str]
    :param include_route_blocked_stops: 
    :type include_route_blocked_stops: bool

    """
    return web.Response(status=200)


async def stop_point_get(request: web.Request, ids, include_crowding_data=None) -> web.Response:
    """Gets a list of StopPoints corresponding to the given list of stop ids.

    

    :param ids: A comma-separated list of stop point ids (station naptan code e.g. 940GZZLUASL). Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
    :type ids: List[str]
    :param include_crowding_data: Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line}
    :type include_crowding_data: bool

    """
    return web.Response(status=200)


async def stop_point_get_by_geo_point(request: web.Request, stop_types, location_lat, location_lon, radius=None, use_stop_point_hierarchy=None, modes=None, categories=None, return_lines=None) -> web.Response:
    """Gets a list of StopPoints within {radius} by the specified criteria

    

    :param stop_types: a list of stopTypes that should be returned (a list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint)
    :type stop_types: List[str]
    :param location_lat: 
    :type location_lat: float
    :param location_lon: 
    :type location_lon: float
    :param radius: the radius of the bounding circle in metres (default : 200)
    :type radius: int
    :param use_stop_point_hierarchy: Re-arrange the output into a parent/child hierarchy
    :type use_stop_point_hierarchy: bool
    :param modes: the list of modes to search (comma separated mode names e.g. tube,dlr)
    :type modes: List[str]
    :param categories: an optional list of comma separated property categories to return in the StopPoint&#39;s property bag. If null or empty, all categories of property are returned. Pass the keyword \&quot;none\&quot; to return no properties (a valid list of categories can be obtained from the /StopPoint/Meta/categories endpoint)
    :type categories: List[str]
    :param return_lines: true to return the lines that each stop point serves as a nested resource
    :type return_lines: bool

    """
    return web.Response(status=200)


async def stop_point_get_by_mode(request: web.Request, modes, page=None) -> web.Response:
    """Gets a list of StopPoints filtered by the modes available at that StopPoint.

    

    :param modes: A comma-seperated list of modes e.g. tube,dlr
    :type modes: List[str]
    :param page: The data set page to return. Page 1 equates to the first 1000 stop points, page 2 equates to 1001-2000 etc. Must be entered for bus mode as data set is too large.
    :type page: int

    """
    return web.Response(status=200)


async def stop_point_get_by_sms(request: web.Request, id, output=None) -> web.Response:
    """Gets a StopPoint for a given sms code.

    

    :param id: A 5-digit Countdown Bus Stop Code e.g. 73241, 50435, 56334.
    :type id: str
    :param output: If set to \&quot;web\&quot;, a 302 redirect to relevant website bus stop page is returned. Valid values are : web. All other values are ignored.
    :type output: str

    """
    return web.Response(status=200)


async def stop_point_get_by_type(request: web.Request, types) -> web.Response:
    """Gets all stop points of a given type

    

    :param types: A comma-separated list of the types to return. Max. approx. 12 types.               A list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint.
    :type types: List[str]

    """
    return web.Response(status=200)


async def stop_point_get_by_type_with_pagination(request: web.Request, types, page) -> web.Response:
    """Gets all the stop points of given type(s) with a page number

    

    :param types: 
    :type types: List[str]
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def stop_point_get_car_parks_by_id(request: web.Request, stop_point_id) -> web.Response:
    """Get car parks corresponding to the given stop point id.

    

    :param stop_point_id: stopPointId is required to get the car parks.
    :type stop_point_id: str

    """
    return web.Response(status=200)


async def stop_point_get_service_types(request: web.Request, id, line_ids=None, modes=None) -> web.Response:
    """Gets the service types for a given stoppoint

    

    :param id: The Naptan id of the stop
    :type id: str
    :param line_ids: The lines which contain the given Naptan id (all lines relevant to the given stoppoint if empty)
    :type line_ids: List[str]
    :param modes: The modes which the lines are relevant to (all if empty)
    :type modes: List[str]

    """
    return web.Response(status=200)


async def stop_point_get_taxi_ranks_by_ids(request: web.Request, stop_point_id) -> web.Response:
    """Gets a list of taxi ranks corresponding to the given stop point id.

    

    :param stop_point_id: stopPointId is required to get the taxi ranks.
    :type stop_point_id: str

    """
    return web.Response(status=200)


async def stop_point_id_place_types_get(request: web.Request, id, place_types) -> web.Response:
    """Get a list of places corresponding to a given id and place types.

    

    :param id: A naptan id for a stop point (station naptan code e.g. 940GZZLUASL).
    :type id: str
    :param place_types: A comcomma-separated value representing the place types.
    :type place_types: List[str]

    """
    return web.Response(status=200)


async def stop_point_meta_categories(request: web.Request, ) -> web.Response:
    """Gets the list of available StopPoint additional information categories

    


    """
    return web.Response(status=200)


async def stop_point_meta_modes(request: web.Request, ) -> web.Response:
    """Gets the list of available StopPoint modes

    


    """
    return web.Response(status=200)


async def stop_point_meta_stop_types(request: web.Request, ) -> web.Response:
    """Gets the list of available StopPoint types

    


    """
    return web.Response(status=200)


async def stop_point_reachable_from(request: web.Request, id, line_id, service_types=None) -> web.Response:
    """Gets Stopoints that are reachable from a station/line combination.

    

    :param id: The id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) of the stop point to filter by
    :type id: str
    :param line_id: Line id of the line to filter by (e.g. victoria)
    :type line_id: str
    :param service_types: A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified
    :type service_types: List[str]

    """
    return web.Response(status=200)


async def stop_point_route(request: web.Request, id, service_types=None) -> web.Response:
    """Returns the route sections for all the lines that service the given stop point ids

    

    :param id: A stop point id (station naptan codes e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    :type id: str
    :param service_types: A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified
    :type service_types: List[str]

    """
    return web.Response(status=200)


async def stop_point_search(request: web.Request, query, modes=None, fares_only=None, max_results=None, lines=None, include_hubs=None, tfl_operated_national_rail_stations_only=None) -> web.Response:
    """Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

    

    :param query: The query string, case-insensitive. Leading and trailing wildcards are applied automatically.
    :type query: str
    :param modes: An optional, parameter separated list of the modes to filter by
    :type modes: List[str]
    :param fares_only: True to only return stations in that have Fares data available for single fares to another station.
    :type fares_only: bool
    :param max_results: An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items.
    :type max_results: int
    :param lines: An optional, parameter separated list of the lines to filter by
    :type lines: List[str]
    :param include_hubs: If true, returns results including HUBs.
    :type include_hubs: bool
    :param tfl_operated_national_rail_stations_only: If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned
    :type tfl_operated_national_rail_stations_only: bool

    """
    return web.Response(status=200)


async def stop_point_search_get(request: web.Request, query, modes=None, fares_only=None, max_results=None, lines=None, include_hubs=None, tfl_operated_national_rail_stations_only=None) -> web.Response:
    """Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

    

    :param query: The query string, case-insensitive. Leading and trailing wildcards are applied automatically.
    :type query: str
    :param modes: An optional, parameter separated list of the modes to filter by
    :type modes: List[str]
    :param fares_only: True to only return stations in that have Fares data available for single fares to another station.
    :type fares_only: bool
    :param max_results: An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items.
    :type max_results: int
    :param lines: An optional, parameter separated list of the lines to filter by
    :type lines: List[str]
    :param include_hubs: If true, returns results including HUBs.
    :type include_hubs: bool
    :param tfl_operated_national_rail_stations_only: If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned
    :type tfl_operated_national_rail_stations_only: bool

    """
    return web.Response(status=200)
