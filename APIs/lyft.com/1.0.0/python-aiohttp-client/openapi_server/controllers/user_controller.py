from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.cancellation_cost_error import CancellationCostError
from openapi_server.models.cancellation_request import CancellationRequest
from openapi_server.models.location import Location
from openapi_server.models.profile import Profile
from openapi_server.models.rating_request import RatingRequest
from openapi_server.models.ride import Ride
from openapi_server.models.ride_detail import RideDetail
from openapi_server.models.ride_receipt import RideReceipt
from openapi_server.models.ride_request import RideRequest
from openapi_server.models.ride_request_error import RideRequestError
from openapi_server.models.rides_response import RidesResponse
from openapi_server import util


async def cancel_ride(request: web.Request, id, request=None) -> web.Response:
    """Cancel a ongoing requested ride

    Cancel a ongoing ride which was requested earlier by providing the ride id. 

    :param id: The ID of the ride
    :type id: str
    :param request: 
    :type request: dict | bytes

    """
    request = CancellationRequest.from_dict(request)
    return web.Response(status=200)


async def get_profile(request: web.Request, ) -> web.Response:
    """The user&#39;s general info

    The v1 of this endpoint returns the user&#39;s ID, v2 will return more general info about the user. We require authentication for this endpoint, so we extract the user ID from the access token. 


    """
    return web.Response(status=200)


async def get_ride(request: web.Request, id) -> web.Response:
    """Get the ride detail of a given ride ID

    Get the status of a ride along with information about the driver, vehicle and price of a given ride ID 

    :param id: The ID of the ride
    :type id: str

    """
    return web.Response(status=200)


async def get_ride_receipt(request: web.Request, id) -> web.Response:
    """Get the receipt of the rides.

    Get the receipt information of a processed ride by providing the ride id. Receipts will only be available to view once the payment has been processed. In the case of canceled ride, cancellation penalty is included if applicable. 

    :param id: The ID of the ride
    :type id: str

    """
    return web.Response(status=200)


async def get_rides(request: web.Request, start_time, end_time=None, limit=None) -> web.Response:
    """List rides

    Get a list of past &amp; current rides for this passenger. 

    :param start_time: Restrict to rides starting after this point in time. The earliest supported date is 2015-01-01T00:00:00+00:00 
    :type start_time: str
    :param end_time: Restrict to rides starting before this point in time. The earliest supported date is 2015-01-01T00:00:00+00:00 
    :type end_time: str
    :param limit: The maximum number of rides to return. The default limit is 10 if not specified. The maximum allowed value is 50, an integer greater that 50 will return at most 50 results. 
    :type limit: int

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def new_ride(request: web.Request, request) -> web.Response:
    """Request a Lyft

    Request a Lyft come pick you up at the given location. 

    :param request: Ride request information
    :type request: dict | bytes

    """
    request = Ride.from_dict(request)
    return web.Response(status=200)


async def set_ride_destination(request: web.Request, id, request) -> web.Response:
    """Update the destination of the ride

    Add or update the ride&#39;s destination. Note that the ride must still be active (not droppedOff or canceled), and that destinations on Lyft Line rides can not be changed. 

    :param id: The ID of the ride
    :type id: str
    :param request: The coordinates and optional address of the destination
    :type request: dict | bytes

    """
    request = Location.from_dict(request)
    return web.Response(status=200)


async def set_ride_rating(request: web.Request, id, request) -> web.Response:
    """Add the passenger&#39;s rating, feedback, and tip

    Add the passenger&#39;s 1 to 5 star rating of the ride, optional written feedback, and optional tip amount in minor units and currency. The ride must already be dropped off, and ratings must be given within 24 hours of drop off. For purposes of display, 5 is considered the default rating. When this endpoint is successfully called, payment processing will begin. 

    :param id: The ID of the ride
    :type id: str
    :param request: The rating and optional feedback
    :type request: dict | bytes

    """
    request = RatingRequest.from_dict(request)
    return web.Response(status=200)
