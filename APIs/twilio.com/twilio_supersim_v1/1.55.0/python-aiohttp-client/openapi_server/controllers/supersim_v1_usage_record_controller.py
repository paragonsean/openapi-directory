from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_usage_record_response import ListUsageRecordResponse
from openapi_server.models.usage_record_enum_granularity import UsageRecordEnumGranularity
from openapi_server.models.usage_record_enum_group import UsageRecordEnumGroup
from openapi_server import util


async def list_usage_record(request: web.Request, sim=None, fleet=None, network=None, iso_country=None, group=None, granularity=None, start_time=None, end_time=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_usage_record

    List UsageRecords

    :param sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
    :type sim: str
    :param fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
    :type fleet: str
    :param network: SID of a Network resource. Only show UsageRecords representing usage on this network.
    :type network: str
    :param iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
    :type iso_country: str
    :param group: Dimension over which to aggregate usage records. Can be: &#x60;sim&#x60;, &#x60;fleet&#x60;, &#x60;network&#x60;, &#x60;isoCountry&#x60;. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the &#x60;Granularity&#x60; parameter.
    :type group: str
    :param granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: &#x60;hour&#x60;, &#x60;day&#x60;, or &#x60;all&#x60;. Default is &#x60;all&#x60;. &#x60;all&#x60; returns one UsageRecord that describes the usage for the entire period.
    :type granularity: str
    :param start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the &#x60;end_time&#x60;.
    :type start_time: str
    :param end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
    :type end_time: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)
