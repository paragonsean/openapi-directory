from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_funds_to_carrier_request_body import AddFundsToCarrierRequestBody
from openapi_server.models.add_funds_to_carrier_response_body import AddFundsToCarrierResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_carrier_by_id_response_body import GetCarrierByIdResponseBody
from openapi_server.models.get_carrier_options_response_body import GetCarrierOptionsResponseBody
from openapi_server.models.get_carriers_response_body import GetCarriersResponseBody
from openapi_server.models.list_carrier_package_types_response_body import ListCarrierPackageTypesResponseBody
from openapi_server.models.list_carrier_services_response_body import ListCarrierServicesResponseBody
from openapi_server import util


async def add_funds_to_carrier(request: web.Request, carrier_id, body) -> web.Response:
    """Add Funds To Carrier

    Add Funds To A Carrier

    :param carrier_id: Carrier ID
    :type carrier_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddFundsToCarrierRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_carrier_by_id(request: web.Request, carrier_id) -> web.Response:
    """Get Carrier By ID

    Retrive carrier info by ID

    :param carrier_id: Carrier ID
    :type carrier_id: str

    """
    return web.Response(status=200)


async def get_carrier_options(request: web.Request, carrier_id) -> web.Response:
    """Get Carrier Options

    Get a list of the options available for the carrier

    :param carrier_id: Carrier ID
    :type carrier_id: str

    """
    return web.Response(status=200)


async def list_carrier_package_types(request: web.Request, carrier_id) -> web.Response:
    """List Carrier Package Types

    List the package types associated with the carrier

    :param carrier_id: Carrier ID
    :type carrier_id: str

    """
    return web.Response(status=200)


async def list_carrier_services(request: web.Request, carrier_id) -> web.Response:
    """List Carrier Services

    List the services associated with the carrier ID

    :param carrier_id: Carrier ID
    :type carrier_id: str

    """
    return web.Response(status=200)


async def list_carriers(request: web.Request, ) -> web.Response:
    """List Carriers

    List all carriers that have been added to this account


    """
    return web.Response(status=200)
