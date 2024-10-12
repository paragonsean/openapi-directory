from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_aggregated_aggregated_summary_result import ApiCoreDtoAggregatedAggregatedSummaryResult
from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage
from openapi_server.models.api_core_dto_datapoints_datapoint import ApiCoreDtoDatapointsDatapoint
from openapi_server.models.api_core_dto_groups_group import ApiCoreDtoGroupsGroup
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server import util


async def groups_count(request: web.Request, status=None, tags=None, text_search=None, created_after=None, created_before=None, write=None) -> web.Response:
    """Count the groups associated to the user.

    

    :param status: Status of the datapoint
    :type status: str
    :param tags: A comma separated list of tags you want to filter with.
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude groups created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude groups created after this date (YYYYMMDD)
    :type created_before: str
    :param write: Write permission
    :type write: bool

    """
    return web.Response(status=200)


async def groups_delete(request: web.Request, id) -> web.Response:
    """Delete group specified by id

    

    :param id: Id of the group
    :type id: int

    """
    return web.Response(status=200)


async def groups_get(request: web.Request, offset=None, limit=None, status=None, tags=None, text_search=None, created_after=None, created_before=None, write=None) -> web.Response:
    """List of all the groups associated to the user.

    

    :param offset: Where to start when retrieving elements. Default is 0 if not specified.
    :type offset: int
    :param limit: Maximum elements to retrieve. Default to 20 if not specified.
    :type limit: int
    :param status: Status of the group
    :type status: str
    :param tags: A comma separated list of tags you want to filter with.
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude groups created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude groups created after this date (YYYYMMDD)
    :type created_before: str
    :param write: Write permission
    :type write: bool

    """
    return web.Response(status=200)


async def groups_get_datapoints(request: web.Request, id, offset=None, limit=None, type=None, status=None, tags=None, text_search=None, only_favorites=None, sort_by=None, sort_direction=None, created_after=None, created_before=None) -> web.Response:
    """List of all the datapoints associated to the user in this group.

    

    :param id: Id of the group
    :type id: int
    :param offset: Where to start when retrieving elements. Default is 0 if not specified.
    :type offset: int
    :param limit: Maximum elements to retrieve. Default to 20 if not specified.
    :type limit: int
    :param type: Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;)
    :type type: str
    :param status: Status of the datapoint
    :type status: str
    :param tags: A comma separated list of tags you want to filter with.
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param only_favorites: Filter fields by favourite status
    :type only_favorites: bool
    :param sort_by: Field to sort by
    :type sort_by: str
    :param sort_direction: Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot;
    :type sort_direction: str
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def groups_get_datapoints_count(request: web.Request, id, type=None, status=None, tags=None, text_search=None, only_favorites=None, created_after=None, created_before=None) -> web.Response:
    """Count the datapoints associated to the user in this group.

    

    :param id: Id of the group
    :type id: int
    :param type: Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;)
    :type type: str
    :param status: Status of the datapoint
    :type status: str
    :param tags: A comma separated list of tags you want to filter with.
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param only_favorites: Filter fields by favourite status
    :type only_favorites: bool
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def groups_get_datapoints_summary(request: web.Request, id, time_frame, type=None, from_day=None, to_day=None, status=None, tag=None, favourite=None, sort_by=None, sort_direction=None, offset=None, limit=None, text_search=None) -> web.Response:
    """Retrieve statistics about a subset of datapoints for a timeframe with datapoints data

    

    :param id: Filter by this group id
    :type id: int
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
    :param text_search: Filter fields by this pattern
    :type text_search: str

    """
    return web.Response(status=200)


async def groups_get_hits(request: web.Request, id, timeframe, limit=None, offset=None, from_day=None, to_day=None, filter=None) -> web.Response:
    """Retrieve the list of events related to this group.

    

    :param id: Id of the group
    :type id: int
    :param timeframe: Timeframe of the request. See list at $timeframeList
    :type timeframe: str
    :param limit: Limit results to this number
    :type limit: int
    :param offset: Offset where to start from (it&#39;s the lastKey field in the response object)
    :type offset: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param filter: Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;)
    :type filter: str

    """
    return web.Response(status=200)


async def groups_get_statistics_aggregated_single(request: web.Request, time_frame, from_day=None, to_day=None, hourly=None, status=None, tag=None, favourite=None) -> web.Response:
    """Retrieve statistics about this customer for a timeframe by groups

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param hourly: If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail
    :type hourly: bool
    :param status: Status of group (\&quot;deleted\&quot;/\&quot;active\&quot;)
    :type status: str
    :param tag: A comma separated list of tags you want to filter with.
    :type tag: str
    :param favourite: Is the group is marked as favourite
    :type favourite: bool

    """
    return web.Response(status=200)


async def groups_get_statistics_all_list(request: web.Request, time_frame, from_day=None, to_day=None, status=None, tag=None, favourite=None, group_by=None) -> web.Response:
    """Retrieve statistics about all groups of this customer for a timeframe grouped by some temporal entity (day/week/month)

    

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
    :param favourite: Is the group is marked as favourite
    :type favourite: bool
    :param group_by: The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;.
    :type group_by: str

    """
    return web.Response(status=200)


async def groups_get_statistics_list(request: web.Request, id, time_frame, from_day=None, to_day=None, group_by=None) -> web.Response:
    """Retrieve statistics about this group for a timeframe grouped by some temporal entity (day/week/month)

    

    :param id: Id of the group
    :type id: int
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


async def groups_get_statistics_single(request: web.Request, id, time_frame, from_day=None, to_day=None, hourly=None) -> web.Response:
    """Retrieve statistics about this group for a timeframe

    

    :param id: Id of the group
    :type id: int
    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param hourly: If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail
    :type hourly: bool

    """
    return web.Response(status=200)


async def groups_id_get(request: web.Request, id) -> web.Response:
    """Get a group

    

    :param id: The id of the group
    :type id: int

    """
    return web.Response(status=200)


async def groups_patch_favourite(request: web.Request, id) -> web.Response:
    """Fast switch the \&quot;favourite\&quot; field of a group

    

    :param id: Id of the group
    :type id: int

    """
    return web.Response(status=200)


async def groups_patch_notes(request: web.Request, id, body) -> web.Response:
    """Fast patch the \&quot;notes\&quot; field of a group

    

    :param id: Id of the group
    :type id: int
    :param body: Patch requests
    :type body: dict | bytes

    """
    body = ApiCoreRequestsGenericTextPatch.from_dict(body)
    return web.Response(status=200)


async def groups_post(request: web.Request, id, body) -> web.Response:
    """Update a group

    

    :param id: The id of the group
    :type id: int
    :param body: The body of the group
    :type body: dict | bytes

    """
    body = ApiCoreDtoGroupsGroup.from_dict(body)
    return web.Response(status=200)


async def groups_put(request: web.Request, body) -> web.Response:
    """Create a group

    

    :param body: The body of the group
    :type body: dict | bytes

    """
    body = ApiCoreDtoGroupsGroup.from_dict(body)
    return web.Response(status=200)


async def groups_put_datapoint(request: web.Request, id, body) -> web.Response:
    """Create a datapoint in this group

    

    :param id: The id of the group
    :type id: int
    :param body: The body of the datapoint
    :type body: dict | bytes

    """
    body = ApiCoreDtoDatapointsDatapoint.from_dict(body)
    return web.Response(status=200)
