from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_usage_usage_trigger import ApiV2010AccountUsageUsageTrigger
from openapi_server.models.list_usage_trigger_response import ListUsageTriggerResponse
from openapi_server.models.usage_trigger_enum_recurring import UsageTriggerEnumRecurring
from openapi_server.models.usage_trigger_enum_trigger_field import UsageTriggerEnumTriggerField
from openapi_server.models.usage_trigger_enum_usage_category import UsageTriggerEnumUsageCategory
from openapi_server import util


async def create_usage_trigger(request: web.Request, account_sid, callback_url, trigger_value, usage_category, callback_method=None, friendly_name=None, recurring=None, trigger_by=None) -> web.Response:
    """create_usage_trigger

    Create a new UsageTrigger

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param callback_url: The URL we should call using &#x60;callback_method&#x60; when the trigger fires.
    :type callback_url: str
    :param trigger_value: The usage value at which the trigger should fire.  For convenience, you can use an offset value such as &#x60;+30&#x60; to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a &#x60;+&#x60; as &#x60;%2B&#x60;.
    :type trigger_value: str
    :param usage_category: 
    :type usage_category: str
    :param callback_method: The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;.
    :type callback_method: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param recurring: 
    :type recurring: str
    :param trigger_by: 
    :type trigger_by: str

    """
    return web.Response(status=200)


async def delete_usage_trigger(request: web.Request, account_sid, sid) -> web.Response:
    """delete_usage_trigger

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_usage_trigger(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_usage_trigger

    Fetch and instance of a usage-trigger

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_usage_trigger(request: web.Request, account_sid, recurring=None, trigger_by=None, usage_category=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_usage_trigger

    Retrieve a list of usage-triggers belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read.
    :type account_sid: str
    :param recurring: The frequency of recurring UsageTriggers to read. Can be: &#x60;daily&#x60;, &#x60;monthly&#x60;, or &#x60;yearly&#x60; to read recurring UsageTriggers. An empty value or a value of &#x60;alltime&#x60; reads non-recurring UsageTriggers.
    :type recurring: str
    :param trigger_by: The trigger field of the UsageTriggers to read.  Can be: &#x60;count&#x60;, &#x60;usage&#x60;, or &#x60;price&#x60; as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).
    :type trigger_by: str
    :param usage_category: The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories).
    :type usage_category: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_usage_trigger(request: web.Request, account_sid, sid, callback_method=None, callback_url=None, friendly_name=None) -> web.Response:
    """update_usage_trigger

    Update an instance of a usage trigger

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
    :type sid: str
    :param callback_method: The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;.
    :type callback_method: str
    :param callback_url: The URL we should call using &#x60;callback_method&#x60; when the trigger fires.
    :type callback_url: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
