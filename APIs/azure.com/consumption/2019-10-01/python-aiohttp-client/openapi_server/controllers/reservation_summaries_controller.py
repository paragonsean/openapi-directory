from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.reservation_summaries_list_result import ReservationSummariesListResult
from openapi_server import util


async def reservations_summaries_list(request: web.Request, scope, grain, api_version, start_date=None, end_date=None, filter=None) -> web.Response:
    """reservations_summaries_list

    Lists the reservations summaries for the defined scope daily or monthly grain.

    :param scope: The scope associated with reservations summaries operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for BillingAccount scope (legacy), and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope (modern). 
    :type scope: str
    :param grain: Can be daily or monthly
    :type grain: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01.
    :type api_version: str
    :param start_date: Start date
    :type start_date: str
    :param end_date: End date
    :type end_date: str
    :param filter: Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;
    :type filter: str

    """
    return web.Response(status=200)


async def reservations_summaries_list_by_reservation_order(request: web.Request, reservation_order_id, grain, api_version, filter=None) -> web.Response:
    """reservations_summaries_list_by_reservation_order

    Lists the reservations summaries for daily or monthly grain.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param grain: Can be daily or monthly
    :type grain: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01.
    :type api_version: str
    :param filter: Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;
    :type filter: str

    """
    return web.Response(status=200)


async def reservations_summaries_list_by_reservation_order_and_reservation(request: web.Request, reservation_order_id, reservation_id, grain, api_version, filter=None) -> web.Response:
    """reservations_summaries_list_by_reservation_order_and_reservation

    Lists the reservations summaries for daily or monthly grain.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param reservation_id: Id of the reservation
    :type reservation_id: str
    :param grain: Can be daily or monthly
    :type grain: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01.
    :type api_version: str
    :param filter: Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;
    :type filter: str

    """
    return web.Response(status=200)
