from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage
from openapi_server.models.api_core_dto_conversions_conversion import ApiCoreDtoConversionsConversion
from openapi_server.models.api_core_requests_conversion_patch_body import ApiCoreRequestsConversionPatchBody
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_requests_patch_body_batch import ApiCoreRequestsPatchBodyBatch
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server import util


async def conversions_conversion_id_datapoints_batch_patch_put(request: web.Request, conversion_id, body) -> web.Response:
    """Modify the association between a conversion and multiple datapoints

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
    :param body: Patch requests
    :type body: dict | bytes

    """
    body = ApiCoreRequestsPatchBodyBatch.from_dict(body)
    return web.Response(status=200)


async def conversions_conversion_id_get(request: web.Request, conversion_id) -> web.Response:
    """Retrieve conversion specified by id

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int

    """
    return web.Response(status=200)


async def conversions_count(request: web.Request, status=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """Retrieve a count of conversions

    

    :param status: Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;)
    :type status: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude conversions created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude conversions created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def conversions_delete(request: web.Request, conversion_id) -> web.Response:
    """Delete conversion specified by id

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int

    """
    return web.Response(status=200)


async def conversions_get(request: web.Request, offset=None, limit=None, status=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """Retrieve a list of conversions

    

    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param status: Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;)
    :type status: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude conversions created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude conversions created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def conversions_get_datapoints(request: web.Request, conversion_id, offset=None, limit=None, type=None, status=None, tags=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """Retrieve a list of datapoints connected to this conversion

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
    :param offset: Offset where to start from
    :type offset: int
    :param limit: Limit results to this number
    :type limit: int
    :param type: Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;)
    :type type: str
    :param status: Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;)
    :type status: str
    :param tags: Filter by this tag name
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def conversions_get_datapoints_count(request: web.Request, conversion_id, type=None, status=None, tags=None, text_search=None, created_after=None, created_before=None) -> web.Response:
    """Retrieve a count of datapoints connected to this conversion

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
    :param type: Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;)
    :type type: str
    :param status: Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;)
    :type status: str
    :param tags: Filter by this tag name
    :type tags: str
    :param text_search: Filter fields by this pattern
    :type text_search: str
    :param created_after: Exclude datapoints created before this date (YYYYMMDD)
    :type created_after: str
    :param created_before: Exclude datapoints created after this date (YYYYMMDD)
    :type created_before: str

    """
    return web.Response(status=200)


async def conversions_get_hits(request: web.Request, conversion_id, timeframe, limit=None, offset=None, from_day=None, to_day=None, filter=None) -> web.Response:
    """Retrieve the list of events related to this conversion.

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
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


async def conversions_get_statistics_all_list(request: web.Request, time_frame, from_day=None, to_day=None, status=None, group_by=None) -> web.Response:
    """Retrieve statistics about this customer for a timeframe related to a subset of conversions grouped by some temporal entity (day/week/month)

    

    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param status: Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;)
    :type status: str
    :param group_by: The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;.
    :type group_by: str

    """
    return web.Response(status=200)


async def conversions_get_statistics_list(request: web.Request, conversion_id, time_frame, from_day=None, to_day=None, group_by=None) -> web.Response:
    """Retrieve statistics about this conversion for a timeframe grouped by some temporal entity (day/week/month)

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
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


async def conversions_get_statistics_single(request: web.Request, conversion_id, time_frame, from_day=None, to_day=None, tag=None, favourite=None, hourly=None) -> web.Response:
    """Retrieve statistics about this conversion for a timeframe

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
    :param time_frame: Timeframe of the request. See list at $timeframeList
    :type time_frame: str
    :param from_day: If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD)
    :type from_day: str
    :param to_day: If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD)
    :type to_day: str
    :param tag: Filter by this tag name
    :type tag: str
    :param favourite: Is the datapoint marked as favourite
    :type favourite: bool
    :param hourly: If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail
    :type hourly: bool

    """
    return web.Response(status=200)


async def conversions_patch(request: web.Request, conversion_id, body) -> web.Response:
    """Modify the association between a conversion and a datapoint

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
    :param body: Patch request
    :type body: dict | bytes

    """
    body = ApiCoreRequestsConversionPatchBody.from_dict(body)
    return web.Response(status=200)


async def conversions_patch_notes(request: web.Request, conversion_id, body) -> web.Response:
    """Fast patch the \&quot;notes\&quot; field of a conversion

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
    :param body: Patch requests
    :type body: dict | bytes

    """
    body = ApiCoreRequestsGenericTextPatch.from_dict(body)
    return web.Response(status=200)


async def conversions_post(request: web.Request, conversion_id, body) -> web.Response:
    """Update conversion specified by id

    

    :param conversion_id: Id of the conversion
    :type conversion_id: int
    :param body: Updated body of the conversion
    :type body: dict | bytes

    """
    body = ApiCoreDtoConversionsConversion.from_dict(body)
    return web.Response(status=200)


async def conversions_put(request: web.Request, body) -> web.Response:
    """Create a conversion

    

    :param body: The body of the conversion
    :type body: dict | bytes

    """
    body = ApiCoreDtoConversionsConversion.from_dict(body)
    return web.Response(status=200)
