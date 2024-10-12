from typing import List, Dict
from aiohttp import web

from openapi_server.models.landlord_accounting_model import LandlordAccountingModel
from openapi_server.models.landlord_crm_entry import LandlordCrmEntry
from openapi_server.models.landlord_maintenance_model import LandlordMaintenanceModel
from openapi_server.models.landlord_profit_loss_model import LandlordProfitLossModel
from openapi_server.models.landlord_rent_arrears_model import LandlordRentArrearsModel
from openapi_server.models.landlord_settings_model import LandlordSettingsModel
from openapi_server.models.landlord_summary_model import LandlordSummaryModel
from openapi_server.models.landlord_tenancy_model import LandlordTenancyModel
from openapi_server import util


async def landlord_controller_create_maintenance_preference(request: web.Request, short_name, token, tenancy_id, name, notes) -> web.Response:
    """Post tenancy maintenance preferences:-

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param tenancy_id: The Tenancy ID
    :type tenancy_id: str
    :param name: Name of the maintenance preference to add
    :type name: str
    :param notes: Notes of the maintenance preference to add
    :type notes: str

    """
    return web.Response(status=200)


async def landlord_controller_get_accounts(request: web.Request, short_name, token) -> web.Response:
    """Get the accounting details for the landlord.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def landlord_controller_get_document(request: web.Request, short_name, token, id) -> web.Response:
    """Download a Document

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param id: The Document ID
    :type id: str

    """
    return web.Response(status=200)


async def landlord_controller_get_invetory_report(request: web.Request, short_name, token, tenancy_id) -> web.Response:
    """Generate a Inventory PDF for a tenancy

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param tenancy_id: The Tenancy ID
    :type tenancy_id: str

    """
    return web.Response(status=200)


async def landlord_controller_get_invoice(request: web.Request, short_name, token, invoice_id) -> web.Response:
    """Get an invoice pdf belonging to the landlord.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param invoice_id: The invoice ID to load.
    :type invoice_id: str

    """
    return web.Response(status=200)


async def landlord_controller_get_landlord_crm_entries(request: web.Request, short_name, token) -> web.Response:
    """Retrieve landlord&#39;s CRM ID

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def landlord_controller_get_maintenance_jobs(request: web.Request, short_name, token) -> web.Response:
    """Get Active maintenance jobs.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def landlord_controller_get_profit_loss_report(request: web.Request, short_name, token) -> web.Response:
    """Generate a Profit and Loss Report

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def landlord_controller_get_rent_arrears(request: web.Request, short_name, token) -> web.Response:
    """Rent Arrears

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def landlord_controller_get_sas_report(request: web.Request, short_name, token, year_end) -> web.Response:
    """Generate a Self Assessment Tax Report

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param year_end: The Tax Year End.
    :type year_end: int

    """
    return web.Response(status=200)


async def landlord_controller_get_settings(request: web.Request, short_name, token) -> web.Response:
    """Get contact details of all linked landlords.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def landlord_controller_get_summary_details(request: web.Request, short_name, token) -> web.Response:
    """Get the summary details for the landlord.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def landlord_controller_get_tenancy(request: web.Request, short_name, token, tenancy_id) -> web.Response:
    """Get tenancy details.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param tenancy_id: The Tenancy ID
    :type tenancy_id: str

    """
    return web.Response(status=200)


async def landlord_controller_get_tenancy_agreement_report(request: web.Request, short_name, token, tenancy_id) -> web.Response:
    """Generate a Tenancy Agreement Copy (PDF)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param tenancy_id: The Tenancy ID
    :type tenancy_id: str

    """
    return web.Response(status=200)
