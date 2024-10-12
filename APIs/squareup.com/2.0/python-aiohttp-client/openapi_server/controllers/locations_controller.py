from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_location_request import CreateLocationRequest
from openapi_server.models.create_location_response import CreateLocationResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.retrieve_location_response import RetrieveLocationResponse
from openapi_server.models.update_location_request import UpdateLocationRequest
from openapi_server.models.update_location_response import UpdateLocationResponse
from openapi_server import util


async def create_location(request: web.Request, body) -> web.Response:
    """CreateLocation

    Creates a location.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateLocationRequest.from_dict(body)
    return web.Response(status=200)


async def list_locations(request: web.Request, ) -> web.Response:
    """ListLocations

    Provides information of all locations of a business.  Many Square API endpoints require a &#x60;location_id&#x60; parameter. The &#x60;id&#x60; field of the [&#x60;Location&#x60;](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) objects returned by this endpoint correspond to that &#x60;location_id&#x60; parameter.


    """
    return web.Response(status=200)


async def retrieve_location(request: web.Request, location_id) -> web.Response:
    """RetrieveLocation

    Retrieves details of a location. You can specify \&quot;main\&quot;  as the location ID to retrieve details of the  main location.

    :param location_id: The ID of the location to retrieve. If you specify the string \&quot;main\&quot;, then the endpoint returns the main location.
    :type location_id: str

    """
    return web.Response(status=200)


async def update_location(request: web.Request, location_id, body) -> web.Response:
    """UpdateLocation

    Updates a location.

    :param location_id: The ID of the location to update.
    :type location_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateLocationRequest.from_dict(body)
    return web.Response(status=200)
