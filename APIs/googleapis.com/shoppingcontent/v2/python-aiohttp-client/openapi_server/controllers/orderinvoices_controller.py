from typing import List, Dict
from aiohttp import web

from openapi_server.models.orderinvoices_create_charge_invoice_request import OrderinvoicesCreateChargeInvoiceRequest
from openapi_server.models.orderinvoices_create_charge_invoice_response import OrderinvoicesCreateChargeInvoiceResponse
from openapi_server.models.orderinvoices_create_refund_invoice_request import OrderinvoicesCreateRefundInvoiceRequest
from openapi_server.models.orderinvoices_create_refund_invoice_response import OrderinvoicesCreateRefundInvoiceResponse
from openapi_server import util


async def content_orderinvoices_createchargeinvoice(request: web.Request, merchant_id, order_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """content_orderinvoices_createchargeinvoice

    Creates a charge invoice for a shipment group, and triggers a charge capture for orderinvoice enabled orders.

    :param merchant_id: The ID of the account that manages the order. This cannot be a multi-client account.
    :type merchant_id: str
    :param order_id: The ID of the order.
    :type order_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderinvoicesCreateChargeInvoiceRequest.from_dict(body)
    return web.Response(status=200)


async def content_orderinvoices_createrefundinvoice(request: web.Request, merchant_id, order_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """content_orderinvoices_createrefundinvoice

    Creates a refund invoice for one or more shipment groups, and triggers a refund for orderinvoice enabled orders. This can only be used for line items that have previously been charged using &#x60;createChargeInvoice&#x60;. All amounts (except for the summary) are incremental with respect to the previous invoice.

    :param merchant_id: The ID of the account that manages the order. This cannot be a multi-client account.
    :type merchant_id: str
    :param order_id: The ID of the order.
    :type order_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrderinvoicesCreateRefundInvoiceRequest.from_dict(body)
    return web.Response(status=200)
