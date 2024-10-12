from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_invoice_model import CreateInvoiceModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.invoice_output_model import InvoiceOutputModel
from openapi_server.models.invoice_row_output_model import InvoiceRowOutputModel
from openapi_server.models.invoice_settings_output_model import InvoiceSettingsOutputModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.project_invoice_settings_input_model import ProjectInvoiceSettingsInputModel
from openapi_server.models.project_invoice_settings_output_model import ProjectInvoiceSettingsOutputModel
from openapi_server import util


async def invoice_rows_patch_invoice_row(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a invoice row or a part of it

    If CostCenterNumber, SalesAccountNumber or RecurringSalesAccountNumber are changed and the invoice row is related to one or many ProjectFees or ProjectTravelExpenses, the values for those will also be updated.

    :param guid: ID of the invoice row
    :type guid: str
    :param body: JSON Patch document of InvoiceRowModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def invoice_settings_patch_invoice_settings(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) invoice setting

    

    :param guid: ID of the invoice settings
    :type guid: str
    :param body: JSON patch document of InvoiceSettingsModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def invoices_patch_invoice(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an invoice or a part of it

    

    :param guid: GUID of the invoice
    :type guid: str
    :param body: JSON patch document of InvoiceInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def invoices_post_invoice_creation(request: web.Request, body=None) -> web.Response:
    """Add an invoice to project(s)

    

    :param body: CreateInvoiceModel
    :type body: dict | bytes

    """
    body = CreateInvoiceModel.from_dict(body)
    return web.Response(status=200)


async def project_invoice_settings_patch_project_invoice_settings(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) project invoice settings.

    

    :param guid: ID of the project invoice settings.
    :type guid: str
    :param body: JSON patch document of ProjectInvoiceSettingsInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_invoice_settings_post_project_invoice_settings(request: web.Request, body=None) -> web.Response:
    """Create a new project invoice settings.

    

    :param body: Project invoice settings.
    :type body: dict | bytes

    """
    body = ProjectInvoiceSettingsInputModel.from_dict(body)
    return web.Response(status=200)
