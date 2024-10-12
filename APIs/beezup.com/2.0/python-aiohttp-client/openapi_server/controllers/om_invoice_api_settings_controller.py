from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.get_order_invoice_design_preview_response import GetOrderInvoiceDesignPreviewResponse
from openapi_server.models.get_order_invoice_general_settings_response import GetOrderInvoiceGeneralSettingsResponse
from openapi_server.models.order_invoice_design_settings import OrderInvoiceDesignSettings
from openapi_server.models.order_invoice_general_settings import OrderInvoiceGeneralSettings
from openapi_server import util


async def get_order_invoice_design_settings(request: web.Request, ) -> web.Response:
    """Get Order Invoice design settings

    


    """
    return web.Response(status=200)


async def get_order_invoice_design_settings_preview(request: web.Request, accept_encoding, body) -> web.Response:
    """View a preview an Order Invoice using custom design settings

    

    :param accept_encoding: Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
    :type accept_encoding: List[str]
    :param body: 
    :type body: dict | bytes

    """
    body = OrderInvoiceDesignSettings.from_dict(body)
    return web.Response(status=200)


async def get_order_invoice_general_settings(request: web.Request, ) -> web.Response:
    """Get Order Invoice general settings

    


    """
    return web.Response(status=200)


async def save_order_invoice_design_settings(request: web.Request, body) -> web.Response:
    """Save Order Invoice design settings

    

    :param body: 
    :type body: dict | bytes

    """
    body = OrderInvoiceDesignSettings.from_dict(body)
    return web.Response(status=200)


async def save_order_invoice_general_settings(request: web.Request, body) -> web.Response:
    """Save Order Invoice general settings

    

    :param body: 
    :type body: dict | bytes

    """
    body = OrderInvoiceGeneralSettings.from_dict(body)
    return web.Response(status=200)
