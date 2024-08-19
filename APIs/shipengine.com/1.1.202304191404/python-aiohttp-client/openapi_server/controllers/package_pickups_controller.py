from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_pickup_by_id_response_body import DeletePickupByIdResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_pickup_by_id_response_body import GetPickupByIdResponseBody
from openapi_server.models.get_pickups_response_body import GetPickupsResponseBody
from openapi_server.models.schedule_pickup_request_body import SchedulePickupRequestBody
from openapi_server.models.schedule_pickup_response_body import SchedulePickupResponseBody
from openapi_server import util


async def delete_scheduled_pickup(request: web.Request, pickup_id) -> web.Response:
    """Delete a Scheduled Pickup

    Delete a previously-scheduled pickup by ID

    :param pickup_id: 
    :type pickup_id: str

    """
    return web.Response(status=200)


async def get_pickup_by_id(request: web.Request, pickup_id) -> web.Response:
    """Get Pickup By ID

    Get Pickup By ID

    :param pickup_id: 
    :type pickup_id: str

    """
    return web.Response(status=200)


async def list_scheduled_pickups(request: web.Request, carrier_id=None, warehouse_id=None, created_at_start=None, created_at_end=None, page=None, page_size=None) -> web.Response:
    """List Scheduled Pickups

    List all pickups that have been scheduled for this carrier

    :param carrier_id: Carrier ID
    :type carrier_id: str
    :param warehouse_id: Warehouse ID
    :type warehouse_id: str
    :param created_at_start: Only return scheduled pickups that were created on or after a specific date/time
    :type created_at_start: str
    :param created_at_end: Only return scheduled pickups that were created on or before a specific date/time
    :type created_at_end: str
    :param page: Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned. 
    :type page: int
    :param page_size: The number of results to return per response.
    :type page_size: int

    """
    created_at_start = util.deserialize_datetime(created_at_start)
    created_at_end = util.deserialize_datetime(created_at_end)
    return web.Response(status=200)


async def schedule_pickup(request: web.Request, body) -> web.Response:
    """Schedule a Pickup

    Schedule a package pickup with a carrier

    :param body: 
    :type body: dict | bytes

    """
    body = SchedulePickupRequestBody.from_dict(body)
    return web.Response(status=200)
