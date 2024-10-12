# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.generate_batch_order_invoice_error_response_item import GenerateBatchOrderInvoiceErrorResponseItem
from openapi_server.models.generate_batch_order_invoice_request_item import GenerateBatchOrderInvoiceRequestItem
from openapi_server.models.generate_order_invoice_request import GenerateOrderInvoiceRequest
from openapi_server.models.generate_order_invoice_response import GenerateOrderInvoiceResponse
from openapi_server.models.get_order_invoice_pdf_from_html_invoice_url_request import GetOrderInvoicePdfFromHtmlInvoiceUrlRequest
from openapi_server.models.preview_order_invoice_request import PreviewOrderInvoiceRequest
from openapi_server.models.preview_order_invoice_response import PreviewOrderInvoiceResponse


pytestmark = pytest.mark.asyncio

async def test_generate_batch_order_invoice(client):
    """Test case for generate_batch_order_invoice

    Generate an Order Invoice batch
    """
    body = [openapi_server.GenerateBatchOrderInvoiceRequestItem()]
    params = [('userName', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/invoices/generate',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_order_invoice(client):
    """Test case for generate_order_invoice

    Generate an Order Invoice
    """
    body = openapi_server.GenerateOrderInvoiceRequest()
    params = [('userName', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/invoices/{marketplace_technical_code}/{account_id}/{beez_up_order_uuid}/generate'.format(marketplace_technical_code='marketplace_technical_code_example', account_id='account_id_example', beez_up_order_uuid='beez_up_order_uuid_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_invoice_pdf(client):
    """Test case for get_order_invoice_pdf

    Returns the PDF version of the invoice
    """
    body = openapi_server.GetOrderInvoicePdfFromHtmlInvoiceUrlRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/invoices/getPdfInvoice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_invoice_preview(client):
    """Test case for get_order_invoice_preview

    View a preview an Order Invoice
    """
    body = openapi_server.PreviewOrderInvoiceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_encoding': ['accept_encoding_example'],
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/invoices/{marketplace_technical_code}/{account_id}/{beez_up_order_uuid}/preview'.format(marketplace_technical_code='marketplace_technical_code_example', account_id='account_id_example', beez_up_order_uuid='beez_up_order_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

