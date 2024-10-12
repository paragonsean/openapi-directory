from typing import List, Dict
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_invoice_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_invoice import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice
from openapi_server import util


async def order_api_create_invoice_0(request: web.Request, id, include_invoice_pdf=None, template_id=None, send_to_cloud_id=None) -> web.Response:
    """Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

    

    :param id: The internal billbee id of the order
    :type id: int
    :param include_invoice_pdf: If true, the PDF is included in the response as base64 encoded string
    :type include_invoice_pdf: bool
    :param template_id: You can pass the id of an invoice template to overwrite the assigned template for invoice creation
    :type template_id: int
    :param send_to_cloud_id: You can pass the id of a connected cloud printer/storage to send the invoice to it
    :type send_to_cloud_id: int

    """
    return web.Response(status=200)


async def order_api_get_invoice_list_0(request: web.Request, min_invoice_date=None, max_invoice_date=None, page=None, page_size=None, shop_id=None, order_state_id=None, tag=None, min_pay_date=None, max_pay_date=None, include_positions=None, exclude_tags=None) -> web.Response:
    """Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate

    

    :param min_invoice_date: Specifies the oldest invoice date to include
    :type min_invoice_date: str
    :param max_invoice_date: Specifies the newest invoice date to include
    :type max_invoice_date: str
    :param page: Specifies the page to request
    :type page: int
    :param page_size: Specifies the pagesize. Defaults to 50, max value is 250
    :type page_size: int
    :param shop_id: Specifies a list of shop ids for which invoices should be included
    :type shop_id: List[int]
    :param order_state_id: Specifies a list of state ids to include in the response
    :type order_state_id: List[int]
    :param tag: 
    :type tag: List[str]
    :param min_pay_date: 
    :type min_pay_date: str
    :param max_pay_date: 
    :type max_pay_date: str
    :param include_positions: 
    :type include_positions: bool
    :param exclude_tags: If true the list of tags passed to the call are used to filter orders to not include these tags
    :type exclude_tags: bool

    """
    min_invoice_date = util.deserialize_datetime(min_invoice_date)
    max_invoice_date = util.deserialize_datetime(max_invoice_date)
    min_pay_date = util.deserialize_datetime(min_pay_date)
    max_pay_date = util.deserialize_datetime(max_pay_date)
    return web.Response(status=200)
