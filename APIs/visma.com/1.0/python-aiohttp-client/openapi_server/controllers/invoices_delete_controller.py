from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def invoice_rows_delete_invoice_row(request: web.Request, guid, set_as_non_billable=None) -> web.Response:
    """Deletes an invoice row

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the invoice row.
    :type guid: str
    :param set_as_non_billable: 
    :type set_as_non_billable: bool

    """
    return web.Response(status=200)


async def invoices_delete_invoice(request: web.Request, guid) -> web.Response:
    """Delete an invoice.

    Returns: No Content (204) if succeeded. Not found (404) if cost center can&#39;t be found.

    :param guid: ID for the invoice to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def invoices_delete_project_from_invoice(request: web.Request, guid, project_guid) -> web.Response:
    """Delete a project from invoice.

    

    :param guid: The invoice GUID.
    :type guid: str
    :param project_guid: The project GUID.
    :type project_guid: str

    """
    return web.Response(status=200)


async def project_invoice_settings_delete_project_invoice_settings(request: web.Request, guid) -> web.Response:
    """Delete an project invoice settings.

    Returns: No Content (204) if succeeded. Not found (404) if project invoice settings can&#39;t be found.

    :param guid: ID for the project invoice settings to delete.
    :type guid: str

    """
    return web.Response(status=200)
