from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_drivers200_response import GetDrivers200Response
from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.post_charge_request import PostChargeRequest
from openapi_server import util


async def get_vehicle(request: web.Request, id, include_driver=None, include_token=None, include_organization=None) -> web.Response:
    """get_vehicle

    Get a vehicle&#39;s data

    :param id: The vehicule id that needs to be fetched
    :type id: str
    :param include_driver: Populate driver
    :type include_driver: bool
    :param include_token: Populate token
    :type include_token: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    return web.Response(status=200)


async def get_vehicle_battery(request: web.Request, id) -> web.Response:
    """get_vehicle_battery

    Get a vehicle&#39;s battery

    :param id: The vehicle id that needs to be fetched
    :type id: str

    """
    return web.Response(status=200)


async def get_vehicle_charge(request: web.Request, id) -> web.Response:
    """get_vehicle_charge

    Get a vehicle&#39;s charge

    :param id: The vehicle id that needs to be fetched
    :type id: str

    """
    return web.Response(status=200)


async def get_vehicle_location(request: web.Request, id) -> web.Response:
    """get_vehicle_location

    Get a vehicle&#39;s location

    :param id: The vehicle id that needs to be fetched
    :type id: str

    """
    return web.Response(status=200)


async def get_vehicle_odometer(request: web.Request, id) -> web.Response:
    """get_vehicle_odometer

    Get a vehicle&#39;s odometer

    :param id: The vehicle id that needs to be fetched
    :type id: str

    """
    return web.Response(status=200)


async def get_vehicles(request: web.Request, active=None, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_driver=None, include_token=None, include_organization=None) -> web.Response:
    """get_vehicles

    List all vehicles

    :param active: Get a list of active vehicles
    :type active: bool
    :param paginate_limit: Number of results per page
    :type paginate_limit: int
    :param paginate_page: The queried page index
    :type paginate_page: str
    :param paginate_enabled: Enable pagination
    :type paginate_enabled: bool
    :param sort_by: Sort data by this key
    :type sort_by: str
    :param sort_order: asc to sort ascending (default is desc - descending)
    :type sort_order: str
    :param created_at_gte: Date as ISO String
    :type created_at_gte: str
    :param created_at_lte: Date as ISO String
    :type created_at_lte: str
    :param updated_at_gte: Date as ISO String
    :type updated_at_gte: str
    :param updated_at_lte: Date as ISO String
    :type updated_at_lte: str
    :param include_driver: Populate driver
    :type include_driver: bool
    :param include_token: Populate token
    :type include_token: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def post_charge(request: web.Request, id, body) -> web.Response:
    """post_charge

    Change charge

    :param id: The vehicle id that needs to be fetched
    :type id: str
    :param body: Include command properties to send here
    :type body: dict | bytes

    """
    body = PostChargeRequest.from_dict(body)
    return web.Response(status=200)
