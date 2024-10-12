from typing import List, Dict
from aiohttp import web

from openapi_server.models.extended_rateplan_entry import ExtendedRateplanEntry
from openapi_server.models.operation_rate_patch_request import OperationRatePatchRequest
from openapi_server.models.rate_response import RateResponse
from openapi_server.models.rateplans_list_response import RateplansListResponse
from openapi_server.models.rates_batch_update_request_item import RatesBatchUpdateRequestItem
from openapi_server.models.rates_response import RatesResponse
from openapi_server.models.total_count_response import TotalCountResponse
from openapi_server import util


async def rate_plans_batch_update_rates(request: web.Request, app_id, app_key, hotel_id, request) -> web.Response:
    """Update a list of base rateplans for a given period and a given base price for single occupancy.

    Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified time period.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;rateplan\&quot;: \&quot;STDN01\&quot;, \&quot;from\&quot;: \&quot;2018-01-01\&quot;, \&quot;to\&quot;: \&quot;2018-01-30\&quot;, \&quot;base_price\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the rateplan belongs to.
    :type hotel_id: int
    :param request: 
    :type request: list | bytes

    """
    request = [RatesBatchUpdateRequestItem.from_dict(d) for d in request]
    return web.Response(status=200)


async def rate_plans_get_rate(request: web.Request, app_id, app_key, hotel_id, rateplan_code, business_day) -> web.Response:
    """Get the setup of a daily rate for a specific business day and rateplan.

    Read the setup of the daily rate for the defined rateplan for that specific business day.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the rateplan belongs to.
    :type hotel_id: int
    :param rateplan_code: The code of the rateplan you want to see details for.
    :type rateplan_code: str
    :param business_day: The business day you want to get the rate setup for.
    :type business_day: str

    """
    business_day = util.deserialize_datetime(business_day)
    return web.Response(status=200)


async def rate_plans_get_rateplan(request: web.Request, app_id, app_key, hotel_id, rateplan_code) -> web.Response:
    """Get all the details for a specific rateplan in the hotel.

    Read the details about a specific rateplan for the defined hotel.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the rateplan belongs to.
    :type hotel_id: int
    :param rateplan_code: The code of the rateplan you want to see details for.
    :type rateplan_code: str

    """
    return web.Response(status=200)


async def rate_plans_get_rateplans(request: web.Request, app_id, app_key, hotel_id, selling_status=None, commissionable=None, group=None, base_rateplan=None, channel_group=None, channel_code=None, market_codes=None, room_types=None, included_services=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Get a list of rateplans for the specified hotel id matching the filter criteria.

    With this call you can find rateplans for a hotel by different filters. By default and without any filter criteria              defined it will return you all active rateplans.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id you are trying to find rateplans for.
    :type hotel_id: int
    :param selling_status: Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans.
    :type selling_status: str
    :param commissionable: Return all rateplans having commisionable status
    :type commissionable: bool
    :param group: Return all rateplans belonging to the specified rateplan group
    :type group: str
    :param base_rateplan: Return all rateplans having the specified rateplan as base rateplan
    :type base_rateplan: str
    :param channel_group: Return all rateplans that are sold through at least one channel out of the specified channel group
    :type channel_group: str
    :param channel_code: Return all rateplans sold through the specified channel
    :type channel_code: str
    :param market_codes: Return all rateplans having one of the specified values as a market code
    :type market_codes: List[str]
    :param room_types: Return all rateplans by which at least one of the specified room types are sold
    :type room_types: List[str]
    :param included_services: Return all rateplans having at least one of the specified services included
    :type included_services: List[str]
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    return web.Response(status=200)


async def rate_plans_get_rateplans_count(request: web.Request, app_id, app_key, hotel_id, selling_status=None, commissionable=None, group=None, base_rateplan=None, channel_group=None, channel_code=None, market_codes=None, room_types=None, included_services=None) -> web.Response:
    """Get the count of all rateplans in the hotel matching the given filter criteria.

    

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel you are counting the rateplans for.
    :type hotel_id: int
    :param selling_status: Specify which rateplans to return. If you do not specify a value you will by default get active              rateplans.
    :type selling_status: str
    :param commissionable: Return all rateplans having commisionable status
    :type commissionable: bool
    :param group: Return all rateplans belonging to the specified rateplan group
    :type group: str
    :param base_rateplan: Return all rateplans having the specified rateplan as base rateplan
    :type base_rateplan: str
    :param channel_group: Return all rateplans that are sold through at least one channel out of the specified channel group
    :type channel_group: str
    :param channel_code: Return all rateplans sold through the specified channel
    :type channel_code: str
    :param market_codes: Return all rateplans having one of the specified values as a market code
    :type market_codes: List[str]
    :param room_types: Return all rateplans by which at least one of the specified room types are sold
    :type room_types: List[str]
    :param included_services: Return all rateplans having at least one of the specified services included
    :type included_services: List[str]

    """
    return web.Response(status=200)


async def rate_plans_get_rates(request: web.Request, app_id, app_key, hotel_id, rateplan_code, _from, to, expand=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Get the setup of the daily rates for a specific rateplan and a defined timeperiod.

    With this call you can read the daily rates setup including the cancellation policy and minimum guarantee per day for the              specified rateplan. You can specify a timeperiod to read the daily rates for. The rateplan needs to be active for at least              one business day in the defined time period and have rates loaded.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the rateplan belongs to.
    :type hotel_id: int
    :param rateplan_code: The code of the rateplan you want to see details for.
    :type rateplan_code: str
    :param _from: Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days.
    :type _from: str
    :param to: Defines the first business day you would like to get rates for.
    :type to: str
    :param expand: You can expand the supplements per room type on demand. By default they are not shown.
    :type expand: str
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def rate_plans_get_rates_count(request: web.Request, app_id, app_key, hotel_id, rateplan_code, _from, to) -> web.Response:
    """Get the count of all active and loaded daily rates for the defined rateplan in a specified time period.

    

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the rateplan belongs to.
    :type hotel_id: int
    :param rateplan_code: The code of the rateplan you want to count daily rates for.
    :type rateplan_code: str
    :param _from: Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days.
    :type _from: str
    :param to: Defines the first business day you would like to get rates for.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def rate_plans_patch_rate(request: web.Request, app_id, app_key, hotel_id, rateplan_code, business_day, patch_request) -> web.Response:
    """Partially update a rate of the specified rateplan for a defined business day.

    The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified business day.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/base_price\&quot;, \&quot;value\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the rateplan belongs to.
    :type hotel_id: int
    :param rateplan_code: The code of the rateplan you want to update the daily rate details for.
    :type rateplan_code: str
    :param business_day: The business day of the daily rate you want to update.
    :type business_day: str
    :param patch_request: A set of JSON Patch operations.
    :type patch_request: list | bytes

    """
    business_day = util.deserialize_datetime(business_day)
    patch_request = [OperationRatePatchRequest.from_dict(d) for d in patch_request]
    return web.Response(status=200)


async def rate_plans_patch_rates(request: web.Request, app_id, app_key, hotel_id, rateplan_code, _from, to, patch_request) -> web.Response:
    """Partially update a rate of the specified rateplan for the defined time period.

    The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to set the base price for non-derived rateplans if the rateplan              is active and already loaded for the specified time period.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/base_price\&quot;, \&quot;value\&quot;: 120.00                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the rateplan belongs to.
    :type hotel_id: int
    :param rateplan_code: The code of the rateplan you want to update the daily rate details for.
    :type rateplan_code: str
    :param _from: Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days.
    :type _from: str
    :param to: Defines the first business day you would like to get rates for.
    :type to: str
    :param patch_request: A set of JSON Patch operations.
    :type patch_request: list | bytes

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    patch_request = [OperationRatePatchRequest.from_dict(d) for d in patch_request]
    return web.Response(status=200)
