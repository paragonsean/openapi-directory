from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.reservation_details_list_result import ReservationDetailsListResult
from openapi_server.models.reservation_summaries_list_result import ReservationSummariesListResult
from openapi_server import util


async def reservations_details_list_by_reservation_order(request: web.Request, reservation_order_id, filter, api_version) -> web.Response:
    """reservations_details_list_by_reservation_order

    Lists the reservations details for provided date range.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param filter: Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; 
    :type filter: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def reservations_details_list_by_reservation_order_and_reservation(request: web.Request, reservation_order_id, reservation_id, filter, api_version) -> web.Response:
    """reservations_details_list_by_reservation_order_and_reservation

    Lists the reservations details for provided date range.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param reservation_id: Id of the reservation
    :type reservation_id: str
    :param filter: Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; 
    :type filter: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def reservations_summaries_list_by_reservation_order(request: web.Request, reservation_order_id, grain, api_version, filter=None) -> web.Response:
    """reservations_summaries_list_by_reservation_order

    Lists the reservations summaries for daily or monthly grain.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param grain: Can be daily or monthly
    :type grain: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview.
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
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview.
    :type api_version: str
    :param filter: Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;
    :type filter: str

    """
    return web.Response(status=200)
