from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancelreservation_request import CancelreservationRequest
from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.patch_charge_station_variable_request import PatchChargeStationVariableRequest
from openapi_server.models.remotestart_request import RemotestartRequest
from openapi_server.models.remotestop_request import RemotestopRequest
from openapi_server.models.reserve_request import ReserveRequest
from openapi_server.models.reset_request import ResetRequest
from openapi_server.models.setchargingschedule201_response import Setchargingschedule201Response
from openapi_server.models.unlockconnector_request import UnlockconnectorRequest
from openapi_server import util


async def cancelreservation(request: web.Request, body) -> web.Response:
    """cancelreservation

    Use to request a delete an existing reservation. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

    :param body: 
    :type body: dict | bytes

    """
    body = CancelreservationRequest.from_dict(body)
    return web.Response(status=200)


async def get_commands(request: web.Request, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_chargestation=None, include_driver=None, include_transaction=None, include_organization=None) -> web.Response:
    """get_commands

    Get Commands data

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
    :param include_driver: Populate driver
    :type include_driver: bool
    :param include_transaction: Populate transaction
    :type include_transaction: bool
    :param include_organization: Populate organization
    :type include_organization: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)


async def get_variables(request: web.Request, id) -> web.Response:
    """get_variables

    Get a charge station&#39;s config variables

    :param id: The chargestation id
    :type id: str

    """
    return web.Response(status=200)


async def patch_charge_station_variable(request: web.Request, id, body) -> web.Response:
    """patch_charge_station_variable

    Update config variables for a chargestation

    :param id: ID of charge station
    :type id: str
    :param body: Charge Station Variable to set
    :type body: dict | bytes

    """
    body = PatchChargeStationVariableRequest.from_dict(body)
    return web.Response(status=200)


async def remotestart(request: web.Request, body) -> web.Response:
    """remotestart

    Use to request a remote start command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

    :param body: 
    :type body: dict | bytes

    """
    body = RemotestartRequest.from_dict(body)
    return web.Response(status=200)


async def remotestop(request: web.Request, body) -> web.Response:
    """remotestop

    Use to request a remote stop command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

    :param body: Remote stop transaction info here.
    :type body: dict | bytes

    """
    body = RemotestopRequest.from_dict(body)
    return web.Response(status=200)


async def reserve(request: web.Request, body) -> web.Response:
    """reserve

    Use to request a reserve command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

    :param body: 
    :type body: dict | bytes

    """
    body = ReserveRequest.from_dict(body)
    return web.Response(status=200)


async def reset(request: web.Request, body) -> web.Response:
    """reset

    Use to request a reset command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

    :param body: 
    :type body: dict | bytes

    """
    body = ResetRequest.from_dict(body)
    return web.Response(status=200)


async def unlockconnector(request: web.Request, body) -> web.Response:
    """unlockconnector

    Use to request an unlock command for a connector. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

    :param body: 
    :type body: dict | bytes

    """
    body = UnlockconnectorRequest.from_dict(body)
    return web.Response(status=200)
