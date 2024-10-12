from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.post_charge_stations201_response import PostChargeStations201Response
from openapi_server.models.schema1 import Schema1
from openapi_server import util


async def delete_charge_station(request: web.Request, id) -> web.Response:
    """delete_charge_station

    Use to delete a charge station

    :param id: The charge station id that needs to be deleted
    :type id: str

    """
    return web.Response(status=200)


async def get_charge_station(request: web.Request, id, include_location=None, include_evses=None, include_organization=None) -> web.Response:
    """get_charge_station

    Get a single charge station&#39;s data

    :param id: The charge station id that needs to be fetched
    :type id: str
    :param include_location: Populate location
    :type include_location: bool
    :param include_evses: Populate evses
    :type include_evses: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    return web.Response(status=200)


async def get_charge_station_connectors(request: web.Request, id, include_evse=None, include_organization=None) -> web.Response:
    """get_charge_station_connectors

    List connectors for a chargestation

    :param id: chargeStation id
    :type id: str
    :param include_evse: Populate evse
    :type include_evse: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    return web.Response(status=200)


async def get_charge_stations(request: web.Request, organization=None, location=None, online=None, active=None, public=None, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_location=None, include_evses=None, include_organization=None) -> web.Response:
    """get_charge_stations

    List all Chargestations

    :param organization: Filter by Org. Id
    :type organization: str
    :param location: Filter by Location Id
    :type location: str
    :param online: Filter by Online Status
    :type online: bool
    :param active: Chargestations that have been activated/deactivated by the admin
    :type active: bool
    :param public: Chargestations that are public
    :type public: bool
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
    :param include_location: Populate location
    :type include_location: bool
    :param include_evses: Populate evses
    :type include_evses: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def patch_charge_station(request: web.Request, id, body) -> web.Response:
    """patch_charge_station

    Update a charge station&#39;s data

    :param id: ID of charge station that needs to be updated
    :type id: str
    :param body: Include charge station properties to update here
    :type body: dict | bytes

    """
    body = Schema1.from_dict(body)
    return web.Response(status=200)


async def post_charge_stations(request: web.Request, body) -> web.Response:
    """post_charge_stations

    Create a new charge station

    :param body: Include charge station properties to create here
    :type body: dict | bytes

    """
    body = Schema1.from_dict(body)
    return web.Response(status=200)
