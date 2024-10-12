from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_aggregated_aggregated_summary_result import ApiCoreDtoAggregatedAggregatedSummaryResult
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
from openapi_server import util


async def aggregated_get_conversions_summary(request: web.Request, time_frame, from_day=None, to_day=None, status=None, sort_by=None, sort_direction=None, offset=None, limit=None, text_search=None) -> web.Response:
    """Retrieve statistics about a subset of conversions for a timeframe with conversions data

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param status: Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;)
    :type status: str
    :param sort_by: Field to sort by
    :type sort_by: str
    :param sort_direction: Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot;
    :type sort_direction: str
    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param text_search: Filter fields by this pattern
    :type text_search: str

    """
    return web.Response(status=200)


async def aggregated_get_datapoints_summary(request: web.Request, time_frame, type, from_day=None, to_day=None, status=None, tag=None, favourite=None, sort_by=None, sort_direction=None, offset=None, limit=None, group_id=None, text_search=None) -> web.Response:
    """Retrieve statistics about a subset of datapoints for a timeframe with datapoints data

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param type: Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;)
    :type type: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param status: Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;)
    :type status: str
    :param tag: A comma separated list of tags you want to filter with.
    :type tag: str
    :param favourite: Is the datapoint marked as favourite
    :type favourite: bool
    :param sort_by: Field to sort by
    :type sort_by: str
    :param sort_direction: Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot;
    :type sort_direction: str
    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param group_id: Filter by this group id
    :type group_id: int
    :param text_search: Filter fields by this pattern
    :type text_search: str

    """
    return web.Response(status=200)


async def aggregated_get_groups_summary(request: web.Request, time_frame, from_day=None, to_day=None, status=None, tag=None, favourite=None, sort_by=None, sort_direction=None, offset=None, limit=None, text_search=None) -> web.Response:
    """Retrieve statistics about a subset of groups for a timeframe with groups data

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param status: Status of group (\&quot;deleted\&quot;/\&quot;active\&quot;)
    :type status: str
    :param tag: A comma separated list of tags you want to filter with.
    :type tag: str
    :param favourite: Is the group marked as favourite
    :type favourite: bool
    :param sort_by: Field to sort by
    :type sort_by: str
    :param sort_direction: Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot;
    :type sort_direction: str
    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param text_search: Filter fields by this pattern
    :type text_search: str

    """
    return web.Response(status=200)


async def aggregated_get_statistics_list(request: web.Request, time_frame, from_day=None, to_day=None, group_by=None) -> web.Response:
    """Retrieve statistics about this customer for a timeframe grouped by some temporal entity (day/week/month)

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param group_by: The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;.
    :type group_by: str

    """
    return web.Response(status=200)


async def aggregated_get_statistics_single(request: web.Request, time_frame, from_day=None, to_day=None, hourly=None, only_favorites=None) -> web.Response:
    """Retrieve statistics about this customer for a timeframe

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param hourly: If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail
    :type hourly: bool
    :param only_favorites: 
    :type only_favorites: str

    """
    return web.Response(status=200)
