from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_cash_drawer_shift_events_response import ListCashDrawerShiftEventsResponse
from openapi_server.models.list_cash_drawer_shifts_response import ListCashDrawerShiftsResponse
from openapi_server.models.retrieve_cash_drawer_shift_response import RetrieveCashDrawerShiftResponse
from openapi_server import util


async def list_cash_drawer_shift_events(request: web.Request, location_id, shift_id, limit=None, cursor=None) -> web.Response:
    """ListCashDrawerShiftEvents

    Provides a paginated list of events for a single cash drawer shift.

    :param location_id: The ID of the location to list cash drawer shifts for.
    :type location_id: str
    :param shift_id: The shift ID.
    :type shift_id: str
    :param limit: Number of resources to be returned in a page of results (200 by default, 1000 max).
    :type limit: int
    :param cursor: Opaque cursor for fetching the next page of results.
    :type cursor: str

    """
    return web.Response(status=200)


async def list_cash_drawer_shifts(request: web.Request, location_id, sort_order=None, begin_time=None, end_time=None, limit=None, cursor=None) -> web.Response:
    """ListCashDrawerShifts

    Provides the details for all of the cash drawer shifts for a location in a date range.

    :param location_id: The ID of the location to query for a list of cash drawer shifts.
    :type location_id: str
    :param sort_order: The order in which cash drawer shifts are listed in the response, based on their opened_at field. Default value: ASC
    :type sort_order: str
    :param begin_time: The inclusive start time of the query on opened_at, in ISO 8601 format.
    :type begin_time: str
    :param end_time: The exclusive end date of the query on opened_at, in ISO 8601 format.
    :type end_time: str
    :param limit: Number of cash drawer shift events in a page of results (200 by default, 1000 max).
    :type limit: int
    :param cursor: Opaque cursor for fetching the next page of results.
    :type cursor: str

    """
    return web.Response(status=200)


async def retrieve_cash_drawer_shift(request: web.Request, location_id, shift_id) -> web.Response:
    """RetrieveCashDrawerShift

    Provides the summary details for a single cash drawer shift. See [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.

    :param location_id: The ID of the location to retrieve cash drawer shifts from.
    :type location_id: str
    :param shift_id: The shift ID.
    :type shift_id: str

    """
    return web.Response(status=200)
