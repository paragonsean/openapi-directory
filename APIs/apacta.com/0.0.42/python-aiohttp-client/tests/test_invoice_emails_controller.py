# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.get_one_invoice_emails200_response import GetOneInvoiceEmails200Response


pytestmark = pytest.mark.asyncio

async def test_get_one_invoice_emails(client):
    """Test case for get_one_invoice_emails

    Get an invoice emails
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoices/{invoice_id}/emails/{email_id}'.format(invoice_id='invoice_id_example', email_id='email_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

