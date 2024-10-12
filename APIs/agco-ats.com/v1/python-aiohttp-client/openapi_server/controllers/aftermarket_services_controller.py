from typing import List, Dict
from aiohttp import web

from openapi_server.models.agco_power_services_models_ecu import AGCOPowerServicesModelsECU
from openapi_server.models.agco_power_services_models_production_data import AGCOPowerServicesModelsProductionData
from openapi_server.models.agco_power_services_models_user_status import AGCOPowerServicesModelsUserStatus
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server import util


async def aftermarket_services_get_certs(request: web.Request, ) -> web.Response:
    """No Documentation Found.

    No Documentation Found.


    """
    return web.Response(status=200)


async def aftermarket_services_get_connection_status(request: web.Request, ) -> web.Response:
    """Check whether there is connectivity to AGCO Power Web Services

    No Documentation Found.


    """
    return web.Response(status=200)


async def aftermarket_services_get_engine_iqa_codes(request: web.Request, serial_number, edt_instance_id) -> web.Response:
    """Get injector codes given engine.

    No Documentation Found.

    :param serial_number: The serial number of the engine.
    :type serial_number: str
    :param edt_instance_id: The EDT Instance Id of the kit calling this method.
    :type edt_instance_id: str

    """
    return web.Response(status=200)


async def aftermarket_services_get_production_data(request: web.Request, serial_number, edt_instance_id) -> web.Response:
    """Get production calibration data for given engine.

    No Documentation Found.

    :param serial_number: The serial number of the engine.
    :type serial_number: str
    :param edt_instance_id: The EDT Instance Id of the kit calling this method.
    :type edt_instance_id: str

    """
    return web.Response(status=200)


async def aftermarket_services_get_user_status(request: web.Request, voucher_code, dealer_code) -> web.Response:
    """Retrieve the status of an EDT Kit Registration with AGCO Power Web Services

    No Documentation Found.

    :param voucher_code: 
    :type voucher_code: str
    :param dealer_code: 
    :type dealer_code: str

    """
    return web.Response(status=200)


async def aftermarket_services_put_ecu(request: web.Request, serial_number, edt_instance_id, body) -> web.Response:
    """Activate or Deactivate an ECU, or Report an ECU as Damaged.

    No Documentation Found.

    :param serial_number: The serial number of the ECU.
    :type serial_number: str
    :param edt_instance_id: The EDT Instance Id of the kit calling this method.
    :type edt_instance_id: str
    :param body: The ecu to modify.
    :type body: dict | bytes

    """
    body = AGCOPowerServicesModelsECU.from_dict(body)
    return web.Response(status=200)


async def aftermarket_services_put_iqa_codes(request: web.Request, serial_number, edt_instance_id, body) -> web.Response:
    """Report the IQA codes used by an engine

    No Documentation Found.

    :param serial_number: The serial number of the Engine
    :type serial_number: str
    :param edt_instance_id: The EDT Instance Id of the kit calling this method.
    :type edt_instance_id: str
    :param body: A string array of IQA codes in physical order
    :type body: List[str]

    """
    return web.Response(status=200)


async def aftermarket_services_update_user_status(request: web.Request, body) -> web.Response:
    """Update the status of an EDT Kit Registration with AGCO Power Web Services

    No Documentation Found.

    :param body: 
    :type body: dict | bytes

    """
    body = AGCOPowerServicesModelsUserStatus.from_dict(body)
    return web.Response(status=200)
