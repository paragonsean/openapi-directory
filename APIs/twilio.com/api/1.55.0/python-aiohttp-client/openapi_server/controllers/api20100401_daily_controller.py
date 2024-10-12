from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_usage_record_daily_response import ListUsageRecordDailyResponse
from openapi_server.models.usage_record_daily_enum_category import UsageRecordDailyEnumCategory
from openapi_server import util


async def list_usage_record_daily(request: web.Request, account_sid, category=None, start_date=None, end_date=None, include_subaccounts=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_usage_record_daily

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
    :type account_sid: str
    :param category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
    :type category: str
    :param start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. You can also specify offsets from the current date, such as: &#x60;-30days&#x60;, which will set the start date to be 30 days before the current date.
    :type start_date: str
    :param end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.  You can also specify offsets from the current date, such as: &#x60;+30days&#x60;, which will set the end date to 30 days from the current date.
    :type end_date: str
    :param include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: &#x60;true&#x60; (the default) to include usage from the master account and all subaccounts or &#x60;false&#x60; to retrieve usage from only the specified account.
    :type include_subaccounts: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)
