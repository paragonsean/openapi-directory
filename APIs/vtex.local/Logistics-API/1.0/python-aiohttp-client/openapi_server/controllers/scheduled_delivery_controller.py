from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def add_blocked_delivery_windows(request: web.Request, content_type, accept, carrier_id, body) -> web.Response:
    """Add blocked delivery windows

    Adds blocked delivery windows for your store&#39;s shipping policies.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param carrier_id: 
    :type carrier_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def api_logistics_capacity_resources_carriercapacity_typeshipping_policy_id_time_frames_get(request: web.Request, content_type, accept, capacity_type, shipping_policy_id, range_start, range_end) -> web.Response:
    """Search capacity reservations in time range

    Get information on all capacity reservations made to scheduled delivery windows in a given time range.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.    &gt; Note that the combined string &#x60;carrier@{capacityType}@{shippingPolicyId}&#x60; can be referred to as a \&quot;resource\&quot; in the API&#39;s messages.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param capacity_type: How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (&#x60;\&quot;orders_quantity\&quot;&#x60;) or SKUs (&#x60;\&quot;skus_quantity\&quot;&#x60;).
    :type capacity_type: str
    :param shipping_policy_id: ID of shipping policy to search.
    :type shipping_policy_id: str
    :param range_start: Starting date of time range
    :type range_start: str
    :param range_end: End date of time range.
    :type range_end: str

    """
    return web.Response(status=200)


async def api_logistics_capacity_resources_carriercapacity_typeshipping_policy_id_time_frames_window_day_fwindow_start_time_twindow_end_time_get(request: web.Request, content_type, accept, capacity_type, shipping_policy_id, window_day, window_start_time, window_end_time) -> web.Response:
    """Get capacity reservation usage by window

    Retrieves capacity usage of a specific scheduled delivery reservation window.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.    &gt; Note that the combined string &#x60;carrier@{capacityType}@{shippingPolicyId}&#x60; can be referred to as a \&quot;resource\&quot; in the API&#39;s messages.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param capacity_type: How the delivery capacity is measured as defined in the shipping policy. Capacity can be measured by maximum number of orders (&#x60;\&quot;orders_quantity\&quot;&#x60;) or SKUs (&#x60;\&quot;skus_quantity\&quot;&#x60;).
    :type capacity_type: str
    :param shipping_policy_id: ID of shipping policy to search.
    :type shipping_policy_id: str
    :param window_day: Day of the specific scheduled delivery window to be consulted for reservations.
    :type window_day: str
    :param window_start_time: Start time of specific scheduled delivery window to be consulted for reservations.
    :type window_start_time: str
    :param window_end_time: End time of specific scheduled delivery window to be consulted for reservations.
    :type window_end_time: str

    """
    return web.Response(status=200)


async def remove_blocked_delivery_windows(request: web.Request, content_type, accept, carrier_id, body) -> web.Response:
    """Remove blocked delivery windows

    Removes the blocked delivery windows set to your store&#39;s shipping policies.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns time adjusted to the configured time zone of the account.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param carrier_id: 
    :type carrier_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def retrieve_blocked_delivery_windows(request: web.Request, content_type, accept, carrier_id) -> web.Response:
    """Retrieve blocked delivery windows

    Lists all blocked delivery windows of your store&#39;s shipping policies, searching by carrier ID.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param carrier_id: 
    :type carrier_id: str

    """
    return web.Response(status=200)
