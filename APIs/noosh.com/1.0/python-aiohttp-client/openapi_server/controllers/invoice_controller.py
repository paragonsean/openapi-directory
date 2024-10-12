from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_list_response_vo import FileListResponseVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.invoice_detail_list_expand_vo import InvoiceDetailListExpandVO
from openapi_server.models.invoice_expand_vo import InvoiceExpandVO
from openapi_server import util


async def get_invoice(request: web.Request, workgroup_id, project_id, invoice_id) -> web.Response:
    """List a specific invoice of project Level

    List a specific invoice of project Level

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param invoice_id: 
    :type invoice_id: str

    """
    return web.Response(status=200)


async def get_invoice_files(request: web.Request, workgroup_id, project_id, invoice_id) -> web.Response:
    """List files of invoice Level

    List files of invoice Level

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param invoice_id: 
    :type invoice_id: str

    """
    return web.Response(status=200)


async def get_invoices(request: web.Request, workgroup_id, project_id, order_id) -> web.Response:
    """List invoices by a specific order

    List invoices by a specific order

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param order_id: 
    :type order_id: str

    """
    return web.Response(status=200)
