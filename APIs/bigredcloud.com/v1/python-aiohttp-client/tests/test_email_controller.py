# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_quote_dto import EmailQuoteDto
from openapi_server.models.email_statement_dto import EmailStatementDto
from openapi_server.models.sales_invoice_email_info_dto import SalesInvoiceEmailInfoDto


pytestmark = pytest.mark.asyncio

async def test_email_send_email_statement(client):
    """Test case for email_send_email_statement

    Sends a Statement email.  If \"toAddress\" is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer's address.
    """
    body = {"bccAddresses":["bcc1@email.com","bcc2@email.com","bcc3@email.com"],"customerId":1,"fromPeriod":"2016-04-07T00:00:00","messageBody":"Email message","minimumBalance":4,"toAddress":"to@email.com","toPeriod":"2016-06-07T00:00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/email/sendEmailStatement',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_send_quote(client):
    """Test case for email_send_quote

    Sends a Quote email.  If \"toAddress\" is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer's address.
    """
    body = {"bccAddresses":["bcc1@email.com","bcc2@email.com","bcc3@email.com"],"messageBody":"Email message","quoteId":1,"toAddress":"to@email.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/email/sendQuote',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_email_send_sales_invoice(client):
    """Test case for email_send_sales_invoice

    Sends a Sales Invoice email.  If \"toAddress\" is not empty then email will be sent to this address. Otherwise email will be sent to Sales Invoice Customer's address.
    """
    body = {"bccAddresses":["bcc1@email.com","bcc2@email.com","bcc3@email.com"],"messageBody":"Email message","salesInvoiceId":1,"toAddress":"to@email.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/email/sendSalesInvoice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

