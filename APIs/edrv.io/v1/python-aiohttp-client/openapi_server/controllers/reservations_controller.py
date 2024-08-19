from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.updatereservation_request import UpdatereservationRequest
from openapi_server import util


async def get_reservation(request: web.Request, id, include_chargestation=None, include_organization=None) -> web.Response:
    """get_reservation

    Get one reservation data

    :param id: ID of the reservation that needs to be fetched
    :type id: str
    :param include_chargestation: Populate chargestation
    :type include_chargestation: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    return web.Response(status=200)


async def get_reservations(request: web.Request, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_chargestation=None, include_organization=None) -> web.Response:
    """get_reservations

    Get Reservations data

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
    :param include_chargestation: Populate chargestation
    :type include_chargestation: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def updatereservation(request: web.Request, id, body) -> web.Response:
    """updatereservation

    Use to request a update an existing reservation. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

    :param id: ID of the reservation that needs to be fetched
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatereservationRequest.from_dict(body)
    return web.Response(status=200)
