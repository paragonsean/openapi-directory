from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_road_corridor import TflApiPresentationEntitiesRoadCorridor
from openapi_server.models.tfl_api_presentation_entities_road_disruption import TflApiPresentationEntitiesRoadDisruption
from openapi_server.models.tfl_api_presentation_entities_status_severity import TflApiPresentationEntitiesStatusSeverity
from openapi_server import util


async def road_disrupted_streets(request: web.Request, start_date, end_date) -> web.Response:
    """Gets a list of disrupted streets. If no date filters are provided, current disruptions are returned.

    

    :param start_date: Optional, the start time to filter on.
    :type start_date: str
    :param end_date: Optional, The end time to filter on.
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def road_disruption(request: web.Request, ids, strip_content=None, severities=None, categories=None, closures=None) -> web.Response:
    """Get active disruptions, filtered by road ids

    

    :param ids: Comma-separated list of road identifiers e.g. \&quot;A406, A2\&quot; use all for all to ignore id filter (a full list of supported road identifiers can be found at the /Road/ endpoint)
    :type ids: List[str]
    :param strip_content: Optional, defaults to false. When true, removes every property/node except for id, point, severity, severityDescription, startDate, endDate, corridor details, location, comments and streets
    :type strip_content: bool
    :param severities: an optional list of Severity names to filter on (a valid list of severities can be obtained from the /Road/Meta/severities endpoint)
    :type severities: List[str]
    :param categories: an optional list of category names to filter on (a valid list of categories can be obtained from the /Road/Meta/categories endpoint)
    :type categories: List[str]
    :param closures: Optional, defaults to true. When true, always includes disruptions that have road closures, regardless of the severity filter. When false, the severity filter works as normal.
    :type closures: bool

    """
    return web.Response(status=200)


async def road_disruption_by_id(request: web.Request, disruption_ids, strip_content=None) -> web.Response:
    """Gets a list of active disruptions filtered by disruption Ids.

    

    :param disruption_ids: Comma-separated list of disruption identifiers to filter by.
    :type disruption_ids: List[str]
    :param strip_content: Optional, defaults to false. When true, removes every property/node except for id, point, severity, severityDescription, startDate, endDate, corridor details, location and comments.
    :type strip_content: bool

    """
    return web.Response(status=200)


async def road_get(request: web.Request, ) -> web.Response:
    """Gets all roads managed by TfL

    


    """
    return web.Response(status=200)


async def road_ids_get(request: web.Request, ids) -> web.Response:
    """Gets the road with the specified id (e.g. A1)

    

    :param ids: Comma-separated list of road identifiers e.g. \&quot;A406, A2\&quot; (a full list of supported road identifiers can be found at the /Road/ endpoint)
    :type ids: List[str]

    """
    return web.Response(status=200)


async def road_meta_categories(request: web.Request, ) -> web.Response:
    """Gets a list of valid RoadDisruption categories

    


    """
    return web.Response(status=200)


async def road_meta_severities(request: web.Request, ) -> web.Response:
    """Gets a list of valid RoadDisruption severity codes

    


    """
    return web.Response(status=200)


async def road_status(request: web.Request, ids, date_range_nullable_start_date=None, date_range_nullable_end_date=None) -> web.Response:
    """Gets the specified roads with the status aggregated over the date range specified, or now until the end of today if no dates are passed.

    

    :param ids: Comma-separated list of road identifiers e.g. \&quot;A406, A2\&quot; or use \&quot;all\&quot; to ignore id filter (a full list of supported road identifiers can be found at the /Road/ endpoint)
    :type ids: List[str]
    :param date_range_nullable_start_date: 
    :type date_range_nullable_start_date: str
    :param date_range_nullable_end_date: 
    :type date_range_nullable_end_date: str

    """
    date_range_nullable_start_date = util.deserialize_datetime(date_range_nullable_start_date)
    date_range_nullable_end_date = util.deserialize_datetime(date_range_nullable_end_date)
    return web.Response(status=200)
