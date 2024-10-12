from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_usage_record_enum_granularity import AccountUsageRecordEnumGranularity
from openapi_server.models.list_account_usage_record_response import ListAccountUsageRecordResponse
from openapi_server.models.list_usage_record_response import ListUsageRecordResponse
from openapi_server.models.usage_record_enum_granularity import UsageRecordEnumGranularity
from openapi_server import util


async def list_account_usage_record(request: web.Request, end=None, start=None, granularity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_account_usage_record

    

    :param end: Only include usage that has occurred on or before this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
    :type end: str
    :param start: Only include usage that has occurred on or after this date. Format is [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html).
    :type start: str
    :param granularity: How to summarize the usage by time. Can be: &#x60;daily&#x60;, &#x60;hourly&#x60;, or &#x60;all&#x60;. A value of &#x60;all&#x60; returns one Usage Record that describes the usage for the entire period.
    :type granularity: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    end = util.deserialize_datetime(end)
    start = util.deserialize_datetime(start)
    return web.Response(status=200)


async def list_usage_record(request: web.Request, sim_sid, end=None, start=None, granularity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_usage_record

    

    :param sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource)  to read the usage from.
    :type sim_sid: str
    :param end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
    :type end: str
    :param start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the &#x60;end&#x60; parameter value.
    :type start: str
    :param granularity: How to summarize the usage by time. Can be: &#x60;daily&#x60;, &#x60;hourly&#x60;, or &#x60;all&#x60;. The default is &#x60;all&#x60;. A value of &#x60;all&#x60; returns one Usage Record that describes the usage for the entire period.
    :type granularity: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    end = util.deserialize_datetime(end)
    start = util.deserialize_datetime(start)
    return web.Response(status=200)
