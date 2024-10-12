from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage
from openapi_server.models.api_core_dto_datapoints_datapoint import ApiCoreDtoDatapointsDatapoint
from openapi_server.models.api_core_requests_datapoints_batch import ApiCoreRequestsDatapointsBatch
from openapi_server.models.api_core_requests_delete_batch import ApiCoreRequestsDeleteBatch
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_modify_batch_item_responce_api_core_dto_datapoints_datapoint_system_int64 import ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64
from openapi_server import util


async def data_points_batch_delete(request: web.Request, body) -> web.Response:
    """Delete multiple datapoints

    

    :param body: A json containing the datapoints to delete.
    :type body: dict | bytes

    """
    body = ApiCoreRequestsDeleteBatch.from_dict(body)
    return web.Response(status=200)


async def data_points_batch_post(request: web.Request, body) -> web.Response:
    """Update multiple datapoints

    

    :param body: A json containing the datapoints to update.
    :type body: dict | bytes

    """
    body = ApiCoreRequestsDatapointsBatch.from_dict(body)
    return web.Response(status=200)


async def data_points_batch_put(request: web.Request, body) -> web.Response:
    """Create multiple datapoints

    

    :param body: A json containing the datapoints to create.
    :type body: dict | bytes

    """
    body = ApiCoreRequestsDatapointsBatch.from_dict(body)
    return web.Response(status=200)


async def data_points_count(request: web.Request, type=None, status=None, tags=None, text_search=None, only_favorites=None, created_after=None, created_before=None) -> web.Response:
    """Count the datapoints associated to the user

    

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


async def data_points_delete(request: web.Request, id) -> web.Response:
    """Delete a datapoint

    

    :param id: The id of the datapoint
    :type id: int

    """
    return web.Response(status=200)


async def data_points_get(request: web.Request, offset=None, limit=None, type=None, status=None, tags=None, text_search=None, only_favorites=None, sort_by=None, sort_direction=None, created_after=None, created_before=None) -> web.Response:
    """List of all the datapoints associated to the user

    

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


async def data_points_get_hits(request: web.Request, id, timeframe, limit=None, offset=None, from_day=None, to_day=None, filter=None) -> web.Response:
    """Retrieve the list of events related to this datapoint.

    

    :param id: Id of the datapoint
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


async def data_points_get_statistics_aggregated_single(request: web.Request, time_frame, type=None, from_day=None, to_day=None, hourly=None, status=None, tag=None, favourite=None) -> web.Response:
    """Retrieve statistics about this customer for a timeframe by groups

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param type: Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;)
    :type type: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param hourly: If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail
    :type hourly: bool
    :param status: Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;)
    :type status: str
    :param tag: A comma separated list of tags you want to filter with.
    :type tag: str
    :param favourite: Is the datapoint is marked as favourite
    :type favourite: bool

    """
    return web.Response(status=200)


async def data_points_get_statistics_all_list(request: web.Request, type, time_frame, from_day=None, to_day=None, status=None, tag=None, favourite=None, group_by=None) -> web.Response:
    """Retrieve statistics about all datapoints of this customer for a timeframe grouped by some temporal entity (day/week/month)

    

    :param type: Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;)
    :type type: str
    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param status: Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;)
    :type status: str
    :param tag: A comma separated list of tags you want to filter with.
    :type tag: str
    :param favourite: Is the datapoint is marked as favourite
    :type favourite: bool
    :param group_by: The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;.
    :type group_by: str

    """
    return web.Response(status=200)


async def data_points_get_statistics_list(request: web.Request, id, time_frame, from_day=None, to_day=None, group_by=None) -> web.Response:
    """Retrieve statistics about this datapoint for a timeframe grouped by some temporal entity (day/week/month)

    

    :param id: Id of the datapoint
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


async def data_points_get_statistics_single(request: web.Request, id, time_frame, from_day=None, to_day=None, hourly=None) -> web.Response:
    """Retrieve statistics about this datapoint for a timeframe

    

    :param id: Id of the datapoint
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


async def data_points_patch_favourite(request: web.Request, id) -> web.Response:
    """Fast switch the \&quot;favourite\&quot; field of a datapoint

    

    :param id: Id of the datapoint
    :type id: int

    """
    return web.Response(status=200)


async def data_points_patch_notes(request: web.Request, id, body) -> web.Response:
    """Fast patch the \&quot;notes\&quot; field of a datapoint

    

    :param id: Id of the datapoint
    :type id: int
    :param body: Patch requests
    :type body: dict | bytes

    """
    body = ApiCoreRequestsGenericTextPatch.from_dict(body)
    return web.Response(status=200)


async def data_points_post(request: web.Request, id, body) -> web.Response:
    """Update a datapoint

    

    :param id: The id of the datapoint
    :type id: int
    :param body: The body of the datapoint
    :type body: dict | bytes

    """
    body = ApiCoreDtoDatapointsDatapoint.from_dict(body)
    return web.Response(status=200)


async def data_points_put(request: web.Request, body) -> web.Response:
    """Create a datapoint

    

    :param body: The body of the datapoint
    :type body: dict | bytes

    """
    body = ApiCoreDtoDatapointsDatapoint.from_dict(body)
    return web.Response(status=200)


async def datapoints_id_get(request: web.Request, id) -> web.Response:
    """Get a datapoint

    

    :param id: The id of the datapoint
    :type id: int

    """
    return web.Response(status=200)
