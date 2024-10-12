# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_invoice_in import EmailInvoiceIn
from openapi_server.models.email_invoice_out import EmailInvoiceOut
from openapi_server.models.email_refund_in import EmailRefundIn
from openapi_server.models.email_refund_out import EmailRefundOut


pytestmark = pytest.mark.asyncio

async def test_email_invoice(client):
    """Test case for email_invoice

    Email invoice
    """
    input = openapi_server.EmailInvoiceIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{key}/invoice/send_email'.format(key='key_example'),
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_refund(client):
    """Test case for email_refund

    Email credit note
    """
    input = openapi_server.EmailRefundIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{key}/invoice/refunds/{refund_note_number}/send_email'.format(key='key_example', refund_note_number='refund_note_number_example'),
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

